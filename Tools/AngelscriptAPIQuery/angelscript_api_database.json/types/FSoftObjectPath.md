# FSoftObjectPath

A struct that contains a string reference to an object, either a top level asset or a subobject.
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

### opEquals
```angelscript
bool opEquals(FSoftObjectPath Other)
```

### TryLoad
```angelscript
UObject TryLoad()
```

### ResolveObject
```angelscript
UObject ResolveObject()
```

### ToString
```angelscript
FString ToString()
```

### opAssign
```angelscript
FSoftObjectPath& opAssign(FSoftObjectPath Other)
```

