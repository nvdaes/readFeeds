# -*- coding: UTF-8 -*-

import addonHandler
import config
import os
import shutil
import glob
import gui
import wx

basePath = os.path.dirname(__file__)
savePath = os.path.join(basePath, "globalPlugins", "RSS")


addonHandler.initTranslation()

def onInstall():
	configPath = config.getUserDefaultConfigPath()
	addonPath = os.path.join(configPath, "RSS")
	if not os.path.isdir(addonPath):
		return
	addonPathFiles = os.listdir(addonPath)
	validFiles = glob.glob(addonPath+"\\*.txt")
	if len(addonPathFiles) != len(validFiles):
		return
	if gui.messageBox(_("Your configuration folder for NVDA contains files that seem to be derivated from a previous version of this add-on. Do you want to update it?"),
	_("Install or update add-on"),
	wx.YES|wx.NO|wx.ICON_WARNING)==wx.YES:
		for file in validFiles:
			try:
				shutil.copy(file, savePath)
			except IOError:
				pass
