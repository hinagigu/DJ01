# __MaterialEditing

## 方法

### ClearAllMaterialInstanceParameters
```angelscript
void ClearAllMaterialInstanceParameters(UMaterialInstanceConstant Instance)
```
Clears all material parameters set by this Material Instance

### ConnectMaterialExpressions
```angelscript
bool ConnectMaterialExpressions(UMaterialExpression FromExpression, FString FromOutputName, UMaterialExpression ToExpression, FString ToInputName)
```
Create connection between two material expressions
@param  FromExpression          Expression to make connection from
@param  FromOutputName          Name of output of FromExpression to make connection from. Leave empty to use first output.
@param  ToExpression            Expression to make connection to
@param  ToInputName                     Name of input of ToExpression to make connection to. Leave empty to use first input.

### ConnectMaterialProperty
```angelscript
bool ConnectMaterialProperty(UMaterialExpression FromExpression, FString FromOutputName, EMaterialProperty Property)
```
Connect a material expression output to one of the material property inputs (e.g. diffuse color, opacity etc)
@param  FromExpression          Expression to make connection from
@param  FromOutputName          Name of output of FromExpression to make connection from
@param  Property                        Property input on material to make connection to

### CreateMaterialExpression
```angelscript
UMaterialExpression CreateMaterialExpression(UMaterial Material, TSubclassOf<UMaterialExpression> ExpressionClass, int NodePosX, int NodePosY)
```
Create a new material expression node within the supplied material
@param  Material                        Material asset to add an expression to
@param  ExpressionClass         Class of expression to add
@param  NodePosX                        X position of new expression node
@param  NodePosY                        Y position of new expression node

### CreateMaterialExpressionInFunction
```angelscript
UMaterialExpression CreateMaterialExpressionInFunction(UMaterialFunction MaterialFunction, TSubclassOf<UMaterialExpression> ExpressionClass, int NodePosX, int NodePosY)
```
Create a new material expression node within the supplied material function
@param  MaterialFunction        Material function asset to add an expression to
@param  ExpressionClass         Class of expression to add
@param  NodePosX                        X position of new expression node
@param  NodePosY                        Y position of new expression node

### DeleteAllMaterialExpressions
```angelscript
void DeleteAllMaterialExpressions(UMaterial Material)
```
Delete all material expressions in the supplied material

### DeleteAllMaterialExpressionsInFunction
```angelscript
void DeleteAllMaterialExpressionsInFunction(UMaterialFunction MaterialFunction)
```
Delete all material expressions in the supplied material function

### DeleteMaterialExpression
```angelscript
void DeleteMaterialExpression(UMaterial Material, UMaterialExpression Expression)
```
Delete a specific expression from a material. Will disconnect from other expressions.

### DeleteMaterialExpressionInFunction
```angelscript
void DeleteMaterialExpressionInFunction(UMaterialFunction MaterialFunction, UMaterialExpression Expression)
```
Delete a specific expression from a material function. Will disconnect from other expressions.

### DuplicateMaterialExpression
```angelscript
UMaterialExpression DuplicateMaterialExpression(UMaterial Material, UMaterialFunction MaterialFunction, UMaterialExpression Expression)
```
Duplicates the provided material expression adding it to the same material / material function, and copying parameters.
Note: Does not duplicate transient properties (Ex: GraphNode).

@param  Material                        Material asset to add an expression to
@param  MaterialFunction        Specified if adding an expression to a MaterialFunction, used as Outer for new expression object
@param  SourceExpression        Expression to be duplicated

### GetChildInstances
```angelscript
void GetChildInstances(UMaterialInterface Parent, TArray<FAssetData>& ChildInstances)
```
Gets all direct child mat instances

### GetInputNodeOutputNameForMaterialExpression
```angelscript
bool GetInputNodeOutputNameForMaterialExpression(UMaterialExpression MaterialExpression, UMaterialExpression InputNode, FString& OutputName)
```
Get the output name of input node connected to MaterialExpression from an active material editor

### GetInputsForMaterialExpression
```angelscript
TArray<UMaterialExpression> GetInputsForMaterialExpression(UMaterial Material, UMaterialExpression MaterialExpression)
```
Get the set of nodes acting as inputs to a node from an active material editor

### GetMaterialDefaultScalarParameterValue
```angelscript
float32 GetMaterialDefaultScalarParameterValue(UMaterial Material, FName ParameterName)
```
Get the default scalar (float) parameter value from a Material

### GetMaterialDefaultStaticSwitchParameterValue
```angelscript
bool GetMaterialDefaultStaticSwitchParameterValue(UMaterial Material, FName ParameterName)
```
Get the default static switch parameter value from a Material

### GetMaterialDefaultTextureParameterValue
```angelscript
UTexture GetMaterialDefaultTextureParameterValue(UMaterial Material, FName ParameterName)
```
Get the default texture parameter value from a Material

### GetMaterialDefaultVectorParameterValue
```angelscript
FLinearColor GetMaterialDefaultVectorParameterValue(UMaterial Material, FName ParameterName)
```
Get the default vector parameter value from a Material

