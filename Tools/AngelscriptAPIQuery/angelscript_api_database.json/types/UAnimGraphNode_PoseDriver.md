# UAnimGraphNode_PoseDriver

**继承自**: `UAnimGraphNode_PoseHandler`

## 属性

### Node
- **类型**: `FAnimNode_PoseDriver`

### AxisLength
- **类型**: `float32`
- **描述**: Length of axis in world units used for debug drawing

### ConeSubdivision
- **类型**: `int`
- **描述**: Number of subdivisions / lines used when debug drawing a cone

### bDrawDebugCones
- **类型**: `bool`
- **描述**: If checked the cones will be drawn in 3d for debugging

## 方法

### CopyTargetsFromPoseAsset
```angelscript
void CopyTargetsFromPoseAsset()
```
Util to replace current contents of PoseTargets with info from assigned PoseAsset

### GetDrivingBoneNames
```angelscript
void GetDrivingBoneNames(TArray<FName>& BoneNames)
```
Returns the pose-driver its driven bones by name

### GetPoseDriverOutput
```angelscript
EPoseDriverOutput& GetPoseDriverOutput()
```

### GetPoseDriverSource
```angelscript
EPoseDriverSource& GetPoseDriverSource()
```

### GetRBFParameters
```angelscript
FRBFParams& GetRBFParameters()
```

### GetSourceBoneNames
```angelscript
void GetSourceBoneNames(TArray<FName>& BoneNames)
```
Returns the pose-driver its source bones by name

### SetDrivingBones
```angelscript
void SetDrivingBones(TArray<FName> BoneNames)
```
Set the pose-driver its driven bones by name

### SetPoseDriverOutput
```angelscript
void SetPoseDriverOutput(EPoseDriverOutput DriverOutput)
```

### SetPoseDriverSource
```angelscript
void SetPoseDriverSource(EPoseDriverSource DriverSource)
```

### SetRBFParameters
```angelscript
void SetRBFParameters(FRBFParams Parameters)
```

### SetSourceBones
```angelscript
void SetSourceBones(TArray<FName> BoneNames)
```
Sets the pose-driver its source bones by name

