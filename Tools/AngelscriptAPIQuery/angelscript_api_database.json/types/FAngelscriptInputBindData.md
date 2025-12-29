# FAngelscriptInputBindData

It's a shame we have to wrap. But it's not a hot path, and it's better than doing an engine mod. Best would of course be if AS type binds were made aware to UHT so binding worked here.

## 属性

### ConfirmTargetCommand
- **类型**: `FName`

### CancelTargetCommand
- **类型**: `FName`

### EnumName
- **类型**: `FTopLevelAssetPath`

### ConfirmTargetInputID
- **类型**: `int`

### CancelTargetInputID
- **类型**: `int`

## 方法

### opAssign
```angelscript
FAngelscriptInputBindData& opAssign(FAngelscriptInputBindData Other)
```

