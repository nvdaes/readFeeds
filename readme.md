# Read Feeds #

This addon allows to read feeds in Atom or RSS formats using NVDA. 
The feeds will not be updated automatically.

Below when we mention feeds, we mean both RSS and ATOM feeds.

## Installation or Update: ##

If there is an RSS folder in your personal NVDA configuration folder, from a previous version of ReadFeeds, when installing this version, version 5.0 or later, a dialog will ask if you want to upgrade or install.
Choose update to preserve your saved feeds and to continue using them in the new installed version of readFeeds. 

## Commands: ##

### Read Feeds menu ###

Pop up the NVDA menu, NVDA+N, to allow you to access ReadFeeds menu. 

- News list...
Presents the news list from your current feed. Select the news item you want to read and press OK button to open the corresponding page in your browser.
- Temporary address... control + NVDA + shift + enter:
Opens a dialog for typing a new URL to select another feed. The current URL will be shown on this dialog.
- Load saved address... NVDA+control+enter:
Opens a dialog to select a feed from a saved file containing a feed URL.
- Save current address... NVDA+shift+enter:
opens a dialog to select a file where you can save the current feed URL. Use addressFile.txt for saving the URL of the feed you want to select when this add-on is started.
- Update current feed: control+shift+NVDA+8:
Refresh selected feed. The feeds will not be updated automatically when Read Feeds addon is started.
- Copy feeds folder...
opens a dialog to choose a folder where you can save the RSS directory of your feeds. By default the selected folder is the NVDA's configuration directory, which will create the RSS directory.
- Restore feeds...
Opens a dialog to select a folder which replaces your feeds in the RSS folder. Make sure you load a folder containing feeds URLs.
- Open documentation:
Opens the information about Read Feeds add-on, in the NVDA interface language if available, or in English by default.

### Other keyboard commands: ###

- Ctrl+Shift+NVDA+Space:
Reads the article's URL. Pressing twice will open the web page.
- Ctrl+Shift+NVDA+8:
Updates the selected feed and reads its first title.
- Ctrl+Shift+NVDA+I:
Reads the current feed title. Pressing twice will copy the text (title and link) to clipboard.
- Ctrl+Shift+NVDA+U:
Reads the previous feed title.
- Ctrl+Shift+NVDA+O:
Reads the next feed title.

## Notifications: ##

- When the title or URL have been copied;
- When unable to read a feed, probably due to connection problems or the URL corresponds to an invalid feed.
- NVDA could inform with an error message also if it was not possible to copy the saved feeds.
- The title of the news list dialog displays the selected feed name and number of items available.

Last Translation from Spanish: Sun feb 24 01:00 2013, by
Chris

## Changes for 6.0 ##
*	 Initial version.
