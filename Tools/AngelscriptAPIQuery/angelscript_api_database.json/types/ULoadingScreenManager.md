# ULoadingScreenManager

**继承自**: `UGameInstanceSubsystem`

ULoadingScreenManager

Manages the display of loading screens during gameplay.
Automatically shows/hides the loading screen based on various game states and
objects implementing ILoadingProcessInterface.

## 方法

### GetDebugReasonForShowingOrHidingLoadingScreen
```angelscript
FString GetDebugReasonForShowingOrHidingLoadingScreen()
```
Returns the debug reason for showing or hiding the loading screen

### GetLoadingScreenDisplayStatus
```angelscript
bool GetLoadingScreenDisplayStatus()
```
Returns True when the loading screen is currently being shown

