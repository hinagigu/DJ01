# FCreateTextureObjectParams

FCreateTextureObjectParams is a collection of input data intended to be passed to
UModelingObjectsCreationAPI::CreateTextureObject(). Not all data necessarily needs
to be specified, this will depend on the particular implementation. The comments
below are representative of how this data structure is used in the Tools and
API implementation(s) provided with Unreal Engine, but end-user implementors
could abuse these fields as necessary.

The definition of a "texture object" is implementation-specific.
In the UE Editor this is generally a UTexture2D

## 属性

### TypeHintExtended
- **类型**: `int`
- **描述**: An arbitrary integer that can be used to pass data to an API implementation

### TargetWorld
- **类型**: `UWorld`
- **描述**: The World/Level the new texture object should be created in (if known).
Note that Textures generally do not exist as objects in a Level.
However, it may be necessary to store the texture in a path relative to the
level (for example if the level is in a Plugin, this would be necessary in-Editor)

### StoreRelativeToObject
- **类型**: `UObject`
- **描述**: An object to store the Texture relative to. For example the texture could be stored at the same path.

### BaseName
- **类型**: `FString`
- **描述**: The base name of the new mesh object

### GeneratedTransientTexture
- **类型**: `UTexture2D`
- **描述**: Texture source data. Generally assumed that this is a Texture created in the Transient package
that is intended to be saved in a permanent package.

## 方法

### opAssign
```angelscript
FCreateTextureObjectParams& opAssign(FCreateTextureObjectParams Other)
```

