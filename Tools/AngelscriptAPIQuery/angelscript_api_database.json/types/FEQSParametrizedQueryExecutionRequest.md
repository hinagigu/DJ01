# FEQSParametrizedQueryExecutionRequest

## 属性

### QueryTemplate
- **类型**: `UEnvQuery`

### QueryConfig
- **类型**: `TArray<FAIDynamicParam>`

### EQSQueryBlackboardKey
- **类型**: `FBlackboardKeySelector`
- **描述**: blackboard key storing an EQS query template

### RunMode
- **类型**: `EEnvQueryRunMode`
- **描述**: determines which item will be stored (All = only first matching)

### bUseBBKeyForQueryTemplate
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FEQSParametrizedQueryExecutionRequest& opAssign(FEQSParametrizedQueryExecutionRequest Other)
```

