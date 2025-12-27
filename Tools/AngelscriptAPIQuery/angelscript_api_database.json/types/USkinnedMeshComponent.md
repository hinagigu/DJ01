# USkinnedMeshComponent

**继承自**: `UMeshComponent`

Skinned mesh component that supports bone skinned mesh rendering.
This class does not support animation.

@see USkeletalMeshComponent

## 属性

### SkinCacheUsage
- **类型**: `TArray<ESkinCacheUsage>`

### bSetMeshDeformer
- **类型**: `bool`

### MeshDeformerInstanceSettings
- **类型**: `UMeshDeformerInstanceSettings`

### PhysicsAssetOverride
- **类型**: `UPhysicsAsset`

### ForcedLodModel
- **类型**: `int`

### MinLodModel
- **类型**: `int`

### StreamingDistanceMultiplier
- **类型**: `float32`

### VisibilityBasedAnimTickOption
- **类型**: `EVisibilityBasedAnimTickOption`

### LeaderPoseComponent
- **类型**: `TWeakObjectPtr<USkinnedMeshComponent>`

### MeshDeformer
- **类型**: `UMeshDeformer`

### bOverrideMinLod
- **类型**: `bool`

### bUseBoundsFromLeaderPoseComponent
- **类型**: `bool`

### bDisableMorphTarget
- **类型**: `bool`

### bPerBoneMotionBlur
- **类型**: `bool`

### bComponentUseFixedSkelBounds
- **类型**: `bool`

### bConsiderAllBodiesForBounds
- **类型**: `bool`

### bSyncAttachParentLOD
- **类型**: `bool`

### bCastCapsuleDirectShadow
- **类型**: `bool`

### bCastCapsuleIndirectShadow
- **类型**: `bool`

### bEnableUpdateRateOptimizations
- **类型**: `bool`

### bDisplayDebugUpdateRateOptimizations
- **类型**: `bool`

### bRenderStatic
- **类型**: `bool`

### bIgnoreLeaderPoseComponentLOD
- **类型**: `bool`

### CapsuleIndirectShadowMinVisibility
- **类型**: `float32`

## 方法

### BoneIsChildOf
```angelscript
bool BoneIsChildOf(FName BoneName, FName ParentBoneName)
```
Tests if BoneName is child of (or equal to) ParentBoneName.

@param BoneName Name of the bone
@param ParentBone Name to check

@return true if child (strictly, not same). false otherwise
Note - will return false if ChildBoneIndex is the same as ParentBoneIndex ie. must be strictly a child.

### ClearSkinWeightOverride
```angelscript
void ClearSkinWeightOverride(int LODIndex)
```
Clear any applied skin weight override

### ClearSkinWeightProfile
```angelscript
void ClearSkinWeightProfile()
```
Clear the Skin Weight Profile from this component, in case it is set

### ClearVertexColorOverride
```angelscript
void ClearVertexColorOverride(int LODIndex)
```
Clear any applied vertex color override

### FindClosestBone_K2
```angelscript
FName FindClosestBone_K2(FVector TestLocation, FVector& BoneLocation, float32 IgnoreScale, bool bRequirePhysicsAsset)
```
finds the closest bone to the given location

@param TestLocation the location to test against
@param BoneLocation (optional, out) if specified, set to the world space location of the bone that was found, or (0,0,0) if no bone was found
@param IgnoreScale (optional) if specified, only bones with scaling larger than the specified factor are considered
@param bRequirePhysicsAsset (optional) if true, only bones with physics will be considered

@return the name of the bone that was found, or 'None' if no bone was found

### GetBoneIndex
```angelscript
int GetBoneIndex(FName BoneName)
```
Find the index of bone by name. Looks in the current SkeletalMesh being used by this SkeletalMeshComponent.

@param BoneName Name of bone to look up

@return Index of the named bone in the current SkeletalMesh. Will return INDEX_NONE if bone not found.

@see USkeletalMesh::GetBoneIndex.

### GetBoneName
```angelscript
FName GetBoneName(int BoneIndex)
```
Get Bone Name from index
@param BoneIndex Index of the bone

@return the name of the bone at the specified index

### GetBoneTransform
```angelscript
FTransform GetBoneTransform(FName InBoneName, ERelativeTransformSpace TransformSpace)
```
Get world-space bone transform.
@param InBoneName Name of the the bone to get the transform
@return Bone transform in world space if bone is found. Otherwise it will return component's transform in world space.

### GetCurrentSkinWeightProfileName
```angelscript
FName GetCurrentSkinWeightProfileName()
```
Return the name of the Skin Weight Profile that is currently set otherwise returns 'None'

### GetDeltaTransformFromRefPose
```angelscript
FTransform GetDeltaTransformFromRefPose(FName BoneName, FName BaseName)
```
Get delta transform from reference pose based on BaseNode.
This uses last frame up-to-date transform, so it will have a frame delay if you use this info in the AnimGraph

