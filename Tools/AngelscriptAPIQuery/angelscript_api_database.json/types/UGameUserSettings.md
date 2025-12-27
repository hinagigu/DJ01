# UGameUserSettings

**继承自**: `UObject`

Stores user settings for a game (for example graphics and sound settings), with the ability to save and load to and from a file.

## 属性

### OnGameUserSettingsUINeedsUpdate
- **类型**: `FOnGameUserSettingsUINeedsUpdate`

## 方法

### ApplyHardwareBenchmarkResults
```angelscript
void ApplyHardwareBenchmarkResults()
```
Applies the settings stored in ScalabilityQuality and saves settings

### ApplyNonResolutionSettings
```angelscript
void ApplyNonResolutionSettings()
```

### ApplyResolutionSettings
```angelscript
void ApplyResolutionSettings(bool bCheckForCommandLineOverrides)
```

### ApplySettings
```angelscript
void ApplySettings(bool bCheckForCommandLineOverrides)
```
Applies all current user settings to the game and saves to permanent storage (e.g. file), optionally checking for command line overrides.

### ConfirmVideoMode
```angelscript
void ConfirmVideoMode()
```
Mark current video mode settings (fullscreenmode/resolution) as being confirmed by the user

### EnableHDRDisplayOutput
```angelscript
void EnableHDRDisplayOutput(bool bEnable, int DisplayNits)
```
Enables or disables HDR display output. Can be called again to change the desired nit level

### GetAntiAliasingQuality
```angelscript
int GetAntiAliasingQuality()
```
Returns the anti-aliasing quality (0..4, higher is better)

### GetAudioQualityLevel
```angelscript
int GetAudioQualityLevel()
```
Returns the user's audio quality level setting

### GetCurrentHDRDisplayNits
```angelscript
int GetCurrentHDRDisplayNits()
```
Returns 0 if HDR isn't supported or is turned off

### GetDefaultResolutionScale
```angelscript
float32 GetDefaultResolutionScale()
```
Gets the desired resolution quality based on DesiredScreenWidth/Height and the current screen resolution

### GetDesktopResolution
```angelscript
FIntPoint GetDesktopResolution()
```
Returns user's desktop resolution, in pixels.

### GetFoliageQuality
```angelscript
int GetFoliageQuality()
```
Returns the foliage quality (0..4, higher is better)

### GetFrameRateLimit
```angelscript
float32 GetFrameRateLimit()
```
Gets the user's frame rate limit (0 indiciates the frame rate limit is disabled)

### GetFullscreenMode
```angelscript
EWindowMode GetFullscreenMode()
```
Returns the user setting for game window fullscreen mode.

### GetGlobalIlluminationQuality
```angelscript
int GetGlobalIlluminationQuality()
```
Returns the global illumination quality (0..4, higher is better)

### GetLastConfirmedFullscreenMode
```angelscript
EWindowMode GetLastConfirmedFullscreenMode()
```
Returns the last confirmed user setting for game window fullscreen mode.

### GetLastConfirmedScreenResolution
```angelscript
FIntPoint GetLastConfirmedScreenResolution()
```
Returns the last confirmed user setting for game screen resolution, in pixels.

### GetOverallScalabilityLevel
```angelscript
int GetOverallScalabilityLevel()
```
Returns the overall scalability level (can return -1 if the settings are custom)

### GetPostProcessingQuality
```angelscript
int GetPostProcessingQuality()
```
Returns the post-processing quality (0..4, higher is better)

### GetPreferredFullscreenMode
```angelscript
EWindowMode GetPreferredFullscreenMode()
```
Returns the user setting for game window fullscreen mode.

### GetRecommendedResolutionScale
```angelscript
float32 GetRecommendedResolutionScale()
```
Gets the recommended resolution quality based on LastRecommendedScreenWidth/Height and the current screen resolution

### GetReflectionQuality
```angelscript
int GetReflectionQuality()
```
Returns the reflection quality (0..4, higher is better)

