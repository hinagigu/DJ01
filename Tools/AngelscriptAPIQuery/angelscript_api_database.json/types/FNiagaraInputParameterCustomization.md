# FNiagaraInputParameterCustomization

## 属性

### WidgetType
- **类型**: `ENiagaraInputWidgetType`
- **描述**: Changes the widget implementation used for the input

### bHasMinValue
- **类型**: `bool`

### MinValue
- **类型**: `float32`
- **描述**: min ui value (float and int types only)

### bHasMaxValue
- **类型**: `bool`

### MaxValue
- **类型**: `float32`
- **描述**: max ui value (float and int types only)

### bHasStepWidth
- **类型**: `bool`

### StepWidth
- **类型**: `float32`
- **描述**: Step width used by the input when dragging

### InputDropdownValues
- **类型**: `TArray<FWidgetNamedInputValue>`

### EnumStyleDropdownValues
- **类型**: `TArray<FNiagaraWidgetNamedIntegerInputValue>`

### MaxSegmentsPerRow
- **类型**: `int`
- **描述**: Limits the number of buttons shown per row, 0 = unlimited

### SegmentValueOverrides
- **类型**: `TArray<FWidgetSegmentValueOverride>`

## 方法

### opAssign
```angelscript
FNiagaraInputParameterCustomization& opAssign(FNiagaraInputParameterCustomization Other)
```

