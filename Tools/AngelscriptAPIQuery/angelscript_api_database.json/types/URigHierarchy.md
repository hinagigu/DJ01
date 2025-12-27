# URigHierarchy

**继承自**: `UObject`

## 属性

### ModifiedEvent
- **类型**: `FRigHierarchyModifiedDynamicEvent`

## 方法

### Contains
```angelscript
bool Contains(FRigElementKey InKey)
```
Returns true if the provided element key is valid
@param InKey The key to validate
@return Returns true if the provided element key is valid

### CopyHierarchy
```angelscript
void CopyHierarchy(URigHierarchy InHierarchy)
```
Copies the contents of a hierarchy onto this one

### CopyPose
```angelscript
void CopyPose(URigHierarchy InHierarchy, bool bCurrent, bool bInitial, bool bWeights, bool bMatchPoseInGlobalIfNeeded)
```
Copies the contents of a hierarchy onto this one

### FindBone
```angelscript
FRigBoneElement FindBone(FRigElementKey InKey)
```
Returns bone element for a given key, for scripting purpose only, for cpp usage, use Find<FRigBoneElement>()
@param InKey The key of the bone element to retrieve.

### FindControl
```angelscript
FRigControlElement FindControl(FRigElementKey InKey)
```
Returns control element for a given key, for scripting purpose only, for cpp usage, use Find<FRigControlElement>()
@param InKey The key of the control element to retrieve.

### FindNull
```angelscript
FRigNullElement FindNull(FRigElementKey InKey)
```
Returns null element for a given key, for scripting purpose only, for cpp usage, use Find<FRigControlElement>()
@param InKey The key of the null element to retrieve.

### GetAllKeys
```angelscript
TArray<FRigElementKey> GetAllKeys(bool bTraverse)
```
Returns all element keys of this hierarchy
@param bTraverse If set to true the keys will be returned by depth first traversal
@return The keys of all elements

### GetBones
```angelscript
TArray<FRigElementKey> GetBones(bool bTraverse)
```
Returns all Bone elements
@param bTraverse Returns the elements in order of a depth first traversal

### GetBoolArrayMetadata
```angelscript
TArray<bool> GetBoolArrayMetadata(FRigElementKey InItem, FName InMetadataName)
```
Queries and returns the value of bool array metadata
@param InItem The element key to return the metadata for
@param InMetadataName The name of the metadata to query

### GetBoolMetadata
```angelscript
bool GetBoolMetadata(FRigElementKey InItem, FName InMetadataName, bool DefaultValue)
```
Queries and returns the value of bool metadata
@param InItem The element key to return the metadata for
@param InMetadataName The name of the metadata to query
@param DefaultValue The default value to fall back on

### GetChildren
```angelscript
TArray<FRigElementKey> GetChildren(FRigElementKey InKey, bool bRecursive)
```
Returns the child elements of a given element key
@param InKey The key of the element to retrieve the children for
@param bRecursive If set to true grand-children will also be returned etc
@return Returns the child elements

### GetConnectors
```angelscript
TArray<FRigElementKey> GetConnectors(bool bTraverse)
```
Returns all Connector elements
@param bTraverse Returns the elements in order of a depth first traversal

### GetConnectorStates
```angelscript
TArray<FRigConnectorState> GetConnectorStates()
```
Returns all of the connectors' state

### GetControls
```angelscript
TArray<FRigElementKey> GetControls(bool bTraverse)
```
Returns all Control elements
@param bTraverse Returns the elements in order of a depth first traversal

### GetController
```angelscript
URigHierarchyController GetController(bool bCreateIfNeeded)
```
Returns a controller for this hierarchy.
Note: If the controller is not available this will return nullptr
even if the bCreateIfNeeded flag is set to true. You can check the
controller's availability with IsControllerAvailable().
@param bCreateIfNeeded Creates a controller if needed
@return The Controller for this hierarchy

### GetControlPreferredEulerAngles
```angelscript
FVector GetControlPreferredEulerAngles(FRigElementKey InKey, EEulerRotationOrder InRotationOrder, bool bInitial)
```
Returns a control's preferred euler angles (local transform rotation)
@param InKey The key of the element to retrieve the current value for
@param InRotationOrder The rotation order to use when retrieving the euler angles
@param bInitial If true we'll return the preferred euler angles for the initial - otherwise current transform
@return Returns the current preferred euler angles

### GetControlPreferredEulerAnglesByIndex
```angelscript
FVector GetControlPreferredEulerAnglesByIndex(int InElementIndex, EEulerRotationOrder InRotationOrder, bool bInitial)
```
Returns a control's preferred euler angles (local transform rotation)
@param InElementIndex The element index to look up
@param InRotationOrder The rotation order to use when retrieving the euler angles
@param bInitial If true we'll return the preferred euler angles for the initial - otherwise current transform
@return Returns the current preferred euler angles

### GetControlPreferredEulerRotationOrder
```angelscript
EEulerRotationOrder GetControlPreferredEulerRotationOrder(FRigElementKey InKey, bool bFromSettings)
```
Returns a control's preferred euler rotation order
@param InKey The key of the element to retrieve the current value for
@param bFromSettings If true the rotation order will be looked up from the control's settings, otherwise from the currently set animation value
@return Returns the current preferred euler rotation order

### GetControlPreferredEulerRotationOrderByIndex
```angelscript
EEulerRotationOrder GetControlPreferredEulerRotationOrderByIndex(int InElementIndex, bool bFromSettings)
```
Returns a control's preferred euler rotation order
@param InElementIndex The element index to look up
@param bFromSettings If true the rotation order will be looked up from the control's settings, otherwise from the currently set animation value
@return Returns the current preferred euler rotation order

### GetControlPreferredRotator
```angelscript
FRotator GetControlPreferredRotator(FRigElementKey InKey, bool bInitial)
```
Returns a control's preferred rotator (local transform rotation)
@param InKey The key of the element to retrieve the current value for
@param bInitial If true we'll return the preferred rotator for the initial - otherwise current transform
@return Returns the current preferred rotator

