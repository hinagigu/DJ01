# URigHierarchyController

**继承自**: `UObject`

## 方法

### AddAnimationChannel
```angelscript
FRigElementKey AddAnimationChannel(FName InName, FRigElementKey InParentControl, FRigControlSettings InSettings, bool bSetupUndo, bool bPrintPythonCommand)
```
Adds a control to the hierarchy
@param InName The suggested name of the new animation channel - will eventually be corrected by the namespace
@param InParentControl The parent of the new animation channel.
@param InSettings All of the animation channel's settings
@param bSetupUndo If set to true the stack will record the change for undo / redo
@return The key for the newly created animation channel.

### AddBone
```angelscript
FRigElementKey AddBone(FName InName, FRigElementKey InParent, FTransform InTransform, bool bTransformInGlobal, ERigBoneType InBoneType, bool bSetupUndo, bool bPrintPythonCommand)
```
Adds a bone to the hierarchy
@param InName The suggested name of the new bone - will eventually be corrected by the namespace
@param InParent The (optional) parent of the new bone. If you don't need a parent, pass FRigElementKey()
@param InTransform The transform for the new bone - either in local or global space, based on bTransformInGlobal
@param bTransformInGlobal Set this to true if the Transform passed is expressed in global space, false for local space.
@param InBoneType The type of bone to add. This can be used to differentiate between imported bones and user defined bones.
@param bSetupUndo If set to true the stack will record the change for undo / redo
@param bPrintPythonCommand If set to true a python command equivalent to this call will be printed out
@return The key for the newly created bone.

### AddConnector
```angelscript
FRigElementKey AddConnector(FName InName, FRigConnectorSettings InSettings, bool bSetupUndo, bool bPrintPythonCommand)
```
Adds a connector to the hierarchy
@param InName The suggested name of the new connector - will eventually be corrected by the namespace
@param InSettings All of the connector's settings
@param bSetupUndo If set to true the stack will record the change for undo / redo
@param bPrintPythonCommand If set to true a python command equivalent to this call will be printed out
@return The key for the newly created bone.

### AddControl
```angelscript
FRigElementKey AddControl(FName InName, FRigElementKey InParent, FRigControlSettings InSettings, FRigControlValue InValue, bool bSetupUndo, bool bPrintPythonCommand)
```
Adds a control to the hierarchy
@param InName The suggested name of the new control - will eventually be corrected by the namespace
@param InParent The (optional) parent of the new control. If you don't need a parent, pass FRigElementKey()
@param InSettings All of the control's settings
@param InValue The value to use for the control
@param bSetupUndo If set to true the stack will record the change for undo / redo
@return The key for the newly created control.

### AddCurve
```angelscript
FRigElementKey AddCurve(FName InName, float32 InValue, bool bSetupUndo, bool bPrintPythonCommand)
```
Adds a curve to the hierarchy
@param InName The suggested name of the new curve - will eventually be corrected by the namespace
@param InValue The value to use for the curve
@param bSetupUndo If set to true the stack will record the change for undo / redo
@param bPrintPythonCommand If set to true a python command equivalent to this call will be printed out
@return The key for the newly created curve.

### AddNull
```angelscript
FRigElementKey AddNull(FName InName, FRigElementKey InParent, FTransform InTransform, bool bTransformInGlobal, bool bSetupUndo, bool bPrintPythonCommand)
```
Adds a null to the hierarchy
@param InName The suggested name of the new null - will eventually be corrected by the namespace
@param InParent The (optional) parent of the new null. If you don't need a parent, pass FRigElementKey()
@param InTransform The transform for the new null - either in local or global null, based on bTransformInGlobal
@param bTransformInGlobal Set this to true if the Transform passed is expressed in global null, false for local null.
@param bSetupUndo If set to true the stack will record the change for undo / redo
@param bPrintPythonCommand If set to true a python command equivalent to this call will be printed out
@return The key for the newly created null.

