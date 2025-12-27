# ANiagaraPreviewGrid

**继承自**: `AActor`

## 属性

### System
- **类型**: `UNiagaraSystem`

### ResetMode
- **类型**: `ENiagaraPreviewGridResetMode`

### PreviewAxisX
- **类型**: `UNiagaraPreviewAxis`
- **描述**: Object controlling behavior varying on the X axis.

### PreviewAxisY
- **类型**: `UNiagaraPreviewAxis`
- **描述**: Object controlling behavior varying on the Y axis.

### PreviewClass
- **类型**: `TSubclassOf<ANiagaraPreviewBase>`
- **描述**: Class used to for previews in this grid.

### SpacingX
- **类型**: `float32`
- **描述**: The default spacing between previews in X if the axis does not override it.

### SpacingY
- **类型**: `float32`
- **描述**: The default spacing between previews if the axis does not override it.

## 方法

### ActivatePreviews
```angelscript
void ActivatePreviews(bool bReset)
```
AActor Interface End

### DeactivatePreviews
```angelscript
void DeactivatePreviews()
```

### GetPreviews
```angelscript
void GetPreviews(TArray<UNiagaraComponent>& OutPreviews)
```

### SetPaused
```angelscript
void SetPaused(bool bPaused)
```

