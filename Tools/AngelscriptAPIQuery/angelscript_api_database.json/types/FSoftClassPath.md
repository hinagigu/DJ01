# FSoftClassPath

A struct that contains a string reference to a class, can be used to make soft references to classes.
@note The full C++ class is located here: Engine\Source\Runtime\CoreUObject\Public\UObject\SoftObjectPath.h

## 方法

### GetLongPackageName
```angelscript
FString GetLongPackageName()
```

### GetAssetName
```angelscript
FString GetAssetName()
```

### GetAssetPath
```angelscript
FTopLevelAssetPath GetAssetPath()
```

### IsValid
```angelscript
bool IsValid()
```

### IsNull
```angelscript
bool IsNull()
```

### IsAsset
```angelscript
bool IsAsset()
```

### IsSubobject
```angelscript
bool IsSubobject()
```

### ResolveClass
```angelscript
UClass ResolveClass()
```

### TryLoadClass
```angelscript
UClass TryLoadClass()
```

### ToString
```angelscript
FString ToString()
```

### opAssign
```angelscript
FSoftClassPath& opAssign(FSoftClassPath Other)
```

