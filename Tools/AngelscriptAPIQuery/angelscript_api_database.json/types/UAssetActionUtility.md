# UAssetActionUtility

**继承自**: `UEditorUtilityObject`

Base class for all asset action-related utilities
Any functions/events that are exposed on derived classes that have the correct signature will be
included as menu options when right-clicking on a group of assets in the content browser.

## 属性

### bIsActionForBlueprints
- **类型**: `bool`
- **描述**: Is this action designed to work specifically on Blueprints (true) or on all assets (false).
If true, SupportedClasses is treated as a filter against the Parent Class of selected Blueprint assets.

### SupportedConditions
- **类型**: `TArray<FAssetActionSupportCondition>`
- **描述**: The supported conditions for any asset to use these utility functions.  Note: all of these conditions must pass
in sequence.  So if you have earlier failure conditions you want to be run first, put them first in the list,
if those fail, their failure reason will be handled first.

### SupportedClasses
- **类型**: `TArray<TSoftClassPtr<UObject>>`

## 方法

### GetSupportedClasses
```angelscript
TArray<TSoftClassPtr<UObject>> GetSupportedClasses()
```
Gets the statically determined supported classes, these classes are used as a first pass filter when determining
if we can utilize this asset utility action on the asset.

### IsActionForBlueprints
```angelscript
bool IsActionForBlueprints()
```
Returns whether or not this action is designed to work specifically on Blueprints (true) or on all assets (false).
If true, GetSupportedClass() is treated as a filter against the Parent Class of selected Blueprint assets.
@note Returns the value of bIsActionForBlueprints by default.

