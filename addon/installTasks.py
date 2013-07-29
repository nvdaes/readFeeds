# -*- coding: UTF-8 -*-

import addonHandler
import globalVars
import os
import shutil
import glob
import gui
import wx

basePath = os.path.dirname(__file__)
savePath = os.path.join(basePath, "globalPlugins", "readFeeds", "RSS")

addonHandler.initTranslation()

def onInstall():
	configPath = globalVars.appArgs.configPath
	addonPath = os.path.join(configPath, "RSS")
	if not os.path.isdir(addonPath):
		return
	addonPathFiles = os.listdir(addonPath)
	validFiles = glob.glob(addonPath+"\\*.txt")
	if len(addonPathFiles) != len(validFiles):
		return
	if gui.messageBox(
	# Translators: the label of a message box dialog.
	_("Your configuration folder for NVDA contains files that seem to be derivated from a previous version of this add-on. Do you want to update it?"),
	# Translators: the title of a message box dialog.
	_("Install or update add-on"),
	wx.YES|wx.NO|wx.ICON_WARNING)==wx.YES:
		for file in validFiles:
			try:
				shutil.copy(file, savePath)
			except IOError:
				pass
