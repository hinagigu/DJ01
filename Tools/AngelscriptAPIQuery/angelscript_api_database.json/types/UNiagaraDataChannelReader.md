# UNiagaraDataChannelReader

**继承自**: `UObject`

Initial simple API for reading and writing data in a data channel from game code / BP.
Likely to be replaced in the near future with a custom BP node and a helper struct.

## 方法

### InitAccess
```angelscript
bool InitAccess(FNiagaraDataChannelSearchParameters SearchParams, bool bReadPrevFrameData)
```
Call before each access to the data channel to grab the correct data to read.

### Num
```angelscript
int Num()
```

### ReadBool
```angelscript
bool ReadBool(FName VarName, int Index, bool& IsValid)
```

### ReadEnum
```angelscript
uint8 ReadEnum(FName VarName, int Index, bool& IsValid)
```

### ReadFloat
```angelscript
float ReadFloat(FName VarName, int Index, bool& IsValid)
```

### ReadID
```angelscript
FNiagaraID ReadID(FName VarName, int Index, bool& IsValid)
```

### ReadInt
```angelscript
int ReadInt(FName VarName, int Index, bool& IsValid)
```

### ReadLinearColor
```angelscript
FLinearColor ReadLinearColor(FName VarName, int Index, bool& IsValid)
```

### ReadPosition
```angelscript
FVector ReadPosition(FName VarName, int Index, bool& IsValid)
```

### ReadQuat
```angelscript
FQuat ReadQuat(FName VarName, int Index, bool& IsValid)
```

### ReadSpawnInfo
```angelscript
FNiagaraSpawnInfo ReadSpawnInfo(FName VarName, int Index, bool& IsValid)
```

### ReadVector
```angelscript
FVector ReadVector(FName VarName, int Index, bool& IsValid)
```

### ReadVector2D
```angelscript
FVector2D ReadVector2D(FName VarName, int Index, bool& IsValid)
```

### ReadVector4
```angelscript
FVector4 ReadVector4(FName VarName, int Index, bool& IsValid)
```

