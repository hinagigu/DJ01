# TSoftClassPtr

## 方法

### ToSoftObjectPath
```angelscript
FSoftObjectPath ToSoftObjectPath()
```

### ToString
```angelscript
FString ToString()
```

### GetLongPackageName
```angelscript
FString GetLongPackageName()
```

### GetAssetName
```angelscript
FString GetAssetName()
```

### IsValid
```angelscript
bool IsValid()
```

### IsPending
```angelscript
bool IsPending()
```

### IsNull
```angelscript
bool IsNull()
```

### Reset
```angelscript
void Reset()
```

### opAssign
```angelscript
TSoftObjectPtr<T>& opAssign(FSoftObjectPath Path)
```

### opAssign
```angelscript
TSoftClassPtr<T>& opAssign(UClass Object)
```

### opAssign
```angelscript
TSoftClassPtr<T>& opAssign(TSoftClassPtr<T> Other)
```

### opAssign
```angelscript
TSoftClassPtr<T>& opAssign(TSubclassOf<T> Other)
```

### opEquals
```angelscript
bool opEquals(TSoftClassPtr<T> Other)
```

### opEquals
```angelscript
bool opEquals(TSubclassOf<T> Other)
```

### opEquals
```angelscript
bool opEquals(UClass Object)
```

### Get
```angelscript
TSubclassOf<T> Get()
```
Returns the class selected at the specified path.
If the class is not loaded, returns nullptr.

### LoadAsync
```angelscript
void LoadAsync(FOnSoftClassLoaded OnLoaded)
```
Asynchronously loads the package that contains the referenced class.
Delegate may be called immediately if class is already loaded.

