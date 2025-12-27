# UDJ01LoadingScreenWidget

**继承自**: `UUserWidget`

UDJ01LoadingScreenWidget

Base class for loading screen widgets.
You can create a Blueprint based on this class and customize the appearance.

## 属性

### CurrentProgress
- **类型**: `float32`

### CurrentTipText
- **类型**: `FText`

## 方法

### OnLoadingScreenHidden
```angelscript
void OnLoadingScreenHidden()
```
Called when the loading screen is about to be hidden

### OnLoadingScreenShown
```angelscript
void OnLoadingScreenShown()
```
Called when the loading screen is shown

### OnProgressUpdated
```angelscript
void OnProgressUpdated(float Progress)
```
Override in Blueprint to update progress bar

### OnTipTextUpdated
```angelscript
void OnTipTextUpdated(FText TipText)
```
Override in Blueprint to update tip text

### SetLoadingProgress
```angelscript
void SetLoadingProgress(float32 Progress)
```
Updates the loading progress (0.0 to 1.0)

### SetLoadingTipText
```angelscript
void SetLoadingTipText(FText TipText)
```
Updates the loading tip/message text

