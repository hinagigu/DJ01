# __EditorFilter

## 方法

### ByActorLabel
```angelscript
TArray<AActor> ByActorLabel(TArray<AActor> TargetArray, FString NameSubString, EEditorScriptingStringMatchType StringMatch, EEditorScriptingFilterType FilterType, bool bIgnoreCase)
```
Filter the array based on the Actor's label (what we see in the editor)
@param       TargetArray             Array of Actor to filter. The array will not change.
@param       NameSubString   The text the Actor's Label.
@param       FilterType              Should include or not the array's item if it respects the condition.
@param       StringMatch             Contains the NameSubString OR matches with the wildcard *? OR exactly the same value.
@param       bIgnoreCase             Determines case sensitivity options for string comparisons.
@return      The filtered list.

### ByActorTag
```angelscript
TArray<AActor> ByActorTag(TArray<AActor> TargetArray, FName Tag, EEditorScriptingFilterType FilterType)
```
Filter the array by Tag the Actor contains
@param       TargetArray             Array of Actor to filter. The array will not change.
@param       Tag                             The exact name of the Tag the actor contains.
@param       FilterType              Should include or not the array's item if it respects the condition.
@return      The filtered list.

### ByClass
```angelscript
TArray<UObject> ByClass(TArray<UObject> TargetArray, TSubclassOf<UObject> ObjectClass, EEditorScriptingFilterType FilterType)
```
Filter the array based on the Object's class.
@param       TargetArray             Array of Object to filter. The array will not change.
@param       ObjectClass             The Class of the object.
@param       FilterType              Should include or not the array's item if it respects the condition.
@return      The filtered list.

### ByIDName
```angelscript
TArray<UObject> ByIDName(TArray<UObject> TargetArray, FString NameSubString, EEditorScriptingStringMatchType StringMatch, EEditorScriptingFilterType FilterType)
```
Filter the array based on the Object's ID name.
@param       TargetArray             Array of Object to filter. The array will not change.
@param       NameSubString   The text the Object's ID name.
@param       FilterType              Should include or not the array's item if it respects the condition.
@param       StringMatch             Contains the NameSubString OR matches with the wildcard *? OR exactly the same value.
@return      The filtered list.

### ByLayer
```angelscript
TArray<AActor> ByLayer(TArray<AActor> TargetArray, FName LayerName, EEditorScriptingFilterType FilterType)
```
Filter the array by Layer the Actor belongs to.
@param       TargetArray             Array of Actor to filter. The array will not change.
@param       LayerName               The exact name of the Layer the actor belongs to.
@param       FilterType              Should include or not the array's item if it respects the condition.
@return      The filtered list.

### ByLevelName
```angelscript
TArray<AActor> ByLevelName(TArray<AActor> TargetArray, FName LevelName, EEditorScriptingFilterType FilterType)
```
Filter the array by Level the Actor belongs to.
@param       TargetArray             Array of Actor to filter. The array will not change.
@param       LevelName               The name of the Level the actor belongs to (same name as in the ContentBrowser).
@param       FilterType              Should include or not the array's item if it respects the condition.
@return      The filtered list.

### BySelection
```angelscript
TArray<AActor> BySelection(TArray<AActor> TargetArray, EEditorScriptingFilterType FilterType)
```
Filter the array based on Object's selection.
@param       TargetArray             Array of Object to filter. The array will not change.
@param       FilterType              Should include or not the array's item if it respects the condition.
@return      The filtered list.

