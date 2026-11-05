
from calibre.gui2.actions import InterfaceAction
from qt.core import QTimer


class LastFinishedAction(InterfaceAction):

    name = 'Last Finished'

    action_spec = (
        'Last Finished',
        None,
        'Monitor reading progress',
        None
    )

    def genesis(self):
        self.last_positions = {}
        
        icon = get_icons('images/icon.png', 'Last Finished')
        self.qaction.setIcon(icon)

        self.timer = QTimer(self)
        self.timer.setInterval(30000) #30 sec = 30000
        self.timer.timeout.connect(self.check_reading_progress)
        

    def initialization_complete(self):
        # The library database is now available.
        self.initialize_positions()

        # Start monitoring after initialization.
        self.timer.start()
        
        self.qaction.triggered.connect(self.show_info)

    def initialize_positions(self):
        db = self.gui.current_db.new_api

        for book_id in db.all_book_ids():
            positions = db.get_last_read_positions(
                book_id,
                order_by='epoch',
                limit=1
            )

            if positions:
                self.last_positions[book_id] = positions[0]['epoch']

        print(
            f'Last Finished: Tracking {len(self.last_positions)} books'
        )

    def check_reading_progress(self):
        db = self.gui.current_db.new_api

        for book_id in db.all_book_ids():
            positions = db.get_last_read_positions(
                book_id,
                order_by='epoch',
                limit=1
            )

            if not positions:
                continue

            position = positions[0]
            epoch = position['epoch']
            previous_epoch = self.last_positions.get(book_id)

            if previous_epoch != epoch:
                self.last_positions[book_id] = epoch

                progress = position['pos_frac']

                print(
                    f'Book ID: {book_id} | '
                    f'Progress: {progress:.2%} | '
                    f'Epoch: {epoch}'
                )

                if progress >= 0.99:
                    from datetime import datetime

                    db.set_field(
                        '#last_finished',
                        {book_id: datetime.now()}
                    )

                    print(
                        f'Last Finished: Updated book {book_id}'
                    )

    def shutting_down(self):
        if hasattr(self, 'timer'):
            self.timer.stop()
  
    

    def show_info(self):
        from calibre.gui2 import info_dialog

        info_dialog(
            self.gui,
            'Last Finished',
            'Reading progress is checked every 30 seconds.\n\n'
            'When a book reaches 99% completion, its Last Finished '
            'date is updated automatically.',
            show=True
        )