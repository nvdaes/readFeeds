# -*- coding: UTF-8 -*-

# Read feeds: A simple plugin for reading feeds with NVDA
#Copyright (C) 2012-2017 Noelia Ruiz Martínez, Mesar Hameed
# Released under GPL 2

import os
import sys
import shutil
import addonHandler
import globalPluginHandler
import globalVars
import config
import urllib
import scriptHandler
import api
import gui
from gui import guiHelper
import wx
import ui
from logHandler import log
import re
from .skipTranslation import translate

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from xml2.dom import minidom
del sys.path[-1]

addonHandler.initTranslation()

### Constants

ADDON_SUMMARY = addonHandler.getCodeAddon().manifest['summary']
FEEDS_PATH = os.path.join(os.path.dirname(__file__), "personalFeeds").decode("mbcs")
CONFIG_PATH = globalVars.appArgs.configPath
DEFAULT_ADDRESS_FILE = "addressFile"
# Translators: message presented when feeds cannot be reported.
CAN_NOT_REPORT = _("Unable to refresh feed. Check your Internet conectivity or that the specified feed address is correct.")

### Configuration

confspec = {
	"addressFile": "string(default=addressFile)",
}
config.conf.spec["readFeeds"] = confspec

### Dialogs

def getActiveProfile():
	activeProfile = config.conf.profiles[-1].name
	if not activeProfile:
		# Message translated in NVDA core.
		activeProfile = translate("normal configuration")
	return activeProfile

def doCopy(copyDirectory):
	try:
		shutil.rmtree(copyDirectory, ignore_errors=True)
		shutil.copytree(FEEDS_PATH, copyDirectory)
		wx.CallLater(100, ui.message,
			# Translators: Message presented when feeds have been copied.
			_("Feeds copied"))
	except Exception as e:
		wx.CallAfter(gui.messageBox,
			# Translators: label of error dialog shown when cannot copy feeds folder.
			_("Folder not copied"),
			# Translators: title of error dialog shown when cannot copy feeds folder.
			_("Copy Error"),
			wx.OK|wx.ICON_ERROR)
		raise e

def doRestore(restoreDirectory):
	try:
		shutil.rmtree(FEEDS_PATH, ignore_errors=True)
		shutil.copytree(restoreDirectory, FEEDS_PATH)
		wx.CallLater(100, ui.message,
			# Translators: Message presented when feeds have been restored.
			_("Feeds restored"))
	except Exception as e:
		wx.CallAfter(gui.messageBox,
			# Translators: label of error dialog shown when cannot copy feeds folder.
			_("Folder not copied"),
			# Translators: title of error dialog shown when cannot copy feeds folder.
			_("Copy Error"),
			wx.OK|wx.ICON_ERROR)
		raise e

