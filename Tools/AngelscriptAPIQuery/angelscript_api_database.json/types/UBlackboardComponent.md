# UBlackboardComponent

**继承自**: `UActorComponent`

## 属性

### DefaultBlackboardAsset
- **类型**: `UBlackboardData`
- **描述**: data asset defining entries. Will be used as part of InitializeComponent
    call provided BlackboardAsset hasn't been already set (via a InitializeBlackboard
    call).

## 方法

### ClearValue
```angelscript
void ClearValue(FName KeyName)
```

### GetLocationFromEntry
```angelscript
bool GetLocationFromEntry(FName KeyName, FVector& ResultLocation)
```
return false if call failed (most probably no such entry in BB)

### GetRotationFromEntry
```angelscript
bool GetRotationFromEntry(FName KeyName, FRotator& ResultRotation)
```
return false if call failed (most probably no such entry in BB)

### GetValueAsBool
```angelscript
bool GetValueAsBool(FName KeyName)
```

### GetValueAsClass
```angelscript
UClass GetValueAsClass(FName KeyName)
```

### GetValueAsEnum
```angelscript
uint8 GetValueAsEnum(FName KeyName)
```

### GetValueAsFloat
```angelscript
float32 GetValueAsFloat(FName KeyName)
```

### GetValueAsInt
```angelscript
int GetValueAsInt(FName KeyName)
```

### GetValueAsName
```angelscript
FName GetValueAsName(FName KeyName)
```

### GetValueAsObject
```angelscript
UObject GetValueAsObject(FName KeyName)
```

### GetValueAsRotator
```angelscript
FRotator GetValueAsRotator(FName KeyName)
```

### GetValueAsString
```angelscript
FString GetValueAsString(FName KeyName)
```

### GetValueAsVector
```angelscript
FVector GetValueAsVector(FName KeyName)
```

### IsVectorValueSet
```angelscript
bool IsVectorValueSet(FName KeyName)
```
If the vector value has been set (and not cleared), this function returns true (indicating that the value should be valid).  If it's not set, the vector value is invalid and this function will return false.  (Also returns false if the key specified does not hold a vector.)

### SetValueAsBool
```angelscript
void SetValueAsBool(FName KeyName, bool BoolValue)
```

### SetValueAsClass
```angelscript
void SetValueAsClass(FName KeyName, UClass ClassValue)
```

### SetValueAsEnum
```angelscript
void SetValueAsEnum(FName KeyName, uint8 EnumValue)
```

### SetValueAsFloat
```angelscript
void SetValueAsFloat(FName KeyName, float32 FloatValue)
```

### SetValueAsInt
```angelscript
void SetValueAsInt(FName KeyName, int IntValue)
```

### SetValueAsName
```angelscript
void SetValueAsName(FName KeyName, FName NameValue)
```

### SetValueAsObject
```angelscript
void SetValueAsObject(FName KeyName, UObject ObjectValue)
```

### SetValueAsRotator
```angelscript
void SetValueAsRotator(FName KeyName, FRotator VectorValue)
```

### SetValueAsString
```angelscript
void SetValueAsString(FName KeyName, FString StringValue)
```

### SetValueAsVector
```angelscript
void SetValueAsVector(FName KeyName, FVector VectorValue)
```

