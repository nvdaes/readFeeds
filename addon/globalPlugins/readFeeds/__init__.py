# -*- coding: UTF-8 -*-

# Read feeds: A simple plugin for reading feeds with NVDA
# Copyright (C) 2012-2021 Noelia Ruiz Martínez, Mesar Hameed
# Released under GPL 2

import os
import shutil
import addonHandler
import globalPluginHandler
import globalVars
import config
import urllib.request
import scriptHandler
from scriptHandler import script
import api
import gui
from gui import SettingsPanel, NVDASettingsDialog, guiHelper
import core
import wx
import ui
from globalCommands import SCRCAT_CONFIG
from logHandler import log
import re
from .skipTranslation import translate
from .xml.etree import ElementTree
import languageHandler
import time
import datetime
import locale

addonHandler.initTranslation()

# Constants

ADDON_SUMMARY = addonHandler.getCodeAddon().manifest['summary']
ADDON_PANEL_TITLE = ADDON_SUMMARY
FEEDS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "personalFeeds"))
OPML_PATH = os.path.join(FEEDS_PATH, "readFeeds.opml")
HTML_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "html"))
CONFIG_PATH = globalVars.appArgs.configPath
DEFAULT_ADDRESS_FILE = "addressFile"
CAN_NOT_REPORT = _(
	# Translators: message presented when feeds cannot be reported.
	"Unable to refresh feed. Check your Internet conectivity or that the specified feed address is correct."
)
TAG_REGEXP = re.compile('<.*?>')

# Configuration

confspec = {
	"addressFile": "string(default=addressFile)",
	"filterAfterList": "boolean(default=False)",
}
config.conf.spec["readFeeds"] = confspec


def onSettings(evt):
	gui.mainFrame._popupSettingsDialog(NVDASettingsDialog, AddonSettingsPanel)

# Dialogs


def getActiveProfile():
	activeProfile = config.conf.profiles[-1].name
	if not activeProfile:
		# Message translated in NVDA core.
		activeProfile = translate("normal configuration")
	return activeProfile


def doCopy(copyDirectory):
	# to ensure that the removed directory will not be one of the main directories
	# such as documents or music or other important ones
	if not os.path.basename(copyDirectory) == "personalFeeds":
		copyDirectory = os.path.join(copyDirectory, "personalFeeds")
	try:
		if os.path.exists(copyDirectory):
			# if it exists, only personalFeeds folder will be removed, which is the base name of copyDirectory
			shutil.rmtree(copyDirectory, ignore_errors=True)
		shutil.copytree(FEEDS_PATH, copyDirectory)
		core.callLater(
			100, ui.message,
			# Translators: Message presented when feeds have been copied.
			_("Feeds copied")
		)
	except Exception as e:
		wx.CallAfter(
			gui.messageBox,
			# Translators: label of error dialog shown when cannot copy feeds folder.
			_("Folder not copied"),
			# Translators: title of error dialog shown when cannot copy feeds folder.
			_("Copy Error"),
			wx.OK | wx.ICON_ERROR
		)
		raise e


