# UInterchangePipelineConfigurationBase

**继承自**: `UObject`

## 方法

### ScriptedShowPipelineConfigurationDialog
```angelscript
EInterchangePipelineConfigurationDialogResult ScriptedShowPipelineConfigurationDialog(TArray<FInterchangeStackInfo>& PipelineStacks, TArray<UInterchangePipelineBase>& OutPipelines, UInterchangeSourceData SourceData, UInterchangeTranslatorBase Translator, UInterchangeBaseNodeContainer BaseNodeContainer)
```
Non-virtual helper that allows Blueprint to implement an event-based function to implement ShowPipelineConfigurationDialog().

### ScriptedShowReimportPipelineConfigurationDialog
```angelscript
EInterchangePipelineConfigurationDialogResult ScriptedShowReimportPipelineConfigurationDialog(TArray<FInterchangeStackInfo>& PipelineStacks, TArray<UInterchangePipelineBase>& OutPipelines, UInterchangeSourceData SourceData, UInterchangeTranslatorBase Translator, UInterchangeBaseNodeContainer BaseNodeContainer, UObject ReimportAsset)
```
Non-virtual helper that allows Blueprint to implement an event-based function to implement ShowReimportPipelineConfigurationDialog().

### ScriptedShowScenePipelineConfigurationDialog
```angelscript
EInterchangePipelineConfigurationDialogResult ScriptedShowScenePipelineConfigurationDialog(TArray<FInterchangeStackInfo>& PipelineStacks, TArray<UInterchangePipelineBase>& OutPipelines, UInterchangeSourceData SourceData, UInterchangeTranslatorBase Translator, UInterchangeBaseNodeContainer BaseNodeContainer)
```
Non-virtual helper that allows Blueprint to implement an event-based function to implement ShowScenePipelineConfigurationDialog().

