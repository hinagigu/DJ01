# UTypedElementCommonActions

**继承自**: `UObject`

A utility to handle higher-level common actions, but default via UTypedElementWorldInterface,
but asset editors can customize this behavior via FTypedElementCommonActionsCustomization.

## 方法

### CopyNormalizedElements
```angelscript
bool CopyNormalizedElements(FScriptTypedElementListProxy ElementList)
```
* Copy any elements from the given selection set that can be copied into the clipboard.
* @note This list should have been pre-normalized via UTypedElementSelectionSet::GetNormalizedSelection or UTypedElementSelectionSet::GetNormalizedElementList.

### CopyNormalizedElementsToString
```angelscript
bool CopyNormalizedElementsToString(FScriptTypedElementListProxy ElementList, FString& OutputString)
```
* Copy any elements from the given selection set that can be copied into the clipboard.
* @note This list should have been pre-normalized via UTypedElementSelectionSet::GetNormalizedSelection or UTypedElementSelectionSet::GetNormalizedElementList.

### CopySelectedElements
```angelscript
bool CopySelectedElements(UTypedElementSelectionSet SelectionSet)
```
Copy any elements from the given selection set that can be copied into the clipboard
@note Internally this just calls CopyNormalizedElements on the result of UTypedElementSelectionSet::GetNormalizedSelection.

### CopySelectedElementsToString
```angelscript
bool CopySelectedElementsToString(UTypedElementSelectionSet SelectionSet, FString& OutputString)
```
Copy any elements from the given selection set that can be copied into the string
@note Internally this just calls CopyNormalizedElements on the result of UTypedElementSelectionSet::GetNormalizedSelection.

### DeleteNormalizedElements
```angelscript
bool DeleteNormalizedElements(FScriptTypedElementListProxy ElementList, UWorld World, UTypedElementSelectionSet InSelectionSet, FTypedElementDeletionOptions DeletionOptions)
```
Delete any elements from the given list that can be deleted.
@note This list should have been pre-normalized via UTypedElementSelectionSet::GetNormalizedSelection or UTypedElementSelectionSet::GetNormalizedElementList.

### DeleteSelectedElements
```angelscript
bool DeleteSelectedElements(UTypedElementSelectionSet SelectionSet, UWorld World, FTypedElementDeletionOptions DeletionOptions)
```
Delete any elements from the given selection set that can be deleted.
@note Internally this just calls DeleteNormalizedElements on the result of UTypedElementSelectionSet::GetNormalizedSelection.

### DuplicateNormalizedElements
```angelscript
TArray<FScriptTypedElementHandle> DuplicateNormalizedElements(FScriptTypedElementListProxy ElementList, UWorld World, FVector LocationOffset)
```
Duplicate any elements from the given list that can be duplicated.
@note This list should have been pre-normalized via UTypedElementSelectionSet::GetNormalizedSelection or UTypedElementSelectionSet::GetNormalizedElementList.

### DuplicateSelectedElements
```angelscript
TArray<FScriptTypedElementHandle> DuplicateSelectedElements(const UTypedElementSelectionSet SelectionSet, UWorld World, FVector LocationOffset)
```
Duplicate any elements from the given selection set that can be duplicated.
@note Internally this just calls DuplicateNormalizedElements on the result of UTypedElementSelectionSet::GetNormalizedSelection.

### PasteElements
```angelscript
TArray<FScriptTypedElementHandle> PasteElements(UTypedElementSelectionSet SelectionSet, UWorld World, FTypedElementPasteOptions PasteOption)
```
Paste any elements from the clipboard
@note Internally this just calls PasteNormalizedElements on the result of UTypedElementSelectionSet::GetNormalizedSelection.

### PasteNormalizedElements
```angelscript
TArray<FScriptTypedElementHandle> PasteNormalizedElements(FScriptTypedElementListProxy ElementList, UWorld World, FTypedElementPasteOptions PasteOption)
```
Paste any elements from the clipboard
@note This list should have been pre-normalized via UTypedElementSelectionSet::GetNormalizedSelection or UTypedElementSelectionSet::GetNormalizedElementList.

### PasteElementsFromString
```angelscript
TArray<FScriptTypedElementHandle> PasteElementsFromString(UTypedElementSelectionSet SelectionSet, UWorld World, FTypedElementPasteOptions PasteOption, FString InputString)
```
Paste any elements from the given string
@note Internally this just calls PasteNormalizedElements on the result of UTypedElementSelectionSet::GetNormalizedSelection.

### PasteNormalizedElementsFromString
```angelscript
TArray<FScriptTypedElementHandle> PasteNormalizedElementsFromString(FScriptTypedElementListProxy ElementList, UWorld World, FTypedElementPasteOptions PasteOption, FString InputString)
```
Paste any elements from the given string
@note This list should have been pre-normalized via UTypedElementSelectionSet::GetNormalizedSelection or UTypedElementSelectionSet::GetNormalizedElementList.

