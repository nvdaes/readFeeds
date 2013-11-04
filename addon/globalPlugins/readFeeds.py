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


class Feed:

	def __init__(self, range):
		# The URL of the feed
		# Our actual XML document
		try:
			document = minidom.parse(urllib.urlopen(address))
		except:
			self.counter = -1
			self.titlesList = []
			self.title = ""
			self.linksList = []
			self.link = ""
			self.channelName = ""
			return
		index = 0
		self.counter = 0
		self.titlesList = []
		self.linksList = []
		channel = document.getElementsByTagName('channel')
		if len(channel)==1:
			self.RSSArticles = True
		else:
			self.RSSArticles = False
			channel = document.getElementsByTagName('feed')
			if len(channel) <= 0:
				self.counter = -1
				return
		channelTitle = channel[0].getElementsByTagName('title')[0].firstChild
		if channelTitle is None:
			self.channelName = ""
		else:
			self.channelName = channelTitle.data
		# if self.channelName is None or self.channelName == "":
			# ui.message(_("Untitled feed"))
		if self.RSSArticles:
			articles = document.getElementsByTagName('item')
		else:
			articles = document.getElementsByTagName('entry')
			if len(articles) == 0:
				self.counter = -1
				return
		title = None
		link = None
		for item in articles:
			self.counter +=1
			try:
				title = item.getElementsByTagName('title')[0].firstChild.data
			except:
				pass
			if title is None or title == "":
				self.counter = -1
				# Translators: message presented when the current feed has untitled items.
				ui.message(_("This feed contains untitled articles or the titles cannot be retrieved."))
				return
			self.titlesList.append(title)
			if self.RSSArticles:
				try:
					link = item.getElementsByTagName('link')[0].firstChild.data
				except:
					pass
			else:
				try:
					link = item.getElementsByTagName('link')[0].getAttribute('href')
				except:
					pass
			if link is None or link == "":
				self.counter = -1
				# Translators: message presented when the current feed contains items without a recognized link.
				ui.message(_("This feed contains articles without related links or the links cannot be retrieved."))
				return
			self.linksList.append(link)
			if index <= range:
				self.title = title
				self.link = link
				# self.creator = item.getElementsByTagName('dc:creator')[0].firstChild.data
				index +=1

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
		self.copyFeedsItem = self.readFeedsMenu.Append(wx.ID_ANY,
		# Translators: the name of a menu item, which will backup the users feeds.
		_("&Backup personal feeds folder..."),
		# Translators: the tooltip for a menu item.
		_("Backs up your personal feeds folder"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onCopyFeeds, self.copyFeedsItem)
		self.restoreFeedsItem = self.readFeedsMenu.Append(wx.ID_ANY,
		# Translators: the name of a menu item.
		_("R&estore personal feeds..."),
		# Translators: the tooltip for a menu item.
		_("Restore previously saved feeds"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onRestoreFeeds, self.restoreFeedsItem)
		self.aboutItem = self.readFeedsMenu.Append(wx.ID_ANY,
		# Translators: the name of a menu item.
		_("Open &documentation"),
		# Translators: the tooltip for a menu item.
		_("Open documentation in the current language"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onAbout, self.aboutItem)
		self._counter = -1
		self._titlesList = []
		self._linksList = []
		self._index = 0
		self._channelName = ""

	def terminate(self):
		try:
			self.menu.RemoveItem(self.mainItem)
		except wx.PyDeadObjectError:
			pass

	def onList(self, evt):
		self._index = 0
		self._RSS = Feed(self._index)
		self._counter = self._RSS.counter
		if self.getCounter() == -1:
			wx.CallAfter(gui.messageBox,
			cannotReport,
			# Translators: the title of an error dialog.
			_("Refresh Error"),
			wx.OK|wx.ICON_ERROR)
			return
		self._titlesList = self._RSS.titlesList
		self._linksList = self._RSS.linksList
		self._channelName = self._RSS.channelName
		dlg = wx.SingleChoiceDialog(gui.mainFrame,
		# Translators: the label of a single choice dialog.
		_("Open web page of selected article."),
		u"{title} ({itemNumber})".format(title=self._channelName, itemNumber=len(self._titlesList)), choices=self._titlesList)
		dlg.SetSelection(0)
		gui.mainFrame.prePopup()
		try:
			result = dlg.ShowModal()
		except AttributeError:
			pass
		gui.mainFrame.postPopup()
		if result == wx.ID_OK:
			self._index = dlg.GetSelection()
			link = self._linksList[self._index]
			os.startfile(link)

	def onSetAddress(self, evt):
		self.setAddressDialog()

	def onSetAddressFile(self, evt):
		self.setAddressFileDialog()

	def onSaveAddress(self, evt):
		self.saveAddressDialog()

	def onReadFirstFeed(self, evt):
		self._index = 0
		self._RSS = Feed(self._index)
		self._counter = self._RSS.counter
		if self.getCounter() == -1:
			self._titlesList = []
			self._linksList = []
			self._channelName = ""
			ui.message(cannotReport)
			return
		self._titlesList = self._RSS.titlesList
		self._linksList = self._RSS.linksList
		self._channelName = self._RSS.channelName
		ui.message(self._RSS.title)

	def onCopyFeeds(self, evt):
		dlg = wx.DirDialog(gui.mainFrame,
		# Translators: the label of a dialog to select a folder.
		_("Select the folder where your personal feeds will be backed up."),
		configPath, wx.DD_DEFAULT_STYLE)
		gui.mainFrame.prePopup()
		result = dlg.ShowModal()
		gui.mainFrame.postPopup()
		if result == wx.ID_OK:
			copyPath = os.path.join(dlg.GetPath(), "RSS")
			try:
				shutil.rmtree(copyPath, ignore_errors=True)
				shutil.copytree(_savePath, copyPath)
			except WindowsError:
				wx.CallAfter(gui.messageBox,
				# Translators: the label of an error dialog.
				_("Unable to backup folder"),
				# Translators: the title of an error dialog.
				_("Backup Error"),
				wx.OK|wx.ICON_ERROR)

	def onRestoreFeeds(self, evt):
		feedsPath = os.path.join(configPath, "RSS")
		dlg = wx.DirDialog(gui.mainFrame,
		# Translators: the label of a dialog to select a folder.
		_("Restore personal feeds from backup folder"), feedsPath, wx.DD_DIR_MUST_EXIST | wx.DD_DEFAULT_STYLE)
		gui.mainFrame.prePopup()
		result = dlg.ShowModal()
		gui.mainFrame.postPopup()
		if result == wx.ID_OK:
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

	def getDocFolder(self):
		langs = [languageHandler.getLanguage(), "en"]
		for lang in langs:
			docFolder = os.path.join(os.path.dirname(__file__), "..", "doc", lang)
			if os.path.isdir(docFolder):
				return docFolder
			if "_" in lang:
				tryLang = lang.split("_")[0]
				docFolder = os.path.join(os.path.dirname(__file__), "..", "doc", tryLang)
				if os.path.isdir(docFolder):
					return docFolder
				if tryLang == "en":
					break
			if lang == "en":
				break
		return None

	def getDocPath(self, docFileName):
		docPath = self.getDocFolder()
		if docPath is not None:
			docFile = os.path.join(docPath, docFileName)
			if os.path.isfile(docFile):
				docPath = docFile
		return docPath

	def onAbout(self, evt):
		try:
			os.startfile(self.getDocPath("readme.html"))
		except WindowsError:
			pass

	def getCounter(self):
		return self._counter

	def getFeed(self):
		# feed = ""
		feed = self._titlesList[self._index]
		return feed

	def script_readFirstFeed(self, gesture):
		self.onReadFirstFeed(None)
	# Translators: message presented in input mode.
	script_readFirstFeed.__doc__ = _("Refreshes the current feed and reads the most recent article title.")

	def script_readCurrentFeed(self, gesture):
		if self.getCounter() == -1:
			ui.message(cannotReport)
			return
		feed = self.getFeed()
		link = self._linksList[self._index]
		feedLink = u"{title}\r\n\r\n{address}".format(title=feed, address=link)
		if scriptHandler.getLastScriptRepeatCount()==1 and api.copyToClip(feedLink):
			# Translators: message presented when the link of a feed is copied to the clipboard.
			ui.message(_("Copied to clipboard %s") % feedLink)
		else:
			ui.message(feed)
	# Translators: message presented in input mode.
	script_readCurrentFeed.__doc__ = _("Reads the title of the current article. Pressed two times, copies related link to the clipboard.")

	def script_readNextFeed(self, gesture):
		if self.getCounter() == -1:
			ui.message(cannotReport)
			return
		if self._index >= self.getCounter()-1:
			self._index = 0
		else:
			self._index += 1
		ui.message(self.getFeed())
	# Translators: message presented in input mode.
	script_readNextFeed.__doc__ = _("Reads the title of the next article.")

	def script_readPriorFeed(self, gesture):
		if self.getCounter() == -1:
			ui.message(cannotReport)
			return
		if self._index <= 0:
			self._index = self.getCounter()-1
		else:
			self._index -=1
		ui.message(self.getFeed())
	# Translators: message presented in input mode.
	script_readPriorFeed.__doc__ = _("Reads the title of the previous article.")

	def script_reportLink(self, gesture):
		if self.getCounter() == -1:
			ui.message(cannotReport)
			return
		feedLink = self._linksList[self._index]
		if scriptHandler.getLastScriptRepeatCount()==1:
			os.startfile(feedLink)
		else:
			ui.message(feedLink)
	# Translators: message presented in input mode.
	script_reportLink.__doc__ = _("Reads article link, when pressed two times, opens related web page.")

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
		self._index = 0
		self._RSS =Feed(self._index)
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
		self._index = 0
		self._RSS =Feed(self._index)

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
		global address
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
