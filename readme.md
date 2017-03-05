# Read Feeds #

* Authors: Noelia Ruiz Martínez, Mesar Hameed
* Download [stable version][1]
* Download [development version][2]

This addon provides a straightforward  way to read feeds in Atom or RSS formats using NVDA. 
The feeds will not be refreshed automatically.
Below when we mention feeds, we mean both RSS and ATOM feeds.

## Installation or Update: ##

If you used a previous version of this addon, and there is an RSS or personalFeeds folder in your personal NVDA configuration folder, 
when installing version 6.0 or later, a dialog will ask if you want to upgrade or install.
Choose update to preserve your saved feeds and to continue using them in the new installed version of readFeeds. 

## Commands: ##

### Read Feeds menu ###

You can access the Read Feeds submenu from the nvda menu, Tools submenu, where the following menu options are available:

#### Feeds... ####

Opens a dialog with the following controls:

- Filter by: An edit box to search previously saved feeds.
- A list of the saved feeds.
- List of articles: Opens a dialog which presents the articles list from your current feed. Select the article you want to read and press OK button to open the corresponding page in your browser.
- New: Opens a dialog with an edit box to enter the address of a new feed. If the address is valid and the feed can be saved, its name, based on the feed title, will appear at the bottom of the feeds list.
- Rename: Opens a dialog with an edit box to rename the selected feed.
- Delete: Opens a dialog to delete the selected feed after confirmation.
- Set default: Sets the selected feed as the default, so that its articles can be accessed with NVDA's gestures.
- Close: Closes the Feeds dialog.

##### Notes #####

- If a feed named tempFeed is created, please rename it, as this file could be replaced when needed to create a feed whose name already exists.
- The feed set as the default can't be removed. The addressFile feed will be use as the default when the configuration is reset, so it can't be deleted.

####Copy feeds folder... ####

Opens a dialog to choose a folder where you can save the personalFeeds directory of your feeds. By default the selected folder is the NVDA's configuration directory, which will create the personalFeeds directory.

#### Restore feeds... ####

Opens a dialog to select a folder which replaces your feeds in the personalFeeds folder. Make sure you load a folder containing feeds URLs.

### Keyboard commands: ###

- Ctrl+Shift+NVDA+Space: Announces current article's URL. Pressing twice will open the web page.
- Ctrl+Shift+NVDA+8: Refreshes the selected feed and announces its most recent title.
- Ctrl+Shift+NVDA+I: Announces current feed title and link. Pressing twice will copy the title and related link to clipboard.
- Ctrl+Shift+NVDA+U: Announces previous feed title.
- Ctrl+Shift+NVDA+O: Announces next feed title.

## Notifications: ##

- When the title or URL have been copied.
- When unable to connect/refresh a feed, or the URL does not correspond to a valid feed.
- NVDA will display an error message if it was not possible to backup or restore the personalFeeds folder.
- The title of the articles list dialog displays the selected feed name and number of items available.


## Changes for 3.0 ##

- The dialogs to manage feed files have been removed. Now their functionality is included in the Feeds dialog.
- The visual presentation of the dialogs has been enhanced, adhering to the appearance of the dialogs shown in NVDA.
- The default feed is saved on the NVDA's configuration. Therefore, it's possible to set different default feeds in configuration profiles.
- Requires NVDA 2016.4.


## Changes for 2.0 ##

- Add-on help is available from the Add-ons Manager.

## Changes for 1.0 ##

- Initial version.

[1]: http://addons.nvda-project.org/files/get.php?file=rf

[2]: http://addons.nvda-project.org/files/get.php?file=rf-dev