# FAutoReimportWildcard

A filter used by the auto reimport manager to explicitly include/exclude files matching the specified wildcard

## 属性

### Wildcard
- **类型**: `FString`
- **描述**: The wildcard filter as a string. Files that match this wildcard will be included/excluded according to the bInclude member

### bInclude
- **类型**: `bool`
- **描述**: When true, files that match this wildcard will be included (if it doesn't fail any other filters), when false, matches will be excluded from the reimporter

## 方法

### opAssign
```angelscript
FAutoReimportWildcard& opAssign(FAutoReimportWildcard Other)
```

