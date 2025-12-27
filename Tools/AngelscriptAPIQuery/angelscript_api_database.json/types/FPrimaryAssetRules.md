# FPrimaryAssetRules

Structure defining rules for what to do with assets, this is defined per type and can be overridden per asset

## 属性

### Priority
- **类型**: `int`
- **描述**: Primary Assets with a higher priority will take precedence over lower priorities when assigning management for referenced assets. If priorities match, both will manage the same Secondary Asset.

### ChunkId
- **类型**: `int`
- **描述**: Assets will be put into this Chunk ID specifically, if set to something other than -1. The default Chunk is Chunk 0.

### bApplyRecursively
- **类型**: `bool`
- **描述**: If true, this rule will apply to all referenced Secondary Assets recursively, as long as they are not managed by a higher-priority Primary Asset.

### CookRule
- **类型**: `EPrimaryAssetCookRule`
- **描述**: Rule describing when this asset should be cooked.

## 方法

### opAssign
```angelscript
FPrimaryAssetRules& opAssign(FPrimaryAssetRules Other)
```

