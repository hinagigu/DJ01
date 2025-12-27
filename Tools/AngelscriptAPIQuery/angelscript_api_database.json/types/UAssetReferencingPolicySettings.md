# UAssetReferencingPolicySettings

**继承自**: `UDeveloperSettings`

Settings for the Asset Referencing Policy, these settings are used to determine which plugins and game folders can reference content from each other

## 属性

### EnginePlugins
- **类型**: `FARPDomainSettingsForPlugins`
- **描述**: Settings/rules for engine plugins

### ProjectPlugins
- **类型**: `FARPDomainSettingsForPlugins`
- **描述**: Settings/rules for project plugins

### DefaultProjectContentRule
- **类型**: `FARPDefaultProjectDomainRules`
- **描述**: The default rules for project content (if a more specific rule doesn't apply)

### AdditionalDomains
- **类型**: `TArray<FARPDomainDefinitionByContentRoot>`
- **描述**: List of additional domains to carve out from the project content folder

### bIgnoreEditorOnlyReferences
- **类型**: `bool`
- **描述**: If true, ignore any editor-only domain references that will not affect the cooked game

