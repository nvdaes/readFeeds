# वाचन पोषण #

* लेखकहरू: नोलिया रुइज्  मार्डिज्नेज,  मेसर हमिद 
* अनुबहन [स्थिर संस्करण][2]
* अनुबहन [विकास संस्करण][1]

This addon provides a straightforward way to read feeds in Atom or RSS
formats using NVDA.  The feeds will not be refreshed automatically.  Below
when we mention feeds, we mean both RSS and ATOM feeds.

## स्थापना वा अद्यावधिकरण: ##

If you used a previous version of this addon, and there is an RSS or
personalFeeds folder in your personal NVDA configuration folder, when
installing version 6.0 or later, a dialog will ask if you want to upgrade or
install.  Choose update to preserve your saved feeds and to continue using
them in the new installed version of readFeeds.

## आदेसहरू ##

### वाचन पोषण मेनु ###

You can access the Read Feeds submenu from the nvda menu, NVDA+N, where the
following menu options are available:

- Article list...  Presents the article list from your current feed. Select
the article you want to read and press OK button to open the corresponding
page in your browser.  - Temporary feed address... control + NVDA + shift +
enter: Opens a dialog for typing a new URL to select another feed. The
current URL will be shown in this dialog.  - Load feed address from
file... NVDA+control+enter: Opens a dialog to select a feed from a saved
file containing a feed URL.  - Save current feed address to
file... NVDA+shift+enter: opens a dialog for selecting the file where
current feed URL will be saved.  If you save to the special file
addressFile.txt, this particular feed will be used as your default feed.  -
Refresh current feed: control+shift+NVDA+8: Refresh selected feed. The feeds
will not be updated automatically when Read Feeds addon is started.  -
Backup feeds folder...  opens a dialog to choose a folder where you can save
the personalFeeds directory of your feeds. By default the selected folder is
the NVDA's configuration directory, which will create the personalFeeds
directory.  - Restore feeds...  Opens a dialog to select a folder which
replaces your feeds in the personalFeeds folder. Make sure you load a folder
containing feeds URLs.

Note: If you want to delete a previously saved feed URL, just remove the
corresponding file.

### कुञ्जीपाटी आदेसहरू ###

- Ctrl+Shift+नेत्रवाणी +Space: Announces current article's URL. Pressing
twice will open the web page.  - Ctrl+Shift+NVDA+8: Refreshes the selected
feed and announces its most recent title.  - Ctrl+Shift+NVDA+I: Announces
current feed title. Pressing twice will copy the title and related link to
clipboard.  - Ctrl+Shift+NVDA+U: Announces previous feed title.  -
Ctrl+Shift+NVDA+O: Announces next feed title.

## सुचनाहरू ##

- When the title or URL have been copied.  - When unable to connect/refresh
a feed, or the URL does not correspond to a valid feed.  - NVDA will display
an error message if it was not possible to backup the personalFeeds folder.
- The title of the article list dialog displays the selected feed name and
number of items available.

## Changes for 2.0 ##
*	 Add-on help is available from the Add-ons Manager.

## १.० मा गरिएका परिवर्तनहरू ##
*	 सुरुको संस्करण

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=rf-dev

[2]: http://addons.nvda-project.org/files/get.php?file=rf

