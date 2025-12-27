# FDataRegistrySource_DataTableRules

Rules struct for data table access

## 属性

### bPrecacheTable
- **类型**: `bool`
- **描述**: True if the entire table should be loaded into memory when the source is loaded, false if the table is loaded on demand

### CachedTableKeepSeconds
- **类型**: `float32`
- **描述**: Time in seconds to keep cached table alive if hard reference is off. 0 will release immediately, -1 will never release

## 方法

### opAssign
```angelscript
FDataRegistrySource_DataTableRules& opAssign(FDataRegistrySource_DataTableRules Other)
```

