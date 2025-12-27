# UIKRigDefinition

**继承自**: `UObject`

## 属性

### PreviewSkeletalMesh
- **类型**: `TSoftObjectPtr<USkeletalMesh>`
- **描述**: The skeletal mesh to run the IK solve on (loaded into viewport).
NOTE: you can assign ANY Skeletal Mesh to apply the IK Rig to. Compatibility is determined when a new mesh is assigned
by comparing it's hierarchy with the goals, solvers and bone settings required by the rig. See output log for details.

### DrawGoals
- **类型**: `bool`
- **描述**: Draw bones in the viewport.

### GoalSize
- **类型**: `float32`
- **描述**: The size of the Goals in the editor viewport.

### GoalThickness
- **类型**: `float32`
- **描述**: The thickness of the Goals in the editor viewport.

