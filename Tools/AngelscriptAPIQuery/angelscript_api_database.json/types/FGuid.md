# FGuid

A globally unique identifier (mirrored from Guid.h)

## 属性

### A
- **类型**: `int`

### B
- **类型**: `int`

### C
- **类型**: `int`

### D
- **类型**: `int`

## 方法

### opEquals
```angelscript
bool opEquals(FGuid Other)
```

### opCmp
```angelscript
int opCmp(FGuid Other)
```

### opIndex
```angelscript
uint& opIndex(int Index)
```

### opIndex
```angelscript
uint opIndex(int Index)
```

### Invalidate
```angelscript
void Invalidate()
```

### IsValid
```angelscript
bool IsValid()
```

### ToString
```angelscript
FString ToString()
```

### ToString
```angelscript
FString ToString(EGuidFormats Format)
```

### GetTypeHash
```angelscript
uint GetTypeHash()
```

### opAssign
```angelscript
FGuid& opAssign(FGuid Other)
```

