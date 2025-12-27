# UActorActionUtility

**继承自**: `UEditorUtilityObject`

Base class for all actor action-related utilities
Any functions/events that are exposed on derived classes that have the correct signature will be
included as menu options when right-clicking on a group of actors in the level editor.

## 属性

### SupportedClasses
- **类型**: `TArray<TSoftClassPtr<UObject>>`

## 方法

### GetSupportedClasses
```angelscript
TArray<TSoftClassPtr<UObject>> GetSupportedClasses()
```
Gets the statically determined supported classes, these classes are used as a first pass filter when determining
if we can utilize this asset utility action on the asset.

