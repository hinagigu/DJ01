# UPoseableMeshComponent

**继承自**: `USkinnedMeshComponent`

UPoseableMeshComponent that allows bone transforms to be driven by blueprint.

## 方法

### CopyPoseFromSkeletalComponent
```angelscript
void CopyPoseFromSkeletalComponent(USkeletalMeshComponent InComponentToCopy)
```

### GetBoneLocationByName
```angelscript
FVector GetBoneLocationByName(FName BoneName, EBoneSpaces BoneSpace)
```

### GetBoneRotationByName
```angelscript
FRotator GetBoneRotationByName(FName BoneName, EBoneSpaces BoneSpace)
```

### GetBoneScaleByName
```angelscript
FVector GetBoneScaleByName(FName BoneName, EBoneSpaces BoneSpace)
```

### GetBoneTransformByName
```angelscript
FTransform GetBoneTransformByName(FName BoneName, EBoneSpaces BoneSpace)
```

### ResetBoneTransformByName
```angelscript
void ResetBoneTransformByName(FName BoneName)
```

### SetBoneLocationByName
```angelscript
void SetBoneLocationByName(FName BoneName, FVector InLocation, EBoneSpaces BoneSpace)
```

### SetBoneRotationByName
```angelscript
void SetBoneRotationByName(FName BoneName, FRotator InRotation, EBoneSpaces BoneSpace)
```

### SetBoneScaleByName
```angelscript
void SetBoneScaleByName(FName BoneName, FVector InScale3D, EBoneSpaces BoneSpace)
```

### SetBoneTransformByName
```angelscript
void SetBoneTransformByName(FName BoneName, FTransform InTransform, EBoneSpaces BoneSpace)
```

