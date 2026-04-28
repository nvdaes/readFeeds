import sys
import os
from crowdin_api import CrowdinClient

# -----------------------------
# CROWDIN API SCORE
# -----------------------------


def get_score_from_api(lang_id: str, crowdin_file_name: str) -> float:
	"""
	Fetches the translation progress percentage directly from Crowdin API.
	Returns a float between 0.0 and 1.0.
	"""
	token = os.environ.get("crowdinAuthToken")
	project_id_env = os.environ.get("CROWDIN_PROJECT_ID")

	# Ensure credentials are present
	if not token or not project_id_env:
		return 0.0

	client = CrowdinClient(token=token)
	project_id = int(project_id_env)

	try:
		# 1. NORMALIZE SEARCH TERMS
		# Extract base name (e.g., 'askOpenRouter') and extension
		base_target = crowdin_file_name.replace("\\", "/").split("/")[-1].rsplit(".", 1)[0].lower()
		ext_target = crowdin_file_name.split(".")[-1].lower()

		# Mapping: if we check a .po, we look for a .pot on Crowdin
		search_ext = ".pot" if ext_target == "po" else f".{ext_target}"

		# 2. FETCH ALL FILES TO FIND MATCHING ID
		files = client.source_files.with_fetch_all().list_files(project_id, filter=f"{base_target}{search_ext}")
		file_id = None

		for f in files["data"]:
			path_crowdin = f["data"]["path"].lower()
			if path_crowdin.endswith(f"{base_target}{search_ext}"):
				file_id = f["data"]["id"]
				break

		if file_id is None:
			return 0.0

		# 3. FETCH PROGRESS FOR THE SPECIFIC FILE
		# We use get_file_progress which is reliable for specific file IDs
		progress = client.translation_status.with_fetch_all.get_file_progress(projectId=project_id, fileId=file_id)

		for item in progress["data"]:
			if item["data"]["languageId"].lower() == lang_id.lower():
				# Return ratio (0.0 to 1.0)
				return float(item["data"]["translationProgress"]) / 100

	except Exception:
		# Fallback to 0.0 in case of API or network error
		return 0.0

	return 0.0


# -----------------------------
# MAIN ENGINE
# -----------------------------


def main():
	"""
	Main entry point.
	Expects two arguments: <file_name> <language_id>
	"""
	if len(sys.argv) < 3:
		sys.exit(2)

	file_name = sys.argv[1]
	lang = sys.argv[2]

	# All evaluations now go through the Crowdin API
	score = get_score_from_api(lang, file_name)

	# Output formatting for PowerShell capture
	print(f"translationRatio={score}")
	if file_name.lower().endswith(".md"):
		print(f"mdScore={score}")
	else:
		print(f"poScore={score}")

	# Exit with code 0 if score > 5%, otherwise 1
	sys.exit(0 if score > 0.05 else 1)


if __name__ == "__main__":
	main()
