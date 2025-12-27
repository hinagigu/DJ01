# FLocalizationExportingSettings

## 属性

### CollapseMode
- **类型**: `ELocalizedTextCollapseMode`
- **描述**: How should we collapse down text when exporting to PO?

### POFormat
- **类型**: `EPortableObjectFormat`
- **描述**: Which format of PO file should we use?

### ShouldPersistCommentsOnExport
- **类型**: `bool`
- **描述**: Should user comments in existing PO files be persisted after export? Useful if using a third party service that stores editor/translator notes in the PO format's comment fields.

### ShouldAddSourceLocationsAsComments
- **类型**: `bool`
- **描述**: Should source locations be added to PO file entries as comments? Useful if a third party service doesn't expose PO file reference comments, which typically store the source location.

## 方法

### opAssign
```angelscript
FLocalizationExportingSettings& opAssign(FLocalizationExportingSettings Other)
```