### GetResolutionScaleInformationEx
```angelscript
void GetResolutionScaleInformationEx(float32& CurrentScaleNormalized, float32& CurrentScaleValue, float32& MinScaleValue, float32& MaxScaleValue)
```
Returns the current resolution scale and the range

### GetResolutionScaleNormalized
```angelscript
float32 GetResolutionScaleNormalized()
```
Gets the current resolution scale as a normalized 0..1 value between MinScaleValue and MaxScaleValue

### GetScreenResolution
```angelscript
FIntPoint GetScreenResolution()
```
Returns the user setting for game screen resolution, in pixels.

### GetShadingQuality
```angelscript
int GetShadingQuality()
```
Returns the shading quality (0..4, higher is better)

### GetShadowQuality
```angelscript
int GetShadowQuality()
```
Returns the shadow quality (0..4, higher is better)

### GetTextureQuality
```angelscript
int GetTextureQuality()
```
Returns the texture quality (0..4, higher is better)

### GetViewDistanceQuality
```angelscript
int GetViewDistanceQuality()
```
Returns the view distance quality (0..4, higher is better)

### GetVisualEffectQuality
```angelscript
int GetVisualEffectQuality()
```
Returns the visual effects quality (0..4, higher is better)

### IsDirty
```angelscript
bool IsDirty()
```
Checks if any user settings is different from current

### IsDynamicResolutionDirty
```angelscript
bool IsDynamicResolutionDirty()
```
Checks if the dynamic resolution user setting is different from current system setting

### IsDynamicResolutionEnabled
```angelscript
bool IsDynamicResolutionEnabled()
```
Returns the user setting for dynamic resolution.

### IsFullscreenModeDirty
```angelscript
bool IsFullscreenModeDirty()
```
Checks if the FullscreenMode user setting is different from current

### IsHDREnabled
```angelscript
bool IsHDREnabled()
```

### IsScreenResolutionDirty
```angelscript
bool IsScreenResolutionDirty()
```
Checks if the Screen Resolution user setting is different from current

### IsVSyncDirty
```angelscript
bool IsVSyncDirty()
```
Checks if the vsync user setting is different from current system setting

### IsVSyncEnabled
```angelscript
bool IsVSyncEnabled()
```
Returns the user setting for vsync.

### LoadSettings
```angelscript
void LoadSettings(bool bForceReload)
```
Loads the user settings from persistent storage

### ResetToCurrentSettings
```angelscript
void ResetToCurrentSettings()
```
This function resets all settings to the current system settings

### RevertVideoMode
```angelscript
void RevertVideoMode()
```
Revert video mode (fullscreenmode/resolution) back to the last user confirmed values

### RunHardwareBenchmark
```angelscript
void RunHardwareBenchmark(int WorkScale, float32 CPUMultiplier, float32 GPUMultiplier)
```
Runs the hardware benchmark and populates ScalabilityQuality as well as the last benchmark results config members, but does not apply the settings it determines. Designed to be called in conjunction with ApplyHardwareBenchmarkResults

### SaveSettings
```angelscript
void SaveSettings()
```
Save the user settings to persistent storage (automatically happens as part of ApplySettings)

### SetAntiAliasingQuality
```angelscript
void SetAntiAliasingQuality(int Value)
```
Sets the anti-aliasing quality (0..4, higher is better)
@param Value 0:low, 1:medium, 2:high, 3:epic, 4:cinematic (gets clamped if needed)

### SetAudioQualityLevel
```angelscript
void SetAudioQualityLevel(int QualityLevel)
```
Sets the user's audio quality level setting

### SetBenchmarkFallbackValues
```angelscript
void SetBenchmarkFallbackValues()
```
Set scalability settings to sensible fallback values, for use when the benchmark fails or potentially causes a crash

### SetDynamicResolutionEnabled
```angelscript
void SetDynamicResolutionEnabled(bool bEnable)
```
Sets the user setting for dynamic resolution. See UGameUserSettings::bUseDynamicResolution.

