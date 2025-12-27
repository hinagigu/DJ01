# FAddNewSubobjectParams

Options when adding a new subobject

## 属性

### ParentHandle
- **类型**: `FSubobjectDataHandle`

### NewClass
- **类型**: `UClass`
- **描述**: The class of the new subobject that will be added

### BlueprintContext
- **类型**: `UBlueprint`
- **描述**: Pointer to the blueprint context that this subobject is in. If this is null, it is assumed that
this subobject is being added to an instance.

### bSkipMarkBlueprintModified
- **类型**: `bool`

### bConformTransformToParent
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FAddNewSubobjectParams& opAssign(FAddNewSubobjectParams Other)
```

