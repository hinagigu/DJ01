# FGatherTextFromPackagesConfiguration

## 属性

### IsEnabled
- **类型**: `bool`
- **描述**: If enabled, text from packages will be gathered according to this configuration.

### IncludePathWildcards
- **类型**: `TArray<FGatherTextIncludePath>`
- **描述**: Packages whose paths match these wildcard patterns, specified relative to the project's root, may be processed for gathering.

### ExcludePathWildcards
- **类型**: `TArray<FGatherTextExcludePath>`
- **描述**: Packages whose paths match these wildcard patterns will be excluded from gathering.

### FileExtensions
- **类型**: `TArray<FGatherTextFileExtension>`
- **描述**: Packages whose names match these wildcard patterns may be processed for text to gather.

### Collections
- **类型**: `TArray<FName>`
- **描述**: Packages in these collections may be processed for gathering.

### ExcludeClasses
- **类型**: `TArray<FSoftClassPath>`
- **描述**: Classes that should be excluded from gathering.

### ShouldExcludeDerivedClasses
- **类型**: `bool`
- **描述**: Should classes derived from those in the exclude classes list also be excluded from gathering?

### ShouldGatherFromEditorOnlyData
- **类型**: `bool`
- **描述**: If enabled, data that is specified as editor-only may be processed for gathering.

### SkipGatherCache
- **类型**: `bool`
- **描述**: Should we ignore the cached text in the package header and perform a full package load instead?

## 方法

### opAssign
```angelscript
FGatherTextFromPackagesConfiguration& opAssign(FGatherTextFromPackagesConfiguration Other)
```

