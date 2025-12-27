# UTypedElementSelectionSet

**继承自**: `UObject`

A wrapper around an element list that ensures mutation goes via the selection
interfaces, as well as providing some utilities for batching operations.

## 属性

### OnPreSelectionChange
- **类型**: `FOnPreChangeDynamic__TypedElementSelectionSet`

### OnSelectionChange
- **类型**: `FOnChangeDynamic__TypedElementSelectionSet`

## 方法

### AllowSelectionModifiers
```angelscript
bool AllowSelectionModifiers(FScriptTypedElementHandle InElementHandle)
```
Test to see whether selection modifiers (Ctrl or Shift) are allowed while selecting this element.

### CanDeselectElement
```angelscript
bool CanDeselectElement(FScriptTypedElementHandle InElementHandle, FTypedElementSelectionOptions InSelectionOptions)
```
Test to see whether the given element can be deselected.

### CanSelectElement
```angelscript
bool CanSelectElement(FScriptTypedElementHandle InElementHandle, FTypedElementSelectionOptions InSelectionOptions)
```
Test to see whether the given element can be selected.

### ClearSelection
```angelscript
bool ClearSelection(FTypedElementSelectionOptions InSelectionOptions)
```
Clear the current selection.
@return True if the selection was changed, false otherwise.

### CountSelectedElements
```angelscript
int CountSelectedElements(TSubclassOf<UInterface> InBaseInterfaceType)
```
Count the number of selected elements, optionally filtering to elements that implement the given interface.

### CountSelectedObjects
```angelscript
int CountSelectedObjects(const UClass InRequiredClass)
```
Count the number of selected objects.

### DeselectElement
```angelscript
bool DeselectElement(FScriptTypedElementHandle InElementHandle, FTypedElementSelectionOptions InSelectionOptions)
```
Attempt to deselect the given element.
@return True if the selection was changed, false otherwise.

### DeselectElements
```angelscript
bool DeselectElements(TArray<FScriptTypedElementHandle> InElementHandles, FTypedElementSelectionOptions InSelectionOptions)
```
Attempt to deselect the given elements.
@return True if the selection was changed, false otherwise.

### GetBottomSelectedObject
```angelscript
UObject GetBottomSelectedObject(const UClass InRequiredClass)
```
Get the last selected object of the given type.

### GetCurrentSelectionState
```angelscript
FTypedElementSelectionSetState GetCurrentSelectionState()
```
Serializes the current selection set.
The calling code is responsible for storing any state information. The selection set can be returned to a prior state using RestoreSelectionState.

@returns the current state of the selection set.

### GetNumSelectedElements
```angelscript
int GetNumSelectedElements()
```
Get the number of selected elements.

### GetSelectedObjects
```angelscript
TArray<UObject> GetSelectedObjects(const UClass InRequiredClass)
```
Get the array of selected objects from the currently selected elements.

### GetSelectionElement
```angelscript
FScriptTypedElementHandle GetSelectionElement(FScriptTypedElementHandle InElementHandle, ETypedElementSelectionMethod InSelectionMethod)
```
Given an element, return the element that should actually perform a selection operation.

### GetTopSelectedObject
```angelscript
UObject GetTopSelectedObject(const UClass InRequiredClass)
```
Get the first selected object of the given type.

### HasSelectedElements
```angelscript
bool HasSelectedElements(TSubclassOf<UInterface> InBaseInterfaceType)
```
Test whether there selected elements, optionally filtering to elements that implement the given interface.

### HasSelectedObjects
```angelscript
bool HasSelectedObjects(const UClass InRequiredClass)
```
Test whether there are any selected objects.

### IsElementSelected
```angelscript
bool IsElementSelected(FScriptTypedElementHandle InElementHandle, FTypedElementIsSelectedOptions InSelectionOptions)
```
Test to see whether the given element is currently considered selected.

### GetSelectedElementHandles
```angelscript
TArray<FScriptTypedElementHandle> GetSelectedElementHandles(TSubclassOf<UInterface> InBaseInterfaceType)
```
Get the handle of every selected element, optionally filtering to elements that implement the given interface.

### RestoreSelectionState
```angelscript
void RestoreSelectionState(FTypedElementSelectionSetState InSelectionState)
```
Restores the selection set from the given state.
The calling code is responsible for managing any undo state.

### SelectElement
```angelscript
bool SelectElement(FScriptTypedElementHandle InElementHandle, FTypedElementSelectionOptions InSelectionOptions)
```
Attempt to select the given element.
@return True if the selection was changed, false otherwise.

### SelectElements
```angelscript
bool SelectElements(TArray<FScriptTypedElementHandle> InElementHandles, FTypedElementSelectionOptions InSelectionOptions)
```
Attempt to select the given elements.
@return True if the selection was changed, false otherwise.

### SetSelection
```angelscript
bool SetSelection(TArray<FScriptTypedElementHandle> InElementHandles, FTypedElementSelectionOptions InSelectionOptions)
```
Attempt to make the selection the given elements.
@note Equivalent to calling ClearSelection then SelectElements, but happens in a single batch.
@return True if the selection was changed, false otherwise.

