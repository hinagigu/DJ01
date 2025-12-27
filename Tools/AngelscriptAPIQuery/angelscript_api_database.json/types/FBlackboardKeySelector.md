# FBlackboardKeySelector

helper struct for defining types of allowed blackboard entries
(e.g. only entries holding points and objects derived form actor class)

## 属性

### AllowedTypes
- **类型**: `TArray<TObjectPtr<UBlackboardKeyType>>`

### SelectedKeyName
- **类型**: `FName`

### SelectedKeyType
- **类型**: `TSubclassOf<UBlackboardKeyType>`

### SelectedKeyID
- **类型**: `int`

### bNoneIsAllowedValue
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FBlackboardKeySelector& opAssign(FBlackboardKeySelector Other)
```

