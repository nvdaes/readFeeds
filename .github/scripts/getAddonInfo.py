# Copyright (C) 2025 NV Access Limited, Noelia Ruiz Martínez
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

import os
import sys

sys.path.insert(0, os.getcwd())
import buildVars


def main():
	print(os.getcwd)
	addonId = buildVars.addon_info["addon_name"]
	# Print only the addonId so it can be captured by PowerShell
	print(addonId, end="", flush=True)
