# Last Finished — Calibre Plugin

## Author's Note

This plugin was created because my beautiful wife needed a simple way to keep track of when she finished reading books.

The solution does not rely on external software, manual metadata updates, or unnecessary complexity.

**Note:** This plugin was developed and tested using Calibre version 9.17. Compatibility with other versions has not been tested.
**Note:** The plugin automatically checks reading progress every 30 seconds. If you reach the end of the book and close it immediately the plugin would not have enough time to update. 

---

## Solution

Automatically update a user-created custom Date column named `Last Finished` whenever a book reaches 99% reading progress.

The date is stored directly in Calibre's library metadata, making it persistent across Calibre restarts.

## How It Works

- The plugin automatically checks reading progress every 30 seconds.
- When a book reaches 99% completion or higher, its `Last Finished` date is updated to the current date.
- If you reopen or reread a completed book, its previous completion date is preserved.
- If you finish the book again, the date is updated to reflect the most recent completion.
- All dates are saved directly to your Calibre library and remain there between sessions.

## Requirements

- A custom Date column must be created in Calibre (see installation instructions below).
- Reading progress must be tracked using Calibre's built-in ebook viewer. Reading progress from external devices or other reading applications is not supported.

## Installation Guide

### 1. Create the Custom Column

1. In Calibre, go to **Preferences > Interface > Add your own columns**
2. At the bottom-left of the window, click **Add custom column**
3. Enter the following information:

   - **Lookup name:** last_finished
   - **Column heading:** Last Finished
   - **Column type:** Date

4. Click **OK**
5. At the bottom-right of the window, click **Apply**
6. Close and reopen Calibre

The new column should now appear at the end of your library table.


### 2. Download/ prepare the plugin ZIP file

Note: yes, its silly that im asking you to unzip and rezip. GitHub's download is zipped but Calibre needs the inside folder to be zipped for plug ins. 
1. Open the GitHub page: https://github.com/jescobar449/Calibre---Last-Finished
2. Click on the green **"<> Code"** button 
3. Click Download ZIP 
4. Locate the downloaded folder - most likely named Calibre---Last-Finished-main.zip
5. Right click the zipped folder > Extract All > Extract
6. Go into the new unzipped folder - has the same name but it not zipped and has a regular folder icon 
7. Go into the subfolder - you should now see all 5 files 
8. Select all 5 files
9. Right click > Compress to.. > ZIP File > name it LastFinished.zip


### 3. Install the Plugin

1. In Calibre, go to **Preferences > Advanced > Plugins**
2. At the bottom-right of the window, click **Load plugin from file**
3. Locate and select the ZIP folder that you created in the steps above  - LastFinished.zip
7. When the security warning appears, click **Yes** to proceed
8. When the success message appears, click **OK**
9. Click **Apply** at the bottom-right of the Plugins window
10. Close and reopen Calibre

**All done! Enjoy!**
