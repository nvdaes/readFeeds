# Read Feeds #

This addon allows to read feeds in Atom channels or RSS channels using NVDA. 
The channels will not be updated automatically.

## Installation or Update: ##

If there is an RSS folder in your personal NVDA configuration folder, from a previous version of ReadFeeds, when installing this version, version 5.0 or later, a dialog will ask if you want to upgrade or install.
Choose update to preserve your saved channels and to continue using them in the new installed version of readFeeds. 

## Commands: ##

### Read Feeds menu ###

Pop up the NVDA menu, NVDA+N, to allow you to access ReadFeeds menu. 

- News list...
Presents the news list from your current Rss channel. Select the news item you want to read and press OK button to open the corresponding page in your browser.
- Temporary address... control + NVDA + shift + enter:
Opens a dialog to view the current address. You can also type a new URL to select another channel.
- Load saved address... NVDA+control+enter:
Opens a dialog to select a channel from a saved file containing feed URLs.
- Save current address... NVDA+shift+enter:
opens a dialog to select a file where you can save the current feed address.
- Update current feed: control+shift+NVDA+8:
Refresh selected channel. The RSS channels will not be updated automatically when Read Feeds addon is started.
- Copy feeds folder...
opens a dialog to choose a folder where you can save the RSS directory of your RSS channels. By default the selected folder is the NVDA's configuration directory, which will create the RSS directory.
- Restore feeds...
Opens a dialog to select a folder which replaces your channels in the RSS folder. make sure you load a folder containing RSS channels URLs.
- Open documentation:
Opens the information about Read Feeds add-on, if it's available for the NVDA interface language.

### Keyboard commands: ###

- Ctrl+Shift+NVDA+Space:
Reads the article's URL. Pressing twice will open the web page.
- Ctrl+Shift+NVDA+8:
Updates the selected channel and reads the first feed title.
- Ctrl+Shift+NVDA+I:
Reads the current feed title. Pressing twice will copy the text to clipboard.
- Ctrl+Shift+NVDA+U:
Reads the previous feed title.
- Ctrl+Shift+NVDA+O:
Reads the next feed title.
- control+shift+NVDA+enter:
Opens a dialog for entering the address of a feed.
- Shift+NVDA+enter:
Opens a dialog for saving a file containing the selected address.
- control+NVDA+enter:
Opens a dialog for selecting a feed address from file.

When you load the Read Feed addon, it will select automatically the URL contained in addressFile.txt, this file is included in the subdirectory RSS.
If there is no addressFile.txt, the default address will be the one specified in the source code (globalPlugins/readFeeds/__init__.py).

## Notifications: ##

- When the title or URL have been copied;
- When unable to read a feed, probably due to connection problems or the address is an invalid feed address.
- NVDA could inform with an error message also if it was possible to copy the saved RSS channels.
- The title of the news list dialog displays the selected channel name and number of items available.

Last Translation: Sun feb 24 01:00 2013, by
Chris

## Changes for 6.0 ##
*	 Initial version.
