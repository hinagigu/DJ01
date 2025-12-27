# UIKRetargeter

**继承自**: `UObject`

## 属性

### SourceIKRigAsset
- **类型**: `TSoftObjectPtr<UIKRigDefinition>`
- **描述**: The rig to copy animation FROM.

### SourcePreviewMesh
- **类型**: `TSoftObjectPtr<USkeletalMesh>`
- **描述**: Optional. Override the Skeletal Mesh to copy animation from. Uses the preview mesh from the Source IK Rig asset by default.

### TargetIKRigAsset
- **类型**: `TSoftObjectPtr<UIKRigDefinition>`
- **描述**: The rig to copy animation TO.

### TargetPreviewMesh
- **类型**: `TSoftObjectPtr<USkeletalMesh>`
- **描述**: Optional. Override the Skeletal Mesh to preview the retarget on. Uses the preview mesh from the Target IK Rig asset by default.

### TargetMeshOffset
- **类型**: `FVector`
- **描述**: The offset applied to the target mesh in the editor viewport.

### TargetMeshScale
- **类型**: `float32`
- **描述**: Scale the target mesh in the viewport for easier visualization next to the source.

### SourceMeshOffset
- **类型**: `FVector`
- **描述**: The offset applied to the source mesh in the editor viewport.

### bIgnoreRootLockInPreview
- **类型**: `bool`
- **描述**: When true, animation sequences with "Force Root Lock" turned On will act as though it is Off.
This affects only the preview in the retarget editor. Use ExportRootLockMode to control exported animation behavior.
This setting has no effect on runtime retargeting where root motion is copied from the source component.

### bDebugDraw
- **类型**: `bool`
- **描述**: Toggle debug drawing for retargeting in the viewport.

### bDrawFinalGoals
- **类型**: `bool`
- **描述**: Draw final IK goal locations.

### bDrawSourceLocations
- **类型**: `bool`
- **描述**: Draw goal locations from source skeleton.

### ChainDrawSize
- **类型**: `float32`
- **描述**: The visual size of the IK goals in the viewport.

### ChainDrawThickness
- **类型**: `float32`
- **描述**: The thickness of lines on the IK goals in the viewport.

## 方法

### HasSourceIKRig
```angelscript
bool HasSourceIKRig()
```
Returns true if the source IK Rig has been assigned

### HasTargetIKRig
```angelscript
bool HasTargetIKRig()
```
Returns true if the target IK Rig has been assigned