### GetControlPreferredRotatorByIndex
```angelscript
FRotator GetControlPreferredRotatorByIndex(int InElementIndex, bool bInitial)
```
Returns a control's preferred rotator (local transform rotation)
@param InElementIndex The element index to look up
@param bInitial If true we'll return the preferred rotator for the initial - otherwise current transform
@return Returns the current preferred rotator

### GetControlValue
```angelscript
FRigControlValue GetControlValue(FRigElementKey InKey, ERigControlValueType InValueType)
```
Returns a control's current value given its key
@param InKey The key of the element to retrieve the current value for
@param InValueType The type of value to return
@return Returns the current value of the control

### GetControlValueByIndex
```angelscript
FRigControlValue GetControlValueByIndex(int InElementIndex, ERigControlValueType InValueType)
```
Returns a control's current value given its index
@param InElementIndex The index of the element to retrieve the current value for
@param InValueType The type of value to return
@return Returns the current value of the control

### GetCurves
```angelscript
TArray<FRigElementKey> GetCurves()
```
Returns all Curve elements

### GetCurveValue
```angelscript
float32 GetCurveValue(FRigElementKey InKey)
```
Returns a curve's value given its key
@param InKey The key of the element to retrieve the value for
@return Returns the value of the curve

### GetCurveValueByIndex
```angelscript
float32 GetCurveValueByIndex(int InElementIndex)
```
Returns a curve's value given its index
@param InElementIndex The index of the element to retrieve the value for
@return Returns the value of the curve

### GetDefaultParent
```angelscript
FRigElementKey GetDefaultParent(FRigElementKey InKey)
```
Returns the default parent element's key of a given child key
@param InKey The key of the element to retrieve the parent for
@return Returns the default parent element key

### GetFirstParent
```angelscript
FRigElementKey GetFirstParent(FRigElementKey InKey)
```
Returns the first parent element of a given element key
@param InKey The key of the element to retrieve the parents for
@return Returns the first parent element

### GetFloatArrayMetadata
```angelscript
TArray<float32> GetFloatArrayMetadata(FRigElementKey InItem, FName InMetadataName)
```
Queries and returns the value of float array metadata
@param InItem The element key to return the metadata for
@param InMetadataName The name of the metadata to query

### GetFloatMetadata
```angelscript
float32 GetFloatMetadata(FRigElementKey InItem, FName InMetadataName, float32 DefaultValue)
```
Queries and returns the value of float metadata
@param InItem The element key to return the metadata for
@param InMetadataName The name of the metadata to query
@param DefaultValue The default value to fall back on

### GetGlobalControlOffsetTransform
```angelscript
FTransform GetGlobalControlOffsetTransform(FRigElementKey InKey, bool bInitial)
```
Returns the global offset transform for a given control element.
@param InKey The key of the control to retrieve the transform for
@param bInitial If true the initial transform will be used
@return The global offset transform

### GetGlobalControlOffsetTransformByIndex
```angelscript
FTransform GetGlobalControlOffsetTransformByIndex(int InElementIndex, bool bInitial)
```
Returns the global offset transform for a given control element.
@param InElementIndex The index of the control to retrieve the transform for
@param bInitial If true the initial transform will be used
@return The global offset transform

### GetGlobalControlShapeTransform
```angelscript
FTransform GetGlobalControlShapeTransform(FRigElementKey InKey, bool bInitial)
```
Returns the global shape transform for a given control element.
@param InKey The key of the control to retrieve the transform for
@param bInitial If true the initial transform will be used
@return The global shape transform

### GetGlobalControlShapeTransformByIndex
```angelscript
FTransform GetGlobalControlShapeTransformByIndex(int InElementIndex, bool bInitial)
```
Returns the global shape transform for a given control element.
@param InElementIndex The index of the control to retrieve the transform for
@param bInitial If true the initial transform will be used
@return The global shape transform

### GetGlobalTransform
```angelscript
FTransform GetGlobalTransform(FRigElementKey InKey, bool bInitial)
```
Returns the global current or initial value for a given key.
If the key is invalid FTransform::Identity will be returned.
@param InKey The key to retrieve the transform for
@param bInitial If true the initial transform will be used
@return The global current or initial transform's value.

### GetGlobalTransformByIndex
```angelscript
FTransform GetGlobalTransformByIndex(int InElementIndex, bool bInitial)
```
Returns the global current or initial value for a element index.
If the index is invalid FTransform::Identity will be returned.
@param InElementIndex The index to retrieve the transform for
@param bInitial If true the initial transform will be used
@return The global current or initial transform's value.

### GetIndex
```angelscript
int GetIndex(FRigElementKey InKey)
```
Returns the index of an element given its key
@param InKey The key of the element to retrieve the index for
@return The index of the element or INDEX_NONE

### GetInt32ArrayMetadata
```angelscript
TArray<int> GetInt32ArrayMetadata(FRigElementKey InItem, FName InMetadataName)
```
Queries and returns the value of int32 array metadata
@param InItem The element key to return the metadata for
@param InMetadataName The name of the metadata to query

### GetInt32Metadata
```angelscript
int GetInt32Metadata(FRigElementKey InItem, FName InMetadataName, int DefaultValue)
```
Queries and returns the value of int32 metadata
@param InItem The element key to return the metadata for
@param InMetadataName The name of the metadata to query
@param DefaultValue The default value to fall back on

### GetKey
```angelscript
FRigElementKey GetKey(int InElementIndex)
```
Returns the key of an element given its index
@param InElementIndex The index of the element to retrieve the key for
@return The key of an element given its index

### GetKeys
```angelscript
TArray<FRigElementKey> GetKeys(TArray<int> InElementIndices)
```
Returns the keys of an array of indices
@param InElementIndices The indices to retrieve the keys for
@return The keys of the elements given the indices

### GetLinearColorArrayMetadata
```angelscript
TArray<FLinearColor> GetLinearColorArrayMetadata(FRigElementKey InItem, FName InMetadataName)
```
Queries and returns the value of FLinearColor array metadata
@param InItem The element key to return the metadata for
@param InMetadataName The name of the metadata to query