def doRestore(restoreDirectory):
	try:
		shutil.rmtree(FEEDS_PATH, ignore_errors=True)
		shutil.copytree(restoreDirectory, FEEDS_PATH)
		core.callLater(
			100, ui.message,
			# Translators: Message presented when feeds have been restored.
			_("Feeds restored")
		)
	except Exception as e:
		wx.CallAfter(
			gui.messageBox,
			# Translators: label of error dialog shown when cannot copy feeds folder.
			_("Folder not copied"),
			# Translators: title of error dialog shown when cannot copy feeds folder.
			_("Copy Error"),
			wx.OK | wx.ICON_ERROR
		)
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
		addressFile = config.conf["readFeeds"]["addressFile"]
		self._opml = Opml(OPML_PATH)
		super(FeedsDialog, self).__init__(
			# Translators: Title of a dialog.
			parent, title=_("Feeds: {file} ({profile})".format(file=addressFile, profile=getActiveProfile()))
		)

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		sHelper = guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)
		# Translators: Label of a dialog (message translated in NVDA's core in different contexts).
		searchTextLabel = _("&Filter by:")
		if not config.conf["readFeeds"]["filterAfterList"]:
			self.searchTextEdit = sHelper.addLabeledControl(searchTextLabel, wx.TextCtrl)

		feedsListGroupSizer = wx.StaticBoxSizer(wx.StaticBox(self), wx.HORIZONTAL)
		feedsListGroupContents = wx.BoxSizer(wx.HORIZONTAL)
		changeFeedsSizer = wx.BoxSizer(wx.VERTICAL)

		self.choices = [outline.get("title") for outline in self._opml._document.getroot().iter("outline")]
		self.feedsList = wx.ListBox(
			self, choices=self.choices
		)
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

		feedsListGroupContents.Add(changeFeedsSizer, flag=wx.EXPAND)
		feedsListGroupContents.AddSpacer(guiHelper.SPACE_BETWEEN_ASSOCIATED_CONTROL_HORIZONTAL)

		if config.conf["readFeeds"]["filterAfterList"]:
			self.searchTextEdit = sHelper.addLabeledControl(searchTextLabel, wx.TextCtrl)

		self.searchTextEdit.Bind(wx.EVT_TEXT, self.onSearchEditTextChange)

		buttonHelper = guiHelper.ButtonHelper(wx.VERTICAL)
		# Translators: The label of a button to open a feed.
		self.openButton = buttonHelper.addButton(self, label=_("&Open feed"))
		self.openButton.Bind(wx.EVT_BUTTON, self.onOpen)

		# Translators: The label of a button to open a feed as HTML.
		self.openHtmlButton = buttonHelper.addButton(self, label=_("Open feed as &HTML"))
		self.openHtmlButton.Bind(wx.EVT_BUTTON, self.onOpenHtml)

		# Translators: The label of a button to copy the feed URL.
		self.copyButton = buttonHelper.addButton(self, label=_("Cop&y feed address"))
		self.copyButton.Bind(wx.EVT_BUTTON, self.onCopy)

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

		# Translators: The label of a button to open a folder containing a backup of feeds.
		self.openFolderButton = buttonHelper.addButton(self, label=_("Open &folder containing a backup of feeds"))
		self.openFolderButton.Bind(wx.EVT_BUTTON, self.onOpenFolder)

		# Translators: The label of a button to import feeds from OPML.
		self.importButton = buttonHelper.addButton(self, label=_("&Import feeds from OPML file"))
		self.importButton.Bind(wx.EVT_BUTTON, self.onImportOpml)

		# Translators: The label of a button to open the settings dialog for readFeeds.
		self.settingsButton = buttonHelper.addButton(self, label=_("&Preferences..."))
		self.settingsButton.Bind(wx.EVT_BUTTON, onSettings)
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
		self.feedsList.SetFocus()
		self.CentreOnScreen()

	def __del__(self):
		FeedsDialog._instance = None

	def createFeed(self, address):
		try:
			feed = Feed(address)
		except Exception as e:
			wx.CallAfter(
				gui.messageBox,
				# Translators: Message presented when a feed cannot be added.
				_('Cannot add feed: %s' % e),
				# Translators: error message.
				_("Error"),
				wx.OK | wx.ICON_ERROR
			)
			raise e
		feedName = feed.getFeedName().strip()
		self._opml.addFeed(feedName, address)
		return feedName

	def onSearchEditTextChange(self, evt):
		self.feedsList.Clear()
		# Based on the filter of the Input gestures dialog of NVDA's core.
		filter = self.searchTextEdit.Value
		if filter:
			filter = re.escape(filter)
			filterReg = re.compile(r"(?=.*?" + r")(?=.*?".join(filter.split(r"\ ")) + r")", re.U | re.IGNORECASE)
		for choice in self.choices:
			if filter and not filterReg.match(choice):
				continue
			self.feedsList.Append(choice)
		try:
			self.feedsList.Selection = 0
			self.onFeedsListChoice(None)
		except Exception:
			for control in (
				self.feedsList, self.articlesButton, self.openButton,
				self.renameButton, self.deleteButton, self.defaultButton
			):
				control.disable

	def onFeedsListChoice(self, evt):
		self.feedsList.Enable()
		self.sel = self.feedsList.Selection
		self.stringSel = self.feedsList.StringSelection
		self.articlesButton.Enabled = self.sel >= 0
		self.openButton.Enabled = self.sel >= 0
		self.openHtmlButton.Enabled = self.sel >= 0
		self.deleteButton.Enabled = (
			self.sel >= 0 and self.stringSel != DEFAULT_ADDRESS_FILE
			and config.conf["readFeeds"]["addressFile"] != self.stringSel
		)
		self.renameButton.Enabled = (
			self.sel >= 0 and self.stringSel != DEFAULT_ADDRESS_FILE
			and config.conf["readFeeds"]["addressFile"] != self.stringSel
		)
		self.defaultButton.Enabled = (
			self.sel >= 0 and self.stringSel != config.conf["readFeeds"]["addressFile"]
		)

	def onArticles(self, evt):
		address = self._opml._document.getroot().findall("./body/outline")[self.sel].get("xmlUrl")
		self.feed = Feed(address)
		self.Disable()
		try:
			ArticlesDialog(self).Show()
		except Exception as e:
			self.Enable()
			raise e

	def onOpen(self, evt):
		address = self._opml._document.getroot().findall("./body/outline")[self.sel].get("xmlUrl")
		os.startfile(address)

	def onOpenHtml(self, evt):
		address = self._opml._document.getroot().findall("./body/outline")[self.sel].get("xmlUrl")
		self.feed = Feed(address)
		self.feed.buildHtml()
		os.startfile(os.path.join(HTML_PATH, "feed.html"))

	def onCopy(self, evt):
		address = self._opml._document.getroot().findall("./body/outline")[self.sel].get("xmlUrl")
		if gui.messageBox(
			# Translators: the label of a message box dialog.
			_("Do you want to copy feed address to the clipboard\r\n\r\n{feedAddress}?".format(feedAddress=address)),
			# Translators: the title of a message box dialog.
			_("Copy feed address"),
			wx.YES | wx.NO | wx.CANCEL | wx.ICON_QUESTION
		) == wx.YES:
			api.copyToClip(address)

	def onNew(self, evt):
		# Translators: The label of a field to enter an address for a new feed.
		with wx.TextEntryDialog(
			# Translators: Label of a dialog.
			self, _("Address of a new feed:"),
			# Translators: The title of a dialog to create a new feed.
			_("New feed")
		) as d:
			if d.ShowModal() == wx.ID_CANCEL:
				self.feedsList.SetFocus()
				return
			name = self.createFeed(d.Value)
			self.feedsList.Append(name)
			self.feedsList.SetFocus()

	def onDelete(self, evt):
		if gui.messageBox(
			# Translators: The confirmation prompt displayed when the user requests to delete a feed.
			_("Are you sure you want to delete this feed? This cannot be undone."),
			# Message translated in NVDA core.
			translate("Confirm Deletion"),
			wx.YES | wx.NO | wx.ICON_QUESTION, self
		) == wx.NO:
			self.feedsList.SetFocus()
			return
		element = self._opml._document.getroot().findall("./body/outline")[self.sel]
		self._opml._document.getroot().find("body").remove(element)
		self._opml._document.write(OPML_PATH)
		self.feedsList.Delete(self.sel)
		self.onFeedsListChoice(None)
		self.feedsList.SetFocus()

	def onDefault(self, evt):
		config.conf["readFeeds"]["addressFile"] = self.stringSel
		self.onFeedsListChoice(None)
		self.feedsList.SetFocus()

	def onRename(self, evt):
		with wx.TextEntryDialog(
			# Translators: The label of a field to enter a new name for a feed.
			self, _("New name:"),
			# Translators: The title of a dialog to rename a feed.
			_("Rename feed"), value=self.stringSel
		) as d:
			if d.ShowModal() == wx.ID_CANCEL or not d.Value:
				self.feedsList.SetFocus()
				return
			newName = d.Value
			element = self._opml._document.getroot().findall(".body/outline")[self.sel]
			element.set("title", newName)
			self._opml._document.write(OPML_PATH)
		self.feedsList.SetString(self.sel, newName)
		self.feedsList.SetFocus()

	def onClose(self, evt):
		self.Destroy()
		FeedsDialog._instance = None

	def onOpenFolder(self, evt):
		path = os.path.join(CONFIG_PATH, "personalFeeds")
		if not os.path.isdir(path):
			os.makedirs(path)
		os.startfile(path)

	def onImportOpml(self, evt):
		with wx.FileDialog(
			# Translators: Label for a file dialog.
			self, _("Open OPML file"),
			# Translators: Wildcards for a file dialog
			wildcard=_("OPML files (*.opml)|*.opml"),
			style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
		) as fileDialog:
			if fileDialog.ShowModal() == wx.ID_CANCEL:
				return
			pathname = fileDialog.GetPath()
		opml = Opml(pathname)
		feeds = opml._document.getroot().findall("./body/outline")
		body = self._opml._document.getroot().find("body")
		for feed in feeds:
			body.append(feed)
		outlines = sorted(body.findall("outline"), key=lambda el: el.get("title"))
		for outline in outlines:
			body.remove(outline)
			body.append(outline)
		self._opml._document.write(OPML_PATH)
		self.feedsList.Clear()
		for outline in outlines:
			self.feedsList.Append(outline.get("title"))
		self.feedsList.Selection = 0
		self.feedsList.SetFocus()