### AddParent
```angelscript
bool AddParent(FRigElementKey InChild, FRigElementKey InParent, float32 InWeight, bool bMaintainGlobalTransform, bool bSetupUndo)
```
Adds a new parent to an element. For elements that allow only one parent the parent will be replaced (Same as ::SetParent).
@param InChild The key of the element to add the parent for
@param InParent The key of the new parent to add
@param InWeight The initial weight to give to the parent
@param bMaintainGlobalTransform If set to true the child will stay in the same place spatially, otherwise it will maintain it's local transform (and potential move).
@param bSetupUndo If set to true the stack will record the change for undo / redo
@return Returns true if successful.

### AddRigidBody
```angelscript
FRigElementKey AddRigidBody(FName InName, FRigElementKey InParent, FRigRigidBodySettings InSettings, FTransform InLocalTransform, bool bSetupUndo, bool bPrintPythonCommand)
```
Adds a rigidbody to the hierarchy
@param InName The suggested name of the new rigidbody - will eventually be corrected by the namespace
@param InParent The (optional) parent of the new rigidbody. If you don't need a parent, pass FRigElementKey()
@param InSettings All of the rigidbody's settings
@param InLocalTransform The transform for the new rigidbody - in the space of the provided parent
@param bSetupUndo If set to true the stack will record the change for undo / redo
@param bPrintPythonCommand If set to true a python command equivalent to this call will be printed out
@return The key for the newly created rigidbody.

### AddSocket
```angelscript
FRigElementKey AddSocket(FName InName, FRigElementKey InParent, FTransform InTransform, bool bTransformInGlobal, FLinearColor InColor, FString InDescription, bool bSetupUndo, bool bPrintPythonCommand)
```
Adds a socket to the hierarchy
@param InName The suggested name of the new socket - will eventually be corrected by the namespace
@param InParent The (optional) parent of the new null. If you don't need a parent, pass FRigElementKey()
@param InTransform The transform for the new socket - either in local or global space, based on bTransformInGlobal
@param bTransformInGlobal Set this to true if the Transform passed is expressed in global space, false for local space.
@param InColor The color of the socket
@param InDescription The description of the socket
@param bSetupUndo If set to true the stack will record the change for undo / redo
@param bPrintPythonCommand If set to true a python command equivalent to this call will be printed out
@return The key for the newly created bone.

### ClearSelection
```angelscript
bool ClearSelection()
```
Clears the selection
@return Returns true if the selection was applied

### DeselectElement
```angelscript
bool DeselectElement(FRigElementKey InKey)
```
Deselects or deselects an element in the hierarchy
@param InKey The key of the element to deselect
@return Returns true if the selection was applied

### DuplicateElements
```angelscript
TArray<FRigElementKey> DuplicateElements(TArray<FRigElementKey> InKeys, bool bSelectNewElements, bool bSetupUndo, bool bPrintPythonCommands)
```
Duplicate the given elements
@param InKeys The keys of the elements to duplicate
@param bSelectNewElements If set to true the new elements will be selected
@param bSetupUndo If set to true the stack will record the change for undo / redo
@param bPrintPythonCommand If set to true a python command equivalent to this call will be printed out
@return The keys of the 4d items

### ExportSelectionToText
```angelscript
FString ExportSelectionToText()
```
Exports the selected items to text
@return The text representation of the selected items

### ExportToText
```angelscript
FString ExportToText(TArray<FRigElementKey> InKeys)
```
Exports a list of items to text
@param InKeys The keys to export to text
@return The text representation of the requested elements

### GeneratePythonCommands
```angelscript
TArray<FString> GeneratePythonCommands()
```

### GetControlSettings
```angelscript
FRigControlSettings GetControlSettings(FRigElementKey InKey)
```
Returns the control settings of a given control
@param InKey The key of the control to receive the settings for
@return The settings of the given control

### GetHierarchy
```angelscript
URigHierarchy GetHierarchy()
```
Returns the hierarchy currently linked to this controller

### ImportBones
```angelscript
TArray<FRigElementKey> ImportBones(USkeleton InSkeleton, FName InNameSpace, bool bReplaceExistingBones, bool bRemoveObsoleteBones, bool bSelectBones, bool bSetupUndo, bool bPrintPythonCommand)
```
Imports an existing skeleton to the hierarchy
@param InSkeleton The skeleton to import
@param InNameSpace The namespace to prefix the bone names with
@param bReplaceExistingBones If true existing bones will be removed
@param bRemoveObsoleteBones If true bones non-existent in the skeleton will be removed from the hierarchy
@param bSelectBones If true the bones will be selected upon import
@param bSetupUndo If set to true the stack will record the change for undo / redo
@param bPrintPythonCommand If set to true a python command equivalent to this call will be printed out
@return The keys of the imported elements

