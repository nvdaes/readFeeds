# -*- coding: UTF-8 -*-

# installTasks for the readFeeds add-on
# Copyright (C) 2013-2021 Noelia Ruiz Martínez, other contributors
# Released under GPL2

import os
import shutil
import glob

import addonHandler
import globalVars

ADDON_DIR = os.path.abspath(os.path.dirname(__file__))
FEEDS_PATH = os.path.join(ADDON_DIR, "globalPlugins", "readFeeds", "personalFeeds")
CONFIG_PATH = globalVars.appArgs.configPath

addonHandler.initTranslation()


def onInstall():
	previousFeedsPath = os.path.join(
		CONFIG_PATH, "addons", "readFeeds",
		"globalPlugins", "readFeeds", "personalFeeds"
	)
	if os.path.isdir(previousFeedsPath):
		validFiles = glob.glob(previousFeedsPath + "\\*.txt")
		validFiles.append(os.path.join(previousFeedsPath, "readFeeds.opml"))
		if not os.path.isdir(FEEDS_PATH):
			os.makedirs(FEEDS_PATH)
		for file in validFiles:
			try:
				shutil.copy(file, FEEDS_PATH)
			except IOError:
				pass
