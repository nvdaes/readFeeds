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

address = 'http://rss.slashdot.org/Slashdot/slashdot' # Default address
_savePath = os.path.join(os.path.dirname(__file__), "RSS")
addressFile = os.path.join(_savePath, "addressFile.txt")
configPath = globalVars.appArgs.configPath

try:
	f = open(addressFile, "r")
	address = f.read()
	f.close()
except IOError:
	pass

class Feed:

	def __init__(self, range):
		# The URL of the RSS feed
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
		for item in articles:
			self.counter +=1
			title = item.getElementsByTagName('title')[0].firstChild.data
			if title is None or title == "":
				self.counter = -1
				# Translators: message presented when the current feed has untitled items.
				ui.message(_("This feed contains untitled items"))
				return
			self.titlesList.append(title)
			if self.RSSArticles:
				link = item.getElementsByTagName('link')[0].firstChild.data
			else:
				link = item.getElementsByTagName('link')[0].getAttribute('href')
			if link is None or link == "":
				self.counter = -1
				# Translators: message presented when the current feed contains items without a link.
				ui.message(_("This feed contains items without a link"))
				return
			self.linksList.append(link)
			if index <= range:
				self.title = title
				self.link = link
				# self.creator = item.getElementsByTagName('dc:creator')[0].firstChild.data
				index +=1

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self):
		super(globalPluginHandler.GlobalPlugin, self).__init__()
		self.menu = gui.mainFrame.sysTrayIcon.menu
		self.readFeedsMenu = wx.Menu()
		self.mainItem = self.menu.AppendSubMenu(self.readFeedsMenu,
		# Translators: the name of a submenu.
		_("&Read feeds"),
		# Translators: the tooltip for a submenu.
		"Manage RSS and Atom feeds")
		self.newsListItem = self.readFeedsMenu.Append(wx.ID_ANY,
		# Translators: the name of a menu item.
		_("News &list..."),
		# Translators: the tooltip for a menu item.
		_("View news list"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onList, self.newsListItem)
		self.setAddressItem = self.readFeedsMenu.Append(wx.ID_ANY,
		# Translators: the name of a menu item.
		_("&Temporary address..."),
		# Translators: the tooltip for a menu item.
		_("View or choose current feed address"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onSetAddress, self.setAddressItem)
		self.setAddressFileItem = self.readFeedsMenu.Append(wx.ID_ANY,
		# Translators: the name of a menu item.
		_("L&oad saved address..."),
		# Translators: the tooltip for a menu item.
		_("Choose file containing address"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onSetAddressFile, self.setAddressFileItem)
		self.saveAddressItem = self.readFeedsMenu.Append(wx.ID_ANY,
		# Translators: the name of a menu item.
		_("Save current address..."),
		# Translators: the tooltip for a menu item.
		_("Copy current address to text file"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onSaveAddress, self.saveAddressItem)
		self.readFirstItem = self.readFeedsMenu.Append(wx.ID_ANY,
		# Translators: the name of a menu item.
		_("Updat&e current feed"),
		# Translators: the tooltip for a menu item.
		_("Reload current feed"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onReadFirstFeed, self.readFirstItem)
		self.copyFeedsItem = self.readFeedsMenu.Append(wx.ID_ANY,
		# Translators: the name of a menu item.
		_("&Copy feeds folder..."),
		# Translators: the tooltip for a menu item.
		_("Backup of feeds folder"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onCopyFeeds, self.copyFeedsItem)
		self.restoreFeedsItem = self.readFeedsMenu.Append(wx.ID_ANY,
		# Translators: the name of a menu item.
		_("R&estore feeds..."),
		# Translators: the tooltip for a menu item.
		_("Restore previously saved feeds"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onRestoreFeeds, self.restoreFeedsItem)
		self.aboutItem = self.readFeedsMenu.Append(wx.ID_ANY,
		# Translators: the name of a menu item.
		_("Open &documentation"),
		# Translators: the tooltip for a menu item.
		_("Open documentation for current language"))
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
			# Translators: the label of an error dialog.
			_("Feeds can not be reported. Check your Internet conectivity or specified address"),
			# Translators: the title of an error dialog.
			_("Update Error"),
			wx.OK|wx.ICON_ERROR)
			return
		self._titlesList = self._RSS.titlesList
		self._linksList = self._RSS.linksList
		self._channelName = self._RSS.channelName
		dlg = wx.SingleChoiceDialog(gui.mainFrame,
		# Translators: the label of a single choice dialog.
		_("Open the web page for reading your selected article"),
		"%s (%d)" % (self._channelName, len(self._titlesList)), choices=self._titlesList)
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
			# Translators: message presented when feeds cannot be reported.
			ui.message(_("Feeds can not be reported. Check your Internet conectivity or specified address"))
			return
		self._titlesList = self._RSS.titlesList
		self._linksList = self._RSS.linksList
		self._channelName = self._RSS.channelName
		ui.message(self._RSS.title)

	def onCopyFeeds(self, evt):
		dlg = wx.DirDialog(gui.mainFrame,
		# Translators: the label of a dialog to select a folder.
		_("Select a folder for copying your saved feeds"),
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
				_("Folder not copied"),
				# Translators: the title of an error dialog.
				_("Copy Error"),
				wx.OK|wx.ICON_ERROR)

	def onRestoreFeeds(self, evt):
		feedsPath = os.path.join(configPath, "RSS")
		dlg = wx.DirDialog(gui.mainFrame,
		# Translators: the label of a dialog to select a folder.
		_("Select the feeds folder you wish to restore"), feedsPath, wx.DD_DIR_MUST_EXIST | wx.DD_DEFAULT_STYLE)
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
				_("Folder not copied"),
				# Translators: the title of an error dialog.
				_("Copy Error"),
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
	script_readFirstFeed.__doc__ = _("Updates the selected channel and reads the first feed title.")

	def script_readCurrentFeed(self, gesture):
		if self.getCounter() == -1:
			# Translators: message presented when feeds cannot be reported.
			ui.message(_("Feeds can not be reported. Check your Internet conectivity or specified address"))
			return
		feed = self.getFeed()
		link = self._linksList[self._index]
		feedLink = "%s\r\n\r\n%s" % (feed, link)
		if scriptHandler.getLastScriptRepeatCount()==1 and api.copyToClip(feedLink):
			# Translators: message presented when the link of a feed is copied to the clipboard.
			ui.message(_("Copied to clipboard %s") % feedLink)
		else:
			ui.message(feed)
	# Translators: message presented in input mode.
	script_readCurrentFeed.__doc__ = _("Reads the title of the current feed. Pressed two times, copies the text to the clipboard.")

	def script_readNextFeed(self, gesture):
		if self.getCounter() == -1:
			# Translators: message presented when feeds cannot be reported.
			ui.message(_("Feeds can not be reported. Check your Internet conectivity or specified address"))
			return
		if self._index >= self.getCounter()-1:
			self._index = 0
		else:
			self._index += 1
		ui.message(self.getFeed())
	# Translators: message presented in input mode.
	script_readNextFeed.__doc__ = _("Reads the title of the next feed.")

	def script_readPriorFeed(self, gesture):
		if self.getCounter() == -1:
			# Translators: message presented when feeds cannot be reported.
			ui.message(_("Feeds can not be reported. Check your Internet conectivity or specified address"))
			return
		if self._index <= 0:
			self._index = self.getCounter()-1
		else:
			self._index -=1
		ui.message(self.getFeed())
	# Translators: message presented in input mode.
	script_readPriorFeed.__doc__ = _("Reads the prior feed title.")

	def script_reportLink(self, gesture):
		if self.getCounter() == -1:
			# Translators: message presented when feeds cannot be reported.
			ui.message(_("Feeds can not be reported. Check your Internet conectivity or specified address"))
			return
		feedLink = self._linksList[self._index]
		if scriptHandler.getLastScriptRepeatCount()==1:
			os.startfile(feedLink)
		else:
			ui.message(feedLink)
	# Translators: message presented in input mode.
	script_reportLink.__doc__ = _("Reads the article link, that allows open its web page. Pressed two times, opens the web.")

	def setAddressDialog(self):
		d = wx.TextEntryDialog(gui.mainFrame,
		# Translators: the label of a text entry dialog.
		_("The address of the channel you wish to follow"),
		# Translators: the title of a text entry dialog.
		_("Address"),
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
	script_setAddress.__doc__ = _("Opens a dialog for setting the address of the feeds channel.")

	def setAddressFileDialog(self):
		d =wx.FileDialog(gui.mainFrame,
		# Translators: the label of a file dialog.
		_("Choose a file containing a channel address"),
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
			# Translators: message presented when cannot select the address of a feed.
			ui.message(_("Address can not be selected"))
			return
		self._index = 0
		self._RSS =Feed(self._index)

	def script_setAddressFile(self, gesture):
		self.onSetAddressFile(None)
	# Translators: message presented in input mode.
	script_setAddressFile.__doc__ = _("Opens a dialog for setting the address of the feeds channel from a selected file.")

	def saveAddressDialog(self):
		d =wx.FileDialog(gui.mainFrame,
		# Translators: the label of a file dialog.
		_("File for saving your current address"),
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
			# Translators: message presented when cannot save the address of a feed.
			ui.message(_("Address can not be saved"))

	def script_saveAddress(self, gesture):
		self.onSaveAddress(None)
	# Translators: message presented in input mode.
	script_saveAddress.__doc__ = _("Opens a dialog for saving a file containing the selected address.")

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