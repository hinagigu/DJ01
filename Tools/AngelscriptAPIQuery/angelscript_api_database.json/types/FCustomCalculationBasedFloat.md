# FCustomCalculationBasedFloat

Structure to encapsulate magnitudes that are calculated via custom calculation

## 属性

### CalculationClassMagnitude
- **类型**: `TSubclassOf<UGameplayModMagnitudeCalculation>`

### Coefficient
- **类型**: `FScalableFloat`
- **描述**: Coefficient to the custom calculation

### PreMultiplyAdditiveValue
- **类型**: `FScalableFloat`
- **描述**: Additive value to the attribute calculation, added in before the coefficient applies

### PostMultiplyAdditiveValue
- **类型**: `FScalableFloat`
- **描述**: Additive value to the attribute calculation, added in after the coefficient applies

### FinalLookupCurve
- **类型**: `FCurveTableRowHandle`
- **描述**: If a curve table entry is specified, the OUTPUT of this custom class magnitude (including the pre and post additive values) lookup into the curve instead of using the attribute directly.

## 方法

### opAssign
```angelscript
FCustomCalculationBasedFloat& opAssign(FCustomCalculationBasedFloat Other)
```

