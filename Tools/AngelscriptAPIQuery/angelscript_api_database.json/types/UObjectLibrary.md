# UObjectLibrary

**继承自**: `UObject`

Class that holds a library of Objects

## 属性

### ObjectBaseClass
- **类型**: `UClass`
- **描述**: Class that Objects must be of. If ContainsBlueprints is true, this is the native class that the blueprints are instances of and not UClass

### bHasBlueprintClasses
- **类型**: `bool`
- **描述**: True if this library holds blueprint classes, false if it holds other objects

### Objects
- **类型**: `TArray<TObjectPtr<UObject>>`
- **描述**: List of Objects in library

