# TSoftObjectPtr

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
TSoftObjectPtr<T>& opAssign(T Object)
```

### opAssign
```angelscript
TSoftObjectPtr<T>& opAssign(TSoftObjectPtr<T> Other)
```

### opEquals
```angelscript
bool opEquals(TSoftObjectPtr<T> Other)
```

### opEquals
```angelscript
bool opEquals(T Object)
```

### Get
```angelscript
T Get()
```
Returns the object selected at the specified path.
If the object is not loaded, returns nullptr.

### LoadAsync
```angelscript
void LoadAsync(FOnSoftObjectLoaded OnLoaded)
```
Asynchronously loads the package that contains the referenced object.
Delegate may be called immediately if object is already loaded.