### SetFoliageQuality
```angelscript
void SetFoliageQuality(int Value)
```
Sets the foliage quality (0..4, higher is better)
@param Value 0:low, 1:medium, 2:high, 3:epic, 4:cinematic (gets clamped if needed)

### SetFrameRateLimit
```angelscript
void SetFrameRateLimit(float32 NewLimit)
```
Sets the user's frame rate limit (0 will disable frame rate limiting)

### SetFullscreenMode
```angelscript
void SetFullscreenMode(EWindowMode InFullscreenMode)
```
Sets the user setting for the game window fullscreen mode. See UGameUserSettings::FullscreenMode.

### SetGlobalIlluminationQuality
```angelscript
void SetGlobalIlluminationQuality(int Value)
```
Sets the global illumination quality (0..4, higher is better)
@param Value 0:low, 1:medium, 2:high, 3:epic, 4:cinematic (gets clamped if needed)

### SetOverallScalabilityLevel
```angelscript
void SetOverallScalabilityLevel(int Value)
```
Changes all scalability settings at once based on a single overall quality level
@param Value 0:low, 1:medium, 2:high, 3:epic, 4:cinematic

### SetPostProcessingQuality
```angelscript
void SetPostProcessingQuality(int Value)
```
Sets the post-processing quality (0..4, higher is better)
@param Value 0:low, 1:medium, 2:high, 3:epic, 4:cinematic (gets clamped if needed)

### SetReflectionQuality
```angelscript
void SetReflectionQuality(int Value)
```
Sets the reflection quality (0..4, higher is better)
@param Value 0:low, 1:medium, 2:high, 3:epic, 4:cinematic (gets clamped if needed)

### SetResolutionScaleNormalized
```angelscript
void SetResolutionScaleNormalized(float32 NewScaleNormalized)
```
Sets the current resolution scale as a normalized 0..1 value between MinScaleValue and MaxScaleValue

### SetResolutionScaleValueEx
```angelscript
void SetResolutionScaleValueEx(float32 NewScaleValue)
```
Sets the current resolution scale

### SetScreenResolution
```angelscript
void SetScreenResolution(FIntPoint Resolution)
```
Sets the user setting for game screen resolution, in pixels.

### SetShadingQuality
```angelscript
void SetShadingQuality(int Value)
```
Sets the shading quality (0..4, higher is better)
@param Value 0:low, 1:medium, 2:high, 3:epic, 4:cinematic (gets clamped if needed)

### SetShadowQuality
```angelscript
void SetShadowQuality(int Value)
```
Sets the shadow quality (0..4, higher is better)
@param Value 0:low, 1:medium, 2:high, 3:epic, 4:cinematic (gets clamped if needed)

### SetTextureQuality
```angelscript
void SetTextureQuality(int Value)
```
Sets the texture quality (0..4, higher is better)
@param Value 0:low, 1:medium, 2:high, 3:epic, 4:cinematic  (gets clamped if needed)

### SetToDefaults
```angelscript
void SetToDefaults()
```

### SetViewDistanceQuality
```angelscript
void SetViewDistanceQuality(int Value)
```
Sets the view distance quality (0..4, higher is better)
@param Value 0:low, 1:medium, 2:high, 3:epic, 4:cinematic (gets clamped if needed)

### SetVisualEffectQuality
```angelscript
void SetVisualEffectQuality(int Value)
```
Sets the visual effects quality (0..4, higher is better)
@param Value 0:low, 1:medium, 2:high, 3:epic, 4:cinematic (gets clamped if needed)

### SetVSyncEnabled
```angelscript
void SetVSyncEnabled(bool bEnable)
```
Sets the user setting for vsync. See UGameUserSettings::bUseVSync.

### SupportsHDRDisplayOutput
```angelscript
bool SupportsHDRDisplayOutput()
```
Whether the curently running system supports HDR display output

### ValidateSettings
```angelscript
void ValidateSettings()
```
Validates and resets bad user settings to default. Deletes stale user settings file if necessary.

