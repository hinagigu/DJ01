# FKeyMappingRow

Stores all mappings bound to a single mapping name.

Since a single mapping can have multiple bindings to it and this system should be Blueprint friendly,
this needs to be a struct (blueprint don't support nested containers).

## 属性

### Mappings
- **类型**: `TSet<FPlayerKeyMapping>`

## 方法

### opAssign
```angelscript
FKeyMappingRow& opAssign(FKeyMappingRow Other)
```

