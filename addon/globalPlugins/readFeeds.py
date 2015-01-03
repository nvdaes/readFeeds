# -*- coding: UTF-8 -*-

# Read feeds: A simple plugin for reading feeds with NVDA
# Version: 6.0
# Used globalVars to get config path, for better results with temporary copies, as instantTranslate or SaveLog add-ons
# Version: 5.0
# Control instead of alt in gesture. Added installTask to update the add-on
# Version: 4.2
# Channel title and number of articles in News list dialog
# Date: 23/06/2012

import addonHandler
import globalPluginHandler
import languageHandler
import os
import sys
import shutil
import globalVars
import urllib
import scriptHandler
import api
import gui
import wx
import ui
from logHandler import log

sys.path.append(os.path.dirname(__file__))
from xml2.dom import minidom
del sys.path[-1]

addonHandler.initTranslation()

# Default address, used when addressFile cannot be read
address = 'http://rss.slashdot.org/Slashdot/slashdot'

# The root of the addon folder
_addonDir = os.path.join(os.path.dirname(__file__), "..").decode("mbcs")
_curAddon = addonHandler.Addon(_addonDir)
_addonSummary = _curAddon.manifest['summary']
_savePath = os.path.join(_addonDir, "globalPlugins", "personalFeeds")
# File containing the default feed address when the add-on starts
addressFile = os.path.join(_savePath, "addressFile.txt")
configPath = globalVars.appArgs.configPath

try:
	f = open(addressFile, "r")
	address = f.read()
	f.close()
except IOError:
	pass

# Translators: message presented when feeds cannot be reported.
cannotReport = _("Unable to refresh feed. Check your Internet conectivity or that the specified feed address is correct.")

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

	scriptCategory = unicode(_addonSummary)

	def __init__(self):
		super(globalPluginHandler.GlobalPlugin, self).__init__()
		self.menu = gui.mainFrame.sysTrayIcon.menu
		self.readFeedsMenu = wx.Menu()
		self.mainItem = self.menu.AppendSubMenu(self.readFeedsMenu,
		# Translators: the name of a submenu.
		_("&Read Feeds"),
		# Translators: the tooltip for a submenu.
		_("Manage feeds."))
		self.newsListItem = self.readFeedsMenu.Append(wx.ID_ANY,
		# Translators: the name of a menu item.
		_("Article &list..."),
		# Translators: the tooltip for a menu item.
		_("View article list"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onList, self.newsListItem)
		self.setAddressItem = self.readFeedsMenu.Append(wx.ID_ANY,
		# Translators: the name of a menu item.
		_("&Temporary feed address..."),
		# Translators: the tooltip for a menu item.
		_("View or choose current feed address"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onSetAddress, self.setAddressItem)
		self.setAddressFileItem = self.readFeedsMenu.Append(wx.ID_ANY,
		# Translators: the name of a menu item.
		_("L&oad feed address from file..."),
		# Translators: the tooltip for a menu item.
		_("Select file which contains feed address."))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onSetAddressFile, self.setAddressFileItem)
		self.saveAddressItem = self.readFeedsMenu.Append(wx.ID_ANY,
		# Translators: the name of a menu item.
		_("Save current feed address to file..."),
		# Translators: the tooltip for a menu item.
		_("Save current feed address to file"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onSaveAddress, self.saveAddressItem)
		self.readFirstItem = self.readFeedsMenu.Append(wx.ID_ANY,
		# Translators: the name of a menu item.
		_("R&efresh current feed"),
		# Translators: the tooltip for a menu item.
		_("Checks for new articles for the current feed"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onReadFirstFeed, self.readFirstItem)
		self.ReadFeedsFileManagerItem = self.readFeedsMenu.Append(wx.ID_ANY,
		# Translators: the name of a menu item.
		_("&ReadFeeds file manager..."),
		# Translators: the tooltip for a menu item.
		_("Opens the ReadFeedsFileManager dialog"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onReadFeedsFileManager, self.ReadFeedsFileManagerItem)
		self._feed = None

	def terminate(self):
		try:
			self.menu.RemoveItem(self.mainItem)
		except wx.PyDeadObjectError:
			pass

	def onList(self, evt):
		try:
			self._feed = Feed(address)
		except:
			wx.CallAfter(gui.messageBox,
			cannotReport,
			# Translators: the title of an error dialog.
			_("Refresh Error"),
			wx.OK|wx.ICON_ERROR)
			return
		articleTitles = [self._feed.getArticleTitle(index) for index in range(0, self._feed.getNumberOfArticles())]
		dlg = wx.SingleChoiceDialog(gui.mainFrame,
		# Translators: the label of a single choice dialog.
		_("Open web page of selected article."),
		u"{title} ({itemNumber})".format(title=self._feed.getFeedName(), itemNumber=self._feed.getNumberOfArticles()), choices=articleTitles)
		dlg.SetSelection(0)
		gui.mainFrame.prePopup()
		try:
			result = dlg.ShowModal()
		except AttributeError:
			pass
		gui.mainFrame.postPopup()
		if result == wx.ID_OK:
			os.startfile(self._feed.getArticleLink(dlg.GetSelection()))

	def onSetAddress(self, evt):
		self.setAddressDialog()

	def onSetAddressFile(self, evt):
		self.setAddressFileDialog()

	def onSaveAddress(self, evt):
		self.saveAddressDialog()

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

	def setAddressFileDialog(self):
		d =wx.FileDialog(gui.mainFrame,
		# Translators: the label of a file dialog.
		_("Select feed address from file"),
		_savePath, "addressFile.txt", _("Text files (*.txt) |*.txt"), wx.FD_OPEN)
		def callback(result):
			if result == wx.ID_OK:
				# Make sure this happens after focus returns to the document.
				wx.CallLater(100, self.doSetAddressFile, d.GetPath())
		gui.runScriptModalDialog(d, callback)

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

	def saveAddressDialog(self):
		d =wx.FileDialog(gui.mainFrame,
		# Translators: the label of a file dialog.
		_("Save current feed address to file"),
		_savePath, "addressFile.txt", _("Text files (*.txt) | *.txt"), wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
		def callback(result):
			if result == wx.ID_OK:
				# Make sure this happens after focus returns to the document.
				wx.CallLater(200, self.doSaveAddress, d.GetPath())
		gui.runScriptModalDialog(d, callback)

	def doSaveAddress(self, file):
		if not file:
			return
		try:
			f = open (file, "w")
			f.write(address)
			f.close()
			# Translators: message presented when the address of a feed has been saved.
			ui.message(_("Saved %s") % address)
		except IOError:
			# Translators: Message presented when the feed address cannot be saved.
			ui.message(_("Feed address can not be saved"))

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
