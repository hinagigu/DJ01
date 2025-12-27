# UCommonUISettings

**继承自**: `UObject`

## 属性

### bAutoLoadData
- **类型**: `bool`
- **描述**: Controls if the data referenced is automatically loaded.
If False then game code must call LoadData() on it's own.

### DefaultImageResourceObject
- **类型**: `TSoftObjectPtr<UObject>`
- **描述**: The Default Image Resource, newly created CommonImage Widgets will use this style.

### DefaultThrobberMaterial
- **类型**: `TSoftObjectPtr<UMaterialInterface>`
- **描述**: The Default Throbber Material, newly created CommonLoadGuard Widget will use this style.

### DefaultRichTextDataClass
- **类型**: `TSoftClassPtr<UCommonUIRichTextData>`
- **描述**: The Default Data for rich text to show inline icon and others.

### PlatformTraits
- **类型**: `TArray<FGameplayTag>`
- **描述**: The set of traits defined per-platform (e.g., the default input mode, whether or not you can exit the application, etc...)