@param BoneName Name of the bone
@param BaseName Name of the base bone - if none, it will use parent as a base

@return the delta transform from refpose in that given space (BaseName)

### GetForcedLOD
```angelscript
int GetForcedLOD()
```
Get ForcedLodModel of the mesh component. Note that the actual forced LOD level is the return value minus one and zero means no forced LOD

### GetMeshDeformerInstance
```angelscript
UMeshDeformerInstance GetMeshDeformerInstance()
```

### GetNumBones
```angelscript
int GetNumBones()
```
Returns the number of bones in the skeleton.

### GetNumLODs
```angelscript
int GetNumLODs()
```
Get the number of LODs on this component

### GetParentBone
```angelscript
FName GetParentBone(FName BoneName)
```
Get Parent Bone of the input bone

@param BoneName Name of the bone

@return the name of the parent bone for the specified bone. Returns 'None' if the bone does not exist or it is the root bone

### GetPredictedLODLevel
```angelscript
int GetPredictedLODLevel()
```
Get predicted LOD level. This value is usually calculated in UpdateLODStatus, but can be modified by skeletal mesh streaming.

### GetRefPosePosition
```angelscript
FVector GetRefPosePosition(int BoneIndex)
```
Gets the local-space position of a bone in the reference pose.

@param BoneIndex Index of the bone

@return Local space reference position

### GetRefPoseTransform
```angelscript
FTransform GetRefPoseTransform(int BoneIndex)
```
Gets the local-space transform of a bone in the reference pose.

@param BoneIndex Index of the bone

@return Local space reference transform

### GetSkinnedAsset
```angelscript
USkinnedAsset GetSkinnedAsset()
```
Get the SkinnedAsset rendered for this mesh.

@return the SkinnedAsset set to this mesh.

### GetSocketBoneName
```angelscript
FName GetSocketBoneName(FName InSocketName)
```
Returns bone name linked to a given named socket on the skeletal mesh component.
If you're unsure to deal with sockets or bones names, you can use this function to filter through, and always return the bone name.

@param       bone name or socket name

@return      bone name

### GetTwistAndSwingAngleOfDeltaRotationFromRefPose
```angelscript
bool GetTwistAndSwingAngleOfDeltaRotationFromRefPose(FName BoneName, float32& OutTwistAngle, float32& OutSwingAngle)
```
Get Twist and Swing Angle in Degree of Delta Rotation from Reference Pose in Local space

First this function gets rotation of current, and rotation of ref pose in local space, and
And gets twist/swing angle value from refpose aligned.

@param BoneName Name of the bone
@param OutTwistAngle TwistAngle in degree
@param OutSwingAngle SwingAngle in degree

@return true if succeed. False otherwise. Often due to incorrect bone name.

### GetVertexOffsetUsage
```angelscript
int GetVertexOffsetUsage(int LODIndex)
```

### HideBoneByName
```angelscript
void HideBoneByName(FName BoneName, EPhysBodyOp PhysBodyOption)
```
Hides the specified bone with name.  Currently this just enforces a scale of 0 for the hidden bones.
Compared to HideBone By Index - This keeps track of list of bones and update when LOD changes

@param  BoneName            Name of bone to hide
@param  PhysBodyOption          Option for physics bodies that attach to the bones to be hidden

### IsBoneHiddenByName
```angelscript
bool IsBoneHiddenByName(FName BoneName)
```
Determines if the specified bone is hidden.

@param  BoneName            Name of bone to check

@return true if hidden

### IsMaterialSectionShown
```angelscript
bool IsMaterialSectionShown(int MaterialID, int LODIndex)
```
Returns whether a specific material section is currently hidden on this component (by using ShowMaterialSection)

### IsUsingSkinWeightProfile
```angelscript
bool IsUsingSkinWeightProfile()
```
Check whether or not a Skin Weight Profile is currently set

### OverrideMinLOD
```angelscript
void OverrideMinLOD(int InNewMinLOD)
```
Override the Min LOD of the mesh component

@param       InNewMinLOD     Override new MinLodModel that make sure the LOD does not go below of this value. Range from [0, Max Number of LOD - 1]. This will affect in the next tick update.

### SetCapsuleIndirectShadowMinVisibility
```angelscript
void SetCapsuleIndirectShadowMinVisibility(float32 NewValue)
```

### SetCastCapsuleDirectShadow
```angelscript
void SetCastCapsuleDirectShadow(bool bNewValue)
```

### SetCastCapsuleIndirectShadow
```angelscript
void SetCastCapsuleIndirectShadow(bool bNewValue)
```

### SetForcedLOD
```angelscript
void SetForcedLOD(int InNewForcedLOD)
```
Set ForcedLodModel of the mesh component

@param       InNewForcedLOD  Set new ForcedLODModel that forces to set the incoming LOD. Range from [1, Max Number of LOD]. This will affect in the next tick update.

