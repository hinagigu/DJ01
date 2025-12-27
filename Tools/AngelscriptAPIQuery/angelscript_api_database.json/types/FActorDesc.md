# FActorDesc

Snapshot of an actor descriptor, which represents the state of an actor on disk.
The actor may or may not be loaded.

## 属性

### Guid
- **类型**: `FGuid`
- **描述**: The actor GUID of this descriptor.

### NativeClass
- **类型**: `UClass`
- **描述**: Actor first native class.

### Class
- **类型**: `FSoftObjectPath`
- **描述**: Actor class, can point to a native or Blueprint class and may be redirected.

### Name
- **类型**: `FName`
- **描述**: Internal name of the acgor.

### Label
- **类型**: `FName`
- **描述**: Actor's label.

### Bounds
- **类型**: `FBox`
- **描述**: Streaming bounds of this actor.

### RuntimeGrid
- **类型**: `FName`
- **描述**: Actor's target runtime grid.

### bIsSpatiallyLoaded
- **类型**: `bool`
- **描述**: Actor's streaming state.

### bActorIsEditorOnly
- **类型**: `bool`
- **描述**: Actor's editor-only property.

### ActorPackage
- **类型**: `FName`
- **描述**: Actor's package name.

### ActorPath
- **类型**: `FName`
- **描述**: Actor's path name.

### DataLayerAssets
- **类型**: `TArray<FSoftObjectPath>`
- **描述**: Actor's data layer assets.

## 方法

### opAssign
```angelscript
FActorDesc& opAssign(FActorDesc Other)
```

