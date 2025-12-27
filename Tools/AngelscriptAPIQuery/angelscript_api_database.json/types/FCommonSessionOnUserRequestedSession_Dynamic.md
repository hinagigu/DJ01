# FCommonSessionOnUserRequestedSession_Dynamic

## 方法

### opAssign
```angelscript
FCommonSessionOnUserRequestedSession_Dynamic& opAssign(FCommonSessionOnUserRequestedSession_Dynamic Other)
```

### IsBound
```angelscript
bool IsBound()
```

### Clear
```angelscript
void Clear()
```

### AddUFunction
```angelscript
void AddUFunction(const UObject Object, FName FunctionName)
```

### Unbind
```angelscript
void Unbind(UObject Object, FName FunctionName)
```

### UnbindObject
```angelscript
void UnbindObject(UObject Object)
```

### Broadcast
```angelscript
void Broadcast(const FPlatformUserId&in LocalPlatformUserId, UCommonSession_SearchResult RequestedSession, const FOnlineResultInformation&in RequestedSessionResult)
```

