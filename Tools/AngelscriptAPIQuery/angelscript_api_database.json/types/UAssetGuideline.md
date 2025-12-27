# UAssetGuideline

**继承自**: `UAssetUserData`

User data that can be attached to assets to check on load for guidlelines (plugins, project settings, etc).

This class intentionally does not accept FText arguments. The project using your bundled asset would need to have
your localization tables, and we currently do not support text table referencing.

## 属性

### Plugins
- **类型**: `TArray<FString>`
- **描述**: Plugins to check for on load

### ProjectSettings
- **类型**: `TArray<FIniStringValue>`
- **描述**: Project settings to check for on load. Look at your .ini's to populate this.

### GuidelineName
- **类型**: `FName`
- **描述**: Name of this guideline, we will only check once per unique guideline name.