### ImportBonesFromAsset
```angelscript
TArray<FRigElementKey> ImportBonesFromAsset(FString InAssetPath, FName InNameSpace, bool bReplaceExistingBones, bool bRemoveObsoleteBones, bool bSelectBones, bool bSetupUndo)
```
Imports an existing skeleton to the hierarchy
@param InAssetPath The path to the uasset to import from
@param InNameSpace The namespace to prefix the bone names with
@param bReplaceExistingBones If true existing bones will be removed
@param bRemoveObsoleteBones If true bones non-existent in the skeleton will be removed from the hierarchy
@param bSelectBones If true the bones will be selected upon import
@param bSetupUndo If set to true the stack will record the change for undo / redo
@return The keys of the imported elements

### ImportCurves
```angelscript
TArray<FRigElementKey> ImportCurves(USkeleton InSkeleton, FName InNameSpace, bool bSelectCurves, bool bSetupUndo, bool bPrintPythonCommand)
```
Imports all curves from a skeleton to the hierarchy
@param InSkeleton The skeleton to import the curves from
@param InNameSpace The namespace to prefix the bone names with
@param bSelectCurves If true the curves will be selected upon import
@param bSetupUndo If set to true the stack will record the change for undo / redo
@return The keys of the imported elements

### ImportCurvesFromAsset
```angelscript
TArray<FRigElementKey> ImportCurvesFromAsset(FString InAssetPath, FName InNameSpace, bool bSelectCurves, bool bSetupUndo)
```
Imports all curves from a skeleton to the hierarchy
@param InAssetPath The path to the uasset to import from
@param InNameSpace The namespace to prefix the bone names with
@param bSelectCurves If true the curves will be selected upon import
@param bSetupUndo If set to true the stack will record the change for undo / redo
@return The keys of the imported elements

### ImportFromText
```angelscript
TArray<FRigElementKey> ImportFromText(FString InContent, bool bReplaceExistingElements, bool bSelectNewElements, bool bSetupUndo, bool bPrintPythonCommands)
```
Imports the content of a text buffer to the hierarchy
@param InContent The string buffer representing the content to import
@param bReplaceExistingElements If set to true existing items will be replaced / updated with the content in the buffer
@param bSelectNewElements If set to true the new elements will be selected
@param bSetupUndo If set to true the stack will record the change for undo / redo
@param bPrintPythonCommand If set to true a python command equivalent to this call will be printed out

### MirrorElements
```angelscript
TArray<FRigElementKey> MirrorElements(TArray<FRigElementKey> InKeys, FRigVMMirrorSettings InSettings, bool bSelectNewElements, bool bSetupUndo, bool bPrintPythonCommands)
```
Mirrors the given elements
@param InKeys The keys of the elements to mirror
@param InSettings The settings to use for the mirror operation
@param bSelectNewElements If set to true the new elements will be selected
@param bSetupUndo If set to true the stack will record the change for undo / redo
@param bPrintPythonCommand If set to true a python command equivalent to this call will be printed out
@return The keys of the mirrored items

### RemoveAllParents
```angelscript
bool RemoveAllParents(FRigElementKey InChild, bool bMaintainGlobalTransform, bool bSetupUndo, bool bPrintPythonCommand)
```
Removes all parents from an element in the hierarchy.
@param InChild The key of the element to remove all parents for
@param bMaintainGlobalTransform If set to true the child will stay in the same place spatially, otherwise it will maintain it's local transform (and potential move).
@param bSetupUndo If set to true the stack will record the change for undo / redo
@param bPrintPythonCommand If set to true a python command equivalent to this call will be printed out
@return Returns true if successful.

### RemoveElement
```angelscript
bool RemoveElement(FRigElementKey InElement, bool bSetupUndo, bool bPrintPythonCommand)
```
Removes an existing element from the hierarchy
@param InElement The key of the element to remove
@param bSetupUndo If set to true the stack will record the change for undo / redo
@param bPrintPythonCommand If set to true a python command equivalent to this call will be printed out
@return Returns true if successful.

