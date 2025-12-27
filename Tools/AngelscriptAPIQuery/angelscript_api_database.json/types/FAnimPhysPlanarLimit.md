# FAnimPhysPlanarLimit

## 属性

### DrivingBone
- **类型**: `FBoneReference`
- **描述**: When using a driving bone, the plane transform will be relative to the bone transform

### PlaneTransform
- **类型**: `FTransform`
- **描述**: Transform of the plane, this is either in component-space if no DrivinBone is specified
or in bone-space if a driving bone is present.

## 方法

### opAssign
```angelscript
FAnimPhysPlanarLimit& opAssign(FAnimPhysPlanarLimit Other)
```

