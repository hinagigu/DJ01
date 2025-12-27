# FLocalizationCompilationSettings

## 属性

### SkipSourceCheck
- **类型**: `bool`
- **描述**: Should we skip the source check when compiling translations? This will allow translations whose source no longer matches the active source to still be used by the game at runtime.

### ValidateFormatPatterns
- **类型**: `bool`
- **描述**: Should we validate that format patterns are valid for the culture being compiled (eg, detect invalid plural rules or broken syntax).

### ValidateSafeWhitespace
- **类型**: `bool`
- **描述**: Should we validate that text doesn't contain any unsafe whitespace (leading or trailing whitespace) that could get lost during the translation process.

## 方法

### opAssign
```angelscript
FLocalizationCompilationSettings& opAssign(FLocalizationCompilationSettings Other)
```

