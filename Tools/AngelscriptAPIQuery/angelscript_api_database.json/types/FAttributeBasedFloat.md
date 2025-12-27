# FAttributeBasedFloat

Struct representing a float whose magnitude is dictated by a backing attribute and a calculation policy, follows basic form of:
(Coefficient * (PreMultiplyAdditiveValue + [Eval'd Attribute Value According to Policy])) + PostMultiplyAdditiveValue

## 属性

### Coefficient
- **类型**: `FScalableFloat`
- **描述**: Coefficient to the attribute calculation

### PreMultiplyAdditiveValue
- **类型**: `FScalableFloat`
- **描述**: Additive value to the attribute calculation, added in before the coefficient applies

### PostMultiplyAdditiveValue
- **类型**: `FScalableFloat`
- **描述**: Additive value to the attribute calculation, added in after the coefficient applies

### BackingAttribute
- **类型**: `FGameplayEffectAttributeCaptureDefinition`
- **描述**: Attribute backing the calculation

### AttributeCurve
- **类型**: `FCurveTableRowHandle`
- **描述**: If a curve table entry is specified, the attribute will be used as a lookup into the curve instead of using the attribute directly.

### AttributeCalculationType
- **类型**: `EAttributeBasedFloatCalculationType`
- **描述**: Calculation policy in regards to the attribute

### FinalChannel
- **类型**: `EGameplayModEvaluationChannel`
- **描述**: Channel to terminate evaluation on when using AttributeEvaluatedUpToChannel calculation type

### SourceTagFilter
- **类型**: `FGameplayTagContainer`
- **描述**: Filter to use on source tags; If specified, only modifiers applied with all of these tags will factor into the calculation

### TargetTagFilter
- **类型**: `FGameplayTagContainer`
- **描述**: Filter to use on target tags; If specified, only modifiers applied with all of these tags will factor into the calculation

## 方法

### opAssign
```angelscript
FAttributeBasedFloat& opAssign(FAttributeBasedFloat Other)
```

