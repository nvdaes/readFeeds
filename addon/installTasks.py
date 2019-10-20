# -*- coding: UTF-8 -*-

# installTasks for the readFeeds add-on
#Copyright (C) 2013-2019 Noelia Ruiz Martínez, other contributors
# Released under GPL2

import addonHandler
import globalVars
import os
import shutil
import glob
import gui
import wx

ADDON_DIR = os.path.abspath(os.path.dirname(__file__))
FEEDS_PATH = os.path.join(ADDON_DIR, "globalPlugins", "readFeeds", "personalFeeds")
CONFIG_PATH = globalVars.appArgs.configPath

addonHandler.initTranslation()

def onInstall():
	addonPath = [os.path.join(CONFIG_PATH, "RSS"), os.path.join(CONFIG_PATH, "personalFeeds")]
	for path in addonPath:
		if not os.path.isdir(path):
			continue
		pathFiles = os.listdir(path)
		validFiles = glob.glob(path+"\\*.txt")
		if len(pathFiles) != len(validFiles):
			return
		if gui.messageBox(
			# Translators: the label of a message box dialog.
			_("Your configuration folder for NVDA contains files that seem to be derived from a previous version of this add-on. Do you want to update it?"),
			# Translators: the title of a message box dialog.
			_("Install or update add-on"),
			wx.YES|wx.NO|wx.ICON_WARNING) == wx.YES:
				for file in validFiles:
					try:
						shutil.copy(file, FEEDS_PATH)
					except IOError:
						pass
				return
	previousFeedsPath = os.path.join(CONFIG_PATH, "addons", "readFeeds", "globalPlugins", "readFeeds", "personalFeeds")
	if os.path.isdir(previousFeedsPath):
		validFiles = glob.glob(previousFeedsPath+"\\*.txt")
		for file in validFiles:
			try:
				shutil.copy(file, FEEDS_PATH)
			except IOError:
				pass