class FeedsDialog(wx.Dialog):

	_instance = None
	def __new__(cls, *args, **kwargs):
		# Make this a singleton.
		if FeedsDialog._instance is None:
			return super(FeedsDialog, cls).__new__(cls, *args, **kwargs)
		return FeedsDialog._instance

	def __init__(self, parent):
		if FeedsDialog._instance is not None:
			return
		FeedsDialog._instance = self
		# Translators: The title of a dialog.
		super(FeedsDialog, self).__init__(parent, title=_(u"Feed: {defaultFeed} ({configProfile})".format(configProfile=getActiveProfile(),
			defaultFeed=config.conf["readFeeds"]["addressFile"])))

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		sHelper = guiHelper.BoxSizerHelper(self,orientation=wx.VERTICAL)
		# Label of a dialog (message translated in NVDA core in different contexts).
		searchTextLabel = _("&Filter by:")
		self.searchTextEdit = sHelper.addLabeledControl(searchTextLabel, wx.TextCtrl)
		self.searchTextEdit.Bind(wx.EVT_TEXT, self.onSearchEditTextChange)

		feedsListGroupSizer = wx.StaticBoxSizer(wx.StaticBox(self), wx.HORIZONTAL)
		feedsListGroupContents = wx.BoxSizer(wx.HORIZONTAL)
		changeFeedsSizer = wx.BoxSizer(wx.VERTICAL)

		self.choices = [os.path.splitext(filename)[0] for filename in os.listdir(FEEDS_PATH)]
		self.feedsList = wx.ListBox(self,
			choices=self.choices)
		self.feedsList.Selection = 0
		self.feedsList.Bind(wx.EVT_LISTBOX, self.onFeedsListChoice)
		changeFeedsSizer.Add(self.feedsList, proportion=1.0)
		changeFeedsSizer.AddSpacer(guiHelper.SPACE_BETWEEN_BUTTONS_VERTICAL)

		# Translators: The label of a button to open the list of articles of a feed.
		self.articlesButton = wx.Button(self, label=_("List of &articles..."))
		self.articlesButton.Bind(wx.EVT_BUTTON, self.onArticles)
		self.AffirmativeId = self.articlesButton.Id
		self.articlesButton.SetDefault()
		changeFeedsSizer.Add(self.articlesButton)

		feedsListGroupContents.Add(changeFeedsSizer, flag = wx.EXPAND)
		feedsListGroupContents.AddSpacer(guiHelper.SPACE_BETWEEN_ASSOCIATED_CONTROL_HORIZONTAL)

		buttonHelper = guiHelper.ButtonHelper(wx.VERTICAL)
		# Translators: The label of a button to open a feed.
		self.openButton = buttonHelper.addButton(self, label=_("&Open feed"))
		self.openButton.Bind(wx.EVT_BUTTON, self.onOpen)

		# Translators: The label of a button to add a new feed.
		newButton = buttonHelper.addButton(self, label=_("&New..."))
		newButton.Bind(wx.EVT_BUTTON, self.onNew)

		# Translators: The label of a button to rename a feed.
		self.renameButton = buttonHelper.addButton(self, label=_("&Rename..."))
		self.renameButton.Bind(wx.EVT_BUTTON, self.onRename)

		# Translators: The label of a button to delete a feed.
		self.deleteButton = buttonHelper.addButton(self, label=_("&Delete..."))
		self.deleteButton.Bind(wx.EVT_BUTTON, self.onDelete)

