# -*- coding: UTF-8 -*-

# Read feeds: A simple plugin for reading feeds with NVDA
#Copyright (C) 2012-2016 Noelia Ruiz Martínez, Mesar Hameed
# Released under GPL 2

# Version: 6.0
# Used globalVars to get config path, for better results with temporary copies, as instantTranslate or SaveLog add-ons
# Version: 5.0
# Control instead of alt in gesture. Added installTask to update the add-on
# Version: 4.2
# Channel title and number of articles in News list dialog
# Date: 23/06/2012

import addonHandler
import globalPluginHandler
import os
import sys
import shutil
import globalVars
import urllib
import scriptHandler
import api
import gui
from gui import guiHelper
import wx
import ui
from logHandler import log

sys.path.append(os.path.dirname(__file__))
from xml2.dom import minidom
del sys.path[-1]

addonHandler.initTranslation()

### Constants
ADDON_DIR = os.path.join(os.path.dirname(__file__), "..")  # The root of the addon folder
ADDON_INSTANCE = addonHandler.Addon(ADDON_DIR)
ADDON_SUMMARY = ADDON_INSTANCE.manifest['summary']
FEEDS_PATH = os.path.join(ADDON_DIR, "globalPlugins", "personalFeeds")
CONFIG_PATH = globalVars.appArgs.configPath

# Translators: message presented when feeds cannot be reported.
CAN_NOT_REPORT = _("Unable to refresh feed. Check your Internet conectivity or that the specified feed address is correct.")

