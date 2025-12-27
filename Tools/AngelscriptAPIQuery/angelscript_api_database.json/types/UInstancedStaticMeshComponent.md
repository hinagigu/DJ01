# UInstancedStaticMeshComponent

**继承自**: `UStaticMeshComponent`

A component that efficiently renders multiple instances of the same StaticMesh.

## 属性

### PerInstanceSMData
- **类型**: `TArray<FInstancedStaticMeshInstanceData>`
- **描述**: Array of instances, bulk serialized.

### PerInstanceSMCustomData
- **类型**: `TArray<float32>`
- **描述**: Array of custom data for instances. This will contains NumCustomDataFloats*InstanceCount entries. The entries are represented sequantially, in instance order. Can be read in a material and manipulated through Blueprints.
    Example: If NumCustomDataFloats is 1, then each entry will belong to an instance. Custom data 0 will belong to Instance 0. Custom data 1 will belong to Instance 1 etc.
    Example: If NumCustomDataFloats is 2, then each pair of sequential entries belong to an instance. Custom data 0 and 1 will belong to Instance 0. Custom data 2 and 3 will belong to Instance 2 etc.

### InstancingRandomSeed
- **类型**: `int`

### InstanceLODDistanceScale
- **类型**: `float32`

### InstanceStartCullDistance
- **类型**: `int`

### InstanceEndCullDistance
- **类型**: `int`

### bUseGpuLodSelection
- **类型**: `bool`

## 方法

### AddInstance
```angelscript
int AddInstance(FTransform InstanceTransform, bool bWorldSpace)
```
Add an instance to this component. Transform is given in local space of this component unless bWorldSpace is set.

### AddInstances
```angelscript
TArray<int> AddInstances(TArray<FTransform> InstanceTransforms, bool bShouldReturnIndices, bool bWorldSpace, bool bUpdateNavigation)
```
Add multiple instances to this component. Transform is given in local space of this component unless bWorldSpace is set.

### BatchUpdateInstancesTransform
```angelscript
bool BatchUpdateInstancesTransform(int StartInstanceIndex, int NumInstances, FTransform NewInstancesTransform, bool bWorldSpace, bool bMarkRenderStateDirty, bool bTeleport)
```
Update the transform for a number of instances.

@param StartInstanceIndex             The starting index of the instances to update
@param NumInstances                   The number of instances to update
@param NewInstancesTransform  The new transform
@param bWorldSpace                    If true, the new transform is interpreted as a World Space transform, otherwise it is interpreted as Local Space
@param bMarkRenderStateDirty  If true, the change should be visible immediately. If you are updating many instances you should only set this to true for the last instance.
@param bTeleport                              Whether or not the instances physics should be moved normally, or teleported (moved instantly, ignoring velocity).
@return                                               True on success.

### BatchUpdateInstancesTransforms
```angelscript
bool BatchUpdateInstancesTransforms(int StartInstanceIndex, TArray<FTransform> NewInstancesTransforms, bool bWorldSpace, bool bMarkRenderStateDirty, bool bTeleport)
```
Update the transform for an array of instances.

@param StartInstanceIndex             The starting index of the instances to update
@param NewInstancesTransforms The new transforms
@param bWorldSpace                    If true, the new transforms are interpreted as a World Space transform, otherwise it is interpreted as Local Space
@param bMarkRenderStateDirty  If true, the change should be visible immediately. If you are updating many instances you should only set this to true for the last instance.
@param bTeleport                              Whether or not the instances physics should be moved normally, or teleported (moved instantly, ignoring velocity).
@return                                               True on success.

### ClearInstances
```angelscript
void ClearInstances()
```
Clear all instances being rendered by this component.

### GetCullDistances
```angelscript
void GetCullDistances(int& OutStartCullDistance, int& OutEndCullDistance)
```
Gets the fading start and culling end distances for this component.

### GetInstanceCount
```angelscript
int GetInstanceCount()
```
Get the number of instances in this component.

### GetInstancesOverlappingBox
```angelscript
TArray<int> GetInstancesOverlappingBox(FBox Box, bool bBoxInWorldSpace)
```
Returns the instances with instance bounds overlapping the specified box. The return value is an array of instance indices.

### GetInstancesOverlappingSphere
```angelscript
TArray<int> GetInstancesOverlappingSphere(FVector Center, float32 Radius, bool bSphereInWorldSpace)
```
Returns the instances with instance bounds overlapping the specified sphere. The return value is an array of instance indices.

### GetInstanceTransform
```angelscript
bool GetInstanceTransform(int InstanceIndex, FTransform& OutInstanceTransform, bool bWorldSpace)
```
Get the transform for the instance specified. Instance is returned in local space of this component unless bWorldSpace is set.  Returns True on success.

### GetLODDistanceScale
```angelscript
float32 GetLODDistanceScale()
```
Gets the current LOD scale.

### IsValidInstance
```angelscript
bool IsValidInstance(int InstanceIndex)
```
Does the given index map to a valid instance in this component?

### RemoveInstance
```angelscript
bool RemoveInstance(int InstanceIndex)
```
Remove the instance specified. Returns True on success.

### RemoveInstances
```angelscript
bool RemoveInstances(TArray<int> InstancesToRemove)
```
Remove the instances specified. Returns True on success.

### SetCullDistances
```angelscript
void SetCullDistances(int StartCullDistance, int EndCullDistance)
```
Sets the fading start and culling end distances for this component.

### SetCustomDataValue
```angelscript
bool SetCustomDataValue(int InstanceIndex, int CustomDataIndex, float32 CustomDataValue, bool bMarkRenderStateDirty)
```
Update custom data for specific instance

### SetLODDistanceScale
```angelscript
void SetLODDistanceScale(float32 InLODDistanceScale)
```
Sets the LOD scale.

### SetNumCustomDataFloats
```angelscript
void SetNumCustomDataFloats(int InNumCustomDataFloats)
```
Update number of custom data entries per instance. This applies to all instances and will reallocate the full custom data buffer and reset all values to 0

### UpdateInstanceTransform
```angelscript
bool UpdateInstanceTransform(int InstanceIndex, FTransform NewInstanceTransform, bool bWorldSpace, bool bMarkRenderStateDirty, bool bTeleport)
```
Update the transform for the instance specified.

@param InstanceIndex                  The index of the instance to update
@param NewInstanceTransform   The new transform
@param bWorldSpace                    If true, the new transform is interpreted as a World Space transform, otherwise it is interpreted as Local Space
@param bMarkRenderStateDirty  If true, the change should be visible immediately. If you are updating many instances you should only set this to true for the last instance.
@param bTeleport                              Whether or not the instance's physics should be moved normally, or teleported (moved instantly, ignoring velocity).
@return                                               True on success.

