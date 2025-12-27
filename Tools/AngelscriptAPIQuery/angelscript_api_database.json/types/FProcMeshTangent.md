# FProcMeshTangent

Struct used to specify a tangent vector for a vertex
The Y tangent is computed from the cross product of the vertex normal (Tangent Z) and the TangentX member.

## 属性

### TangentX
- **类型**: `FVector`

### bFlipTangentY
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FProcMeshTangent& opAssign(FProcMeshTangent Other)
```

