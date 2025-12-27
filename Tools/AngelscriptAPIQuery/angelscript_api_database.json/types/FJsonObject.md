# FJsonObject

## 方法

### IsValid
```angelscript
bool IsValid()
```

### HasField
```angelscript
bool HasField(FString FieldName)
```

### RemoveField
```angelscript
void RemoveField(FString FieldName)
```

### RemoveAllFields
```angelscript
void RemoveAllFields()
```

### GetStringField
```angelscript
FString GetStringField(FString FieldName)
```

### GetNumberField
```angelscript
float GetNumberField(FString FieldName)
```

### GetBoolField
```angelscript
bool GetBoolField(FString FieldName)
```

### GetObjectField
```angelscript
FJsonObject GetObjectField(FString FieldName)
```

### GetArrayField
```angelscript
FJsonArray GetArrayField(FString FieldName)
```

### SetStringField
```angelscript
void SetStringField(FString FieldName, FString StringValue)
```

### SetNumberField
```angelscript
void SetNumberField(FString FieldName, float Number)
```

### SetBoolField
```angelscript
void SetBoolField(FString FieldName, bool InValue)
```

### SetObjectField
```angelscript
void SetObjectField(FString FieldName, FJsonObject InObject)
```

### SetArrayField
```angelscript
void SetArrayField(FString FieldName, FJsonArray InArray)
```

### TryGetObjectField
```angelscript
bool TryGetObjectField(FString FieldName, FJsonObject& OutObject)
```

### CreateObjectField
```angelscript
FJsonObject CreateObjectField(FString FieldName)
```

### TryGetArrayField
```angelscript
bool TryGetArrayField(FString FieldName, FJsonArray& OutArray)
```

### LoadFromString
```angelscript
bool LoadFromString(FString JsonStr)
```

### SaveToString
```angelscript
FString SaveToString(bool bPrettyPrint)
```

### Iterator
```angelscript
FJsonObjectFieldIterator Iterator()
```

