# FTopLevelAssetPath

A struct that can reference a top level asset such as '/Path/To/Package.AssetName'
@note The full C++ class is located here: Engine\Source\Runtime\CoreUObject\Public\UObject\TopLevelAssetPath.h

## 属性

### PackageName
- **类型**: `FName`

### AssetName
- **类型**: `FName`

## 方法

### IsValid
```angelscript
bool IsValid()
```

### IsNull
```angelscript
bool IsNull()
```

### Reset
```angelscript
void Reset()
```

### opEquals
```angelscript
bool opEquals(FTopLevelAssetPath Other)
```

### opAssign
```angelscript
FTopLevelAssetPath& opAssign(FString AssetPath)
```

### ToString
```angelscript
FString ToString()
```

### opAssign
```angelscript
FTopLevelAssetPath& opAssign(FTopLevelAssetPath Other)
```