class ArticlesDialog(wx.Dialog):

	def __init__(self, parent):
		# Translators: The title of the articles dialog.
		super(ArticlesDialog, self).__init__(parent, title="{feedTitle} ({feedNumber})".format(
			feedTitle=parent.stringSel, feedNumber=parent.feed.getNumberOfArticles()
		))

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		sHelper = guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)

		# Translators: The label of the articles list in the articles dialog.
		articlesText = _("List of articles")
		articlesChoices = [re.sub(
			TAG_REGEXP, '',
			parent.feed.getArticleTitle(index)) for index in range(parent.feed.getNumberOfArticles()
		)]
		self.articlesList = sHelper.addLabeledControl(articlesText, wx.ListBox, choices=articlesChoices)
		self.articlesList.Selection = 0
		self.articlesList.Bind(wx.EVT_CHOICE, self.onArticlesListChoice)

		buttonHelper = guiHelper.ButtonHelper(wx.VERTICAL)
		# Translators: The label of a button to open the selected article of a feed.
		self.articleButton = wx.Button(self, label=_("Open &web page of selected article."))
		self.articleButton.Bind(wx.EVT_BUTTON, self.onArticlesListChoice)
		self.AffirmativeId = self.articleButton.Id
		self.articleButton.SetDefault()
		buttonHelper.addButton(self.articleButton)
		
		# Translators: The label of a button to show information of a feed article.
		self.infoButton = wx.Button(self, label=_("&About article..."))
		self.infoButton.Bind(wx.EVT_BUTTON, self.onArticlesListInfo)
		buttonHelper.addButton(self.infoButton)
		
		closeButton = sHelper.addDialogDismissButtons(wx.Button(self, wx.ID_CLOSE, label=translate("&Close")))
		closeButton.Bind(wx.EVT_BUTTON, lambda evt: self.Close())
		self.Bind(wx.EVT_CLOSE, self.onClose)
		self.EscapeId = wx.ID_CLOSE
		mainSizer.Add(buttonHelper.sizer)
		mainSizer.Add(sHelper.sizer, border=guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.CentreOnScreen()

	def onArticlesListChoice(self, evt):
		os.startfile(self.Parent.feed.getArticleLink(self.articlesList.Selection))

	def onArticlesListInfo(self, evt):
		articleInfo = "{title}\r\n\r\n{address}".format(
			title=self.articlesList.StringSelection,
			address=self.Parent.feed.getArticleLink(self.articlesList.Selection)
		)
		if gui.messageBox(
			# Translators: the label of a message box dialog.
			_("%sDo you want to copy article title and link to the clipboard?" % (articleInfo + "\r\n\r\n")),
			# Translators: the title of a message box dialog.
			_("Article information"),
			wx.YES | wx.NO | wx.CANCEL | wx.ICON_QUESTION
		) == wx.YES:
			api.copyToClip(articleInfo)

	def onClose(self, evt):
		self.Parent.Enable()
		self.Parent.feedsList.SetFocus()
		self.Destroy()


class CopyDialog(wx.Dialog):

	def __init__(self, parent):
		# Translators: The title of the Copy dialog.
		super(CopyDialog, self).__init__(parent, title=_("Copy feeds"))

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		sHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)

		# Translators: An informational message displayed in the Copy dialog.
		dialogCaption = _("Select a folder to save a backup of your current feeds")
		sHelper.addItem(wx.StaticText(self, label=dialogCaption))

		# Translators: The label of a grouping containing controls to select the destination directory
		# in the Copy dialog.
		directoryGroupText = _("directory for backup:")
		groupHelper = sHelper.addItem(
			gui.guiHelper.BoxSizerHelper(
				self, sizer=wx.StaticBoxSizer(wx.StaticBox(self, label=directoryGroupText), wx.VERTICAL)
			)
		)
		# Message translated in NVDA core.
		browseText = translate("Browse...")
		# Translators: The title of the dialog presented
		# when browsing for the destination directory when copying feeds.
		dirDialogTitle = _("Select directory to copy")
		directoryEntryControl = groupHelper.addItem(
			gui.guiHelper.PathSelectionHelper(self, browseText, dirDialogTitle)
		)
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
		self.CentreOnScreen()

	def onCopy(self, evt):
		if not self.copyDirectoryEdit.Value:
			# Message translated in NVDA core.
			gui.messageBox(
				translate("Please specify a directory."),
				# Message translated in NVDA core.
				translate("Error"),
				wx.OK | wx.ICON_ERROR)
			return
		drv = os.path.splitdrive(self.copyDirectoryEdit.Value)[0]
		if drv and not os.path.isdir(drv):
			gui.messageBox(
				# Message translated in NVDA core.
				translate("Invalid drive %s") % drv,
				# Message translated in NVDA core.
				translate("Error"),
				wx.OK | wx.ICON_ERROR
			)
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
		with wx.DirDialog(
			self._parent, self._browseForDirectoryTitle, defaultPath=startPath,
			style=wx.DD_DIR_MUST_EXIST | wx.DD_DEFAULT_STYLE
		) as d:
			if d.ShowModal() == wx.ID_OK:
				self._textCtrl.Value = d.Path


