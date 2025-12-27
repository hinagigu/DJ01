# UPaperGroupedSpriteComponent

**继承自**: `UMeshComponent`

A component that handles rendering and collision for many instances of one or more UPaperSprite assets.

@see UPrimitiveComponent, UPaperSprite

## 属性

### PerInstanceSpriteData
- **类型**: `TArray<FSpriteInstanceData>`
- **描述**: Array of instances

## 方法

### AddInstance
```angelscript
int AddInstance(FTransform Transform, UPaperSprite Sprite, bool bWorldSpace, FLinearColor Color)
```
Add an instance to this component. Transform can be given either in the local space of this component or world space.

### ClearInstances
```angelscript
void ClearInstances()
```
Clear all instances being rendered by this component

### GetInstanceCount
```angelscript
int GetInstanceCount()
```
Get the number of instances in this component

### GetInstanceTransform
```angelscript
bool GetInstanceTransform(int InstanceIndex, FTransform& OutInstanceTransform, bool bWorldSpace)
```
Get the transform for the instance specified. Instance is returned in local space of this component unless bWorldSpace is set.  Returns True on success.

### RemoveInstance
```angelscript
bool RemoveInstance(int InstanceIndex)
```
Remove the instance specified. Returns True on success.

### SortInstancesAlongAxis
```angelscript
void SortInstancesAlongAxis(FVector WorldSpaceSortAxis)
```
Sort all instances by their world space position along the specified axis

### UpdateInstanceColor
```angelscript
bool UpdateInstanceColor(int InstanceIndex, FLinearColor NewInstanceColor, bool bMarkRenderStateDirty)
```
Update the color for the instance specified. Returns True on success.

### UpdateInstanceTransform
```angelscript
bool UpdateInstanceTransform(int InstanceIndex, FTransform NewInstanceTransform, bool bWorldSpace, bool bMarkRenderStateDirty, bool bTeleport)
```
Update the transform for the instance specified. Instance is given in local space of this component unless bWorldSpace is set.  Returns True on success.

