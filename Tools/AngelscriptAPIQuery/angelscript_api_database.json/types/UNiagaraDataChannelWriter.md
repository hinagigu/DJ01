# UNiagaraDataChannelWriter

**继承自**: `UObject`

## 方法

### InitWrite
```angelscript
bool InitWrite(FNiagaraDataChannelSearchParameters SearchParams, int Count, bool bVisibleToGame, bool bVisibleToCPU, bool bVisibleToGPU, FString DebugSource)
```
Call before each batch of writes to allocate the data we'll be writing to.

### Num
```angelscript
int Num()
```

### WriteBool
```angelscript
void WriteBool(FName VarName, int Index, bool InData)
```

### WriteEnum
```angelscript
void WriteEnum(FName VarName, int Index, uint8 InData)
```

### WriteFloat
```angelscript
void WriteFloat(FName VarName, int Index, float InData)
```

### WriteID
```angelscript
void WriteID(FName VarName, int Index, FNiagaraID InData)
```

### WriteInt
```angelscript
void WriteInt(FName VarName, int Index, int InData)
```

### WriteLinearColor
```angelscript
void WriteLinearColor(FName VarName, int Index, FLinearColor InData)
```

### WritePosition
```angelscript
void WritePosition(FName VarName, int Index, FVector InData)
```

### WriteQuat
```angelscript
void WriteQuat(FName VarName, int Index, FQuat InData)
```

### WriteSpawnInfo
```angelscript
void WriteSpawnInfo(FName VarName, int Index, FNiagaraSpawnInfo InData)
```

### WriteVector
```angelscript
void WriteVector(FName VarName, int Index, FVector InData)
```

### WriteVector2D
```angelscript
void WriteVector2D(FName VarName, int Index, FVector2D InData)
```

### WriteVector4
```angelscript
void WriteVector4(FName VarName, int Index, FVector4 InData)
```

