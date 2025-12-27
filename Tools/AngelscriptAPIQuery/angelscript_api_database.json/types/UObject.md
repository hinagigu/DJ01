# UObject

Direct base class for all UE objects
@note The full C++ class is located here: Engine\Source\Runtime\CoreUObject\Public\UObject\Object.h

## 方法

### AddToRoot
```angelscript
void AddToRoot()
```

### RemoveFromRoot
```angelscript
void RemoveFromRoot()
```

### GetIsRooted
```angelscript
bool GetIsRooted()
```

### IsTransient
```angelscript
bool IsTransient()
```

### Modify
```angelscript
bool Modify(bool bAlwaysMarkDirty)
```

### SetTransactional
```angelscript
void SetTransactional(bool bTransactional)
```

### IsSupportedForNetworking
```angelscript
bool IsSupportedForNetworking()
```

### GetClass
```angelscript
UClass GetClass()
```

### GetOuter
```angelscript
UObject GetOuter()
```

### GetTypedOuter
```angelscript
UObject GetTypedOuter(TSubclassOf<UObject> Target)
```
Traverses the outer chain searching for the next object of a certain type.
@param Target class to search for.
@return The first object in this object's Outer chain which is of the correct type.


### GetOutermost
```angelscript
UPackage GetOutermost()
```

### GetPackage
```angelscript
UPackage GetPackage()
```

### MarkPackageDirty
```angelscript
bool MarkPackageDirty()
```

### GetWorld
```angelscript
UWorld GetWorld()
```

### GetName
```angelscript
FName GetName()
```

### GetFullName
```angelscript
FString GetFullName(const UObject StopOuter)
```

### GetPathName
```angelscript
FString GetPathName(const UObject StopOuter)
```

### IsA
```angelscript
bool IsA(const UClass Class)
```
Returns true if this object is of the specified type, or a child of that type.

### SaveConfig
```angelscript
void SaveConfig()
```

### LoadConfig
```angelscript
void LoadConfig()
```

### ReloadConfig
```angelscript
void ReloadConfig()
```

### CopyScriptPropertiesFrom
```angelscript
void CopyScriptPropertiesFrom(const UObject OtherObject)
```

### opCast
```angelscript
void opCast(? Address)
```

### ToString
```angelscript
FString ToString()
```

