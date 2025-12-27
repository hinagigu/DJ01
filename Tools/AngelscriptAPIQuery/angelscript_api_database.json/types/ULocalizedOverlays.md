# ULocalizedOverlays

**继承自**: `UOverlays`

Implements an asset that contains a set of Basic Overlays that will be displayed in accordance with
the current locale, or a default set if an appropriate locale is not found

## 属性

### DefaultOverlays
- **类型**: `UBasicOverlays`
- **描述**: The overlays to use if no overlays are found for the current culture

### LocaleToOverlaysMap
- **类型**: `TMap<FString,TObjectPtr<UBasicOverlays>>`
- **描述**: Maps a set of cultures to specific BasicOverlays assets.
Cultures are comprised of three hyphen-separated parts:
             A two-letter ISO 639-1 language code (e.g., "zh")
             An optional four-letter ISO 15924 script code (e.g., "Hans")
             An optional two-letter ISO 3166-1 country code  (e.g., "CN")

### AssetImportData
- **类型**: `UAssetImportData`
- **描述**: The import data used to make this overlays asset

