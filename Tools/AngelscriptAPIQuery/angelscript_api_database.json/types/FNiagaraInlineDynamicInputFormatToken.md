# FNiagaraInlineDynamicInputFormatToken

Defines a single token in a format for displaying dynamic input trees inline in the UI.  These tokens can represent the
      inputs to the dynamic input or additional text and layout options.

## 属性

### Usage
- **类型**: `ENiagaraInlineDynamicInputFormatTokenUsage`
- **描述**: Defines how the value of this token should be used when formatting the dynamic input tree.

### Value
- **类型**: `FString`
- **描述**: The value of this token which is used for formatting an inline dynamic input tree.  The purpose of this value is different
              depending on the value of the Usage property.

## 方法

### opAssign
```angelscript
FNiagaraInlineDynamicInputFormatToken& opAssign(FNiagaraInlineDynamicInputFormatToken Other)
```

