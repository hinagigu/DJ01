# UComboGraphNodeMontage

**继承自**: `UComboGraphNodeAnimBase`

Base Class for Combo Graph nodes acting based on an Anim Montage asset.

Holds runtime properties for animation and effects / cues containers.

## 属性

### Montage
- **类型**: `TSoftObjectPtr<UAnimMontage>`

### StartSection
- **类型**: `FName`

## 方法

### GetMontageStartSection
```angelscript
FName GetMontageStartSection()
```
Blueprint overridable method to return the Start Section name to use with the Combo Play Montage task. Default behavior is simply to return `StartSection` property of the combo node.

