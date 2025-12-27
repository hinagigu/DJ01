# FCreateActorParams

FCreateActorParams is a collection of input data intended to be passed to
UModelingObjectsCreationAPI::CreateNewActor().

## 属性

### TargetWorld
- **类型**: `UWorld`
- **描述**: The World/Level the new Actor should be created in (if known).

### BaseName
- **类型**: `FString`
- **描述**: The base name of the new Actor

### Transform
- **类型**: `FTransform`
- **描述**: The 3D local-to-world transform for the new actor

### TemplateAsset
- **类型**: `UObject`
- **描述**: A template Asset used to determine the type of Actor to spawn.

## 方法

### opAssign
```angelscript
FCreateActorParams& opAssign(FCreateActorParams Other)
```

