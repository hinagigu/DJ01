# FOnQuartzMetronomeEventBP

## 方法

### opAssign
```angelscript
FOnQuartzMetronomeEventBP& opAssign(FOnQuartzMetronomeEventBP Other)
```

### IsBound
```angelscript
bool IsBound()
```

### GetUObject
```angelscript
UObject GetUObject()
```

### GetFunctionName
```angelscript
FName GetFunctionName()
```

### Clear
```angelscript
void Clear()
```

### BindUFunction
```angelscript
void BindUFunction(UObject Object, FName FunctionName)
```

### Execute
```angelscript
void Execute(FName ClockName, EQuartzCommandQuantization QuantizationType, int NumBars, int Beat, float32 BeatFraction)
```

### ExecuteIfBound
```angelscript
void ExecuteIfBound(FName ClockName, EQuartzCommandQuantization QuantizationType, int NumBars, int Beat, float32 BeatFraction)
```

