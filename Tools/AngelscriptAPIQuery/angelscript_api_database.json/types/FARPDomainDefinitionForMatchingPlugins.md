# FARPDomainDefinitionForMatchingPlugins

## 属性

### DisplayName
- **类型**: `FText`
- **描述**: The display name of this rule (used in error message when attempting to reference content incorrectly)
The token {0} will be replaced with the plugin name

### ErrorMessageIfUsedElsewhere
- **类型**: `FText`
- **描述**: The error message if something that is not allowed to attempts to reference content from this domain

### MatchRule
- **类型**: `EARPPluginMatchMode`
- **描述**: Type of matching for this rule

### PluginPathPrefix
- **类型**: `FString`
- **描述**: If set, a plugin with the same rooted directory path will match this rule
(use "/FirstFolder/SecondFolder/" to match a plugin like $YourProjectDir/Plugins/FirstFolder/SecondFolder/MyCoolPlugin/MyCoolPlugin.uplugin)

### PluginCategoryPrefix
- **类型**: `FString`
- **描述**: If set, a plugin with a matching Category will match this rule

### CanReferenceTheseDomains
- **类型**: `TArray<FString>`
- **描述**: The list of additional domains always visible from a plugin
(EngineContent is always visible, as is content from other plugins that are explicitly referenced)

## 方法

### opAssign
```angelscript
FARPDomainDefinitionForMatchingPlugins& opAssign(FARPDomainDefinitionForMatchingPlugins Other)
```