### SetLeaderPoseComponent
```angelscript
void SetLeaderPoseComponent(USkinnedMeshComponent NewLeaderBoneComponent, bool bForceUpdate, bool bInFollowerShouldTickPose)
```
Set LeaderPoseComponent for this component

@param NewLeaderBoneComponent New LeaderPoseComponent
@param bForceUpdate If false, the function will be skipped if NewLeaderBoneComponent is the same as currently setup (default)
@param bInFollowerShouldTickPose If false, Follower components will not execute TickPose (default)

### SetMeshDeformer
```angelscript
void SetMeshDeformer(UMeshDeformer InMeshDeformer)
```
Change the MeshDeformer that is used for this Component.

@param InMeshDeformer New mesh deformer to set for this component

### SetPhysicsAsset
```angelscript
void SetPhysicsAsset(UPhysicsAsset NewPhysicsAsset, bool bForceReInit)
```
Override the Physics Asset of the mesh. It uses SkeletalMesh.PhysicsAsset, but if you'd like to override use this function

@param       NewPhysicsAsset New PhysicsAsset
@param       bForceReInit    Force reinitialize

### SetPostSkinningOffsets
```angelscript
void SetPostSkinningOffsets(int LODIndex, TArray<FVector> Offsets)
```

### SetPreSkinningOffsets
```angelscript
void SetPreSkinningOffsets(int LODIndex, TArray<FVector> Offsets)
```

### SetRenderStatic
```angelscript
void SetRenderStatic(bool bNewValue)
```
Set whether this skinned mesh should be rendered as static mesh in a reference pose

@param       whether this skinned mesh should be rendered as static

### SetSkinnedAssetAndUpdate
```angelscript
void SetSkinnedAssetAndUpdate(USkinnedAsset NewMesh, bool bReinitPose)
```
Change the SkinnedAsset that is rendered for this Component. Will re-initialize the animation tree etc.

@param NewMesh New mesh to set for this component
@param bReinitPose Whether we should keep current pose or reinitialize.

### SetSkinWeightOverride
```angelscript
void SetSkinWeightOverride(int LODIndex, TArray<FSkelMeshSkinWeightInfo> SkinWeights)
```
Allow override of skin weights on a per-component basis.

### SetSkinWeightProfile
```angelscript
bool SetSkinWeightProfile(FName InProfileName)
```
Setup an override Skin Weight Profile for this component

### SetVertexColorOverride_LinearColor
```angelscript
void SetVertexColorOverride_LinearColor(int LODIndex, TArray<FLinearColor> VertexColors)
```
Allow override of vertex colors on a per-component basis, taking array of Blueprint-friendly LinearColors.

### SetVertexOffsetUsage
```angelscript
void SetVertexOffsetUsage(int LODIndex, int Usage)
```

### ShowAllMaterialSections
```angelscript
void ShowAllMaterialSections(int LODIndex)
```
Clear any material visibility modifications made by ShowMaterialSection

### ShowMaterialSection
```angelscript
void ShowMaterialSection(int MaterialID, int SectionIndex, bool bShow, int LODIndex)
```
Allows hiding of a particular material (by ID) on this instance of a SkeletalMesh.

@param MaterialID - Index of the material show/hide
@param bShow - True to show the material, false to hide it
@param LODIndex - Index of the LOD to modify material visibility within

### TransformFromBoneSpace
```angelscript
void TransformFromBoneSpace(FName BoneName, FVector InPosition, FRotator InRotation, FVector& OutPosition, FRotator& OutRotation)
```
Transform a location/rotation in bone relative space to world space.

@param BoneName Name of bone
@param InPosition Input position
@param InRotation Input rotation
@param OutPosition (out) Transformed position
@param OutRotation (out) Transformed rotation

### TransformToBoneSpace
```angelscript
void TransformToBoneSpace(FName BoneName, FVector InPosition, FRotator InRotation, FVector& OutPosition, FRotator& OutRotation)
```
Transform a location/rotation from world space to bone relative space.
This is handy if you know the location in world space for a bone attachment, as AttachComponent takes location/rotation in bone-relative space.

@param BoneName Name of bone
@param InPosition Input position
@param InRotation Input rotation
@param OutPosition (out) Transformed position
@param OutRotation (out) Transformed rotation

### UnHideBoneByName
```angelscript
void UnHideBoneByName(FName BoneName)
```
UnHide the specified bone with name.  Currently this just enforces a scale of 0 for the hidden bones.
Compared to HideBone By Index - This keeps track of list of bones and update when LOD changes
@param  BoneName            Name of bone to unhide

### UnloadSkinWeightProfile
```angelscript
void UnloadSkinWeightProfile(FName InProfileName)
```
Unload a Skin Weight Profile's skin weight buffer (if created)

### UnsetMeshDeformer
```angelscript
void UnsetMeshDeformer()
```
Unset any MeshDeformer applied to this Component.

@param InMeshDeformer New mesh deformer to set for this component

