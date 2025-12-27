# FCollectionTransformSelectionRandomDataflowNode

Selects bones randomly in the Collection

## 属性

### bDeterministic
- **类型**: `bool`
- **描述**: If true, it always generates the same result for the same RandomSeed

### RandomSeed
- **类型**: `float32`
- **描述**: Seed for the random generation, only used if Deterministic is on

### RandomThreshold
- **类型**: `float32`
- **描述**: Bones get selected if RandomValue > RandomThreshold

### bActive
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FCollectionTransformSelectionRandomDataflowNode& opAssign(FCollectionTransformSelectionRandomDataflowNode Other)
```

