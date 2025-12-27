# UUserGeneratedContentLocalizationSettings

**继承自**: `UObject`

Settings controlling UGC localization.

## 属性

### CulturesToDisable
- **类型**: `TArray<FString>`
- **描述**: List of cultures that should be disabled for UGC localization.
@note You can't disable the native culture for the project.

### bCompileDLCLocalizationDuringCook
- **类型**: `bool`
- **描述**: Should we compile UGC localization (if present) for DLC plugins during cook?

### bValidateDLCLocalizationDuringCook
- **类型**: `bool`
- **描述**: Should we validate UGC localization (if present) for DLC plugins during cook?
@note Validation will happen against a UGC localization descriptor that has had InitializeFromProject called on it.

