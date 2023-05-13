# Read Feeds #

* Authors: Noelia Ruiz Martínez, Mesar Hameed
* Download [stable version][1] (compatible with NVDA 2019.3 and beyond)
* Download [beta version][2] (compatible with NVDA 2019.3 and beyond)

This addon provides a straightforward way to read feeds in Atom or RSS formats using NVDA.
The feeds will not be refreshed automatically.
Below when we mention feeds, we mean both RSS and ATOM feeds.

## Commands ##

### Read Feeds dialog ###

You can access the Read Feeds dialog from the nvda menu, Tools submenu, Feeds item.

It contains the following controls:

* Filter by: An edit box to search previously saved feeds.
* A list of the saved feeds, focused when the dialog is opened.
* List of articles: Opens a dialog which presents the articles list from your current feed. Select the article you want to read and press Enter or Open web page of selected article button to open the corresponding page in your browser. Press About article button to open a dialog showing title and link of the selected article; from this dialog, you'll be able to copy this info to the clipboard.
* Open feed: Opens the selected feed in the default application.
* Open feed as HTML: Opens the selected feed in the default web browser. You will be able to show or hide publication dates and buttons to copy information about articles to clipboard.
* Copy feed address: Opens a dialog to confirm if you want to copy the feed address to clipboard.
* New: Opens a dialog with an edit box to enter the address of a new feed. If the address is valid and the feed can be saved, its name, based on the feed title, will appear at the bottom of the feeds list.
* Rename: Opens a dialog with an edit box to rename the selected feed.
* Delete: Opens a dialog to delete the selected feed after confirmation.
* Set default: Sets the selected feed as the default, so that its articles can be accessed with NVDA's gestures.
* Import feeds from OPML file: Opens a dialog to add new feeds from an OPML file.
* Save feeds to OPML file: Opens a dialog to save the feeds available from the Feeds dialog in an OPML file.
* Preferences: Opens the settings dialog for readFeeds, also available in NVDA's menu, Preferences, settings, readFeeds category.
* Close: Closes the Feeds dialog.

### Notes #####

* The Filter by edit box can be placed after the Open article button from NVDA's menu, Preferences, Settings, Read feeds category, or pressing the Preferences button of the Feeds dialog.
* This panel has an option to show article dates on the List of articles dialog.


### Keyboard commands ###

* Ctrl+Shift+NVDA+Space: Announces current article's URL. Pressing twice will open the web page.
* Ctrl+Shift+NVDA+8: Refreshes the selected feed and announces its most recent title.
* Ctrl+Shift+NVDA+I: Announces current feed title and link. Pressing twice will copy the title and related link to clipboard.
* Ctrl+Shift+NVDA+U: Announces previous feed title.
* Ctrl+Shift+NVDA+O: Announces next feed title.

## Notifications ##

* When the title or URL have been copied.
* When unable to connect/refresh a feed, or the URL does not correspond to a valid feed.
* NVDA will display an error message if a new feed cannot be created.
* The title of the articles list dialog displays the selected feed name and number of items available.

## Changes for 21.0

* Feeds with untitled articles can be presented in the Articles dialog, and opened as HTML.

## Changes for 20.0

* universalFeedParser is updated to 5.0.1, adding support for more feeds.

## Changes for 15.0

* Compatible with NVDA 2023.1.

## Changes for 14.0

* Fixed a bug that made impossible to add some feeds.

## Changes for 13.0

* The add-on cannot be used on secure screens.
* Feeds are managed from OPML files.
* Due to changes in the feeds management system, there are changes in the configuration file where the default feed is set. Please, use the Feeds dialog if you want to set it again.
* Your old text files used in previous versions will be automatically imported into the new OPML format when the add-on is started.
* The copy and restore feeds feature has been replaced with the ability to import from and save to OPML files.
* Non well-formed feeds can be processed before being added to make them compatible with the add-on.
* In the Read Feeds settings panel, a new option allows to show article dates on the List of articles dialog.

## Changes for 12.0

* Fixed a bug which made shortcuts for items of NVDA's tools menu don't work as expected.

## Changes for 11.0

* Compatible with NVDA 2021.1

## Changes for 10.0 ##

* Added a button to open the selected feed as HTML in the default web browser.
* If a new feed cannot be created, this will be notified in an error dialog.
* Improved order and presentation of some articles.
* More feeds may be supported.
* When the feeds dialog is opened, the list of feeds will be focused instead of the search edit box.
* You can choose if the search edit box is placed after the list of feeds, useful to focus the list even when switching from another window without closing the Feeds dialog.
* Added a button to copy the feed address to clipboard from the feeds dialog.

## Changes for 9.0 ##

* Requires NVDA 2019.3 or later.

## Changes for 8.0 ##

* When the add-on is updated, feeds saved in the previous version of the add-on will be automatically copied to the new version, unless you prefer to import feeds saved in the main configuration folder of NVDA.
* When using the dialog to copy feeds, if the chosen folder is not named personalFeeds, a subfolder with this name will be created to prevent the deletion of directories containing important data, such as Documents or Downloads.

## Changes for 7.0 ##

* The Feeds dialog includes a button to open a folder which may contain a backup of feeds.
* When using the edit box to filter feeds, if no results are found, the list of feeds and other controls are disabled, so that NVDA doesn't report "unknown" in the empty list.
* If the list of articles dialog can't be shown, for example due to errors in the feed, NVDA will raise an error, so that the feeds dialog can be used without restarting NVDA.

## Changes for 6.0 ##

* When the default feed has been updated and it stops working due to server issues, the previous articles aren't deleted and can be read with the corresponding keystrokes.
* Fix regression: The default feed can be updated twice again.

## Changes for 5.0 ##

* The articles list dialog has been enhanced.
* Compatible with NVDA 2018.3 or later (required).
* If needed, you can download the [last version compatible with NVDA 2017.3][3].

## Changes for 4.0 ##

* Added a button to open the selected feed from the Feeds dialog.

## Changes for 3.0 ##

* The dialogs to manage feed files have been removed. Now their functionality is included in the Feeds dialog.
* The visual presentation of the dialogs has been enhanced, adhering to the appearance of the dialogs shown in NVDA.
* The default feed is saved on the NVDA's configuration. Therefore, it's possible to set different default feeds in configuration profiles.
* Requires NVDA 2016.4.

## Changes for 2.0 ##

* Add-on help is available from the Add-ons Manager.

## Changes for 1.0 ##

* Initial version.

[1]: https://www.nvaccess.org/addonStore/legacy?file=readFeeds

[2]: https://www.nvaccess.org/addonStore/legacy?file=readFeeds-beta

[3]: https://www.nvaccess.org/addonStore/legacy?file=rf-o
