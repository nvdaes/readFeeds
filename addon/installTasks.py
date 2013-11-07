# -*- coding: UTF-8 -*-

import addonHandler
import globalVars
import os
import shutil
import glob
import gui
import wx

basePath = os.path.dirname(__file__).decode("mbcs")
savePath = os.path.join(basePath, "globalPlugins", "personalFeeds")

addonHandler.initTranslation()

def onInstall():
	for addon in addonHandler.getAvailableAddons():
		if addon.manifest['name'] == "ReadFeeds":
			if gui.messageBox(
				# Translators: the label of a message box dialog.
				_("You have installed the ReadFeeds add-on, probably an old and incompatible version with this one. Do you want to uninstall the old version?"),
				# Translators: the title of a message box dialog.
				_("Uninstall incompatible add-on"),
				wx.YES|wx.NO|wx.ICON_WARNING)==wx.YES:
					addon.requestRemove()
			break
	configPath = globalVars.appArgs.configPath
	addonPath = [os.path.join(configPath, "RSS"), os.path.join(configPath, "personalFeeds")]
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
		wx.YES|wx.NO|wx.ICON_WARNING)==wx.YES:
			for file in validFiles:
				try:
					shutil.copy(file, savePath)
				except IOError:
					pass