### GetLinearColorMetadata
```angelscript
FLinearColor GetLinearColorMetadata(FRigElementKey InItem, FName InMetadataName, FLinearColor DefaultValue)
```
Queries and returns the value of FLinearColor metadata
@param InItem The element key to return the metadata for
@param InMetadataName The name of the metadata to query
@param DefaultValue The default value to fall back on

### GetLocalControlShapeTransform
```angelscript
FTransform GetLocalControlShapeTransform(FRigElementKey InKey, bool bInitial)
```
Returns the local shape transform for a given control element.
@param InKey The key of the control to retrieve the transform for
@param bInitial If true the initial transform will be used
@return The local shape transform

### GetLocalControlShapeTransformByIndex
```angelscript
FTransform GetLocalControlShapeTransformByIndex(int InElementIndex, bool bInitial)
```
Returns the local shape transform for a given control element.
@param InElementIndex The index of the control to retrieve the transform for
@param bInitial If true the initial transform will be used
@return The local shape transform

### GetLocalIndex
```angelscript
int GetLocalIndex(FRigElementKey InKey)
```
Returns the index of an element given its key within its default parent (or root)
@param InKey The key of the element to retrieve the index for
@return The index of the element or INDEX_NONE

### GetLocalTransform
```angelscript
FTransform GetLocalTransform(FRigElementKey InKey, bool bInitial)
```
Returns the local current or initial value for a given key.
If the key is invalid FTransform::Identity will be returned.
@param InKey The key to retrieve the transform for
@param bInitial If true the initial transform will be used
@return The local current or initial transform's value.

### GetLocalTransformByIndex
```angelscript
FTransform GetLocalTransformByIndex(int InElementIndex, bool bInitial)
```
Returns the local current or initial value for a element index.
If the index is invalid FTransform::Identity will be returned.
@param InElementIndex The index to retrieve the transform for
@param bInitial If true the initial transform will be used
@return The local current or initial transform's value.

### GetMetadataNames
```angelscript
TArray<FName> GetMetadataNames(FRigElementKey InItem)
```
Returns the name of metadata for a given element
@param InItem The element key to return the metadata keys for

### GetMetadataType
```angelscript
ERigMetadataType GetMetadataType(FRigElementKey InItem, FName InMetadataName)
```
Returns the type of metadata given its name the item it is stored under
@param InItem The element key to return the metadata type for
@param InMetadataName The name of the metadata to return the type for

