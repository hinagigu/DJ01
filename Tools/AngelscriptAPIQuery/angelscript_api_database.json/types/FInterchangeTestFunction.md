# FInterchangeTestFunction

## 属性

### AssetClass
- **类型**: `TSubclassOf<UObject>`
- **描述**: Type of the asset being tested

### OptionalAssetName
- **类型**: `FString`
- **描述**: Optional name of the asset to test, if there are various contenders

### CheckFunction
- **类型**: `UFunction`
- **描述**: A function to be called to determine whether the result is correct

### Parameters
- **类型**: `TMap<FName,FString>`
- **描述**: Parameters and their bound values as text

## 方法

### opAssign
```angelscript
FInterchangeTestFunction& opAssign(FInterchangeTestFunction Other)
```

