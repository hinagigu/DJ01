# USubobjectDataSubsystem

**继承自**: `UEngineSubsystem`

The Subobject Data Subsystem will produce the reflected subobject data
based on a given root object. A root object can be anything, an actor
instance clicked on via the level editor, a UBlueprint* by opening an asset,
or something piped in from python or other scripting languages.

## 方法

### AddNewSubobject
```angelscript
FSubobjectDataHandle AddNewSubobject(FAddNewSubobjectParams Params, FText& FailReason)
```
Add a new subobject as a child to the given parent object

@param Params                 Options to consider when adding this subobject

@return FSubobjectDataHandle          Handle to the newly created subobject, Invalid handle if creation failed

### AttachSubobject
```angelscript
bool AttachSubobject(FSubobjectDataHandle OwnerHandle, FSubobjectDataHandle ChildToAddHandle)
```
Add the given subobject to a new owner. This will remove the subobject from its previous
owner if necessary.

@param OwnerHandle           The new owner to attach to
@param ChildToAddHandle      Handle to the subobject that will become a child of the owner

@return true if the child was added successfully

### CanCopySubobjects
```angelscript
bool CanCopySubobjects(TArray<FSubobjectDataHandle> Handles)
```
Returns true if the given array of handles represents subobjects that
can be copied.

### CanPasteSubobjects
```angelscript
bool CanPasteSubobjects(FSubobjectDataHandle RootHandle, UBlueprint BPContext)
```

### ChangeSubobjectClass
```angelscript
bool ChangeSubobjectClass(FSubobjectDataHandle Handle, const UClass NewClass)
```
Attempts to change the subclass of a native component

@param Handle                 Handle to the subobject to change class of
@param NewClass               The new class that is desired for the given subobject

@return True if the class change was successful, false otherwise.

### CopySubobjects
```angelscript
void CopySubobjects(TArray<FSubobjectDataHandle> Handles, UBlueprint BpContext)
```

### DeleteSubobject
```angelscript
int DeleteSubobject(FSubobjectDataHandle ContextHandle, FSubobjectDataHandle SubobjectToDelete, UBlueprint BPContext)
```
Attempts to delete the given subobject from its blueprint context

@param ContextHandle                  The owning context of the subobjects that should be removed
@param SubobjectToDelete              The subobject handles that should be deleted
@param BPContext                              The blueprint context for the given

@return       The number of subobjects successfully deleted

### DeleteSubobjects
```angelscript
int DeleteSubobjects(FSubobjectDataHandle ContextHandle, TArray<FSubobjectDataHandle> SubobjectsToDelete, UBlueprint BPContext)
```
Attempts to delete the given array of subobjects from their context

@param ContextHandle                  The owning context of the subobjects that should be removed
@param SubobjectsToDelete             Array of subobject handles that should be deleted
@param BPContext                              The blueprint context for the given

@return       The number of subobjects successfully deleted

### DetachSubobject
```angelscript
bool DetachSubobject(FSubobjectDataHandle OwnerHandle, FSubobjectDataHandle ChildToRemove)
```
Remove the child subobject from the owner

@return True if the child was successfully removed.

### FindHandleForObject
```angelscript
FSubobjectDataHandle FindHandleForObject(FSubobjectDataHandle Context, const UObject ObjectToFind, UBlueprint BPContext)
```
Attempt to find an existing handle for the given object.

@param Context                The context that the object to find is within
@param ObjectToFind   The object that you want to find the handle for within the context

@return FSubobjectDataHandle  The subobject handle for the object, Invalid handle if not found.

### IsValidRename
```angelscript
bool IsValidRename(FSubobjectDataHandle Handle, FText InNewText, FText& OutErrorMessage)
```
Returns true if the given new text is a valid option to rename the
subobject with the given handle. Populates the OutErrorMessage if
it is not valid.

@param Handle                        Handle to the subobject that is being checked
@param InNewText                     The new name that is desired
@param OutErrorMessage       The reasoning for an invalid name

@return True if the rename is valid

### DeleteSubobjectFromInstance
```angelscript
int DeleteSubobjectFromInstance(FSubobjectDataHandle ContextHandle, FSubobjectDataHandle SubobjectToDelete)
```
Attempts to delete the given subobject from its context

@param ContextHandle                  The owning context of the subobjects that should be removed
@param SubobjectToDelete              The subobject handles that should be deleted

@return       The number of subobjects successfully deleted

### DeleteSubobjectsFromInstance
```angelscript
int DeleteSubobjectsFromInstance(FSubobjectDataHandle ContextHandle, TArray<FSubobjectDataHandle> SubobjectsToDelete)
```
Attempts to delete the given array of subobjects from their context

@param ContextHandle                  The owning context of the subobjects that should be removed
@param SubobjectsToDelete             Array of subobject handles that should be deleted

@return       The number of subobjects successfully deleted

### FindSubobjectDataFromHandle
```angelscript
bool FindSubobjectDataFromHandle(FSubobjectDataHandle Handle, FSubobjectData& OutData)
```
Attempt to find the subobject data for a given handle. OutData will only
be valid if the function returns true.

@param Handle         Handle of the subobject data you want to acquire
@param OutData        Reference to the subobject data to populate

@return bool          true if the data was found

### GatherSubobjectDataForBlueprint
```angelscript
void GatherSubobjectDataForBlueprint(UBlueprint Context, TArray<FSubobjectDataHandle>& OutArray)
```
Gather all subobjects that the given Blueprint context has. Populates an array of
handles that will have the given context and all it's subobjects.

@param Context                Object to gather subobjects for
@param OutArray               Array to populate (will be emptied first)

### GatherSubobjectDataForInstance
```angelscript
void GatherSubobjectDataForInstance(AActor Context, TArray<FSubobjectDataHandle>& OutArray)
```
Gather all subobjects that the given actor instance has. Populates an array of
handles that will have the given context and all it's subobjects.

@param Context                Object to gather subobjects for
@param OutArray               Array to populate (will be emptied first)

### MakeNewSceneRoot
```angelscript
bool MakeNewSceneRoot(FSubobjectDataHandle Context, FSubobjectDataHandle NewSceneRoot, UBlueprint BPContext)
```

### RenameSubobject
```angelscript
bool RenameSubobject(FSubobjectDataHandle Handle, FText InNewName)
```
Attempts to rename the given subobject to the new name.

@param Handle                 Handle to the subobject to rename
@param InNewName              The new name that is desired for the given subobject

@return True if the rename was successful, false otherwise.

### ReparentSubobject
```angelscript
bool ReparentSubobject(FReparentSubobjectParams Params, FSubobjectDataHandle ToReparentHandle)
```
Attempts to reparent the given subobject to the new parent

@param NewParentHandle                Handle of the new parent
@param ToReparentHandle               The handle of the subobject that will get moved

@return True if the reparent was successful, false otherwise.

### ReparentSubobjects
```angelscript
bool ReparentSubobjects(FReparentSubobjectParams Params, TArray<FSubobjectDataHandle> HandlesToMove)
```
Attempts to reparent all subobjects in the HandlesToMove array to the new parent handle.

@param NewParentHandle                Handle of the new parent