### GetMaterialExpressionInputNames
```angelscript
TArray<FString> GetMaterialExpressionInputNames(UMaterialExpression MaterialExpression)
```
Get the array of input pin names for a material expression

### GetMaterialExpressionInputTypes
```angelscript
TArray<int> GetMaterialExpressionInputTypes(UMaterialExpression MaterialExpression)
```
Get the array of input pin types for a material expression

### GetMaterialExpressionNodePosition
```angelscript
void GetMaterialExpressionNodePosition(UMaterialExpression MaterialExpression, int& NodePosX, int& NodePosY)
```
Get the position of the MaterialExpression node.

### GetMaterialInstanceRuntimeVirtualTextureParameterValue
```angelscript
URuntimeVirtualTexture GetMaterialInstanceRuntimeVirtualTextureParameterValue(UMaterialInstanceConstant Instance, FName ParameterName, EMaterialParameterAssociation Association)
```
Get the current texture parameter value from a Material Instance

### GetMaterialInstanceScalarParameterValue
```angelscript
float32 GetMaterialInstanceScalarParameterValue(UMaterialInstanceConstant Instance, FName ParameterName, EMaterialParameterAssociation Association)
```
Get the current scalar (float) parameter value from a Material Instance

### GetMaterialInstanceSparseVolumeTextureParameterValue
```angelscript
USparseVolumeTexture GetMaterialInstanceSparseVolumeTextureParameterValue(UMaterialInstanceConstant Instance, FName ParameterName, EMaterialParameterAssociation Association)
```
Get the current texture parameter value from a Material Instance

### GetMaterialInstanceStaticSwitchParameterValue
```angelscript
bool GetMaterialInstanceStaticSwitchParameterValue(UMaterialInstanceConstant Instance, FName ParameterName, EMaterialParameterAssociation Association)
```
Get the current static switch parameter value from a Material Instance

### GetMaterialInstanceTextureParameterValue
```angelscript
UTexture GetMaterialInstanceTextureParameterValue(UMaterialInstanceConstant Instance, FName ParameterName, EMaterialParameterAssociation Association)
```
Get the current texture parameter value from a Material Instance

### GetMaterialInstanceVectorParameterValue
```angelscript
FLinearColor GetMaterialInstanceVectorParameterValue(UMaterialInstanceConstant Instance, FName ParameterName, EMaterialParameterAssociation Association)
```
Get the current vector parameter value from a Material Instance

### GetMaterialPropertyInputNode
```angelscript
UMaterialExpression GetMaterialPropertyInputNode(UMaterial Material, EMaterialProperty Property)
```
Get the node providing the output for a given material property from an active material editor

### GetMaterialPropertyInputNodeOutputName
```angelscript
FString GetMaterialPropertyInputNodeOutputName(UMaterial Material, EMaterialProperty Property)
```
Get the node output name providing the output for a given material property from an active material editor

### GetMaterialSelectedNodes
```angelscript
TSet<UObject> GetMaterialSelectedNodes(UMaterial Material)
```
Get the set of selected nodes from an active material editor

### GetNaniteOverrideMaterial
```angelscript
UMaterialInterface GetNaniteOverrideMaterial(UMaterialInterface Material)
```
Returns any nanite override material for the given material

### GetNumMaterialExpressions
```angelscript
int GetNumMaterialExpressions(const UMaterial Material)
```
Returns number of material expressions in the supplied material

### GetNumMaterialExpressionsInFunction
```angelscript
int GetNumMaterialExpressionsInFunction(const UMaterialFunction MaterialFunction)
```
Returns number of material expressions in the supplied material

### GetScalarParameterNames
```angelscript
void GetScalarParameterNames(UMaterialInterface Material, TArray<FName>& ParameterNames)
```
Gets all scalar parameter names

### GetScalarParameterSource
```angelscript
bool GetScalarParameterSource(UMaterialInterface Material, FName ParameterName, FSoftObjectPath& ParameterSource)
```
Returns the path of the asset where the parameter originated, as well as true/false if it was found
@param  Material        The material or material instance you want to look up a parameter from
@param  ParameterName           The parameter name
@param  ParameterSource         The soft object path of the asset the parameter originates in
@return Whether or not the parameter was found in this material

### GetStaticSwitchParameterNames
```angelscript
void GetStaticSwitchParameterNames(UMaterialInterface Material, TArray<FName>& ParameterNames)
```
Gets all static switch parameter names

### GetStaticSwitchParameterSource
```angelscript
bool GetStaticSwitchParameterSource(UMaterialInterface Material, FName ParameterName, FSoftObjectPath& ParameterSource)
```
Returns the path of the asset where the parameter originated, as well as true/false if it was found
@param  Material        The material or material instance you want to look up a parameter from
@param  ParameterName           The parameter name
@param  ParameterSource         The soft object path of the asset the parameter originates in
@return Whether or not the parameter was found in this material

### GetStatistics
```angelscript
FMaterialStatistics GetStatistics(UMaterialInterface Material)
```
Returns statistics about the given material

### GetTextureParameterNames
```angelscript
void GetTextureParameterNames(UMaterialInterface Material, TArray<FName>& ParameterNames)
```
Gets all texture parameter names

