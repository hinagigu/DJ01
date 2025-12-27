# FCollectionTransformSelectionInSphereDataflowNode

Selects bones if their Vertices/BoundingBox/Centroid in a sphere

## 属性

### Transform
- **类型**: `FTransform`
- **描述**: Transform for the sphere

### Type
- **类型**: `ESelectSubjectTypeEnum`
- **描述**: Subject (Vertices/BoundingBox/Centroid) to check against box

### bAllVerticesMustContainedInSphere
- **类型**: `bool`
- **描述**: If true all the vertices of the piece must be inside of box

### bActive
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FCollectionTransformSelectionInSphereDataflowNode& opAssign(FCollectionTransformSelectionInSphereDataflowNode Other)
```