### RemoveParent
```angelscript
bool RemoveParent(FRigElementKey InChild, FRigElementKey InParent, bool bMaintainGlobalTransform, bool bSetupUndo, bool bPrintPythonCommand)
```
Removes an existing parent from an element in the hierarchy. For elements that allow only one parent the element will be unparented (same as ::RemoveAllParents)
@param InChild The key of the element to remove the parent for
@param InParent The key of the parent to remove
@param bMaintainGlobalTransform If set to true the child will stay in the same place spatially, otherwise it will maintain it's local transform (and potential move).
@param bSetupUndo If set to true the stack will record the change for undo / redo
@param bPrintPythonCommand If set to true a python command equivalent to this call will be printed out
@return Returns true if successful.

### RenameElement
```angelscript
FRigElementKey RenameElement(FRigElementKey InElement, FName InName, bool bSetupUndo, bool bPrintPythonCommand, bool bClearSelection)
```
Renames an existing element in the hierarchy
@param InElement The key of the element to rename
@param InName The new name to set for the element
@param bSetupUndo If set to true the stack will record the change for undo / redo
@param bPrintPythonCommand If set to true a python command equivalent to this call will be printed out
@param bClearSelection True if the selection should be cleared after a rename
@return Returns the new element key used for the element

### ReorderElement
```angelscript
bool ReorderElement(FRigElementKey InElement, int InIndex, bool bSetupUndo, bool bPrintPythonCommand)
```
Changes the element's index within its default parent (or the top level)
@param InElement The key of the element to rename
@param InIndex The new index of the element to take within its default parent (or the top level)
@param bSetupUndo If set to true the stack will record the change for undo / redo
@param bPrintPythonCommand If set to true a python command equivalent to this call will be printed out
@return Returns true if the element has been reordered accordingly

### SelectElement
```angelscript
bool SelectElement(FRigElementKey InKey, bool bSelect, bool bClearSelection)
```
Selects or deselects an element in the hierarchy
@param InKey The key of the element to select
@param bSelect If set to false the element will be deselected
@return Returns true if the selection was applied

### SetControlSettings
```angelscript
bool SetControlSettings(FRigElementKey InKey, FRigControlSettings InSettings, bool bSetupUndo)
```
Sets a control's settings given a control key
@param InKey The key of the control to set the settings for
@param The settings to set
@return Returns true if the settings have been set correctly

### SetDisplayName
```angelscript
FName SetDisplayName(FRigElementKey InControl, FName InDisplayName, bool bRenameElement, bool bSetupUndo, bool bPrintPythonCommand)
```
Sets the display name on a control
@param InControl The key of the control to change the display name for
@param InDisplayName The new display name to set for the control
@param bRenameElement True if the control should also be renamed
@param bSetupUndo If set to true the stack will record the change for undo / redo
@param bPrintPythonCommand If set to true a python command equivalent to this call will be printed out
@return Returns the new display name used for the control

### SetHierarchy
```angelscript
void SetHierarchy(URigHierarchy InHierarchy)
```
Sets the hierarchy currently linked to this controller

### SetParent
```angelscript
bool SetParent(FRigElementKey InChild, FRigElementKey InParent, bool bMaintainGlobalTransform, bool bSetupUndo, bool bPrintPythonCommand)
```
Sets a new parent to an element. For elements that allow more than one parent the parent list will be replaced.
@param InChild The key of the element to set the parent for
@param InParent The key of the new parent to set
@param bMaintainGlobalTransform If set to true the child will stay in the same place spatially, otherwise it will maintain it's local transform (and potential move).
@param bSetupUndo If set to true the stack will record the change for undo / redo
@param bPrintPythonCommand If set to true a python command equivalent to this call will be printed out
@return Returns true if successful.

### SetSelection
```angelscript
bool SetSelection(TArray<FRigElementKey> InKeys, bool bPrintPythonCommand)
```
Sets the selection based on a list of keys
@param InKeys The array of keys of the elements to select
@return Returns true if the selection was applied

