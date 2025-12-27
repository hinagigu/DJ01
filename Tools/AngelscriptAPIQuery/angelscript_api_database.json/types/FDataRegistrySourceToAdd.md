# FDataRegistrySourceToAdd

Defines which source assets to add and conditions for adding

## 属性

### RegistryToAddTo
- **类型**: `FName`
- **描述**: Name of the registry to add to

### AssetPriority
- **类型**: `int`
- **描述**: Priority to use when adding to the registry.  Higher priorities are searched first

### DataTableToAdd
- **类型**: `TSoftObjectPtr<UDataTable>`
- **描述**: Link to the data table to add to the registry

### CurveTableToAdd
- **类型**: `TSoftObjectPtr<UCurveTable>`
- **描述**: Link to the curve table to add to the registry

### bClientSource
- **类型**: `bool`

### bServerSource
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FDataRegistrySourceToAdd& opAssign(FDataRegistrySourceToAdd Other)
```

