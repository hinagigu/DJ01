# UNiagaraDataInterfaceRenderTarget2DArray

**继承自**: `UNiagaraDataInterfaceRWBase`

## 属性

### Size
- **类型**: `FIntVector`

### OverrideRenderTargetFormat
- **类型**: `ETextureRenderTargetFormat`
- **描述**: When enabled overrides the format of the render target, otherwise uses the project default setting.

### OverrideRenderTargetFilter
- **类型**: `TextureFilter`
- **描述**: When enabled overrides the filter of the render target, otherwise uses the project default setting.

### RenderTargetUserParameter
- **类型**: `FNiagaraUserParameterBinding`
- **描述**: When valid the user parameter is used as the render target rather than creating one internal, note that the input render target will be adjusted by the Niagara simulation

### bInheritUserParameterSettings
- **类型**: `bool`

### bOverrideFormat
- **类型**: `bool`

### bPreviewRenderTarget
- **类型**: `bool`

