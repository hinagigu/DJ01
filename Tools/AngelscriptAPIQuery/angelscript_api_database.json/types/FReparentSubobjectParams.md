# FReparentSubobjectParams

Options for reparenting subobjects

## 属性

### NewParentHandle
- **类型**: `FSubobjectDataHandle`
- **描述**: The handle of the subobject to reparent to.

### BlueprintContext
- **类型**: `UBlueprint`
- **描述**: Pointer to the blueprint context that this subobject is in. If this is null, it is assumed that
this subobject is being added to an instance.

### ActorPreviewContext
- **类型**: `AActor`
- **描述**: The preview actor context to be used if in a blueprint context.
This must have a value if BlueprintContext is needed.

## 方法

### opAssign
```angelscript
FReparentSubobjectParams& opAssign(FReparentSubobjectParams Other)
```

