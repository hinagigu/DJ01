# UMetasoundParameterPack

**继承自**: `UObject`

Here is the UObject BlueprintType that can be used in c++ and blueprint code. It holds a FMetasoundParamStorage
instance and can pass it along to the audio system's SetObjectParameter function via an AudioProxy.

## 方法

### GetBool
```angelscript
bool GetBool(FName ParameterName, ESetParamResult& Result)
```

### GetFloat
```angelscript
float32 GetFloat(FName ParameterName, ESetParamResult& Result)
```

### GetInt
```angelscript
int GetInt(FName ParameterName, ESetParamResult& Result)
```

### GetString
```angelscript
FString GetString(FName ParameterName, ESetParamResult& Result)
```

### GetTrigger
```angelscript
bool GetTrigger(FName ParameterName, ESetParamResult& Result)
```

### HasBool
```angelscript
bool HasBool(FName ParameterName)
```

### HasFloat
```angelscript
bool HasFloat(FName ParameterName)
```

### HasInt
```angelscript
bool HasInt(FName ParameterName)
```

### HasString
```angelscript
bool HasString(FName ParameterName)
```

### HasTrigger
```angelscript
bool HasTrigger(FName ParameterName)
```

### SetBool
```angelscript
ESetParamResult SetBool(FName ParameterName, bool InValue, bool OnlyIfExists)
```

### SetFloat
```angelscript
ESetParamResult SetFloat(FName ParameterName, float32 InValue, bool OnlyIfExists)
```

### SetInt
```angelscript
ESetParamResult SetInt(FName ParameterName, int InValue, bool OnlyIfExists)
```

### SetString
```angelscript
ESetParamResult SetString(FName ParameterName, FString InValue, bool OnlyIfExists)
```

### SetTrigger
```angelscript
ESetParamResult SetTrigger(FName ParameterName, bool OnlyIfExists)
```

