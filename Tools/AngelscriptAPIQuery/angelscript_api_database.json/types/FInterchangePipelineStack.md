# FInterchangePipelineStack

## 属性

### Pipelines
- **类型**: `TArray<FSoftObjectPath>`
- **描述**: The list of pipelines in this stack. The pipelines are executed in fixed order, from top to bottom.

### PerTranslatorPipelines
- **类型**: `TArray<FInterchangeTranslatorPipelines>`
- **描述**: Specifies a different list of pipelines for this stack to use when importing data from specific translators.

## 方法

### opAssign
```angelscript
FInterchangePipelineStack& opAssign(FInterchangePipelineStack Other)
```

