# FSkeletalMeshVertexAttributeInfo

A structure to store user-controllable settings for attributes

## 属性

### EnabledForRender
- **类型**: `FPerPlatformBool`
- **描述**: Whether this vertex attribute should be included in the render data. Requires a rebuild of the render mesh.

### DataType
- **类型**: `ESkeletalMeshVertexAttributeDataType`
- **描述**: The data type to store the vertex data as for rendering

## 方法

### opAssign
```angelscript
FSkeletalMeshVertexAttributeInfo& opAssign(FSkeletalMeshVertexAttributeInfo Other)
```

