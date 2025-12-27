# USkeletonModifier

**继承自**: `UObject`

FSkeletalMeshSkeletonModifier

## 方法

### AddBone
```angelscript
bool AddBone(FName InBoneName, FName InParentName, FTransform InTransform)
```
Creates a new bone in the skeleton hierarchy at desired transform
@param InBoneName The new bone's name.
@param InParentName The new bone parent's name.
@param InTransform The default local transform in the parent space.
@return \c true if the operation succeeded, false otherwise.

### AddBones
```angelscript
bool AddBones(TArray<FName> InBonesName, TArray<FName> InParentsName, TArray<FTransform> InTransforms)
```

### CommitSkeletonToSkeletalMesh
```angelscript
bool CommitSkeletonToSkeletalMesh()
```
Actually applies the skeleton modifications to the skeletal mesh.
@return true if commit succeeded.

### GetAllBoneNames
```angelscript
TArray<FName> GetAllBoneNames()
```
Get All Bone Names
@return \c All bone names list

### GetBoneTransform
```angelscript
FTransform GetBoneTransform(FName InBoneName, bool bGlobal)
```
Get Bone Transform
@param InBoneName The current bone's name.
@param bGlobal Whether it should return the parent space or global transform
@return \c The current bone's transform

### GetChildrenNames
```angelscript
TArray<FName> GetChildrenNames(FName InBoneName, bool bRecursive)
```
Get Children Names
@param InBoneName The parent's name.
@param bRecursive If set to true grand-children will also be added recursively
@return \c The children names list

### GetParentName
```angelscript
FName GetParentName(FName InBoneName)
```
Get Parent Name
@param InBoneName The current bone's name.
@return \c The current bone's parent name

### MirrorBone
```angelscript
bool MirrorBone(FName InBoneName, FMirrorOptions InOptions)
```
Mirror bones
@param InBoneName The new bone's name.
@param InOptions The mirroring options
@return \c true if the operation succeeded, false otherwise.

### MirrorBones
```angelscript
bool MirrorBones(TArray<FName> InBonesName, FMirrorOptions InOptions)
```

### OrientBone
```angelscript
bool OrientBone(FName InBoneName, FOrientOptions InOptions)
```
Align bones
@param InBoneName The current bone's name.
@param InOptions The orienting options
@return \c true if the operation succeeded, false otherwise.

### OrientBones
```angelscript
bool OrientBones(TArray<FName> InBoneNames, FOrientOptions InOptions)
```

### ParentBone
```angelscript
bool ParentBone(FName InBoneName, FName InParentName)
```
Parent bones
@param InBoneName The current bone's name.
@param InParentName The new parent's name (Name_NONE to unparent).
@return \c true if the operation succeeded, false otherwise.

### ParentBones
```angelscript
bool ParentBones(TArray<FName> InBoneNames, TArray<FName> InParentNames)
```

### RemoveBone
```angelscript
bool RemoveBone(FName InBoneName, bool bRemoveChildren)
```
Remove a bone in the skeleton hierarchy
@param InBoneName The new bone's name.
@param bRemoveChildren Remove children recursively.
@return \c true if the operation succeeded, false otherwise.

### RemoveBones
```angelscript
bool RemoveBones(TArray<FName> InBoneNames, bool bRemoveChildren)
```

### RenameBone
```angelscript
bool RenameBone(FName InOldBoneName, FName InNewBoneName)
```
Rename bones
@param InOldBoneName The current bone's name.
@param InNewBoneName The new bone's name.
@return \c true if the operation succeeded, false otherwise.

### RenameBones
```angelscript
bool RenameBones(TArray<FName> InOldBoneNames, TArray<FName> InNewBoneNames)
```

### SetBonesTransforms
```angelscript
bool SetBonesTransforms(TArray<FName> InBoneNames, TArray<FTransform> InNewTransforms, bool bMoveChildren)
```

### SetBoneTransform
```angelscript
bool SetBoneTransform(FName InBoneName, FTransform InNewTransform, bool bMoveChildren)
```
Sets the bone the desired local transform
@param InBoneName The new bone's name that needs to be moved.
@param InNewTransform The new local transform in the bone's parent space.
@param bMoveChildren Propagate new transform to children
@return \c true if the operation succeeded, false otherwise.

### SetSkeletalMesh
```angelscript
bool SetSkeletalMesh(USkeletalMesh InSkeletalMesh)
```

