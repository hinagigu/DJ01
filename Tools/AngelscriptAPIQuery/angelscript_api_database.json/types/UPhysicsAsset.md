# UPhysicsAsset

**继承自**: `UObject`

PhysicsAsset contains a set of rigid bodies and constraints that make up a single ragdoll.
The asset is not limited to human ragdolls, and can be used for any physical simulation using bodies and constraints.
A SkeletalMesh has a single PhysicsAsset, which allows for easily turning ragdoll physics on or off for many SkeletalMeshComponents
The asset can be configured inside the Physics Asset Editor.

@see https://docs.unrealengine.com/InteractiveExperiences/Physics/PhysicsAssetEditor
@see USkeletalMesh

## 属性

### PhysicalAnimationProfiles
- **类型**: `TArray<FName>`

### ConstraintProfiles
- **类型**: `TArray<FName>`

### SolverSettings
- **类型**: `FPhysicsAssetSolverSettings`
- **描述**: Solver settings when the asset is used with a RigidBody Anim Node (RBAN).

### SolverType
- **类型**: `EPhysicsAssetSolverType`
- **描述**: Solver type used in physics asset editor. This can be used to make what you see in the asset editror more closely resembles what you
see in game (though there will be differences owing to framerate variation etc). If your asset will primarily be used as a ragdoll
select "World", but if it will be used in the AnimGraph select "RBAN".

### ThumbnailInfo
- **类型**: `UThumbnailInfo`
- **描述**: Information for thumbnail rendering

### bNotForDedicatedServer
- **类型**: `bool`

## 方法

### GetConstraintByBoneNames
```angelscript
FConstraintInstanceAccessor GetConstraintByBoneNames(FName Bone1Name, FName Bone2Name)
```
Gets a constraint by its joint name
@param Bone1Name name of the first bone in the joint
@param Bone2Name name of the second bone in the joint
@return ConstraintInstance accessor to the constraint data

### GetConstraintByName
```angelscript
FConstraintInstanceAccessor GetConstraintByName(FName ConstraintName)
```
Gets a constraint by its joint name
@param ConstraintName name of the constraint
@return ConstraintInstance accessor to the constraint data

### GetConstraints
```angelscript
void GetConstraints(bool bIncludesTerminated, TArray<FConstraintInstanceAccessor>& OutConstraints)
```
Gets all constraints
@param IncludesTerminated whether or not to return terminated constraints
@param OutConstraints returned list of constraints matching the parameters