### Dialogs

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
		super(FeedsDialog, self).__init__(parent, title=_("Feeds"))

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		sHelper = guiHelper.BoxSizerHelper(self,orientation=wx.VERTICAL)
		feedsListGroupSizer = wx.StaticBoxSizer(wx.StaticBox(self), wx.HORIZONTAL)
		feedsListGroupContents = wx.BoxSizer(wx.HORIZONTAL)
		changeFeedsSizer = wx.BoxSizer(wx.VERTICAL)
		names = [os.path.splitext(filename)[0] for filename in os.listdir(FEEDS_PATH)]
		self.feedsList = wx.ListBox(self,
			choices=names)
		self.feedsList.Selection = 0
		self.feedsList.Bind(wx.EVT_LISTBOX, self.onFeedsListChoice)
		changeFeedsSizer.Add(self.feedsList, proportion=1.0)
		changeFeedsSizer.AddSpacer(guiHelper.SPACE_BETWEEN_BUTTONS_VERTICAL)

		# Translators: The label of a button to open the list of articles of a feed.
		self.articlesButton = wx.Button(self, label=_("List of articles..."))
		self.articlesButton.Bind(wx.EVT_BUTTON, self.onArticles)
		self.AffirmativeId = self.articlesButton.Id
		self.articlesButton.SetDefault()
		changeFeedsSizer.Add(self.articlesButton)

		feedsListGroupContents.Add(changeFeedsSizer, flag = wx.EXPAND)
		feedsListGroupContents.AddSpacer(guiHelper.SPACE_BETWEEN_ASSOCIATED_CONTROL_HORIZONTAL)

		buttonHelper = guiHelper.ButtonHelper(wx.VERTICAL)
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

		# Translators: The label of a button to close a dialog.
		closeButton = wx.Button(self, wx.ID_CLOSE, label=_("&Close"))
		closeButton.Bind(wx.EVT_BUTTON, lambda evt: self.Close())
		sHelper.addDialogDismissButtons(closeButton)
		self.Bind(wx.EVT_CLOSE, self.onClose)
		self.EscapeId = wx.ID_CLOSE

		self.onFeedsListChoice(None)
		mainSizer.Add(sHelper.sizer, flag=wx.ALL, border=guiHelper.BORDER_FOR_DIALOGS)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.feedsList.SetFocus()
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

	def onFeedsListChoice(self, evt):
		self.sel = self.feedsList.Selection
		self.stringSel = self.feedsList.StringSelection
		self.articlesButton.Enabled = self.sel>= 0
		self.deleteButton.Enabled = self.sel >= 0
		self.renameButton.Enabled = self.sel >= 0
		self.defaultButton.Enabled = self.sel >= 0

	def onArticles(self, evt):
		with open(os.path.join(FEEDS_PATH, "%s.txt" % self.stringSel), "r") as f:
			address = f.read()
			f.close()
		feed = Feed(address)
		with wx.SingleChoiceDialog(self,
			# Translators: Caption of a dialog.
			_("Open an article"),
			# Translators: Title of a dialog.
			_("List of feeds (%d)" % feed.getNumberOfArticles()),
			[feed.getArticleTitle(index) for index in xrange(feed.getNumberOfArticles())]) as d:
			if d.ShowModal() == wx.ID_CANCEL:
				return
			os.startfile(feed.getArticleLink(d.Selection))

	def onNew(self, evt):
		# Translators: The label of a field to enter an adress for a new feed.
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
			# Translators: The title of the confirmation dialog for deletion of a feed.
			_("Confirm Deletion"),
			wx.YES | wx.NO | wx.ICON_QUESTION, self
		) == wx.NO:
			return
		os.remove(os.path.join(FEEDS_PATH, "%s.txt" % self.stringSel))
		self.feedsList.Delete(self.sel)
		self.feedsList.Selection = 0
		self.onFeedsListChoice(None)

	def onDefault(self, evt):
		pass

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


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	scriptCategory = unicode(ADDON_SUMMARY)

	def __init__(self):
		super(globalPluginHandler.GlobalPlugin, self).__init__()
		self.menu = gui.mainFrame.sysTrayIcon.toolsMenu
		self.readFeedsMenu = wx.Menu()
		self.mainItem = self.menu.AppendSubMenu(self.readFeedsMenu,
		# Translators: the name of a submenu.
		_("&Read Feeds"),
		# Translators: the tooltip for a submenu.
		_("Manage feeds."))
		self.feedsListItem = self.readFeedsMenu.Append(wx.ID_ANY,
		# Translators: the name of a menu item.
		_("&Feeds..."),
		# Translators: the tooltip for a menu item.
		_("View and manage feeds"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onList, self.feedsListItem)

	def terminate(self):
		try:
			self.menu.RemoveItem(self.mainItem)
		except wx.PyDeadObjectError:
			pass

	def onList(self, evt):
		gui.mainFrame.prePopup()
		d = FeedsDialog(gui.mainFrame)
		d.Show()
		gui.mainFrame.postPopup()

	def onReadFirstFeed(self, evt):
		try:
			self._feed = Feed(address)
		except Exception as e:
			ui.message(cannotReport)
			return
		ui.message(self._feed.getArticleTitle())

	def onReadFeedsFileManager(self, evt):
		gui.mainFrame._popupSettingsDialog(ReadFeedsManagerDialog)

	def script_readFirstFeed(self, gesture):
		self.onReadFirstFeed(None)
	# Translators: message presented in input mode.
	script_readFirstFeed.__doc__ = _("Refreshes the current feed and announces the most recent article title.")

	def script_readCurrentFeed(self, gesture):
		if not self._feed:
			ui.message(_("Refresh your selected feed to read the current article."))
			return
		feedInfo = u"{title}\r\n\r\n{address}".format(title=self._feed.getArticleTitle(), address=self._feed.getArticleLink())
		if scriptHandler.getLastScriptRepeatCount()==1 and api.copyToClip(feedInfo):
			# Translators: message presented when the information about an article of a feed is copied to the clipboard.
			ui.message(_("Copied to clipboard %s") % feedInfo)
		else:
			ui.message(feedInfo)
	# Translators: message presented in input mode.
	script_readCurrentFeed.__doc__ = _("Announces the title of the current article. Pressed two times, copies title and related link to the clipboard.")

	def script_readNextFeed(self, gesture):
		if not self._feed:
			ui.message(cannotReport)
			return
		self._feed.next()
		ui.message(self._feed.getArticleTitle())
	# Translators: message presented in input mode.
	script_readNextFeed.__doc__ = _("Announces the title of the next article.")

	def script_readPriorFeed(self, gesture):
		if not self._feed:
			ui.message(cannotReport)
			return
		self._feed.previous()
		ui.message(self._feed.getArticleTitle())
	# Translators: message presented in input mode.
	script_readPriorFeed.__doc__ = _("Announces the title of the previous article.")

	def script_reportLink(self, gesture):
		if not self._feed:
			ui.message(cannotReport)
			return
		feedLink = self._feed.getArticleLink()
		if scriptHandler.getLastScriptRepeatCount()==1:
			os.startfile(feedLink)
		else:
			ui.message(feedLink)
	# Translators: message presented in input mode.
	script_reportLink.__doc__ = _("Announces article link, when pressed two times, opens related web page.")

	def setAddressDialog(self):
		d = wx.TextEntryDialog(gui.mainFrame,
		# Translators: the label of a text entry dialog.
		_("Feed address to follow"),
		# Translators: the title of a text entry dialog.
		_("Feed address"),
		defaultValue=address)
		def callback(result):
			if result == wx.ID_OK:
				# Make sure this happens after focus returns to the document.
				wx.CallLater(100, self.doSetAddress, d.GetValue())
		gui.runScriptModalDialog(d, callback)

	def doSetAddress(self, text):
		if not text:
			return
		global address
		address=text
		self._feed = Feed(address)
		# Translators: message presented when the address of a feed has been selected.
		ui.message(_("Selected %s") % address)

	def script_setAddress(self, gesture):
		self.onSetAddress(None)
	# Translators: message presented in input mode.
	script_setAddress.__doc__ = _("Opens a dialog for entering a feed address.")

	def doSetAddressFile(self, file):
		if not file:
			return
		global address
		try:
			f = open (file, "r")
			address = f.read()
			f.close()
			# Translators: message presented when the address of a feed has been selected.
			ui.message(_("Selected %s") % address)
		except IOError:
			# Translators: message presented when unable to read feed address.
			ui.message(_("Unable to read feed address, feed can not be selected"))
			return
		self._Feed = Feed(address)

	def script_setAddressFile(self, gesture):
		self.onSetAddressFile(None)
	# Translators: message presented in input mode.
	script_setAddressFile.__doc__ = _("Opens a dialog for selecting a file containing a feed address.")

	def script_saveAddress(self, gesture):
		self.onSaveAddress(None)
	# Translators: message presented in input mode.
	script_saveAddress.__doc__ = _("Opens a dialog where you can enter a filename to which the current feed address will be saved.")

	__gestures = {
		"kb:control+shift+NVDA+8": "readFirstFeed",
		"kb:control+shift+NVDA+i": "readCurrentFeed",
		"kb:control+shift+NVDA+o": "readNextFeed",
		"kb:control+shift+NVDA+u": "readPriorFeed",
		"kb:control+shift+NVDA+space": "reportLink",
		"kb:control+shift+NVDA+enter": "setAddress",
		"kb:control+NVDA+enter": "setAddressFile",
		"kb:shift+NVDA+enter": "saveAddress",
	}

class ReadFeedsManagerDialog(gui.SettingsDialog):

	title = _("Feeds manager")

	def makeSettings(self, settingsSizer):
		foldersSizer = wx.BoxSizer(wx.VERTICAL)
		# Translators: the name of a dialog button.
		self.focusedCtrl = wx.Button(self, label = _("&Backup personal feeds folder..."))
		self.focusedCtrl.Bind(wx.EVT_BUTTON, self.onBrowseForBackupDirectory)
		foldersSizer.Add(self.focusedCtrl)
		# Translators: the name of a dialog button.
		ctrl = wx.Button(self, label=_("R&estore personal feeds..."))
		ctrl.Bind(wx.EVT_BUTTON, self.onBrowseForRestoreDirectory)
		foldersSizer.Add(ctrl)
		settingsSizer.Add(foldersSizer)

	def postInit(self):
		self.focusedCtrl.SetFocus()
	def onBrowseForBackupDirectory(self, evt):
		with wx.DirDialog(self,
		# Translators: the label of a dialog to select a folder.
		_("Select the folder where your personal feeds will be backed up."),
		configPath) as dlg:
			gui.mainFrame.prePopup()
			if dlg.ShowModal() == wx.ID_OK:
				gui.mainFrame.postPopup()
				copyPath = os.path.join(dlg.GetPath(), "personalFeeds")
				try:
					shutil.rmtree(copyPath, ignore_errors=True)
					shutil.copytree(_savePath, copyPath)
				except WindowsError:
					wx.CallAfter(gui.messageBox,
					## Translators: the label of an error dialog.
					_("Unable to backup folder"),
					# Translators: the title of an error dialog.
					_("Backup Error"),
					wx.OK|wx.ICON_ERROR)

	def onBrowseForRestoreDirectory(self, evt):
		feedsPath = os.path.join(configPath, "personalFeeds")
		with wx.DirDialog(self,
		# Translators: the label of a dialog to select a folder.
		_("Restore personal feeds from backup folder"),
		feedsPath, wx.DD_DIR_MUST_EXIST  | wx.DD_DEFAULT_STYLE) as dlg:
			gui.mainFrame.prePopup()
			if dlg.ShowModal() == wx.ID_OK:
				gui.mainFrame.postPopup()
				feedsPath = dlg.GetPath()
				try:
					shutil.rmtree(_savePath, ignore_errors=True)
					shutil.copytree(feedsPath, _savePath)
				except WindowsError:
					wx.CallAfter(gui.messageBox,
					# Translators: the label of an error dialog.
					_("Folder not restored"),
					# Translators: the title of an error dialog.
					_("Restore Error"),
					wx.OK|wx.ICON_ERROR)
