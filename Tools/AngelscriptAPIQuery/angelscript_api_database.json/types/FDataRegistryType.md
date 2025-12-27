# FDataRegistryType

Wrapper struct to represent a global data registry, represented as an FName internally and implicitly convertible back and forth.
This exists so the blueprint API can understand it's not a normal FName.

## 属性

### Name
- **类型**: `FName`

## 方法

### opAssign
```angelscript
FDataRegistryType& opAssign(FDataRegistryType Other)
```

