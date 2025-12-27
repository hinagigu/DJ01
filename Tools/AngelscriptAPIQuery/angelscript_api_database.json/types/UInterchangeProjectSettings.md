# UInterchangeProjectSettings

**继承自**: `UDeveloperSettings`

## 属性

### ContentImportSettings
- **类型**: `FInterchangeContentImportSettings`
- **描述**: Settings used when importing into the Content Browser.

### SceneImportSettings
- **类型**: `FInterchangeImportSettings`
- **描述**: Settings used when importing into a level.

### FilePickerClass
- **类型**: `TSoftClassPtr<UInterchangeFilePickerBase>`
- **描述**: This tells Interchange which file picker class to construct when we need to choose a file for a source.

### bStaticMeshUseSmoothEdgesIfSmoothingInformationIsMissing
- **类型**: `bool`
- **描述**: If enabled, both Interchange translators and the legacy import process smooth the edges of static meshes that don't contain smoothing information.
If you have an older project that relies on leaving hard edges by default, you can disable this setting to preserve consistency with older assets.

### GenericPipelineClass
- **类型**: `TSoftClassPtr<UInterchangePipelineBase>`
- **描述**: Specifies which pipeline class Interchange should use when editor tools import or reimport an asset with base settings.
Unreal Editor depends on this class to be set. You can only edit this property in the .ini file.

