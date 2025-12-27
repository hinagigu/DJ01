# UPluginMetadataObject

**继承自**: `UObject`

We use this object to display plugin properties using details view.

## 属性

### VersionName
- **类型**: `FString`
- **描述**: Name of the version for this plugin.  This is the front-facing part of the version number.  It doesn't need to match
      the version number numerically, but should be updated when the version number is increased accordingly.

### FriendlyName
- **类型**: `FString`
- **描述**: Friendly name of the plugin

### Description
- **类型**: `FString`
- **描述**: Description of the plugin

### Category
- **类型**: `FString`
- **描述**: The category that this plugin belongs to

### CreatedBy
- **类型**: `FString`
- **描述**: The company or individual who created this plugin.  This is an optional field that may be displayed in the user interface.

### CreatedByURL
- **类型**: `FString`
- **描述**: Hyperlink URL string for the company or individual who created this plugin.  This is optional.

### DocsURL
- **类型**: `FString`
- **描述**: Documentation URL string.

### MarketplaceURL
- **类型**: `FString`
- **描述**: Marketplace URL string.

### SupportURL
- **类型**: `FString`
- **描述**: Support URL/email for this plugin. Email addresses must be prefixed with 'mailto:'

### EditorCustomVirtualPath
- **类型**: `FString`
- **描述**: Optional custom virtual path to display in editor to better organize. Inserted just before this plugin's directory in the path: /All/Plugins/EditorCustomVirtualPath/PluginName

### bCanContainContent
- **类型**: `bool`
- **描述**: Can this plugin contain content?

### bIsBetaVersion
- **类型**: `bool`
- **描述**: Marks the plugin as beta in the UI

### bIsSealed
- **类型**: `bool`
- **描述**: If true, prevents other plugins from depending on this plugin

### bNoCode
- **类型**: `bool`

### Plugins
- **类型**: `TArray<FPluginReferenceMetadata>`
- **描述**: Plugins used by this plugin

### DisallowedPlugins
- **类型**: `TArray<FPluginDisallowedMetadata>`
- **描述**: Plugins that cannot be used by this plugin

