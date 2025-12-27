# FGameplayEffectModifierMagnitude

Struct representing the magnitude of a gameplay effect modifier, potentially calculated in numerous different ways

## 属性

### MagnitudeCalculationType
- **类型**: `EGameplayEffectMagnitudeCalculation`
- **描述**: Type of calculation to perform to derive the magnitude

### ScalableFloatMagnitude
- **类型**: `FScalableFloat`
- **描述**: Magnitude value represented by a scalable float

### AttributeBasedMagnitude
- **类型**: `FAttributeBasedFloat`
- **描述**: Magnitude value represented by an attribute-based float
      (Coefficient * (PreMultiplyAdditiveValue + [Eval'd Attribute Value According to Policy])) + PostMultiplyAdditiveValue

### CustomMagnitude
- **类型**: `FCustomCalculationBasedFloat`
- **描述**: Magnitude value represented by a custom calculation class

### SetByCallerMagnitude
- **类型**: `FSetByCallerFloat`
- **描述**: Magnitude value represented by a SetByCaller magnitude

## 方法

### opAssign
```angelscript
FGameplayEffectModifierMagnitude& opAssign(FGameplayEffectModifierMagnitude Other)
```

