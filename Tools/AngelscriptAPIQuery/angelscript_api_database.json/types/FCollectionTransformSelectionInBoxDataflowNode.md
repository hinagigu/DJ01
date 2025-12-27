# FCollectionTransformSelectionInBoxDataflowNode

Selects bones if their Vertices/BoundingBox/Centroid in a box

## 属性

### Transform
- **类型**: `FTransform`
- **描述**: Transform for the box

### Type
- **类型**: `ESelectSubjectTypeEnum`
- **描述**: Subject (Vertices/BoundingBox/Centroid) to check against box

### bAllVerticesMustContainedInBox
- **类型**: `bool`
- **描述**: If true all the vertices of the piece must be inside of box

### bActive
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FCollectionTransformSelectionInBoxDataflowNode& opAssign(FCollectionTransformSelectionInBoxDataflowNode Other)
```

