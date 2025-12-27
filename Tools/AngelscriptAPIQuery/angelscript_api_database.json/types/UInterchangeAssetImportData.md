# UInterchangeAssetImportData

**继承自**: `UAssetImportData`

## 属性

### SceneImportAsset
- **类型**: `FSoftObjectPath`
- **描述**: On a level import, set to the UInterchangeSceneImportAsset created during the import.

## 方法

### GetNodeContainer
```angelscript
UInterchangeBaseNodeContainer GetNodeContainer()
```

### GetNumberOfPipelines
```angelscript
int GetNumberOfPipelines()
```

### GetPipelines
```angelscript
TArray<UObject> GetPipelines()
```
Returns Array of non-null pipelines

### GetStoredFactoryNode
```angelscript
UInterchangeFactoryBaseNode GetStoredFactoryNode(FString InNodeUniqueId)
```

### GetStoredNode
```angelscript
const UInterchangeBaseNode GetStoredNode(FString InNodeUniqueId)
```

### GetTranslatorSettings
```angelscript
const UInterchangeTranslatorSettings GetTranslatorSettings()
```

### ScriptExtractDisplayLabels
```angelscript
TArray<FString> ScriptExtractDisplayLabels()
```
Extract all the filename labels.

### ScriptExtractFilenames
```angelscript
TArray<FString> ScriptExtractFilenames()
```
Extract all the (resolved) filenames.

### ScriptGetFirstFilename
```angelscript
FString ScriptGetFirstFilename()
```
Return the first filename stored in this data. The resulting filename will be absolute (that is, not relative to the asset).

### SetNodeContainer
```angelscript
void SetNodeContainer(UInterchangeBaseNodeContainer InNodeContainer)
```

### SetPipelines
```angelscript
void SetPipelines(TArray<UObject> InPipelines)
```

### SetTranslatorSettings
```angelscript
void SetTranslatorSettings(UInterchangeTranslatorSettings TranslatorSettings)
```

