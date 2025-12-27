# FGatherTextFromMetaDataConfiguration

## 属性

### IsEnabled
- **类型**: `bool`
- **描述**: If enabled, metadata will be gathered according to this configuration.

### IncludePathWildcards
- **类型**: `TArray<FGatherTextIncludePath>`
- **描述**: Metadata from source files whose paths match these wildcard patterns, specified relative to the project's root, may be processed for gathering.

### ExcludePathWildcards
- **类型**: `TArray<FGatherTextExcludePath>`
- **描述**: Metadata from source files whose paths match these wildcard patterns will be excluded from gathering.

### KeySpecifications
- **类型**: `TArray<FMetaDataKeyGatherSpecification>`
- **描述**: Specifications for how to gather text from specific metadata keys.

### FieldTypesToInclude
- **类型**: `TArray<FString>`
- **描述**: List of field types (eg, Property, Function, ScriptStruct, Enum, etc) that should be included in the gather, or empty to include everything.

### FieldTypesToExclude
- **类型**: `TArray<FString>`
- **描述**: List of field types (eg, Property, Function, ScriptStruct, Enum, etc) the should be excluded from the gather.

### FieldOwnerTypesToInclude
- **类型**: `TArray<FString>`
- **描述**: List of field owner types (eg, MyClass, MyStruct, etc) that should have fields within them included in the gather, or empty to include everything.

### FieldOwnerTypesToExclude
- **类型**: `TArray<FString>`
- **描述**: List of field owner types (eg, MyClass, MyStruct, etc) that should have fields within them excluded from the gather.

### ShouldGatherFromEditorOnlyData
- **类型**: `bool`
- **描述**: If enabled, data that is specified as editor-only may be processed for gathering.

## 方法

### opAssign
```angelscript
FGatherTextFromMetaDataConfiguration& opAssign(FGatherTextFromMetaDataConfiguration Other)
```

