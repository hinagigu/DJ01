# FUnitTest

## 方法

### Fail
```angelscript
void Fail(FString Message)
```

### AssertTrue
```angelscript
void AssertTrue(bool Expression, FString Message)
```

### AssertFalse
```angelscript
void AssertFalse(bool Expression, FString Message)
```

### AssertNull
```angelscript
void AssertNull(const UObject Object, FString Message)
```

### AssertNotNull
```angelscript
void AssertNotNull(const UObject Object, FString Message)
```

### AssertEquals
```angelscript
void AssertEquals(int Expected, int Actual, FString Message)
```

### AssertEquals
```angelscript
void AssertEquals(float32 Expected, float32 Actual, FString Message)
```

### AssertEquals
```angelscript
void AssertEquals(float Expected, float Actual, FString Message)
```

### AssertEquals
```angelscript
void AssertEquals(bool Expected, bool Actual, FString Message)
```

### AssertEquals
```angelscript
void AssertEquals(FName Expected, FName Actual, FString Message)
```

### AssertEquals
```angelscript
void AssertEquals(FString Expected, FString Actual, FString Message)
```

### AssertEquals
```angelscript
void AssertEquals(FVector Expected, FVector Actual, FString Message)
```

### AssertEquals
```angelscript
void AssertEquals(FRotator Expected, FRotator Actual, FString Message)
```

### AssertEquals
```angelscript
void AssertEquals(FUniqueNetIdRepl Expected, FUniqueNetIdRepl Actual, FString Message)
```

### AssertNotEquals
```angelscript
void AssertNotEquals(int Expected, int Actual, FString Message)
```

### AssertNotEquals
```angelscript
void AssertNotEquals(float32 Expected, float32 Actual, FString Message)
```

### AssertNotEquals
```angelscript
void AssertNotEquals(float Expected, float Actual, FString Message)
```

### AssertNotEquals
```angelscript
void AssertNotEquals(bool Expected, bool Actual, FString Message)
```

### AssertNotEquals
```angelscript
void AssertNotEquals(FName Expected, FName Actual, FString Message)
```

### AssertNotEquals
```angelscript
void AssertNotEquals(FString Expected, FString Actual, FString Message)
```

### AssertNotEquals
```angelscript
void AssertNotEquals(FVector Expected, FVector Actual, FString Message)
```

### AssertNotEquals
```angelscript
void AssertNotEquals(FRotator Expected, FRotator Actual, FString Message)
```

### AssertNotEquals
```angelscript
void AssertNotEquals(FUniqueNetIdRepl Expected, FUniqueNetIdRepl Actual, FString Message)
```

### AssertAlmostEquals
```angelscript
void AssertAlmostEquals(float32 Expected, float32 Actual, float32 AbsError, FString Message)
```

### AssertAlmostEquals
```angelscript
void AssertAlmostEquals(float Expected, float Actual, float AbsError, FString Message)
```

### AssertLessThan
```angelscript
void AssertLessThan(int Left, int Right, FString Message)
```

### AssertLessThan
```angelscript
void AssertLessThan(float32 Left, float32 Right, FString Message)
```

### AssertLessThan
```angelscript
void AssertLessThan(float Left, float Right, FString Message)
```

### AssertGreaterThan
```angelscript
void AssertGreaterThan(int Left, int Right, FString Message)
```

### AssertGreaterThan
```angelscript
void AssertGreaterThan(float32 Left, float32 Right, FString Message)
```

### AssertGreaterThan
```angelscript
void AssertGreaterThan(float Left, float Right, FString Message)
```

### AssertLessThanOrEqual
```angelscript
void AssertLessThanOrEqual(int Left, int Right, FString Message)
```

### AssertLessThanOrEqual
```angelscript
void AssertLessThanOrEqual(float32 Left, float32 Right, FString Message)
```

### AssertLessThanOrEqual
```angelscript
void AssertLessThanOrEqual(float Left, float Right, FString Message)
```

### AssertGreaterThanOrEqual
```angelscript
void AssertGreaterThanOrEqual(int Left, int Right, FString Message)
```

### AssertGreaterThanOrEqual
```angelscript
void AssertGreaterThanOrEqual(float32 Left, float32 Right, FString Message)
```

### AssertGreaterThanOrEqual
```angelscript
void AssertGreaterThanOrEqual(float Left, float Right, FString Message)
```

### AssertSame
```angelscript
void AssertSame(const UObject Expected, const UObject Actual, FString Message)
```

### AssertNotSame
```angelscript
void AssertNotSame(const UObject Expected, const UObject Actual, FString Message)
```

### AdvanceTime
```angelscript
void AdvanceTime(float32 DeltaSecs)
```

### AddExpectedError
```angelscript
void AddExpectedError(FString Regex, int Occurrences)
```

### CallNativeBeginPlayFor
```angelscript
void CallNativeBeginPlayFor(AActor Actor, bool bFromLevelStreaming)
```

### CallNativeBeginPlayFor
```angelscript
void CallNativeBeginPlayFor(UActorComponent ActorComponent)
```

### SetIsServer
```angelscript
void SetIsServer(bool bIsServer)
```

### GetParam
```angelscript
FString GetParam()
```

### ForceGarbageCollectionNow
```angelscript
void ForceGarbageCollectionNow()
```