### GetModulePath
```angelscript
FString GetModulePath(FRigElementKey InItem)
```
Returns the path of the module an element belong to (or an empty string in case the element doesn't belong to a module)
@return The path the element belongs to (or empty string)

### GetModulePathFName
```angelscript
FName GetModulePathFName(FRigElementKey InItem)
```
Returns the path of the module an element belong to (or NAME_None in case the element doesn't belong to a module)
@return The path the element belongs to (or NAME_None)

### GetNameArrayMetadata
```angelscript
TArray<FName> GetNameArrayMetadata(FRigElementKey InItem, FName InMetadataName)
```
Queries and returns the value of FName array metadata
@param InItem The element key to return the metadata for
@param InMetadataName The name of the metadata to query

### GetNameMetadata
```angelscript
FName GetNameMetadata(FRigElementKey InItem, FName InMetadataName, FName DefaultValue)
```
Queries and returns the value of FName metadata
@param InItem The element key to return the metadata for
@param InMetadataName The name of the metadata to query
@param DefaultValue The default value to fall back on

### GetNameSpace
```angelscript
FString GetNameSpace(FRigElementKey InItem)
```
Returns the namespace of an element belong to (or an empty string in case the element doesn't belong to a module / namespace)
@return The namespace the element belongs to (or empty string)

### GetNameSpaceFName
```angelscript
FName GetNameSpaceFName(FRigElementKey InItem)
```
Returns the namespace of an element belong to (or NAME_None in case the element doesn't belong to a module / namespace)
@return The namespace the element belongs to (or NAME_None)

### GetNulls
```angelscript
TArray<FRigElementKey> GetNulls(bool bTraverse)
```
Returns all Null elements
@param bTraverse Returns the elements in order of a depth first traversal

### GetNumberOfParents
```angelscript
int GetNumberOfParents(FRigElementKey InKey)
```
Returns the number of parents of an element
@param InKey The key of the element to retrieve the number of parents for
@return Returns the number of parents of an element

### GetParents
```angelscript
TArray<FRigElementKey> GetParents(FRigElementKey InKey, bool bRecursive)
```
Returns the parent elements of a given element key
@param InKey The key of the element to retrieve the parents for
@param bRecursive If set to true parents of parents will also be returned
@return Returns the parent elements

### GetParentTransform
```angelscript
FTransform GetParentTransform(FRigElementKey InKey, bool bInitial)
```
Returns the global current or initial value for a given key.
If the element does not have a parent FTransform::Identity will be returned.
@param InKey The key of the element to retrieve the transform for
@param bInitial If true the initial transform will be used
@return The element's parent's global current or initial transform's value.

### GetParentTransformByIndex
```angelscript
FTransform GetParentTransformByIndex(int InElementIndex, bool bInitial)
```
Returns the global current or initial value for a given element index.
If the element does not have a parent FTransform::Identity will be returned.
@param InElementIndex The index of the element to retrieve the transform for
@param bInitial If true the initial transform will be used
@return The element's parent's global current or initial transform's value.

### GetParentWeight
```angelscript
FRigElementWeight GetParentWeight(FRigElementKey InChild, FRigElementKey InParent, bool bInitial)
```
Returns the weight of a parent below a multi parent element
@param InChild The key of the multi parented element
@param InParent The key of the parent to look up the weight for
@param bInitial If true the initial weights will be used
@return Returns the weight of a parent below a multi parent element, or FLT_MAX if the parent is invalid

### GetParentWeightArray
```angelscript
TArray<FRigElementWeight> GetParentWeightArray(FRigElementKey InChild, bool bInitial)
```
Returns the weights of all parents below a multi parent element
@param InChild The key of the multi parented element
@param bInitial If true the initial weights will be used
@return Returns the weight of a parent below a multi parent element, or FLT_MAX if the parent is invalid

### GetPose
```angelscript
FRigPose GetPose(bool bInitial, bool bIncludeTransientControls)
```
Returns the current / initial pose of the hierarchy
@param bInitial If set to true the initial pose will be returned
@return The pose of the hierarchy
@param bIncludeTransientControls If true the transient controls will be included in the pose

### GetPreviousName
```angelscript
FName GetPreviousName(FRigElementKey InKey)
```
Returns the previous name of an element prior to a rename operation
@param InKey The key of the element to request the old name for

### GetPreviousParent
```angelscript
FRigElementKey GetPreviousParent(FRigElementKey InKey)
```
Returns the previous parent of an element prior to a reparent operation
@param InKey The key of the element to request the old parent  for

### GetQuatArrayMetadata
```angelscript
TArray<FQuat> GetQuatArrayMetadata(FRigElementKey InItem, FName InMetadataName)
```
Queries and returns the value of FQuat array metadata
@param InItem The element key to return the metadata for
@param InMetadataName The name of the metadata to query

### GetQuatMetadata
```angelscript
FQuat GetQuatMetadata(FRigElementKey InItem, FName InMetadataName, FQuat DefaultValue)
```
Queries and returns the value of FQuat metadata
@param InItem The element key to return the metadata for
@param InMetadataName The name of the metadata to query
@param DefaultValue The default value to fall back on

### GetReferences
```angelscript
TArray<FRigElementKey> GetReferences(bool bTraverse)
```
Returns all references
@param bTraverse Returns the elements in order of a depth first traversal

### GetRigElementKeyArrayMetadata
```angelscript
TArray<FRigElementKey> GetRigElementKeyArrayMetadata(FRigElementKey InItem, FName InMetadataName)
```
Queries and returns the value of FRigElementKey array metadata
@param InItem The element key to return the metadata for
@param InMetadataName The name of the metadata to query

### GetRigElementKeyMetadata
```angelscript
FRigElementKey GetRigElementKeyMetadata(FRigElementKey InItem, FName InMetadataName, FRigElementKey DefaultValue)
```
Queries and returns the value of FRigElementKey metadata
@param InItem The element key to return the metadata for
@param InMetadataName The name of the metadata to query
@param DefaultValue The default value to fall back on

### GetRigidBodies
```angelscript
TArray<FRigElementKey> GetRigidBodies(bool bTraverse)
```
Returns all RigidBody elements
@param bTraverse Returns the elements in order of a depth first traversal

### GetRootElements
```angelscript
TArray<FRigElementKey> GetRootElements()
```
Returns all root element keys

### GetRotatorArrayMetadata
```angelscript
TArray<FRotator> GetRotatorArrayMetadata(FRigElementKey InItem, FName InMetadataName)
```
Queries and returns the value of FRotator array metadata
@param InItem The element key to return the metadata for
@param InMetadataName The name of the metadata to query

### GetRotatorMetadata
```angelscript
FRotator GetRotatorMetadata(FRigElementKey InItem, FName InMetadataName, FRotator DefaultValue)
```
Queries and returns the value of FRotator metadata
@param InItem The element key to return the metadata for
@param InMetadataName The name of the metadata to query
@param DefaultValue The default value to fall back on

### GetRuleManager
```angelscript
UModularRigRuleManager GetRuleManager(bool bCreateIfNeeded)
```
Returns a rule manager for this hierarchy
Note: If the manager is not available this will return nullptr
even if the bCreateIfNeeded flag is set to true.
@param bCreateIfNeeded Creates a controller if needed
@return The Controller for this hierarchy

### GetSelectedKeys
```angelscript
TArray<FRigElementKey> GetSelectedKeys(ERigElementType InTypeFilter)
```
Returns the keys of selected elements
@InTypeFilter The types to retrieve the selection for
@return An array of the currently selected elements

### GetSockets
```angelscript
TArray<FRigElementKey> GetSockets(bool bTraverse)
```
Returns all Socket elements
@param bTraverse Returns the elements in order of a depth first traversal

### GetSocketStates
```angelscript
TArray<FRigSocketState> GetSocketStates()
```
Returns all of the sockets' state

### GetTags
```angelscript
TArray<FName> GetTags(FRigElementKey InItem)
```
* Returns the tags for a given item
* @param InItem The item to return the tags for

### GetTransformArrayMetadata
```angelscript
TArray<FTransform> GetTransformArrayMetadata(FRigElementKey InItem, FName InMetadataName)
```
Queries and returns the value of FTransform array metadata
@param InItem The element key to return the metadata for
@param InMetadataName The name of the metadata to query

### GetTransformMetadata
```angelscript
FTransform GetTransformMetadata(FRigElementKey InItem, FName InMetadataName, FTransform DefaultValue)
```
Queries and returns the value of FTransform metadata
@param InItem The element key to return the metadata for
@param InMetadataName The name of the metadata to query
@param DefaultValue The default value to fall back on

### GetVectorArrayMetadata
```angelscript
TArray<FVector> GetVectorArrayMetadata(FRigElementKey InItem, FName InMetadataName)
```
Queries and returns the value of FVector array metadata
@param InItem The element key to return the metadata for
@param InMetadataName The name of the metadata to query

### GetVectorMetadata
```angelscript
FVector GetVectorMetadata(FRigElementKey InItem, FName InMetadataName, FVector DefaultValue)
```
Queries and returns the value of FVector metadata
@param InItem The element key to return the metadata for
@param InMetadataName The name of the metadata to query
@param DefaultValue The default value to fall back on

### HasTag
```angelscript
bool HasTag(FRigElementKey InItem, FName InTag)
```
* Returns true if a given item has a certain tag
* @param InItem The item to return the tags for
* @param InTag The tag to check

### IsControllerAvailable
```angelscript
bool IsControllerAvailable()
```
Returns true if the hierarchy controller is currently available
The controller may not be available during certain events.
If the controller is not available then GetController() will return nullptr.

### IsCurveValueSet
```angelscript
bool IsCurveValueSet(FRigElementKey InKey)
```
Returns whether a curve's value is set, given its key
@param InKey The key of the element to retrieve the value for
@return Returns true if the value is set, false otherwise.

### IsCurveValueSetByIndex
```angelscript
bool IsCurveValueSetByIndex(int InElementIndex)
```
Returns a curve's value given its index
@param InElementIndex The index of the element to retrieve the value for
@return Returns true if the value is set, false otherwise.

### IsParentedTo
```angelscript
bool IsParentedTo(FRigElementKey InChild, FRigElementKey InParent)
```
Returns true if an element is parented to another element
@param InChild The key of the child element to check for a parent
@param InParent The key of the parent element to check for
@return True if the given parent and given child have a parent-child relationship

### IsProcedural
```angelscript
bool IsProcedural(FRigElementKey InKey)
```
Returns true if the provided element is procedural.
@param InKey The key to validate
@return Returns true if the element is procedural

### IsSelected
```angelscript
bool IsSelected(FRigElementKey InKey)
```
Returns true if a given element is selected
@param InKey The key to check
@return true if a given element is selected

### IsSelectedByIndex
```angelscript
bool IsSelectedByIndex(int InIndex)
```
Returns true if a given element is selected
@param InIndex The index to check
@return true if a given element is selected

### IsValidIndex
```angelscript
bool IsValidIndex(int InElementIndex)
```
Returns true if the provided element index is valid
@param InElementIndex The index to validate
@return Returns true if the provided element index is valid

### Num
```angelscript
int Num()
```
Returns the number of elements in the Hierarchy.
@return The number of elements in the Hierarchy

### RemoveAllMetadata
```angelscript
bool RemoveAllMetadata(FRigElementKey InItem)
```
Removes all of the metadata under a given item
@param InItem The element key to search under

### RemoveMetadata
```angelscript
bool RemoveMetadata(FRigElementKey InItem, FName InMetadataName)
```
Removes the metadata under a given element
@param InItem The element key to search under
@param InMetadataName The name of the metadata to remove

### Reset
```angelscript
void Reset()
```
Clears the whole hierarchy and removes all elements.

### ResetCurveValues
```angelscript
void ResetCurveValues()
```
Resets all curves to 0.0

### ResetPoseToInitial
```angelscript
void ResetPoseToInitial(ERigElementType InTypeFilter)
```
Resets the current pose of a filtered list of elements to the initial / ref pose.

### ResetToDefault
```angelscript
void ResetToDefault()
```
Resets the hierarchy to the state of its default. This refers to the
hierarchy on the default object.

### RestoreConnectorsFromStates
```angelscript
TArray<FRigElementKey> RestoreConnectorsFromStates(TArray<FRigConnectorState> InStates, bool bSetupUndoRedo)
```
Try to restore the connectors from the state structs

### RestoreSocketsFromStates
```angelscript
TArray<FRigElementKey> RestoreSocketsFromStates(TArray<FRigSocketState> InStates, bool bSetupUndoRedo)
```
Try to restore the sockets from the state structs

### SendAutoKeyEvent
```angelscript
void SendAutoKeyEvent(FRigElementKey InElement, float32 InOffsetInSeconds, bool bAsynchronous)
```
Sends an autokey event from the hierarchy to the world
@param InElement The element to send the autokey for
@param InOffsetInSeconds The time offset in seconds
@param bAsynchronous If set to true the event will go on a thread safe queue

### SetBoolArrayMetadata
```angelscript
bool SetBoolArrayMetadata(FRigElementKey InItem, FName InMetadataName, TArray<bool> InValue)
```
Sets the metadata to a bool array value
@param InItem The element key to set the metadata for
@param InMetadataName The name of the metadata to set
@param InValue The value to set
@return Returns true if setting the metadata was successful

### SetBoolMetadata
```angelscript
bool SetBoolMetadata(FRigElementKey InItem, FName InMetadataName, bool InValue)
```
Sets the metadata to a bool value
@param InItem The element key to set the metadata for
@param InMetadataName The name of the metadata to set
@param InValue The value to set
@return Returns true if setting the metadata was successful

### SetConnectorSettings
```angelscript
void SetConnectorSettings(FRigElementKey InKey, FRigConnectorSettings InSettings, bool bSetupUndo, bool bForce, bool bPrintPythonCommands)
```
Sets the connector settings for a given connector element by key
@param InKey The key of the connector element to set the settings for
@param InSettings The new connector settings value to set
@param bSetupUndo If true the transform stack will be setup for undo / redo

### SetConnectorSettingsByIndex
```angelscript
void SetConnectorSettingsByIndex(int InElementIndex, FRigConnectorSettings InSettings, bool bSetupUndo, bool bForce, bool bPrintPythonCommands)
```
Sets the connector settings for a given connector element by index
@param InElementIndex The index of the connector element to set the settings for
@param InSettings The new connector settings value to set
@param bSetupUndo If true the transform stack will be setup for undo / redo

### SetControlOffsetTransform
```angelscript
void SetControlOffsetTransform(FRigElementKey InKey, FTransform InTransform, bool bInitial, bool bAffectChildren, bool bSetupUndo, bool bPrintPythonCommands)
```
Sets the offset transform for a given control element by key
@param InKey The key of the control element to set the offset transform for
@param InTransform The new offset transform value to set
@param bInitial If true the initial value will be used
@param bAffectChildren If set to false children will not move (maintain global).
@param bSetupUndo If true the transform stack will be setup for undo / redo

### SetControlOffsetTransformByIndex
```angelscript
void SetControlOffsetTransformByIndex(int InElementIndex, FTransform InTransform, bool bInitial, bool bAffectChildren, bool bSetupUndo, bool bPrintPythonCommands)
```
Sets the local offset transform for a given control element by index
@param InElementIndex The index of the control element to set the offset transform for
@param InTransform The new local offset transform value to set
@param bInitial If true the initial value will be used
@param bAffectChildren If set to false children will not move (maintain global).
@param bSetupUndo If true the transform stack will be setup for undo / redo

### SetControlPreferredEulerAngles
```angelscript
void SetControlPreferredEulerAngles(FRigElementKey InKey, FVector InEulerAngles, EEulerRotationOrder InRotationOrder, bool bInitial, bool bFixEulerFlips)
```
Sets a control's preferred euler angles (local transform rotation)
@param InKey The key of the element to retrieve the current value for
@param InEulerAngles The new preferred euler angles to set
@param InRotationOrder The rotation order to use when setting the euler angles
@param bInitial If true we'll return the preferred euler angles for the initial - otherwise current transform
@param bFixEulerFlips If true the new euler angles value will use the shortest path

### SetControlPreferredEulerAnglesByIndex
```angelscript
void SetControlPreferredEulerAnglesByIndex(int InElementIndex, FVector InEulerAngles, EEulerRotationOrder InRotationOrder, bool bInitial, bool bFixEulerFlips)
```
Sets a control's preferred euler angles (local transform rotation)
@param InElementIndex The element index to look up
@param InEulerAngles The new preferred euler angles to set
@param InRotationOrder The rotation order to use when setting the euler angles
@param bInitial If true we'll return the preferred euler angles for the initial - otherwise current transform
@param bFixEulerFlips If true the new euler angles value will use the shortest path

### SetControlPreferredRotationOrder
```angelscript
void SetControlPreferredRotationOrder(FRigElementKey InKey, EEulerRotationOrder InRotationOrder)
```
Sets a control's preferred euler rotation order
@param InKey The key of the element to retrieve the current value for
@param InRotationOrder The rotation order to use when setting the euler angles

### SetControlPreferredRotationOrderByIndex
```angelscript
void SetControlPreferredRotationOrderByIndex(int InElementIndex, EEulerRotationOrder InRotationOrder)
```
Sets a control's preferred euler rotation order
@param InElementIndex The element index to look up
@param InRotationOrder The rotation order to use when setting the euler angles

### SetControlPreferredRotator
```angelscript
void SetControlPreferredRotator(FRigElementKey InKey, FRotator InRotator, bool bInitial, bool bFixEulerFlips)
```
Sets a control's preferred rotator (local transform rotation)
@param InKey The key of the element to retrieve the current value for
@param InRotator The new preferred rotator to set
@param bInitial If true we'll return the preferred rotator for the initial - otherwise current transform
@param bFixEulerFlips If true the new rotator value will use the shortest path

### SetControlPreferredRotatorByIndex
```angelscript
void SetControlPreferredRotatorByIndex(int InElementIndex, FRotator InRotator, bool bInitial, bool bFixEulerFlips)
```
Sets a control's preferred rotator (local transform rotation)
@param InElementIndex The element index to look up
@param InRotator The new preferred rotator to set
@param bInitial If true we'll return the preferred rotator for the initial - otherwise current transform
@param bFixEulerFlips If true the new rotator value will use the shortest path

### SetControlSettings
```angelscript
void SetControlSettings(FRigElementKey InKey, FRigControlSettings InSettings, bool bSetupUndo, bool bForce, bool bPrintPythonCommands)
```
Sets the control settings for a given control element by key
@param InKey The key of the control element to set the settings for
@param InSettings The new control settings value to set
@param bSetupUndo If true the transform stack will be setup for undo / redo

### SetControlSettingsByIndex
```angelscript
void SetControlSettingsByIndex(int InElementIndex, FRigControlSettings InSettings, bool bSetupUndo, bool bForce, bool bPrintPythonCommands)
```
Sets the control settings for a given control element by index
@param InElementIndex The index of the control element to set the settings for
@param InSettings The new control settings value to set
@param bSetupUndo If true the transform stack will be setup for undo / redo

### SetControlShapeTransform
```angelscript
void SetControlShapeTransform(FRigElementKey InKey, FTransform InTransform, bool bInitial, bool bSetupUndo)
```
Sets the shape transform for a given control element by key
@param InKey The key of the control element to set the shape transform for
@param InTransform The new shape transform value to set
@param bInitial If true the initial value will be used
@param bSetupUndo If true the transform stack will be setup for undo / redo

### SetControlShapeTransformByIndex
```angelscript
void SetControlShapeTransformByIndex(int InElementIndex, FTransform InTransform, bool bInitial, bool bSetupUndo)
```
Sets the local shape transform for a given control element by index
@param InElementIndex The index of the control element to set the shape transform for
@param InTransform The new local shape transform value to set
@param bInitial If true the initial value will be used
@param bSetupUndo If true the transform stack will be setup for undo / redo

### SetControlValue
```angelscript
void SetControlValue(FRigElementKey InKey, FRigControlValue InValue, ERigControlValueType InValueType, bool bSetupUndo, bool bPrintPythonCommands)
```
Sets a control's current value given its key
@param InKey The key of the element to set the current value for
@param InValue The value to set on the control
@param InValueType The type of value to set
@param bSetupUndo If true the transform stack will be setup for undo / redo

### SetControlValueByIndex
```angelscript
void SetControlValueByIndex(int InElementIndex, FRigControlValue InValue, ERigControlValueType InValueType, bool bSetupUndo, bool bPrintPythonCommands)
```
Sets a control's current value given its index
@param InElementIndex The index of the element to set the current value for
@param InValue The value to set on the control
@param InValueType The type of value to set
@param bSetupUndo If true the transform stack will be setup for undo / redo

### SetControlVisibility
```angelscript
void SetControlVisibility(FRigElementKey InKey, bool bVisibility)
```
Sets a control's current visibility based on a key
@param InKey The key of the element to set the visibility for
@param bVisibility The visibility to set on the control

### SetControlVisibilityByIndex
```angelscript
void SetControlVisibilityByIndex(int InElementIndex, bool bVisibility)
```
Sets a control's current visibility based on a key
@param InElementIndex The index of the element to set the visibility for
@param bVisibility The visibility to set on the control

### SetCurveValue
```angelscript
void SetCurveValue(FRigElementKey InKey, float32 InValue, bool bSetupUndo)
```
Sets a curve's value given its key
@param InKey The key of the element to set the value for
@param InValue The value to set on the curve
@param bSetupUndo If true the transform stack will be setup for undo / redo

### SetCurveValueByIndex
```angelscript
void SetCurveValueByIndex(int InElementIndex, float32 InValue, bool bSetupUndo)
```
Sets a curve's value given its index
@param InElementIndex The index of the element to set the value for
@param InValue The value to set on the curve
@param bSetupUndo If true the transform stack will be setup for undo / redo

### SetFloatArrayMetadata
```angelscript
bool SetFloatArrayMetadata(FRigElementKey InItem, FName InMetadataName, TArray<float32> InValue)
```
Sets the metadata to a float array value
@param InItem The element key to set the metadata for
@param InMetadataName The name of the metadata to set
@param InValue The value to set
@return Returns true if setting the metadata was successful

### SetFloatMetadata
```angelscript
bool SetFloatMetadata(FRigElementKey InItem, FName InMetadataName, float32 InValue)
```
Sets the metadata to a float value
@param InItem The element key to set the metadata for
@param InMetadataName The name of the metadata to set
@param InValue The value to set
@return Returns true if setting the metadata was successful

### SetGlobalTransform
```angelscript
void SetGlobalTransform(FRigElementKey InKey, FTransform InTransform, bool bInitial, bool bAffectChildren, bool bSetupUndo, bool bPrintPythonCommand)
```
Sets the global current or initial transform for a given key.
@param InKey The key to set the transform for
@param InTransform The new transform value to set
@param bInitial If true the initial transform will be used
@param bAffectChildren If set to false children will not move (maintain global).
@param bSetupUndo If true the transform stack will be setup for undo / redo

### SetGlobalTransformByIndex
```angelscript
void SetGlobalTransformByIndex(int InElementIndex, FTransform InTransform, bool bInitial, bool bAffectChildren, bool bSetupUndo, bool bPrintPythonCommand)
```
Sets the global current or initial transform for a given element index.
@param InElementIndex The index of the element to set the transform for
@param InTransform The new transform value to set
@param bInitial If true the initial transform will be used
@param bAffectChildren If set to false children will not move (maintain global).
@param bSetupUndo If true the transform stack will be setup for undo / redo

### SetInt32ArrayMetadata
```angelscript
bool SetInt32ArrayMetadata(FRigElementKey InItem, FName InMetadataName, TArray<int> InValue)
```
Sets the metadata to a int32 array value
@param InItem The element key to set the metadata for
@param InMetadataName The name of the metadata to set
@param InValue The value to set
@return Returns true if setting the metadata was successful

### SetInt32Metadata
```angelscript
bool SetInt32Metadata(FRigElementKey InItem, FName InMetadataName, int InValue)
```
Sets the metadata to a int32 value
@param InItem The element key to set the metadata for
@param InMetadataName The name of the metadata to set
@param InValue The value to set
@return Returns true if setting the metadata was successful

### SetLinearColorArrayMetadata
```angelscript
bool SetLinearColorArrayMetadata(FRigElementKey InItem, FName InMetadataName, TArray<FLinearColor> InValue)
```
Sets the metadata to a FLinearColor array value
@param InItem The element key to set the metadata for
@param InMetadataName The name of the metadata to set
@param InValue The value to set
@return Returns true if setting the metadata was successful

### SetLinearColorMetadata
```angelscript
bool SetLinearColorMetadata(FRigElementKey InItem, FName InMetadataName, FLinearColor InValue)
```
Sets the metadata to a FLinearColor value
@param InItem The element key to set the metadata for
@param InMetadataName The name of the metadata to set
@param InValue The value to set
@return Returns true if setting the metadata was successful

### SetLocalTransform
```angelscript
void SetLocalTransform(FRigElementKey InKey, FTransform InTransform, bool bInitial, bool bAffectChildren, bool bSetupUndo, bool bPrintPythonCommands)
```
Sets the local current or initial transform for a given key.
@param InKey The key to set the transform for
@param InTransform The new transform value to set
@param bInitial If true the initial transform will be used
@param bSetupUndo If true the transform stack will be setup for undo / redo
@param bAffectChildren If set to false children will not move (maintain global).

### SetLocalTransformByIndex
```angelscript
void SetLocalTransformByIndex(int InElementIndex, FTransform InTransform, bool bInitial, bool bAffectChildren, bool bSetupUndo, bool bPrintPythonCommands)
```
Sets the local current or initial transform for a given element index.
@param InElementIndex The index of the element to set the transform for
@param InTransform The new transform value to set
@param bInitial If true the initial transform will be used
@param bSetupUndo If true the transform stack will be setup for undo / redo
@param bAffectChildren If set to false children will not move (maintain global).

### SetNameArrayMetadata
```angelscript
bool SetNameArrayMetadata(FRigElementKey InItem, FName InMetadataName, TArray<FName> InValue)
```
Sets the metadata to a FName array value
@param InItem The element key to set the metadata for
@param InMetadataName The name of the metadata to set
@param InValue The value to set
@return Returns true if setting the metadata was successful

### SetNameMetadata
```angelscript
bool SetNameMetadata(FRigElementKey InItem, FName InMetadataName, FName InValue)
```
Sets the metadata to a FName value
@param InItem The element key to set the metadata for
@param InMetadataName The name of the metadata to set
@param InValue The value to set
@return Returns true if setting the metadata was successful

### SetParentWeight
```angelscript
bool SetParentWeight(FRigElementKey InChild, FRigElementKey InParent, FRigElementWeight InWeight, bool bInitial, bool bAffectChildren)
```
Sets the weight of a parent below a multi parent element
@param InChild The key of the multi parented element
@param InParent The key of the parent to look up the weight for
@param InWeight The new weight to set for the parent
@param bInitial If true the initial weights will be used
@param bAffectChildren If set to false children will not move (maintain global).
@return Returns true if changing the weight was successful

### SetParentWeightArray
```angelscript
bool SetParentWeightArray(FRigElementKey InChild, TArray<FRigElementWeight> InWeights, bool bInitial, bool bAffectChildren)
```
Sets the all of the weights of the parents of a multi parent element
@param InChild The key of the multi parented element
@param InWeights The new weights to set for the parents
@param bInitial If true the initial weights will be used
@param bAffectChildren If set to false children will not move (maintain global).
@return Returns true if changing the weight was successful

### SetPose
```angelscript
void SetPose(FRigPose InPose)
```
Sets the current / initial pose of the hierarchy
@param InPose The pose to set on the hierarchy

### SetQuatArrayMetadata
```angelscript
bool SetQuatArrayMetadata(FRigElementKey InItem, FName InMetadataName, TArray<FQuat> InValue)
```
Sets the metadata to a FQuat array value
@param InItem The element key to set the metadata for
@param InMetadataName The name of the metadata to set
@param InValue The value to set
@return Returns true if setting the metadata was successful

### SetQuatMetadata
```angelscript
bool SetQuatMetadata(FRigElementKey InItem, FName InMetadataName, FQuat InValue)
```
Sets the metadata to a FQuat value
@param InItem The element key to set the metadata for
@param InMetadataName The name of the metadata to set
@param InValue The value to set
@return Returns true if setting the metadata was successful

### SetRigElementKeyArrayMetadata
```angelscript
bool SetRigElementKeyArrayMetadata(FRigElementKey InItem, FName InMetadataName, TArray<FRigElementKey> InValue)
```
Sets the metadata to a FRigElementKey array value
@param InItem The element key to set the metadata for
@param InMetadataName The name of the metadata to set
@param InValue The value to set
@return Returns true if setting the metadata was successful

### SetRigElementKeyMetadata
```angelscript
bool SetRigElementKeyMetadata(FRigElementKey InItem, FName InMetadataName, FRigElementKey InValue)
```
Sets the metadata to a FRigElementKey value
@param InItem The element key to set the metadata for
@param InMetadataName The name of the metadata to set
@param InValue The value to set
@return Returns true if setting the metadata was successful

### SetRotatorArrayMetadata
```angelscript
bool SetRotatorArrayMetadata(FRigElementKey InItem, FName InMetadataName, TArray<FRotator> InValue)
```
Sets the metadata to a FRotator array value
@param InItem The element key to set the metadata for
@param InMetadataName The name of the metadata to set
@param InValue The value to set
@return Returns true if setting the metadata was successful

### SetRotatorMetadata
```angelscript
bool SetRotatorMetadata(FRigElementKey InItem, FName InMetadataName, FRotator InValue)
```
Sets the metadata to a FRotator value
@param InItem The element key to set the metadata for
@param InMetadataName The name of the metadata to set
@param InValue The value to set
@return Returns true if setting the metadata was successful

### SetTag
```angelscript
bool SetTag(FRigElementKey InItem, FName InTag)
```
* Sets a tag on an element in the hierarchy
* @param InItem The item to set the tag for
* @param InTag The tag to set

### SetTransformArrayMetadata
```angelscript
bool SetTransformArrayMetadata(FRigElementKey InItem, FName InMetadataName, TArray<FTransform> InValue)
```
Sets the metadata to a FTransform array value
@param InItem The element key to set the metadata for
@param InMetadataName The name of the metadata to set
@param InValue The value to set
@return Returns true if setting the metadata was successful

### SetTransformMetadata
```angelscript
bool SetTransformMetadata(FRigElementKey InItem, FName InMetadataName, FTransform InValue)
```
Sets the metadata to a FTransform value
@param InItem The element key to set the metadata for
@param InMetadataName The name of the metadata to set
@param InValue The value to set
@return Returns true if setting the metadata was successful

### SetVectorArrayMetadata
```angelscript
bool SetVectorArrayMetadata(FRigElementKey InItem, FName InMetadataName, TArray<FVector> InValue)
```
Sets the metadata to a FVector array value
@param InItem The element key to set the metadata for
@param InMetadataName The name of the metadata to set
@param InValue The value to set
@return Returns true if setting the metadata was successful

### SetVectorMetadata
```angelscript
bool SetVectorMetadata(FRigElementKey InItem, FName InMetadataName, FVector InValue)
```
Sets the metadata to a FVector value
@param InItem The element key to set the metadata for
@param InMetadataName The name of the metadata to set
@param InValue The value to set
@return Returns true if setting the metadata was successful

### SortKeys
```angelscript
TArray<FRigElementKey> SortKeys(TArray<FRigElementKey> InKeys)
```
Sorts the input key list by traversing the hierarchy
@param InKeys The keys to sort
@return The sorted keys

### SwitchToDefaultParent
```angelscript
bool SwitchToDefaultParent(FRigElementKey InChild, bool bInitial, bool bAffectChildren)
```
Switches a multi parent element to its first parent
@param InChild The key of the multi parented element
@param bInitial If true the initial weights will be used
@param bAffectChildren If set to false children will not move (maintain global).
@return Returns true if changing the weight was successful

### SwitchToParent
```angelscript
bool SwitchToParent(FRigElementKey InChild, FRigElementKey InParent, bool bInitial, bool bAffectChildren)
```
Switches a multi parent element to a single parent.
This sets the new parent's weight to 1.0 and disables
weights for all other potential parents.
@param InChild The key of the multi parented element
@param InParent The key of the parent to look up the weight for
@param bInitial If true the initial weights will be used
@param bAffectChildren If set to false children will not move (maintain global).
@return Returns true if changing the weight was successful

### SwitchToWorldSpace
```angelscript
bool SwitchToWorldSpace(FRigElementKey InChild, bool bInitial, bool bAffectChildren)
```
Switches a multi parent element to world space.
This injects a world space reference.
@param InChild The key of the multi parented element
@param bInitial If true the initial weights will be used
@param bAffectChildren If set to false children will not move (maintain global).
@return Returns true if changing the weight was successful

### UnsetCurveValue
```angelscript
void UnsetCurveValue(FRigElementKey InKey, bool bSetupUndo)
```
Sets a curve's value given its key
@param InKey The key of the element to set the value for
@param InValue The value to set on the curve
@param bSetupUndo If true the transform stack will be setup for undo / redo

### UnsetCurveValueByIndex
```angelscript
void UnsetCurveValueByIndex(int InElementIndex, bool bSetupUndo)
```
Sets a curve's value given its index
@param InElementIndex The index of the element to set the value for
@param InValue The value to set on the curve
@param bSetupUndo If true the transform stack will be setup for undo / redo

