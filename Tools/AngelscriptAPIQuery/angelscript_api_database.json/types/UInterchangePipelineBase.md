# UInterchangePipelineBase

**继承自**: `UObject`

## 方法

### DoesPropertyStatesExist
```angelscript
bool DoesPropertyStatesExist(FName PropertyPath)
```
Return true if the property has valid states, or false if no states were set for the property.

### FindOrAddPropertyStates
```angelscript
FInterchangePipelinePropertyStates& FindOrAddPropertyStates(FName PropertyPath)
```
Return a mutable property states reference. Add the property states if it doesn't exist.

### ScriptedExecuteExportPipeline
```angelscript
void ScriptedExecuteExportPipeline(UInterchangeBaseNodeContainer BaseNodeContainer)
```
Non-virtual helper that allows Blueprint to implement an event-based function.
The Interchange manager calls this function, not the virtual one that is called by the default implementation.

### ScriptedExecutePipeline
```angelscript
void ScriptedExecutePipeline(UInterchangeBaseNodeContainer BaseNodeContainer, TArray<UInterchangeSourceData> SourceDatas, FString ContentBasePath)
```
ScriptedExecutePipeline, is call after the translation and before we parse the graph to call the factory.
This is where factory node should be created by the pipeline.
Each factory node represent an unreal asset create that will be create by an interchange factory.
@note - the FTaskPipeline is calling this function not the virtual one that is call by the default implementation.

### ScriptedExecutePostFactoryPipeline
```angelscript
void ScriptedExecutePostFactoryPipeline(const UInterchangeBaseNodeContainer BaseNodeContainer, FString FactoryNodeKey, UObject CreatedAsset, bool bIsAReimport)
```
ScriptedExecutePostFactoryPipeline is called after the factory creates an Unreal asset, but before it calls PostEditChange.
@note - The FTaskPreCompletion task calls this function, not the virtual one that is called by the default implementation.

### ScriptedExecutePostImportPipeline
```angelscript
void ScriptedExecutePostImportPipeline(const UInterchangeBaseNodeContainer BaseNodeContainer, FString FactoryNodeKey, UObject CreatedAsset, bool bIsAReimport)
```
ScriptedExecutePostImportPipeline is called after an asset is completely imported, after PostEditChange has already been called.
This can be useful if you need build data for one asset to finish setting up another asset.
@example - A PhysicsAsset needs skeletal mesh render data to be built properly.
@note - the FTaskPostImport calls this function not the virtual one that is call by the default implementation.

### ScriptedGetPipelineDisplayName
```angelscript
FString ScriptedGetPipelineDisplayName()
```
This function is call when we want to list pipeline in the import dialog. If not override the default behavior of this function will search if
the pipeline have a FString UPROPERTY named "PipelineDisplayName" and return the property value. If there is no FString UPROPERTY call "PipelineDisplayName" it will
return the name of the pipeline asset (UObject::GetName).

When creating a pipeline (c++, python or blueprint) you can simply add a UPROPERTY name "PipelineDisplayName" to your pipeline, you do not need to override the function.
Use the same category has your other options and put it on the top.
The meta tag StandAlonePipelineProperty will hide your PROPERTY if your pipeline is a sub object of another pipeline when showing the import dialog.
The meta tag PipelineInternalEditionData make sure the property will be show only when we edit the pipeline object (hidden when showing the import dialog).


UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Textures", meta = (StandAlonePipelineProperty = "True", PipelineInternalEditionData = "True"))
FString PipelineDisplayName;

### ScriptedSetReimportSourceIndex
```angelscript
void ScriptedSetReimportSourceIndex(UClass ReimportObjectClass, int SourceFileIndex)
```
Non-virtual helper that allows Blueprint to implement an event-based function.
the Interchange framework calls this function, not the virtual one that is called by the default implementation.

