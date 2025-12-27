# FCreateMaterialObjectParams

FCreateMaterialObjectParams is a collection of input data intended to be passed to
UModelingObjectsCreationAPI::CreateMaterialObject().

## 属性

### TargetWorld
- **类型**: `UWorld`
- **描述**: The World/Level the new Material object should be created in (if known).
Note that Material generally do not exist as objects in a Level.
However, it may be necessary to store the texture in a path relative to the
level (for example if the level is in a Plugin, this would be necessary in-Editor)

### StoreRelativeToObject
- **类型**: `UObject`
- **描述**: An object to store the Material relative to.

### BaseName
- **类型**: `FString`
- **描述**: The base name of the new Material object

### MaterialToDuplicate
- **类型**: `UMaterialInterface`
- **描述**: The parent UMaterial of this material will be duplicated to create the new UMaterial Asset.

## 方法

### opAssign
```angelscript
FCreateMaterialObjectParams& opAssign(FCreateMaterialObjectParams Other)
```