class RestoreDialog(wx.Dialog):

	def __init__(self, parent):
		# Translators: The title of the Restore dialog.
		super(RestoreDialog, self).__init__(parent, title=_("Restore feeds"))

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		sHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)

		# Translators: An informational message displayed in the Restore dialog.
		dialogCaption = _("Select a folder to restore a backup of your previous copied feeds")
		sHelper.addItem(wx.StaticText(self, label=dialogCaption))

		# Translators: The label of a grouping containing controls to select the destination directory
		# in the Restore dialog.
		directoryGroupText = _("directory containing backup:")
		groupHelper = sHelper.addItem(
			gui.guiHelper.BoxSizerHelper(
				self, sizer=wx.StaticBoxSizer(wx.StaticBox(
					self, label=directoryGroupText), wx.VERTICAL
				)
			)
		)
		# Message translated in NVDA core.
		browseText = translate("Browse...")
		# Translators: The title of the dialog presented when browsing for the destination directory
		# when restoring feeds.
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
		self.CentreOnScreen()

	def onRestore(self, evt):
		if not self.restoreDirectoryEdit.Value:
			gui.messageBox(
				# Message translated in NVDA core.
				translate("Please specify a directory."),
				# Message translated in NVDA core.
				translate("Error"),
				wx.OK | wx.ICON_ERROR
			)
			return
		drv = os.path.splitdrive(self.restoreDirectoryEdit.Value)[0]
		if drv and not os.path.isdir(drv):
			gui.messageBox(
				# Message translated in NVDA core.
				translate("Invalid drive %s") % drv,
				# Message translated in NVDA core.
				translate("Error"),
				wx.OK | wx.ICON_ERROR
			)
			return
		self.Hide()
		doRestore(self.restoreDirectoryEdit.Value)
		self.Destroy()

	def onCancel(self, evt):
		self.Destroy()