### GetTextureParameterSource
```angelscript
bool GetTextureParameterSource(UMaterialInterface Material, FName ParameterName, FSoftObjectPath& ParameterSource)
```
Returns the path of the asset where the parameter originated, as well as true/false if it was found
@param  Material        The material or material instance you want to look up a parameter from
@param  ParameterName           The parameter name
@param  ParameterSource         The soft object path of the asset the parameter originates in
@return Whether or not the parameter was found in this material

### GetUsedTextures
```angelscript
TArray<UTexture> GetUsedTextures(UMaterial Material)
```
Get the list of textures used by a material

### GetVectorParameterNames
```angelscript
void GetVectorParameterNames(UMaterialInterface Material, TArray<FName>& ParameterNames)
```
Gets all vector parameter names

### GetVectorParameterSource
```angelscript
bool GetVectorParameterSource(UMaterialInterface Material, FName ParameterName, FSoftObjectPath& ParameterSource)
```
Returns the path of the asset where the parameter originated, as well as true/false if it was found
@param  Material        The material or material instance you want to look up a parameter from
@param  ParameterName           The parameter name
@param  ParameterSource         The soft object path of the asset the parameter originates in
@return Whether or not the parameter was found in this material

### HasMaterialUsage
```angelscript
bool HasMaterialUsage(UMaterial Material, EMaterialUsage Usage)
```
Check if a particular usage is enabled for the supplied material (e.g. SkeletalMesh, ParticleSprite etc)
@param  Material                        Material to check usage for
@param  Usage                           Usage type to check for this material

### LayoutMaterialExpressions
```angelscript
void LayoutMaterialExpressions(UMaterial Material)
```
Layouts the expressions in a grid pattern

### LayoutMaterialFunctionExpressions
```angelscript
void LayoutMaterialFunctionExpressions(UMaterialFunction MaterialFunction)
```
Layouts the expressions in a grid pattern

### RecompileMaterial
```angelscript
void RecompileMaterial(UMaterial Material)
```
Trigger a recompile of a material. Must be performed after making changes to the graph to have changes reflected.

### SetMaterialInstanceParent
```angelscript
void SetMaterialInstanceParent(UMaterialInstanceConstant Instance, UMaterialInterface NewParent)
```
Set the parent Material or Material Instance to use for this Material Instance

### SetMaterialInstanceRuntimeVirtualTextureParameterValue
```angelscript
bool SetMaterialInstanceRuntimeVirtualTextureParameterValue(UMaterialInstanceConstant Instance, FName ParameterName, URuntimeVirtualTexture Value, EMaterialParameterAssociation Association)
```
Set the texture parameter value for a Material Instance

### SetMaterialInstanceScalarParameterValue
```angelscript
bool SetMaterialInstanceScalarParameterValue(UMaterialInstanceConstant Instance, FName ParameterName, float32 Value, EMaterialParameterAssociation Association)
```
Set the scalar (float) parameter value for a Material Instance

### SetMaterialInstanceSparseVolumeTextureParameterValue
```angelscript
bool SetMaterialInstanceSparseVolumeTextureParameterValue(UMaterialInstanceConstant Instance, FName ParameterName, USparseVolumeTexture Value, EMaterialParameterAssociation Association)
```
Set the texture parameter value for a Material Instance

### SetMaterialInstanceStaticSwitchParameterValue
```angelscript
bool SetMaterialInstanceStaticSwitchParameterValue(UMaterialInstanceConstant Instance, FName ParameterName, bool Value, EMaterialParameterAssociation Association)
```
Set the static switch parameter value for a Material Instance

### SetMaterialInstanceTextureParameterValue
```angelscript
bool SetMaterialInstanceTextureParameterValue(UMaterialInstanceConstant Instance, FName ParameterName, UTexture Value, EMaterialParameterAssociation Association)
```
Set the texture parameter value for a Material Instance

### SetMaterialInstanceVectorParameterValue
```angelscript
bool SetMaterialInstanceVectorParameterValue(UMaterialInstanceConstant Instance, FName ParameterName, FLinearColor Value, EMaterialParameterAssociation Association)
```
Set the vector parameter value for a Material Instance

### SetMaterialUsage
```angelscript
bool SetMaterialUsage(UMaterial Material, EMaterialUsage Usage, bool& bNeedsRecompile)
```
Enable a particular usage for the supplied material (e.g. SkeletalMesh, ParticleSprite etc)
@param  Material                        Material to change usage for
@param  Usage                           New usage type to enable for this material
@param  bNeedsRecompile         Returned to indicate if material needs recompiling after this change

### UpdateMaterialFunction
```angelscript
void UpdateMaterialFunction(UMaterialFunctionInterface MaterialFunction, UMaterial PreviewMaterial)
```
Update a Material Function after edits have been made.
Will recompile any Materials that use the supplied Material Function.

### UpdateMaterialInstance
```angelscript
void UpdateMaterialInstance(UMaterialInstanceConstant Instance)
```
Called after making modifications to a Material Instance to recompile shaders etc.

