# __Automation

## 方法

### AddExpectedLogError
```angelscript
void AddExpectedLogError(FString ExpectedPatternString, int Occurrences, bool ExactMatch, bool IsRegex)
```
Mute the report of log error and warning matching a pattern during an automated test. Treat the pattern as regex by default.
@param ExpectedPatternString Expects a Regex pattern.

### AddExpectedLogMessage
```angelscript
void AddExpectedLogMessage(FString ExpectedPatternString, int Occurrences, bool ExactMatch, bool IsRegex)
```
Expect a specific log message to match a pattern during an automated test regardless of its verbosity. Treat the pattern as regex by default.

### AddExpectedPlainLogError
```angelscript
void AddExpectedPlainLogError(FString ExpectedString, int Occurrences, bool ExactMatch)
```
Mute the report of log error and warning matching a plain string during an automated test

### AddExpectedPlainLogMessage
```angelscript
void AddExpectedPlainLogMessage(FString ExpectedString, int Occurrences, bool ExactMatch)
```
Expect a specific log message to match a plain string during an automated test regardless of its verbosity

### AddTestError
```angelscript
void AddTestError(FString InLogItem)
```
Add error to currently running automated test.

### AddTestInfo
```angelscript
void AddTestInfo(FString InLogItem)
```
Add info to currently running automated test.

### AddTestTelemetryData
```angelscript
void AddTestTelemetryData(FString DataPoint, float32 Measurement, FString Context)
```
Add Telemetry data to currently running automated test.

### AddTestWarning
```angelscript
void AddTestWarning(FString InLogItem)
```
Add warning to currently running automated test.

### AreAutomatedTestsRunning
```angelscript
bool AreAutomatedTestsRunning()
```
Lets you know if any automated tests are running, or are about to run and the automation system is spinning up tests.

### AutomationWaitForLoading
```angelscript
void AutomationWaitForLoading(UObject WorldContextObject, FLatentActionInfo LatentInfo, FAutomationWaitForLoadingOptions Options)
```

### CompareImageAgainstReference
```angelscript
bool CompareImageAgainstReference(FString ImageFilePath, FString ComparisonName, EComparisonTolerance ComparisonTolerance, FString ComparisonNotes, UObject WorldContextObject)
```
request image comparison.
@param ImageFilePath  Absolute path to the image location. All 8bit RGBA channels supported formats by the engine are accepted.
@param ComparisonName Optional name for the comparison, by default the basename of ImageFilePath is used
@return                               True if comparison was successfully enqueued

### DisableStatGroup
```angelscript
void DisableStatGroup(UObject WorldContextObject, FName GroupName)
```

### EnableStatGroup
```angelscript
void EnableStatGroup(UObject WorldContextObject, FName GroupName)
```

### FinishLoadingBeforeScreenshot
```angelscript
void FinishLoadingBeforeScreenshot()
```

### GetDefaultScreenshotOptionsForGameplay
```angelscript
FAutomationScreenshotOptions GetDefaultScreenshotOptionsForGameplay(EComparisonTolerance Tolerance, float32 Delay)
```

### GetDefaultScreenshotOptionsForRendering
```angelscript
FAutomationScreenshotOptions GetDefaultScreenshotOptionsForRendering(EComparisonTolerance Tolerance, float32 Delay)
```

### GetStatCallCount
```angelscript
float32 GetStatCallCount(FName StatName)
```

### GetStatExcAverage
```angelscript
float32 GetStatExcAverage(FName StatName)
```

### GetStatExcMax
```angelscript
float32 GetStatExcMax(FName StatName)
```

### GetStatIncAverage
```angelscript
float32 GetStatIncAverage(FName StatName)
```

### GetStatIncMax
```angelscript
float32 GetStatIncMax(FName StatName)
```

### SetEditorViewportViewMode
```angelscript
void SetEditorViewportViewMode(EViewModeIndex Index)
```
Sets all viewports of the first found level editor to have the given ViewMode (Lit/Unlit/etc.) *

### SetEditorViewportVisualizeBuffer
```angelscript
void SetEditorViewportVisualizeBuffer(FName BufferName)
```
Sets all viewports of the first found level editor to have the VisualizeBuffer ViewMode and also display a given buffer (BaseColor/Metallic/Roughness/etc.) *

### SetScalabilityQualityLevelRelativeToMax
```angelscript
void SetScalabilityQualityLevelRelativeToMax(UObject WorldContextObject, int Value)
```
Sets all other settings based on an overall value
@param Value 0:Cinematic, 1:Epic...etc.

### SetScalabilityQualityToEpic
```angelscript
void SetScalabilityQualityToEpic(UObject WorldContextObject)
```

### SetScalabilityQualityToLow
```angelscript
void SetScalabilityQualityToLow(UObject WorldContextObject)
```

### SetTestTelemetryStorage
```angelscript
void SetTestTelemetryStorage(FString StorageName)
```
Set Telemetry data storage name of currently running automated test.

### TakeAutomationScreenshot
```angelscript
void TakeAutomationScreenshot(UObject WorldContextObject, FLatentActionInfo LatentInfo, FString Name, FString Notes, FAutomationScreenshotOptions Options)
```
Takes a screenshot of the game's viewport.  Does not capture any UI.

### TakeAutomationScreenshotAtCamera
```angelscript
void TakeAutomationScreenshotAtCamera(UObject WorldContextObject, FLatentActionInfo LatentInfo, ACameraActor Camera, FString NameOverride, FString Notes, FAutomationScreenshotOptions Options)
```
Takes a screenshot of the game's viewport, from a particular camera actors POV.  Does not capture any UI.

### TakeAutomationScreenshotOfUI
```angelscript
void TakeAutomationScreenshotOfUI(UObject WorldContextObject, FLatentActionInfo LatentInfo, FString Name, FAutomationScreenshotOptions Options)
```

### TakeHighResScreenshot
```angelscript
UAutomationEditorTask TakeHighResScreenshot(int ResX, int ResY, FString Filename, ACameraActor Camera, bool bMaskEnabled, bool bCaptureHDR, EComparisonTolerance ComparisonTolerance, FString ComparisonNotes, float32 Delay, bool bForceGameView)
```
take high res screenshot in editor.

