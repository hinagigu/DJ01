# FFBIKConstraintOption

## 属性

### Item
- **类型**: `FRigElementKey`
- **描述**: Bone Name

### bEnabled
- **类型**: `bool`

### bUseStiffness
- **类型**: `bool`

### LinearStiffness
- **类型**: `FVector`
- **描述**: Scale of [0, 1] and applied to linear motion strength - linear stiffness works on their local frame

### AngularStiffness
- **类型**: `FVector`
- **描述**: Scale of [0, 1] and applied to angular motion strength, xyz is applied to twist, swing1, swing2

### bUseAngularLimit
- **类型**: `bool`

### AngularLimit
- **类型**: `FFBIKBoneLimit`
- **描述**: Angular delta limit of this joints local transform. [-Limit, Limit]

### bUsePoleVector
- **类型**: `bool`

### PoleVectorOption
- **类型**: `EPoleVectorOption`

### PoleVector
- **类型**: `FVector`
- **描述**: Pole Vector in their local space

### OffsetRotation
- **类型**: `FRotator`
- **描述**: this is offset rotation applied when constructing the local frame

## 方法

### opAssign
```angelscript
FFBIKConstraintOption& opAssign(FFBIKConstraintOption Other)
```

