# FNiagaraSystemVisibilityCullingSettings

Scalability settings for Niagara Systems for a particular platform set (unless overridden).

## 属性

### MaxTimeOutsideViewFrustum
- **类型**: `float32`
- **描述**: Effects will be culled if they go longer than this time outside the view frustum.

### MaxTimeWithoutRender
- **类型**: `float32`
- **描述**: Effects will be culled if they go longer than this time without being rendered.

### bCullWhenNotRendered
- **类型**: `bool`

### bCullByViewFrustum
- **类型**: `bool`

### bAllowPreCullingByViewFrustum
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FNiagaraSystemVisibilityCullingSettings& opAssign(FNiagaraSystemVisibilityCullingSettings Other)
```

