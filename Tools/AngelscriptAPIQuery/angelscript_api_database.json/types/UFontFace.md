# UFontFace

**继承自**: `UObject`

A font face asset contains the raw payload data for a source TTF/OTF file as used by FreeType.
During cook this asset type generates a ".ufont" file containing the raw payload data (unless loaded "Inline").

## 属性

### SourceFilename
- **类型**: `FString`

### Hinting
- **类型**: `EFontHinting`

### LoadingPolicy
- **类型**: `EFontLoadingPolicy`

### LayoutMethod
- **类型**: `EFontLayoutMethod`

### AscendOverriddenValue
- **类型**: `int`
- **描述**: The typographic ascender of the face, expressed in font units.

### bIsAscendOverridden
- **类型**: `bool`
- **描述**: Activate this option to use the specified ascend value instead of the value from the font.

### DescendOverriddenValue
- **类型**: `int`
- **描述**: The typographic ascender of the face, expressed in font units.

### bIsDescendOverridden
- **类型**: `bool`
- **描述**: Activate this option to use the specified descend value instead of the value from the font.

