# __TypedElementList

## 方法

### Add
```angelscript
bool Add(FScriptTypedElementListProxy ElementList, FScriptTypedElementHandle ElementHandle)
```
Add the given element handle to this element list, if it isn't already in the list.
@return True if the element handle was added, false if it is already in the list.

### Append
```angelscript
void Append(FScriptTypedElementListProxy ElementList, TArray<FScriptTypedElementHandle> ElementHandles)
```
Append the given element handles to this element list.

### AppendList
```angelscript
void AppendList(FScriptTypedElementListProxy ElementList, FScriptTypedElementListProxy OtherElementList)
```
Append the another element list to this element list.

### Clone
```angelscript
FScriptTypedElementListProxy Clone(FScriptTypedElementListProxy ElementList)
```
Clone this list instance.
@note Only copies elements; does not copy any bindings!

### Contains
```angelscript
bool Contains(FScriptTypedElementListProxy ElementList, FScriptTypedElementHandle ElementHandle)
```
Does this element list contain an entry for the given element handle?

### CountElements
```angelscript
int CountElements(FScriptTypedElementListProxy ElementList, TSubclassOf<UInterface> BaseInterfaceType)
```
Count the number of elements in this list, optionally filtering to elements that implement the given interface.

### CountElementsOfType
```angelscript
int CountElementsOfType(FScriptTypedElementListProxy ElementList, FName ElementTypeName)
```
Count the number of elements in this list of the given type.

### CreateElementList
```angelscript
FScriptTypedElementListProxy CreateElementList(UTypedElementRegistry Registry)
```
Create an empty list of elements associated with the given registry.

### Empty
```angelscript
void Empty(FScriptTypedElementListProxy ElementList, int Slack)
```
Remove all entries from this element list, potentially leaving space allocated for the given number of entries.

### GetElementHandleAt
```angelscript
FScriptTypedElementHandle GetElementHandleAt(FScriptTypedElementListProxy ElementList, int Index)
```
Get the element handle at the given index.
@note Use IsValidIndex to test for validity.

### GetElementHandles
```angelscript
TArray<FScriptTypedElementHandle> GetElementHandles(FScriptTypedElementListProxy ElementList, TSubclassOf<UInterface> BaseInterfaceType)
```
Get the handle of every element in this list, optionally filtering to elements that implement the given interface.

### GetElementInterface
```angelscript
UObject GetElementInterface(FScriptTypedElementListProxy ElementList, FScriptTypedElementHandle ElementHandle, TSubclassOf<UInterface> BaseInterfaceType)
```
Get the element interface from the given handle.

### HasElements
```angelscript
bool HasElements(FScriptTypedElementListProxy ElementList, TSubclassOf<UInterface> BaseInterfaceType)
```
Test whether there are elements in this list, optionally filtering to elements that implement the given interface.

### HasElementsOfType
```angelscript
bool HasElementsOfType(FScriptTypedElementListProxy ElementList, FName ElementTypeName)
```
Test whether there are elements in this list of the given type.

### IsValidIndex
```angelscript
bool IsValidIndex(FScriptTypedElementListProxy ElementList, int Index)
```
Is the given index a valid entry within this element list?

### Num
```angelscript
int Num(FScriptTypedElementListProxy ElementList)
```
Get the number of entries within this element list.

### Remove
```angelscript
bool Remove(FScriptTypedElementListProxy ElementList, FScriptTypedElementHandle ElementHandle)
```
Remove the given element handle from this element list, if it is in the list.
@return True if the element handle was removed, false if it isn't in the list.

### Reserve
```angelscript
void Reserve(FScriptTypedElementListProxy ElementList, int Size)
```
Pre-allocate enough memory in this element list to store the given number of entries.

### Reset
```angelscript
void Reset(FScriptTypedElementListProxy ElementList)
```
Remove all entries from this element list, preserving existing allocations.

### Shrink
```angelscript
void Shrink(FScriptTypedElementListProxy ElementList)
```
Shrink this element list storage to avoid slack.

