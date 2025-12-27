# UNiagaraDataInterfaceGrid3DCollection

**继承自**: `UNiagaraDataInterfaceGrid3D`

## 属性

### NumAttributes
- **类型**: `int`
- **描述**: Number of attributes stored on the grid

### RenderTargetUserParameter
- **类型**: `FNiagaraUserParameterBinding`
- **描述**: Reference to a user parameter if we're reading one.

### OverrideBufferFormat
- **类型**: `ENiagaraGpuBufferFormat`
- **描述**: When enabled overrides the format used to store data inside the grid, otherwise uses the project default setting.  Lower bit depth formats will save memory and performance at the cost of precision.

### PreviewAttribute
- **类型**: `FName`
- **描述**: When enabled allows you to preview the grid in a debug display

### bOverrideFormat
- **类型**: `bool`

### bPreviewGrid
- **类型**: `bool`

## 方法

### GetRawTextureSize
```angelscript
void GetRawTextureSize(const UNiagaraComponent Component, int& SizeX, int& SizeY, int& SizeZ)
```

### GetTextureSize
```angelscript
void GetTextureSize(const UNiagaraComponent Component, int& SizeX, int& SizeY, int& SizeZ)
```

