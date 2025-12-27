# USequencerCurveEditorObject

**继承自**: `UObject`

* Class to hold sequencer curve editor functions

## 方法

### CloseCurveEditor
```angelscript
void CloseCurveEditor()
```
Close curve editor

### DeleteColorForChannels
```angelscript
void DeleteColorForChannels(UClass Class, FString& Identifier)
```
Delete for specified channel idendified by it's class and identifier.

### EmptySelection
```angelscript
void EmptySelection()
```
Empties the current selection.

### GetChannelsWithSelectedKeys
```angelscript
TArray<FSequencerChannelProxy> GetChannelsWithSelectedKeys()
```
Gets the channel with selected keys

### GetCustomColorForChannel
```angelscript
FLinearColor GetCustomColorForChannel(UClass Class, FString Identifier)
```
Get custom color for specified channel idendified by it's class and identifier,if none exists will return white

### GetSelectedKeys
```angelscript
TArray<int> GetSelectedKeys(FSequencerChannelProxy ChannelProxy)
```
Gets the selected keys with this channel

### HasCustomColorForChannel
```angelscript
bool HasCustomColorForChannel(UClass Class, FString Identifier)
```
Get if a custom color for specified channel idendified by it's class and identifier exists

### IsCurveEditorOpen
```angelscript
bool IsCurveEditorOpen()
```
Is curve editor open

### OpenCurveEditor
```angelscript
void OpenCurveEditor()
```
Open curve editor

### SelectKeys
```angelscript
void SelectKeys(FSequencerChannelProxy Channel, TArray<int> Indices)
```
Select keys

### SetCustomColorForChannel
```angelscript
void SetCustomColorForChannel(UClass Class, FString Identifier, FLinearColor NewColor)
```
Set Custom Color for specified channel idendified by it's class and identifier. This will be stored in editor user preferences.

### SetCustomColorForChannels
```angelscript
void SetCustomColorForChannels(UClass Class, TArray<FString> Identifiers, TArray<FLinearColor> NewColors)
```
Set Custom Color for specified channels idendified by it's class and identifiers. This will be stored in editor user preferences.

### SetRandomColorForChannels
```angelscript
void SetRandomColorForChannels(UClass Class, TArray<FString> Identifiers)
```
Set Random Colors for specified channels idendified by it's class and identifiers. This will be stored in editor user preferences.