# Translators: The label of a button to set a feed as default.
		self.defaultButton = buttonHelper.addButton(self, label=_("S&et default"))
		self.defaultButton.Bind(wx.EVT_BUTTON, self.onDefault)

		feedsListGroupContents.Add(buttonHelper.sizer)
		feedsListGroupSizer.Add(feedsListGroupContents, border=guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		sHelper.addItem(feedsListGroupSizer)

		# Message translated in NVDA core.
		closeButton = wx.Button(self, wx.ID_CLOSE, label=translate("&Close"))
		closeButton.Bind(wx.EVT_BUTTON, lambda evt: self.Close())
		sHelper.addDialogDismissButtons(closeButton)
		self.Bind(wx.EVT_CLOSE, self.onClose)
		self.EscapeId = wx.ID_CLOSE

		self.onFeedsListChoice(None)
		mainSizer.Add(sHelper.sizer, flag=wx.ALL, border=guiHelper.BORDER_FOR_DIALOGS)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.searchTextEdit.SetFocus()
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)

	def __del__(self):
		FeedsDialog._instance = None

	def createFeed(self, address):
		feed = Feed(address)
		feedName = api.filterFileName(feed.getFeedName())
		if os.path.isfile(os.path.join(FEEDS_PATH, "%s.txt" % feedName)):
			feedName = "tempFeed"
		with open(os.path.join(FEEDS_PATH, "%s.txt" % feedName), "w") as f:
			f.write(address)
			f.close()
		return feedName

	def onSearchEditTextChange(self, evt):
		self.feedsList.Clear()
		# Based on the filter of the Input gestures dialog of NVDA's core.
		filter = self.searchTextEdit.Value
		filter = re.escape(filter)
		filterReg = re.compile(r'(?=.*?' + r')(?=.*?'.join(filter.split('\ ')) + r')', re.U|re.IGNORECASE)
		for choice in self.choices:
			if filter and not filterReg.match(choice):
				continue
			self.feedsList.Append(choice)
		self.feedsList.Selection = 0
		self.onFeedsListChoice(None)

	def onFeedsListChoice(self, evt):
		self.sel = self.feedsList.Selection
		self.stringSel = self.feedsList.StringSelection
		self.articlesButton.Enabled = self.sel>= 0
		self.openButton.Enabled = self.sel>= 0
		self.deleteButton.Enabled = (self.sel >= 0 and 
			self.stringSel != DEFAULT_ADDRESS_FILE and 
			config.conf["readFeeds"]["addressFile"] != self.stringSel)
		self.renameButton.Enabled = (self.sel >= 0 and
			self.stringSel != DEFAULT_ADDRESS_FILE and 
			config.conf["readFeeds"]["addressFile"] != self.stringSel)
		self.defaultButton.Enabled = (self.sel >= 0 and 
			self.stringSel != config.conf["readFeeds"]["addressFile"])

	def onArticles(self, evt):
		with open(os.path.join(FEEDS_PATH, "%s.txt" % self.stringSel), "r") as f:
			address = f.read()
			f.close()
		feed = Feed(address)
		with wx.SingleChoiceDialog(self,
			# Translators: the label of a single choice dialog.
			_("Open web page of selected article."),
			# Translators: Title of a dialog.
			u"{feedTitle} ({feedNumber})".format(feedTitle=self.stringSel, feedNumber=feed.getNumberOfArticles()),
			[feed.getArticleTitle(index) for index in xrange(feed.getNumberOfArticles())]) as d:
			if d.ShowModal() == wx.ID_CANCEL:
				return
			os.startfile(feed.getArticleLink(d.Selection))

	def onOpen(self, evt):
		with open(os.path.join(FEEDS_PATH, "%s.txt" % self.stringSel), "r") as f:
			address = f.read()
			f.close()
		os.startfile(address)

	def onNew(self, evt):
		# Translators: The label of a field to enter an address for a new feed.
		with wx.TextEntryDialog(self, _("Address of a new feed:"),
			# Translators: The title of a dialog to create a new feed.
			_("New feed")) as d:
			if d.ShowModal() == wx.ID_CANCEL:
				return
			name = self.createFeed(d.Value)
		self.feedsList.Append(name)

	def onDelete(self, evt):
		if gui.messageBox(
			# Translators: The confirmation prompt displayed when the user requests to delete a feed.
			_("Are you sure you want to delete this feed? This cannot be undone."),
			# Message translated in NVDA core.
			translate("Confirm Deletion"),
			wx.YES | wx.NO | wx.ICON_QUESTION, self
		) == wx.NO:
			return
		os.remove(os.path.join(FEEDS_PATH, "%s.txt" % self.stringSel))
		self.feedsList.Delete(self.sel)
		self.feedsList.Selection = 0
		self.onFeedsListChoice(None)

	def onDefault(self, evt):
		config.conf["readFeeds"]["addressFile"] = self.stringSel
		self.onFeedsListChoice(None)
		self.searchTextEdit.SetFocus()

	def onRename(self, evt):
		# Translators: The label of a field to enter a new name for a feed.
		with wx.TextEntryDialog(self, _("New name:"),
			# Translators: The title of a dialog to rename a feed.
			_("Rename feed"), defaultValue=self.stringSel) as d:
			if d.ShowModal() == wx.ID_CANCEL or not d.Value:
				return
			curName = "%s.txt" % self.stringSel
			newName = "%s.txt" % api.filterFileName(d.Value)
		os.rename(os.path.join(FEEDS_PATH, curName),
			os.path.join(FEEDS_PATH, newName))
		self.feedsList.SetString(self.sel, os.path.splitext(newName)[0])

	def onClose(self, evt):
		self.Destroy()

