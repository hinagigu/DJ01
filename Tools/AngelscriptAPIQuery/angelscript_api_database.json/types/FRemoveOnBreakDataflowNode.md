# FRemoveOnBreakDataflowNode

## 属性

### bEnabledRemoval
- **类型**: `bool`
- **描述**: Whether or not to enable the removal on the selection

### PostBreakTimer
- **类型**: `FVector2f`
- **描述**: How long after the break the removal will start ( Min / Max )

### RemovalTimer
- **类型**: `FVector2f`
- **描述**: How long removal will last ( Min / Max )

### bClusterCrumbling
- **类型**: `bool`
- **描述**: If applied to a cluster this will cause the cluster to crumble upon removal, otherwise will have no effect

### bActive
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FRemoveOnBreakDataflowNode& opAssign(FRemoveOnBreakDataflowNode Other)
```

