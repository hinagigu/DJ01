# __Internationalization

## 方法

### ClearCurrentAssetGroupCulture
```angelscript
void ClearCurrentAssetGroupCulture(FName AssetGroup, bool SaveToConfig)
```
Clear the given asset group category culture.
@param AssetGroup The asset group to clear the culture for.
@param SaveToConfig If true, save the new setting to the users' "GameUserSettings" config so that it persists after a reload.

### GetCultureDisplayName
```angelscript
FString GetCultureDisplayName(FString Culture, bool Localized)
```
Get the display name of the given culture.
@param Culture The culture to get the display name of, as an IETF language tag (eg, "zh-Hans-CN")
@param Localized True to get the localized display name (the name of the culture in its own language), or False to get the display name in the current language.
@return The display name of the culture, or the given culture code on failure.

### GetCurrentAssetGroupCulture
```angelscript
FString GetCurrentAssetGroupCulture(FName AssetGroup)
```
Get the given asset group category culture.
@note Returns the current language if the group category doesn't have a culture override.
@param AssetGroup The asset group to get the culture for.
@return The culture as an IETF language tag (eg, "zh-Hans-CN").

### GetCurrentCulture
```angelscript
FString GetCurrentCulture()
```
Get the current culture as an IETF language tag:
 - A two-letter ISO 639-1 language code (eg, "zh").
 - An optional four-letter ISO 15924 script code (eg, "Hans").
 - An optional two-letter ISO 3166-1 country code (eg, "CN").
@note This function exists for legacy API parity with SetCurrentCulture and is equivalent to GetCurrentLanguage.
@return The culture as an IETF language tag (eg, "zh-Hans-CN").

### GetCurrentLanguage
```angelscript
FString GetCurrentLanguage()
```
Get the current language (for localization) as an IETF language tag:
 - A two-letter ISO 639-1 language code (eg, "zh").
 - An optional four-letter ISO 15924 script code (eg, "Hans").
 - An optional two-letter ISO 3166-1 country code (eg, "CN").
@return The language as an IETF language tag (eg, "zh-Hans-CN").

### GetCurrentLocale
```angelscript
FString GetCurrentLocale()
```
Get the current locale (for internationalization) as an IETF language tag:
 - A two-letter ISO 639-1 language code (eg, "zh").
 - An optional four-letter ISO 15924 script code (eg, "Hans").
 - An optional two-letter ISO 3166-1 country code (eg, "CN").
@return The locale as an IETF language tag (eg, "zh-Hans-CN").

### GetLocalizedCultures
```angelscript
TArray<FString> GetLocalizedCultures(bool IncludeGame, bool IncludeEngine, bool IncludeEditor, bool IncludeAdditional)
```
Get the list of cultures that have localization data available for them.
@param IncludeGame Check for localized game resources.
@param IncludeEngine Check for localized engine resources.
@param IncludeEditor Check for localized editor resources.
@param IncludeAdditional Check for localized additional (eg, plugin) resources.
@return The list of cultures as IETF language tags (eg, "zh-Hans-CN").

### GetNativeCulture
```angelscript
FString GetNativeCulture(ELocalizedTextSourceCategory TextCategory)
```
Get the native culture for the given localization category.
@param Category The localization category to query.
@return The culture as an IETF language tag (eg, "zh-Hans-CN").

### GetSuitableCulture
```angelscript
FString GetSuitableCulture(TArray<FString> AvailableCultures, FString CultureToMatch, FString FallbackCulture)
```
Given a list of available cultures, try and find the most suitable culture from the list based on culture prioritization.
  eg) If your list was [en, fr, de] and the given culture was "en-US", this function would return "en".
  eg) If your list was [zh, ar, pl] and the given culture was "en-US", this function would return the fallback culture.
@param AvailableCultures List of available cultures to filter against (see GetLocalizedCultures).
@param CultureToMatch Culture to try and match (see GetCurrentLanguage).
@param FallbackCulture The culture to return if there is no suitable match in the list (typically your native culture, see GetNativeCulture).
@return The culture as an IETF language tag (eg, "zh-Hans-CN").

### SetCurrentAssetGroupCulture
```angelscript
bool SetCurrentAssetGroupCulture(FName AssetGroup, FString Culture, bool SaveToConfig)
```
Set the given asset group category culture from an IETF language tag (eg, "zh-Hans-CN").
@param AssetGroup The asset group to set the culture for.
@param Culture The culture to set, as an IETF language tag (eg, "zh-Hans-CN").
@param SaveToConfig If true, save the new setting to the users' "GameUserSettings" config so that it persists after a reload.
@return True if the culture was set, false otherwise.

### SetCurrentCulture
```angelscript
bool SetCurrentCulture(FString Culture, bool SaveToConfig)
```
Set the current culture.
@note This function is a sledgehammer, and will set both the language and locale, as well as clear out any asset group cultures that may be set.
@param Culture The culture to set, as an IETF language tag (eg, "zh-Hans-CN").
@param SaveToConfig If true, save the new setting to the users' "GameUserSettings" config so that it persists after a reload.
@return True if the culture was set, false otherwise.

### SetCurrentLanguage
```angelscript
bool SetCurrentLanguage(FString Culture, bool SaveToConfig)
```
Set *only* the current language (for localization).
@note Unless you're doing something advanced, you likely want SetCurrentLanguageAndLocale or SetCurrentCulture instead.
@param Culture The language to set, as an IETF language tag (eg, "zh-Hans-CN").
@param SaveToConfig If true, save the new setting to the users' "GameUserSettings" config so that it persists after a reload.
@return True if the language was set, false otherwise.

### SetCurrentLanguageAndLocale
```angelscript
bool SetCurrentLanguageAndLocale(FString Culture, bool SaveToConfig)
```
Set the current language (for localization) and locale (for internationalization).
@param Culture The language and locale to set, as an IETF language tag (eg, "zh-Hans-CN").
@param SaveToConfig If true, save the new setting to the users' "GameUserSettings" config so that it persists after a reload.
@return True if the language and locale were set, false otherwise.

### SetCurrentLocale
```angelscript
bool SetCurrentLocale(FString Culture, bool SaveToConfig)
```
Set *only* the current locale (for internationalization).
@note Unless you're doing something advanced, you likely want SetCurrentLanguageAndLocale or SetCurrentCulture instead.
@param Culture The locale to set, as an IETF language tag (eg, "zh-Hans-CN").
@param SaveToConfig If true, save the new setting to the users' "GameUserSettings" config so that it persists after a reload.
@return True if the locale was set, false otherwise.

