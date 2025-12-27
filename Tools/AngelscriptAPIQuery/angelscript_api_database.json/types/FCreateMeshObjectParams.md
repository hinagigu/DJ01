# FCreateMeshObjectParams

FCreateMeshObjectParams is a collection of input data intended to be passed to
UModelingObjectsCreationAPI::CreateMeshObject(). Not all data necessarily needs
to be specified, this will depend on the particular implementation. The comments
below are representative of how this data structure is used in the Tools and
API implementation(s) provided with Unreal Engine, but end-user implementors
could abuse these fields as necessary.

The definition of a "mesh object" is implementation-specific.

## 属性

### SourceComponent
- **类型**: `UPrimitiveComponent`
- **描述**: A Source Component the new mesh is based on, if such a Component exists

### TypeHint
- **类型**: `ECreateObjectTypeHint`
- **描述**: A suggested type for the newly-created Mesh (possibly ignored)

### TypeHintClass
- **类型**: `UClass`
- **描述**: A suggested UClass type for the newly-created Object (possibly ignored)

### TypeHintExtended
- **类型**: `int`
- **描述**: An arbitrary integer that can be used to pass data to an API implementation

### TargetWorld
- **类型**: `UWorld`
- **描述**: The World/Level the new mesh object should be created in (if known)

### Transform
- **类型**: `FTransform`
- **描述**: The 3D local-to-world transform for the new mesh object

### BaseName
- **类型**: `FString`
- **描述**: The base name of the new mesh object

### Materials
- **类型**: `TArray<TObjectPtr<UMaterialInterface>>`
- **描述**: Materials for the new mesh object

### AssetMaterials
- **类型**: `TArray<TObjectPtr<UMaterialInterface>>`
- **描述**: Optional Materials for a newly-created Mesh Asset, if this is applicable for the created mesh object

### bEnableCollision
- **类型**: `bool`
- **描述**: Specify whether the new mesh object should have collision support/data

### CollisionMode
- **类型**: `ECollisionTraceFlag`
- **描述**: Which Collision mode to enable on the new mesh object, if supported

### bEnableRaytracingSupport
- **类型**: `bool`
- **描述**: Specify whether normals should be automatically recomputed for this new mesh object

### bGenerateLightmapUVs
- **类型**: `bool`
- **描述**: Specify whether to auto-generate Lightmap UVs (if applicable for the output mesh type)

### bEnableRecomputeNormals
- **类型**: `bool`
- **描述**: Specify whether normals should be automatically recomputed for this new mesh object

### bEnableRecomputeTangents
- **类型**: `bool`
- **描述**: Specify whether tangents should be automatically recomputed for this new mesh object

### bEnableNanite
- **类型**: `bool`
- **描述**: Specify whether Nanite should be enabled on this new mesh object

### NaniteSettings
- **类型**: `FMeshNaniteSettings`
- **描述**: Specify the Nanite Settings for this new mesh object, only used if bEnableNanite=true

## 方法

### opAssign
```angelscript
FCreateMeshObjectParams& opAssign(FCreateMeshObjectParams Other)
```

