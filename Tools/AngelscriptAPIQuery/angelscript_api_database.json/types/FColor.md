# FColor

Stores a color with 8 bits of precision per channel. (BGRA).
@note The full C++ class is located here: Engine\Source\Runtime\Core\Public\Math\Color.h

## 属性

### DWColor
- **类型**: `uint`

### B
- **类型**: `uint8`

### G
- **类型**: `uint8`

### R
- **类型**: `uint8`

### A
- **类型**: `uint8`

## 方法

### opEquals
```angelscript
bool opEquals(FColor ColorB)
```

### opAddAssign
```angelscript
void opAddAssign(FColor ColorB)
```

### ToHex
```angelscript
FString ToHex()
```

### InitFromString
```angelscript
bool InitFromString(FString SourceString)
```

### FromRGBE
```angelscript
FLinearColor FromRGBE()
```

### ReinterpretAsLinear
```angelscript
FLinearColor ReinterpretAsLinear()
```

### ToString
```angelscript
FString ToString()
```

### opAssign
```angelscript
FColor& opAssign(FColor Other)
```

