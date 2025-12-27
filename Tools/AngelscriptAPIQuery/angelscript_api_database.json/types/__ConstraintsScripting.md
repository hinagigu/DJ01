# __ConstraintsScripting

## 方法

### AddConstraint
```angelscript
bool AddConstraint(UWorld InWorld, UTransformableHandle InParentHandle, UTransformableHandle InChildHandle, UTickableTransformConstraint InConstraint, bool bMaintainOffset)
```

### CreateFromType
```angelscript
UTickableTransformConstraint CreateFromType(UWorld InWorld, ETransformConstraintType InType)
```
Create Constraint based on the specified type.
@param InWorld World to create the constraint
@param InType The type of constraint
@return return The constraint object

### CreateTransformableComponentHandle
```angelscript
UTransformableComponentHandle CreateTransformableComponentHandle(UWorld InWorld, USceneComponent InSceneComponent, FName InSocketName)
```
Create the transformable handle that deals with getting and setting transforms on this scene component
@param InWorld, the world you are in
@param InSceneComponent World to create the constraint
@param InSocketName Optional name of the socket to get the transform
@return returns the handle for this scene component

### CreateTransformableHandle
```angelscript
UTransformableHandle CreateTransformableHandle(UWorld InWorld, UObject InObject, FName InAttachmentName)
```
Create the transformable handle that deals with getting and setting transforms on this object
@param InWorld, the world you are in
@param InObject World to create the constraint
@param InAttachmentName Optional name of the attachment to get the transform. Not that this can represent a scene component's socket name or a control rig control for example.
@return returns the handle for this scene component

### GetConstraintsArray
```angelscript
TArray<UTickableConstraint> GetConstraintsArray(UWorld InWorld)
```
Get a copy of the constraints in the current world
      @param InWorld World we are in
      @return Copy of the constraints in the level

### RemoveConstraint
```angelscript
bool RemoveConstraint(UWorld InWorld, int InIndex)
```
Remove constraint at specified index
@param InWorld World to remove the constraint
@param InIndex Index to remove from
@return return If constraint removed correctly

### RemoveThisConstraint
```angelscript
bool RemoveThisConstraint(UWorld InWorld, UTickableConstraint InTickableConstraint)
```
Remove specified constraint
@param InWorld World to remove the constraint
@param InTickableConstraint Constraint to remove
@return return If constraint removed correctly

