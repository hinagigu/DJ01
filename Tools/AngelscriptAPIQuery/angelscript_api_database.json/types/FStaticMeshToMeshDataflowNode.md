# FStaticMeshToMeshDataflowNode

Converts a StaticMesh into a DynamicMesh

## 属性

### StaticMesh
- **类型**: `UStaticMesh`
- **描述**: StaticMesh to convert

### bUseHiRes
- **类型**: `bool`
- **描述**: Output the HiRes representation, if set to true and HiRes doesn't exist it will output empty mesh

### LODLevel
- **类型**: `int`
- **描述**: Specifies the LOD level to use

### bActive
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FStaticMeshToMeshDataflowNode& opAssign(FStaticMeshToMeshDataflowNode Other)
```

