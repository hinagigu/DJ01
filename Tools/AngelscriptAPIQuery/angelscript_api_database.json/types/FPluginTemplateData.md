# FPluginTemplateData

* Data for specifying a usable plugin template.
*      -Plugin templates are a folder/file structure that are duplicated and renamed
*       by the plugin creation wizard to easily create new plugins with a standard
*       format.
* See PluginUtils.h for more information.

## 属性

### Path
- **类型**: `FDirectoryPath`

### Label
- **类型**: `FText`

### Description
- **类型**: `FText`

### DefaultSubfolder
- **类型**: `FString`
- **描述**: Optional sub folder that new plugins will be created in.

### DefaultGameFeatureDataClass
- **类型**: `TSubclassOf<UGameFeatureData>`
- **描述**: The default class of game feature data to create for new game feature plugins (if not set, UGameFeatureData will be used)

### DefaultGameFeatureDataName
- **类型**: `FString`
- **描述**: The default name of the created game feature data assets. If empty, will use the plugin name.

### bIsEnabledByDefault
- **类型**: `bool`
- **描述**: If true, the created plugin will be enabled by default without needing to be added to the project file.

## 方法

### opAssign
```angelscript
FPluginTemplateData& opAssign(FPluginTemplateData Other)
```

