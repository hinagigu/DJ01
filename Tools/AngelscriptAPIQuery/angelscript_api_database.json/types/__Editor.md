# __Editor

## 方法

### AddFunctionGraph
```angelscript
UEdGraph AddFunctionGraph(UBlueprint Blueprint, FString FuncName)
```
Adds a function to the given blueprint

@param Blueprint      The blueprint to add the function to
@param FuncName       Name of the function to add

@return UEdGraph*

### CompileBlueprint
```angelscript
void CompileBlueprint(UBlueprint Blueprint)
```
Compiles the given blueprint.

@param Blueprint      Blueprint to compile

### FindEventGraph
```angelscript
UEdGraph FindEventGraph(UBlueprint Blueprint)
```
Finds the event graph of the given blueprint. Null if it doesn't have one. This will only return
the primary event graph of the blueprint (the graph named "EventGraph").

@param Blueprint              Blueprint to search for the event graph on

@return UEdGraph*             Event graph of the blueprint if it has one, null if it doesn't have one

### FindGraph
```angelscript
UEdGraph FindGraph(UBlueprint Blueprint, FName GraphName)
```
Finds the graph with the given name on the blueprint. Null if it doesn't have one.

@param Blueprint              Blueprint to search
@param GraphName              The name of the graph to search for

@return UEdGraph*             Pointer to the graph with the given name, null if not found

### GeneratedClass
```angelscript
UClass GeneratedClass(UBlueprint BlueprintObj)
```
Gets the class generated when this blueprint is compiled

@param BlueprintObj          The blueprint object
@return UClass*                      The generated class

### GetBlueprintAsset
```angelscript
UBlueprint GetBlueprintAsset(UObject Object)
```
Casts the provided Object to a Blueprint - the root asset type of a blueprint asset. Note
that the blueprint asset itself is editor only and not present in cooked assets.

@param Object                 The object we need to get the UBlueprint from

@return UBlueprint*   The blueprint type of the given object, nullptr if the object is not a blueprint.

### RefreshAllOpenBlueprintEditors
```angelscript
void RefreshAllOpenBlueprintEditors()
```
Refresh any open blueprint editors

### RefreshOpenEditorsForBlueprint
```angelscript
void RefreshOpenEditorsForBlueprint(const UBlueprint BP)
```
Attempt to refresh any open blueprint editors for the given asset

### RemoveFunctionGraph
```angelscript
void RemoveFunctionGraph(UBlueprint Blueprint, FName FuncName)
```
Deletes the function of the given name on this blueprint. Does NOT replace function call sites.

@param Blueprint              The blueprint to remove the function from
@param FuncName               The name of the function to remove

### RemoveGraph
```angelscript
void RemoveGraph(UBlueprint Blueprint, UEdGraph Graph)
```
Removes the given graph from the blueprint if possible

@param Blueprint      The blueprint the graph will be removed from
@param Graph          The graph to remove

### RemoveUnusedNodes
```angelscript
void RemoveUnusedNodes(UBlueprint Blueprint)
```
Remove any nodes in this blueprint that have no connections made to them.

@param Blueprint              The blueprint to remove the nodes from

### RemoveUnusedVariables
```angelscript
int RemoveUnusedVariables(UBlueprint Blueprint)
```
Deletes any unused blueprint created variables the given blueprint.
An Unused variable is any BP variable that is not referenced in any
blueprint graphs

@param Blueprint                      Blueprint that you would like to remove variables from

@return                                       Number of variables removed

### RenameGraph
```angelscript
void RenameGraph(UEdGraph Graph, FString NewNameStr)
```
Attempts to rename the given graph with a new name

@param Graph                  The graph to rename
@param NewNameStr             The new name of the graph

### ReparentBlueprint
```angelscript
void ReparentBlueprint(UBlueprint Blueprint, UClass NewParentClass)
```
Attempts to reparent the given blueprint to the new chosen parent class.

@param Blueprint                      Blueprint that you would like to reparent
@param NewParentClass         The new parent class to use

### ReplaceVariableReferences
```angelscript
void ReplaceVariableReferences(UBlueprint Blueprint, FName OldVarName, FName NewVarName)
```
Replace any references of variables with the OldVarName to references of those with the NewVarName if possible

@param Blueprint              Blueprint to replace the variable references on
@param OldVarName             The variable you want replaced
@param NewVarName             The new variable that will be used in the old one's place

### SetBlueprintVariableExposeOnSpawn
```angelscript
void SetBlueprintVariableExposeOnSpawn(UBlueprint Blueprint, FName VariableName, bool bExposeOnSpawn)
```
Sets "Expose On Spawn" to true/false on a Blueprint variable

@param Blueprint                     The blueprint object
@param VariableName          The variable name
@param bExposeOnSpawn        Set to true to expose on spawn

### SetBlueprintVariableExposeToCinematics
```angelscript
void SetBlueprintVariableExposeToCinematics(UBlueprint Blueprint, FName VariableName, bool bExposeToCinematics)
```
Sets "Expose To Cinematics" to true/false on a Blueprint variable

@param Blueprint                             The blueprint object
@param VariableName                  The variable name
@param bExposeToCinematics   Set to true to expose to cinematics

### SetBlueprintVariableInstanceEditable
```angelscript
void SetBlueprintVariableInstanceEditable(UBlueprint Blueprint, FName VariableName, bool bInstanceEditable)
```
Sets "Instance Editable" to true/false on a Blueprint variable

@param Blueprint                             The blueprint object
@param VariableName                  The variable name
@param bInstanceEditable             Toggle InstanceEditable

### UpgradeOperatorNodes
```angelscript
void UpgradeOperatorNodes(UBlueprint Blueprint)
```
Replace any old operator nodes (float + float, vector + float, int + vector, etc)
with the newer Promotable Operator version of the node. Preserve any connections the
original node had to the newer version of the node.

@param Blueprint      Blueprint to upgrade

### DuplicateSelected
```angelscript
void DuplicateSelected(bool bOffsetLocations)
```

### GetGridSize
```angelscript
float32 GetGridSize()
```
Returns the size (cm) of the current location grid selected in the editor

### IsGridEnabled
```angelscript
bool IsGridEnabled()
```

### IsPlaying
```angelscript
bool IsPlaying()
```

### OpenSettings
```angelscript
void OpenSettings(FName ContainerName, FName CategoryName, FName SectionName)
```

