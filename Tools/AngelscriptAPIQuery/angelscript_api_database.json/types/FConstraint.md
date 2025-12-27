# FConstraint

Constraint Set up

## 属性

### TargetBone
- **类型**: `FBoneReference`
- **描述**: Target Bone this is constraint to

### OffsetOption
- **类型**: `EConstraintOffsetOption`
- **描述**: Maintain offset based on refpose or not.

None - no offset
Offset_RefPose - offset is created based on reference pose

In the future, we'd like to support custom offset, not just based on ref pose

### TransformType
- **类型**: `ETransformConstraintType`
- **描述**: What transform type is constraint to - Translation, Rotation, Scale OR Parent. Parent overrides all component

### PerAxis
- **类型**: `FFilterOptionPerAxis`
- **描述**: Per axis filter options - applied in their local space not in world space

## 方法

### opAssign
```angelscript
FConstraint& opAssign(FConstraint Other)
```