class CopyDialog(wx.Dialog):

	def __init__(self, parent):
		# Translators: The title of the Copy dialog.
		super(CopyDialog, self).__init__(parent, title=_("Copy feeds"))

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		sHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)

		# Translators: An informational message displayed in the Copy dialog.
		dialogCaption=_("""Select a folder to save a backup of your current feeds.\n
		They will be copied from %s.""" % FEEDS_PATH)
		sHelper.addItem(wx.StaticText(self, label=dialogCaption))

		# Translators: The label of a grouping containing controls to select the destination directory in the Copy dialog.
		directoryGroupText = _("directory for backup:")
		groupHelper = sHelper.addItem(gui.guiHelper.BoxSizerHelper(self, sizer=wx.StaticBoxSizer(wx.StaticBox(self, label=directoryGroupText), wx.VERTICAL)))
		# Message translated in NVDA core.
		browseText = translate("Browse...")
		# Translators: The title of the dialog presented when browsing for the destination directory when copying feeds.
		dirDialogTitle = _("Select directory to copy")
		directoryEntryControl = groupHelper.addItem(gui.guiHelper.PathSelectionHelper(self, browseText, dirDialogTitle))
		self.copyDirectoryEdit = directoryEntryControl.pathControl
		self.copyDirectoryEdit.Value = os.path.join(CONFIG_PATH, "personalFeeds")
		bHelper = sHelper.addDialogDismissButtons(gui.guiHelper.ButtonHelper(wx.HORIZONTAL))
		# Message translated in NVDA core.
		continueButton = bHelper.addButton(self, label=translate("&Continue"), id=wx.ID_OK)
		continueButton.SetDefault()
		continueButton.Bind(wx.EVT_BUTTON, self.onCopy)
		bHelper.addButton(self, id=wx.ID_CANCEL)
		mainSizer.Add(sHelper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		self.Sizer = mainSizer
		mainSizer.Fit(self)
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)

	def onCopy(self, evt):
		if not self.copyDirectoryEdit.Value:
			# Message translated in NVDA core.
			gui.messageBox(translate("Please specify a directory."),
				# Message translated in NVDA core.
				translate("Error"),
				wx.OK | wx.ICON_ERROR)
			return
		drv=os.path.splitdrive(self.copyDirectoryEdit.Value)[0]
		if drv and not os.path.isdir(drv):
			# Message translated in NVDA core.
			gui.messageBox(translate("Invalid drive %s")%drv,
				# Message translated in NVDA core.
				translate("Error"),
				wx.OK | wx.ICON_ERROR)
			return
		self.Hide()
		doCopy(self.copyDirectoryEdit.Value)
		self.Destroy()

	def onCancel(self, evt):
		self.Destroy()

class PathSelectionWithoutNewDir(gui.guiHelper.PathSelectionHelper):

	def __init__(self, parent, buttonText, browseForDirectoryTitle):
		super(PathSelectionWithoutNewDir, self).__init__(parent, buttonText, browseForDirectoryTitle)

	def onBrowseForDirectory(self, evt):
		startPath = self.getDefaultBrowseForDirectoryPath()
		with wx.DirDialog(self._parent, self._browseForDirectoryTitle, defaultPath=startPath, style=wx.DD_DIR_MUST_EXIST | wx.DD_DEFAULT_STYLE) as d:
			if d.ShowModal() == wx.ID_OK:
				self._textCtrl.Value = d.Path

class RestoreDialog(wx.Dialog):

	def __init__(self, parent):
		# Translators: The title of the Restore dialog.
		super(RestoreDialog, self).__init__(parent, title=_("Restore feeds"))

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		sHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)

		# Translators: An informational message displayed in the Restore dialog.
		dialogCaption=_("""Select a folder to restore a backup of your previous copied feeds.\n
		They will be copied to %s.""" % FEEDS_PATH)
		sHelper.addItem(wx.StaticText(self, label=dialogCaption))

		# Translators: The label of a grouping containing controls to select the destination directory in the Restore dialog.
		directoryGroupText = _("directory containing backup:")
		groupHelper = sHelper.addItem(gui.guiHelper.BoxSizerHelper(self, sizer=wx.StaticBoxSizer(wx.StaticBox(self, label=directoryGroupText), wx.VERTICAL)))
		# Message translated in NVDA core.
		browseText = translate("Browse...")
		# Translators: The title of the dialog presented when browsing for the destination directory when restoring feeds.
		dirDialogTitle = _("Select directory to restore")
		directoryEntryControl = groupHelper.addItem(PathSelectionWithoutNewDir(self, browseText, dirDialogTitle))
		self.restoreDirectoryEdit = directoryEntryControl.pathControl
		backupDirectory = os.path.join(CONFIG_PATH, "personalFeeds")
		if os.path.isdir(backupDirectory):
			self.restoreDirectoryEdit.Value = backupDirectory
		bHelper = sHelper.addDialogDismissButtons(gui.guiHelper.ButtonHelper(wx.HORIZONTAL))
		# Message translated in NVDA core.
		continueButton = bHelper.addButton(self, label=translate("&Continue"), id=wx.ID_OK)
		continueButton.SetDefault()
		continueButton.Bind(wx.EVT_BUTTON, self.onRestore)
		bHelper.addButton(self, id=wx.ID_CANCEL)
		mainSizer.Add(sHelper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		self.Sizer = mainSizer
		mainSizer.Fit(self)
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)

	def onRestore(self, evt):
		if not self.restoreDirectoryEdit.Value:
			# Message translated in NVDA core.
			gui.messageBox(translate("Please specify a directory."),
				# Message translated in NVDA core.
				translate("Error"),
				wx.OK | wx.ICON_ERROR)
			return
		drv=os.path.splitdrive(self.restoreDirectoryEdit.Value)[0]
		if drv and not os.path.isdir(drv):
			# Message translated in NVDA core.
			gui.messageBox(translate("Invalid drive %s")%drv,
				# Message translated in NVDA core.
				translate("Error"),
				wx.OK | wx.ICON_ERROR)
			return
		self.Hide()
		doRestore(self.restoreDirectoryEdit.Value)
		self.Destroy()

	def onCancel(self, evt):
		self.Destroy()

