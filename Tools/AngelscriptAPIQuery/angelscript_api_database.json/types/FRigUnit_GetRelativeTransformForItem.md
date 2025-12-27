# FRigUnit_GetRelativeTransformForItem

GetRelativeTransform is used to retrieve a single transform from a hierarchy in the space of another transform

## 属性

### Child
- **类型**: `FRigElementKey`

### bChildInitial
- **类型**: `bool`

### Parent
- **类型**: `FRigElementKey`

### bParentInitial
- **类型**: `bool`

### RelativeTransform
- **类型**: `FTransform`
- **描述**: The transform of the given child item relative to the provided parent

## 方法

### opAssign
```angelscript
FRigUnit_GetRelativeTransformForItem& opAssign(FRigUnit_GetRelativeTransformForItem Other)
```

