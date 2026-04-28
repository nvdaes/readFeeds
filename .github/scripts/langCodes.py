import sys

# Explicit mapping based on your NVDA local directory listing
# Format: NVDA-Local-folder: "Crowdin-Code".

langMappings: dict[str, str] ={
	"af_ZA": "af",
	"de_CH": "de-CH",
	"es": "es-ES",
	"es_CO": "es-CO",
	"nb_NO": "nb",
	"nn_NO": "nn-NO",
	"pt_PT": "pt-PT",
	"pt_BR": "pt-BR",
	"sr": "sr-CS",
	"zh_CN": "zh-CN",
	"zh_HK": "zh-HK",
	"zh_TW": "zh-TW"
}

def getCrowdinCode(nvdaCode) -> str:
	"""
	Get the corresponding Crowdin code for a given NVDA code.

param nvdaCode: The NVDA language code to be converted.
return: The corresponding Crowdin code if found, otherwise returns the original NVDA code.
	"""
	return langMappings.get(nvdaCode, nvdaCode)

if __name__ == "__main__":
	if len(sys.argv) > 1:
		# We output the result so PowerShell can capture it
		print(getCrowdinCode(sys.argv[1]))