### Feed object 

class Feed(object):

	def __init__(self, url):
		super(Feed, self).__init__()
		self._url = url
		self._document = None
		self._articles = []
		self.refresh()

	def refresh(self):
		try:
			self._document = minidom.parse(urllib.urlopen(self._url))
		except Exception as e:
			raise e
		# Check if we are dealing with an rss or atom feed.
		rssFeed = self._document.getElementsByTagName('channel')
		if len(rssFeed):
			self._feedType = 'rss'
			self._articles = self._document.getElementsByTagName('item')
		else:
			atomFeed = self._document.getElementsByTagName('feed')
			if len(atomFeed):
				self._feedType = 'atom'
				self._articles = self._document.getElementsByTagName('entry')
			else:
				log.debugWarning("Unknown type of current feed", exc_info=True)
				raise
		self._index = 0

	def getFeedUrl(self):
		return self._url

	def getFeedType(self):
		return self._feedType

	def getFeedName(self):
		try:
			return self._document.getElementsByTagName('title')[0].firstChild.data
		except:
			return ""

	def getArticleTitle(self, index=None):
		if index is None: index = self._index
		try:
			return self._articles[index].getElementsByTagName('title')[0].firstChild.data
		except:
			# Translators: Presented when the current article does not have an associated title.
			return _("Unable to locate article title.")

	def getArticleLink(self, index=None):
		if index is None: index = self._index
		try:
			if self.getFeedType() == u'rss':
				return self._articles[index].getElementsByTagName('link')[0].firstChild.data
			elif self.getFeedType() == u'atom':
				return self._articles[index].getElementsByTagName('link')[0].getAttribute('href')
		except:
			# Translators: Presented when the current article does not have an associated link.
			return _("Unable to locate article link.")

	def next(self):
		self._index += 1
		if self._index == self.getNumberOfArticles():
			self._index = 0

	def previous(self):
		self._index -= 1
		if self._index == -1:
			self._index = self.getNumberOfArticles() - 1

	def getNumberOfArticles(self):
		return len(self._articles)

