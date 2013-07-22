# Read Feeds #

This addon allows to read feeds in Atom channels or RSS channels using NVDA. 
The channels will not be updated automatically when start ReadFeeds addon.

## installation or Update: ##

If in your personal configuration folder of NVDA there are a copy of RSS folder, comming from a previous version of ReadFeeds, when installing this version, 5.0 or later, a dialog will ask if you want upgrade or install. Confirm update to take up your saved channels in the new installed version of readFeeds. 

## Commands: ##

### ReadFeeds menu: ###

Pop up the NVDA menu, NVDA+N, to allow you to access ReadFeeds menu. 

- News list...
Presents the news list of current channel Rss. Select a news you want to read and press OK button to open the corresponding page in your browser.
- Temporary address... control + NVDA + shift + enter:
Opens a dialog to view the current address. Typing a new URL to select another channel.
- Load saved address... NVDA+control+enter:
Opens a dialog to select a channel from a saved file containing URL.
- Save current address... NVDA+shift+enter:
opens a dialog to select a file where you can save the current channel address.
- Update current feed: control+shift+NVDA+8:
Refresh selected channel. The RSS channels will not be updated automatically when start ReadFeeds addon.
- Copy feeds folder...
opens a dialog to choose a folder where you can save the RSS directory of your RSS channels. By default the selected folder is the NVDA's configuration directory, which will create the RSS directory.
- Restore feeds...
Opens a dialog to select a folder which replaces your channels in the RSS folder. make sure you load a folder containing RSS channels.
- Open documentation:
Open the information about ReadFeeds add-on, if it's available for the selected language. 

### Keyboard commands: ###

- Ctrl+Shift+NVDA+Space:
Reads the article's URL, that allows open its web page. Pressing twice will open the web.
- Ctrl+Shift+NVDA+8:
Updates the selected channel and reads the first feed title.
- Ctrl+Shift+NVDA+I:
Reads the current feed title. Pressing twice will copy the text to clipboard.
- Ctrl+Shift+NVDA+U:
Reads the prior feed title.
- Ctrl+Shift+NVDA+O:
Reads the next feed title.
- control+shift+NVDA+enter:
Opens a dialog for setting the address of the feeds channel.
- Shift+NVDA+enter:
Opens a dialog for saving a file containing the selected address.
- control+NVDA+enter:
Opens a dialog for setting the address of the feeds channel from a selected file.

When you load the ReadFeed addon, it will select automatically the URL contained in addressFile.txt, this file is included in the subdirectory RSS.
If there is no addressFile.txt, the default address will be the one specified in the source code (globalPlugins/readFeeds/__init__.py).

## Notifications: ##

NVDA will notify:

- If the title or URL have been copied;
- if you can not read the feeds, probably due to connection problems or the address you entered does not correspond to a RSS channel.
- NVDA could inform with an error message also if it was possible to copy the RSS channels saved.
- In the title of the news list dialog displays the selected channel name and number of items available.

Last Translation: Sun feb 24 01:00 2013, by
Chris

## Changes for 6.0 ##
+	 Initial version.
