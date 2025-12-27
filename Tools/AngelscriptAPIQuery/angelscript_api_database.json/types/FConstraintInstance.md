# FConstraintInstance

Container for a physics representation of an object.

## 属性

### ConstraintBone1
- **类型**: `FName`
- **描述**: Name of first bone (body) that this constraint is connecting.
This will be the 'child' bone in a PhysicsAsset.

### ConstraintBone2
- **类型**: `FName`
- **描述**: Name of second bone (body) that this constraint is connecting.
This will be the 'parent' bone in a PhysicsAset.

### Pos1
- **类型**: `FVector`
- **描述**: Location of constraint in Body1 reference frame (usually the "child" body for skeletal meshes).

### PriAxis1
- **类型**: `FVector`
- **描述**: Primary (twist) axis in Body1 reference frame.

### SecAxis1
- **类型**: `FVector`
- **描述**: Secondary axis in Body1 reference frame. Orthogonal to PriAxis1.

### Pos2
- **类型**: `FVector`
- **描述**: Location of constraint in Body2 reference frame (usually the "parent" body for skeletal meshes).

### PriAxis2
- **类型**: `FVector`
- **描述**: Primary (twist) axis in Body2 reference frame.

### SecAxis2
- **类型**: `FVector`
- **描述**: Secondary axis in Body2 reference frame. Orthogonal to PriAxis2.

### AngularRotationOffset
- **类型**: `FRotator`
- **描述**: Specifies the angular offset between the two frames of reference. By default limit goes from (-Angle, +Angle)
This allows you to bias the limit for swing1 swing2 and twist.

### ProfileInstance
- **类型**: `FConstraintProfileProperties`
- **描述**: Constraint Data (properties easily swapped at runtime based on different constraint profiles)

### bScaleLinearLimits
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FConstraintInstance& opAssign(FConstraintInstance Other)
```

