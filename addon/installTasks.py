# -*- coding: UTF-8 -*-

# installTasks for the readFeeds add-on
# Copyright (C) 2013-2021 Noelia Ruiz Martínez, other contributors
# Released under GPL2

import addonHandler
import globalVars
import os
import shutil

ADDON_DIR = os.path.abspath(os.path.dirname(__file__))
FEEDS_PATH = os.path.join(ADDON_DIR, "globalPlugins", "readFeeds", "personalFeeds")
CONFIG_PATH = globalVars.appArgs.configPath
addonHandler.initTranslation()


def onInstall():
	previousFeedsPath = os.path.join(
		CONFIG_PATH, "addons", "readFeeds",
		"globalPlugins", "readFeeds", "personalFeeds",
		"readFeeds.opml"
	)
	if os.path.isfile(previousFeedsPath):
		try:
			shutil.copy(previousFeedsPath, FEEDS_PATH)
		except IOError:
			pass
