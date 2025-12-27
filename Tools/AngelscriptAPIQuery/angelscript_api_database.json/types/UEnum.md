# UEnum

**继承自**: `UField`

## 方法

### GetNameByIndex
```angelscript
FName GetNameByIndex(int InIndex)
```

### GetIndexByName
```angelscript
int GetIndexByName(FName InName, EGetByNameFlags Flags)
```

### GetNameByValue
```angelscript
FName GetNameByValue(int64 InValue)
```

### GetValueByName
```angelscript
int64 GetValueByName(FName InName, EGetByNameFlags Flags)
```

### GetNameStringByIndex
```angelscript
FString GetNameStringByIndex(int InIndex)
```

### GetIndexByNameString
```angelscript
int GetIndexByNameString(FString SearchString, EGetByNameFlags Flags)
```

### GetNameStringByValue
```angelscript
FString GetNameStringByValue(int64 InValue)
```

### GetValueByNameString
```angelscript
int64 GetValueByNameString(FString SearchString, EGetByNameFlags Flags)
```

### GetDisplayNameTextByIndex
```angelscript
FText GetDisplayNameTextByIndex(int InIndex)
```

### GetDisplayNameTextByValue
```angelscript
FText GetDisplayNameTextByValue(int64 InValue)
```

### GetMaxEnumValue
```angelscript
int64 GetMaxEnumValue()
```

### NumEnums
```angelscript
int NumEnums()
```

### IsValidEnumValue
```angelscript
bool IsValidEnumValue(int64 InValue)
```

### IsValidEnumName
```angelscript
bool IsValidEnumName(FName InName)
```

### ContainsExistingMax
```angelscript
bool ContainsExistingMax()
```

### GenerateEnumPrefix
```angelscript
FString GenerateEnumPrefix()
```

