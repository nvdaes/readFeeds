import sys

# Explicit mapping based on your NVDA local directory listing
# Format: "Crowdin-Code": "NVDA-Local-Folder"
CROWDIN_TO_NVDA = {
	# Arabic variants
	"ar": "ar",
	"ar-SA": "ar_SA",
	
	# Portuguese variants
	"pt-BR": "pt_BR",
	"pt-PT": "pt_PT",
	
	# Spanish variants
	"es-ES": "es",	  # Common Crowdin mapping for Spanish
	"es-CO": "es_CO",
	
	# Chinese variants
	"zh-CN": "zh_CN",
	"zh-HK": "zh_HK",
	"zh-TW": "zh_TW",
	
	# Others from your list
	"af-ZA": "af_ZA",
	"de-CH": "de_CH",
	"nb-NO": "nb_NO",
	"nn-NO": "nn_NO",
}

def get_nvda_code(crowdin_code):
	# 1. Direct check in our verified map
	if crowdin_code in CROWDIN_TO_NVDA:
		return CROWDIN_TO_NVDA[crowdin_code]
	
	# 2. Automated conversion: Crowdin "fr-FR" -> NVDA "fr_FR"
	# This handles most regional codes not explicitly in the map
	if "-" in crowdin_code:
		return crowdin_code.replace("-", "_")
	
	# 3. Default: Return as is (works for 'fr', 'tr', 'bg', 'fi', 'fa', etc.)
	return crowdin_code

if __name__ == "__main__":
	if len(sys.argv) > 1:
		# We output the result so PowerShell can capture it
		print(get_nvda_code(sys.argv[1]))
