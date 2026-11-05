
from calibre.customize import InterfaceActionBase


class LastFinishedPlugin(InterfaceActionBase):

    name = 'Last Finished'
    description = 'Tracks book completion dates'
    supported_platforms = ['windows']
    author = 'Day'
    version = (1, 0, 0)
    minimum_calibre_version = (9, 17, 0)

    actual_plugin = 'calibre_plugins.last_finished.ui:LastFinishedAction'
