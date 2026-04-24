# Copyright (C) 2026 NV Access Limited, Noelia Ruiz Martínez
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

import os
import sys

sys.path.insert(0, os.getcwd())
import buildVars


def main():
	addonId = buildVars.addon_info["addon_name"]
	# Output only the addonId for capture by PowerShell (do not print anything else)
	print(addonId, end="", flush=True)
