# ASwitchActor

**继承自**: `AActor`

Switch Actor allows quickly toggling the visibility of its child actors so that
only one is visible at a time. It can also be captured with the Variant Manager
to expose this capability as a property capture

## 属性

### SceneComponent
- **类型**: `USceneComponent`
- **描述**: Exposing our root component like this allows manual Mobility control on the details panel

## 方法

### GetOptions
```angelscript
TArray<AActor> GetOptions()
```
Returns the child actors that are available options, in a fixed order that may differ from the one displayed in the world outliner

### GetSelectedOption
```angelscript
int GetSelectedOption()
```
If we have exactly one child actor visible, it will return a pointer to it. Returns nullptr otherwise

### SelectOption
```angelscript
void SelectOption(int OptionIndex)
```
Select one of the available options by index

