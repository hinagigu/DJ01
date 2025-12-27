# FRigUnit_ProjectTransformToNewParent

Gets the relative offset between the child and the old parent, then multiplies by new parent's transform.

## 属性

### Child
- **类型**: `FRigElementKey`

### bChildInitial
- **类型**: `bool`

### OldParent
- **类型**: `FRigElementKey`

### bOldParentInitial
- **类型**: `bool`

### NewParent
- **类型**: `FRigElementKey`

### bNewParentInitial
- **类型**: `bool`

### Transform
- **类型**: `FTransform`
- **描述**: The resulting transform

## 方法

### opAssign
```angelscript
FRigUnit_ProjectTransformToNewParent& opAssign(FRigUnit_ProjectTransformToNewParent Other)
```