### Global plugin

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	scriptCategory = unicode(ADDON_SUMMARY)

	def __init__(self):
		super(globalPluginHandler.GlobalPlugin, self).__init__()
		self.menu = gui.mainFrame.sysTrayIcon.toolsMenu
		self.readFeedsMenu = wx.Menu()
		# Translators: the name of a submenu.
		self.mainItem = self.menu.AppendSubMenu(self.readFeedsMenu, _("&Read Feeds"))
		# Translators: the name of a menu item.
		self.feedsListItem = self.readFeedsMenu.Append(wx.ID_ANY, _("&Feeds..."))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onFeeds, self.feedsListItem)
		# Translators: the name of a menu item.
		self.copyItem = self.readFeedsMenu.Append(wx.ID_ANY, _("&Copy feeds folder..."))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onCopy, self.copyItem)
		# Translators: the name of a menu item.
		self.restoreItem = self.readFeedsMenu.Append(wx.ID_ANY, _("R&estore feeds..."))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onRestore, self.restoreItem)

		self.feed = None

	def terminate(self):
		try:
			self.menu.RemoveItem(self.mainItem)
		except wx.PyDeadObjectError:
			pass

	def onFeeds(self, evt):
		gui.mainFrame.prePopup()
		d = FeedsDialog(gui.mainFrame)
		d.Show()
		gui.mainFrame.postPopup()

	def script_activateFeedsDialog(self, gesture):
		wx.CallAfter(self.onFeeds, None)
	# Translators: message presented in input mode.
	script_activateFeedsDialog.__doc__ = _("Activates the Feeds dialog of %s." % ADDON_SUMMARY)

	def onCopy(self, evt):
		gui.mainFrame.prePopup()
		d = CopyDialog(gui.mainFrame)
		d.Show()
		gui.mainFrame.postPopup()

	def script_activateCopyDialog(self, gesture):
		wx.CallAfter(self.onCopy, None)
	# Translators: message presented in input mode.
	script_activateCopyDialog.__doc__ = _("Activates the Copy dialog of %s." % ADDON_SUMMARY)

	def onRestore(self, evt):
		gui.mainFrame.prePopup()
		d = RestoreDialog(gui.mainFrame)
		d.Show()
		gui.mainFrame.postPopup()

	def script_activateRestoreDialog(self, gesture):
		wx.CallAfter(self.onRestore, None)
	# Translators: message presented in input mode.
	script_activateRestoreDialog.__doc__ = _("Activates the Restore dialog of %s." % ADDON_SUMMARY)

	def getFirstArticle(self):
		try:
			addressFile = "%s.txt" % config.conf["readFeeds"]["addressFile"]
			with open(os.path.join(FEEDS_PATH, addressFile), "r") as f:
				address = f.read()
				f.close()
			self.feed = Feed(address)
		except Exception as e:
			ui.message(CAN_NOT_REPORT)
			raise e

	def script_readFirstArticle(self, gesture):
		self.getFirstArticle()
		if self.feed:
			ui.message(self.feed.getArticleTitle())
	# Translators: message presented in input mode.
	script_readFirstArticle.__doc__ = _("Refreshes the current feed and announces the most recent article title.")

	def script_readCurrentArticle(self, gesture):
		if not self.feed:
			self.getFirstArticle()
		articleInfo = u"{title}\r\n\r\n{address}".format(title=self.feed.getArticleTitle(), address=self.feed.getArticleLink())
		if scriptHandler.getLastScriptRepeatCount()==1 and api.copyToClip(articleInfo):
			# Translators: message presented when the information about an article of a feed is copied to the clipboard.
			ui.message(_("Copied to clipboard %s") % articleInfo)
		else:
			ui.message(articleInfo)
	# Translators: message presented in input mode.
	script_readCurrentArticle.__doc__ = _("Announces the title of the current article. Pressed two times, copies title and related link to the clipboard.")

	def script_readNextArticle(self, gesture):
		if not self.feed:
			self.getFirstArticle()
		self.feed.next()
		ui.message(self.feed.getArticleTitle())
	# Translators: message presented in input mode.
	script_readNextArticle.__doc__ = _("Announces the title of the next article.")

	def script_readPriorArticle(self, gesture):
		if not self.feed:
			self.getFirstArticle()
		self.feed.previous()
		ui.message(self.feed.getArticleTitle())
	# Translators: message presented in input mode.
	script_readPriorArticle.__doc__ = _("Announces the title of the previous article.")

	def script_reportLink(self, gesture):
		if not self.feed:
			self.getFirstArticle()
		articleLink = self.feed.getArticleLink()
		if scriptHandler.getLastScriptRepeatCount()==1:
			os.startfile(articleLink)
		else:
			ui.message(articleLink)
	# Translators: message presented in input mode.
	script_reportLink.__doc__ = _("Announces article link, when pressed two times, opens related web page.")

	def script_copyArticleInfo(self, gesture):
		if not self.feed:
			self.getFirstArticle()
		articleInfo = u"{title}\r\n\r\n{address}".format(title=self.feed.getArticleTitle(), address=self.feed.getArticleLink())
		if api.copyToClip(articleInfo):
			# Translators: message presented when the information about an article of a feed is copied to the clipboard.
			ui.message(_("Copied to clipboard %s") % articleInfo)
	# Translators: message presented in input mode.
	script_copyArticleInfo.__doc__ = _("Copies title and related link of the current article to the clipboard.")

	__gestures = {
		"kb:control+shift+NVDA+8": "readFirstArticle",
		"kb:control+shift+NVDA+i": "readCurrentArticle",
		"kb:control+shift+NVDA+o": "readNextArticle",
		"kb:control+shift+NVDA+u": "readPriorArticle",
		"kb:control+shift+NVDA+space": "reportLink",
	}

