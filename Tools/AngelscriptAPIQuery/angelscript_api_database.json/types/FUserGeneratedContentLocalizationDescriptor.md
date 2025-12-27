# FUserGeneratedContentLocalizationDescriptor

Minimal descriptor needed to generate a localization target for UGC localization.

## 属性

### NativeCulture
- **类型**: `FString`
- **描述**: The culture that the source text is authored in.
@note You shouldn't change this once you start to localize your text.

### CulturesToGenerate
- **类型**: `TArray<FString>`
- **描述**: The cultures that we should generate localization data for.
@note Will implicitly always contain the native culture during export/compile.

### PoFormat
- **类型**: `EPortableObjectFormat`
- **描述**: What format of PO file should we use?
@note You can adjust this later and we'll attempt to preserve any existing localization data by importing with the old setting prior to export.

## 方法

### opAssign
```angelscript
FUserGeneratedContentLocalizationDescriptor& opAssign(FUserGeneratedContentLocalizationDescriptor Other)
```