class AddonSettingsPanel(SettingsPanel):

	title = ADDON_PANEL_TITLE

	def makeSettings(self, settingsSizer):
		sHelper = guiHelper.BoxSizerHelper(self, sizer=settingsSizer)

		# Translators: label of a dialog.
		self.filterAfterList = sHelper.addItem(wx.CheckBox(self, label=_("&Search edit box after feeds list")))
		self.filterAfterList.SetValue(config.conf["readFeeds"]["filterAfterList"])

	def onSave(self):
		config.conf["readFeeds"]["filterAfterList"] = self.filterAfterList.GetValue()


# Feed object

class Feed(object):

	def __init__(self, url):
		super(Feed, self).__init__()
		self._url = url
		self._document = None
		self._articles = []
		self.refresh()

	def buildTag(self, tag, ns=None):
		if ns is None:
			return tag
		else:
			return f"{ns}{tag}"

	def getArticleTimestamp(self, article):
		locale.setlocale(locale.LC_TIME, "en")
		try:
			if self.getFeedType() == u'rss':
				date = article.find(self.buildTag("pubDate", self.ns)).text
				timestamp = time.mktime(datetime.datetime.strptime(date, "%a, %d %b %Y %H:%M:%S %Z").timetuple())
			elif self.getFeedType() == 'atom':
				date = article.find(self.buildTag("updated", self.ns)).text
				timestamp = time.mktime(datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S%Z").timetuple())
			return timestamp
		except Exception:
			return 0

	def refresh(self):
		try:
			response = urllib.request.urlopen(self._url)
		except Exception:
			userAgent = "UniversalFeedParser/3.3 +http://feedparser.org/"
			headers = {'User-Agent': userAgent}
			req = urllib.request.Request(self._url, None, headers)
			response = urllib.request.urlopen(req)
		try:
			self._document = ElementTree.parse(response)
		except Exception as e:
			raise e
		tag = self._document.getroot().tag
		self.ns = "%s}" % tag.split("}", 1)[0] if "}" in tag else None
		# Check if we are dealing with an rss or atom feed.
		if tag.endswith("rss"):
			self._main = self._document.getroot().find(self.buildTag("channel", self.ns))
			self._articles = self._main.findall(self.buildTag("item", self.ns))
			self._feedType = "rss"
		elif tag.endswith("feed"):
			self._main = self._document.getroot()
			self._articles = self._main.findall(self.buildTag("entry", self.ns))
			self._feedType = "atom"
		else:
			log.debugWarning("Unknown type of current feed", exc_info=True)
			raise
		self._articles.sort(key=self.getArticleTimestamp, reverse=True)
		self._index = 0

	def getFeedUrl(self):
		return self._url

	def getFeedType(self):
		return self._feedType

	def getFeedName(self):
		try:
			return self._main.find(self.buildTag("title", self.ns)).text
		except Exception:
			return ""

	def getFeedLanguage(self):
		try:
			return self._main.find(self.buildTag("language", self.ns)).text
		except Exception:
			return languageHandler.getLanguage().replace("_", "-")

	def getArticleTitle(self, index=None):
		if index is None:
			index = self._index
		try:
			return self._articles[index].find(self.buildTag("title", self.ns)).text
		except Exception:
			# Translators: Presented when the current article does not have an associated title.
			return _("Unable to locate article title.")

	def getArticleLink(self, index=None):
		if index is None:
			index = self._index
		try:
			if self.getFeedType() == u'rss':
				return self._articles[index].find(self.buildTag("link", self.ns)).text
			elif self.getFeedType() == 'atom':
				return self._articles[index].find(self.buildTag("link", self.ns)).get("href")
		except Exception:
			# Translators: Presented when the current article does not have an associated link.
			return _("Unable to locate article link.")

	def getArticleDescription(self, index=None):
		if index is None:
			index = self._index
		description = None
		try:
			if self.getFeedUrl().startswith("https://www.google.com") and "/alerts/" in self.getFeedUrl():
				description = self._articles[index].find(self.buildTag("content", self.ns)).text
			if description is not None:
				return description
			if self.getFeedType() == u'rss':
				description = self._articles[index].find(self.buildTag("description", self.ns)).text
			elif self.getFeedType() == 'atom':
				description = self._articles[index].find(self.buildTag("summary", self.ns)).text
				if description is None:
					description = self._articles[index].find(self.buildTag("content", self.ns)).text
			return description
		except Exception:
			return None

	def getArticleEnclosureUrl(self, index=None):
		if index is None:
			index = self._index
		try:
			if self.getFeedType() == u'rss':
				return self._articles[index].find(self.buildTag("enclosure", self.ns)).get("url")
			return None
		except Exception:
			return None

	def getArticleEnclosureType(self, index=None):
		if index is None:
			index = self._index
		try:
			if self.getFeedType() == u'rss':
				return self._articles[index].find(self.buildTag("enclosure", self.ns)).get("type")
			return None
		except Exception:
			return None

	def getArticleEnclosureLength(self, index=None):
		if index is None:
			index = self._index
		try:
			if self.getFeedType() == u'rss':
				return int(self._articles[index].find(self.buildTag("enclosure", self.ns)).get("length"))
			return None
		except Exception:
			return None

	def getArticleDate(self, index=None):
		if index is None:
			index = self._index
		try:
			if self.getFeedType() == u'rss':
				date = self._articles[index].find(self.buildTag("pubDate", self.ns)).text
			elif self.getFeedType() == 'atom':
				date = self._articles[index].find(self.buildTag("updated", self.ns)).text
			return date
		except Exception:
			return None

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

	def buildHtml(self):
		raw = "<!DOCTYPE html><html lang=\"" + self.getFeedLanguage()
		raw += "\"><head><title>" + self.getFeedName()
		raw += "</title><meta charset=\"utf-8\" />"
		raw += "<meta http-equiv='X-UA-Compatible' content='IE=edge'>"
		raw += "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"></head>"
		raw += "<body><h1><a href=\"" + self.getFeedUrl() + "\">" + self.getFeedName() + "</a></h1><p><label>"
		# Translators: Label of a checkbox to choose if date should be presented for each feed.
		label = _("Show date")
		raw += label
		raw += "<input type=\"checkbox\" id=\"showDate\" "
		raw += "onclick=\"setDatePresentation()\" accesskey=\"0\"></label></p><p><label>"
		# Translators: Label for a checkbox to show buttons for copying to clipboard.
		label = _("Show buttons to copy")
		raw += label
		raw += "<input id=\"copy\" accesskey=\"8\" type=\"checkbox\" onclick=\"setCopyPresentation()\"></label></p>"
		for index in range(self.getNumberOfArticles()):
			raw += "<div class=\"heading\"><h2><a href=\""
			raw += self.getArticleLink(index) + "\">" + self.getArticleTitle(index) + "</a></h2>"
			# Translators: Label for a button to copy to clipboard.
			label = _("Copy") + " " + str(index + 1)
			raw += "<button aria-hidden=\"true\" aria-pressed=\"false\">" + label + "</button></div>"
			if self.getArticleDate(index):
				raw += "<div class=\"date\" aria-hidden=\"true\">" + self.getArticleDate(index) + "</div>"
			if self.getArticleDescription(index) is not None:
				raw += "<div>" + self.getArticleDescription(index) + "</div>"
			enclosure = self.getArticleEnclosureUrl(index)
			if enclosure is not None:
				enclosureType = self.getArticleEnclosureType(index)
				enclosureLength = self.getArticleEnclosureLength(index)
				raw += "<div><a href=\"" + enclosure + "\">" + enclosureType + f"{str(index+1)}</a>"
				raw += f" ({str(enclosureLength / 1024)} kB)</div>"
		raw += "<script src=\"feed.js\"></script></body></html>"
		with open(os.path.join(HTML_PATH, "feed.html"), "w", encoding="utf-8") as f:
			f.write(raw)


class Opml(object):

	def __init__(self, path):
		super(Opml, self).__init__()
		self._path = path
		self._document = None
		self.validate()

	def getOpmlPath(self):
		return self._path

	def validate(self):
		path = self._path
		try:
			self._document = ElementTree.parse(path)
		except Exception as e:
			raise e

	def isOpml(self):
		if self._document is not None and self._document.getroot().tag == "opml":
			return True
		return False

	def opmlToTextFiles(self):
		for outline in self._document.getroot().iter("outline"):
			title = outline.get("title")
			url = outline.get("xmlUrl")
			filename = api.filterFileName(title.strip())
			pathname = os.path.join(FEEDS_PATH, filename)
			with open(pathname, "w", encoding="utf-8") as f:
				f.write(url)

	def addFeed(self, title, url):
		element = ElementTree.Element("outline")
		element.set("title", title)
		element.text = title
		element.set("xmlUrl", url)
		body = self._document.getroot().find("body")
		body.append(element)
		outlines = sorted(body.findall("outline"), key=lambda el: el.get("title"))
		for outline in outlines:
			body.remove(outline)
			body.append(outline)

		self._document.write(self._path)


# Global plugin

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	scriptCategory = ADDON_SUMMARY

	def __init__(self):
		super(GlobalPlugin, self).__init__()
		NVDASettingsDialog.categoryClasses.append(AddonSettingsPanel)
		self.menu = gui.mainFrame.sysTrayIcon.toolsMenu
		self.readFeedsMenu = wx.Menu()
		# Translators: the name of a submenu.
		self.mainItem = self.menu.AppendSubMenu(self.readFeedsMenu, _("Read Feeds"))
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
			self.menu.Remove(self.mainItem)
			NVDASettingsDialog.categoryClasses.remove(AddonSettingsPanel)
		except Exception:
			pass

	def onFeeds(self, evt):
		gui.mainFrame.prePopup()
		d = FeedsDialog(gui.mainFrame)
		d.Show()
		gui.mainFrame.postPopup()

	@script(
		# Translators: message presented in input mode.
		description=_("Activates the Feeds dialog of Read Feeds.")
	)
	def script_activateFeedsDialog(self, gesture):
		wx.CallAfter(self.onFeeds, None)

	def onCopy(self, evt):
		gui.mainFrame.prePopup()
		d = CopyDialog(gui.mainFrame)
		d.Show()
		gui.mainFrame.postPopup()

	@script(
		# Translators: message presented in input mode.
		description=_("Activates the Copy dialog of Read Feeds.")
	)
	def script_activateCopyDialog(self, gesture):
		wx.CallAfter(self.onCopy, None)

	def onRestore(self, evt):
		gui.mainFrame.prePopup()
		d = RestoreDialog(gui.mainFrame)
		d.Show()
		gui.mainFrame.postPopup()

	@script(
		# Translators: message presented in input mode.
		description=_("Activates the Restore dialog of Read Feeds.")
	)
	def script_activateRestoreDialog(self, gesture):
		wx.CallAfter(self.onRestore, None)

	@script(
		# Translators: message presented in input mode.
		description=_("Shows the %s settings." % ADDON_SUMMARY),
		category=SCRCAT_CONFIG
	)
	def script_settings(self, gesture):
		wx.CallAfter(onSettings, None)

	def getFirstArticle(self):
		addressFile = "%s.txt" % config.conf["readFeeds"]["addressFile"]
		with open(os.path.join(FEEDS_PATH, addressFile), "r", encoding="utf-8") as f:
			address = f.read()
		if self.feed and self.feed.getFeedUrl() == address:
			curFeed = self.feed
		else:
			curFeed = None
		try:
			self.feed = Feed(address)
		except Exception as e:
			ui.message(CAN_NOT_REPORT)
			self.feed = curFeed
			raise e

	@script(
		# Translators: message presented in input mode.
		description=_("Refreshes the current feed and announces the most recent article title."),
		gesture="kb:control+shift+NVDA+8"
	)
	def script_readFirstArticle(self, gesture):
		self.getFirstArticle()
		if self.feed:
			ui.message(re.sub(TAG_REGEXP, '', self.feed.getArticleTitle()))

	@script(
		description=_(
			# Translators: message presented in input mode.
			"Announces the title of the current article. Pressed two times,"
			" copies title and related link to the clipboard."
		),
		gesture="kb:control+shift+NVDA+i"
	)
	def script_readCurrentArticle(self, gesture):
		if not self.feed:
			self.getFirstArticle()
		articleInfo = "{title}\r\n\r\n{address}".format(
			title=re.sub(TAG_REGEXP, '', self.feed.getArticleTitle()),
			address=self.feed.getArticleLink()
		)
		if scriptHandler.getLastScriptRepeatCount() == 1 and api.copyToClip(articleInfo):
			# Translators: message presented when the information about an article of a feed
			# is copied to the clipboard.
			ui.message(_("Copied to clipboard %s") % articleInfo)
		else:
			ui.message(articleInfo)

	@script(
		# Translators: message presented in input mode.
		description=_("Announces the title of the next article."),
		gesture="kb:control+shift+NVDA+o"
	)
	def script_readNextArticle(self, gesture):
		if not self.feed:
			self.getFirstArticle()
		self.feed.next()
		ui.message(re.sub(TAG_REGEXP, '', self.feed.getArticleTitle()))

	@script(
		# Translators: message presented in input mode.
		description=_("Announces the title of the previous article."),
		gesture="kb:control+shift+NVDA+u"
	)
	def script_readPriorArticle(self, gesture):
		if not self.feed:
			self.getFirstArticle()
		self.feed.previous()
		ui.message(re.sub(TAG_REGEXP, '', self.feed.getArticleTitle()))

	@script(
		# Translators: message presented in input mode.
		description=_("Announces article link, when pressed two times, opens related web page."),
		gesture="kb:control+shift+NVDA+space"
	)
	def script_reportLink(self, gesture):
		if not self.feed:
			self.getFirstArticle()
		articleLink = self.feed.getArticleLink()
		if scriptHandler.getLastScriptRepeatCount() == 1:
			os.startfile(articleLink)
		else:
			ui.message(articleLink)

	@script(
		# Translators: message presented in input mode.
		description=_("Copies title and related link of the current article to the clipboard.")
	)
	def script_copyArticleInfo(self, gesture):
		if not self.feed:
			self.getFirstArticle()
		articleInfo = "{title}\r\n\r\n{address}".format(
			title=re.sub(TAG_REGEXP, '', self.feed.getArticleTitle()),
			address=self.feed.getArticleLink()
		)
		if api.copyToClip(articleInfo):
			# Translators: message presented when the information about an article of a feed
			# is copied to the clipboard.
			ui.message(_("Copied to clipboard %s") % articleInfo)
