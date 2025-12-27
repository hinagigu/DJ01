# __TypedElementSelectionSet

## 方法

### DeselectElementsFromList
```angelscript
bool DeselectElementsFromList(UTypedElementSelectionSet SelectionSet, FScriptTypedElementListProxy ElementList, FTypedElementSelectionOptions SelectionOptions)
```
Attempt to deselect the given elements.
@return True if the selection was changed, false otherwise.

### GetNormalizedElementList
```angelscript
FScriptTypedElementListProxy GetNormalizedElementList(UTypedElementSelectionSet SelectionSet, FScriptTypedElementListProxy ElementList, FTypedElementSelectionNormalizationOptions NormalizationOptions)
```
Get a normalized version of the given element list that can be used to perform operations like gizmo manipulation, deletion, copying, etc.
This will do things like expand out groups, and resolve any parent<->child elements so that duplication operations aren't performed on both the parent and the child.

### GetNormalizedSelection
```angelscript
FScriptTypedElementListProxy GetNormalizedSelection(UTypedElementSelectionSet SelectionSet, FTypedElementSelectionNormalizationOptions NormalizationOptions)
```
Get a normalized version of this selection set that can be used to perform operations like gizmo manipulation, deletion, copying, etc.
This will do things like expand out groups, and resolve any parent<->child elements so that duplication operations aren't performed on both the parent and the child.

### SelectElementsFromList
```angelscript
bool SelectElementsFromList(UTypedElementSelectionSet SelectionSet, FScriptTypedElementListProxy ElementList, FTypedElementSelectionOptions SelectionOptions)
```
Attempt to select the given elements.
@return True if the selection was changed, false otherwise.

### SetSelectionFromList
```angelscript
bool SetSelectionFromList(UTypedElementSelectionSet SelectionSet, FScriptTypedElementListProxy ElementList, FTypedElementSelectionOptions SelectionOptions)
```
Attempt to make the selection the given elements.
@note Equivalent to calling ClearSelection then SelectElements, but happens in a single batch.
@return True if the selection was changed, false otherwise.

