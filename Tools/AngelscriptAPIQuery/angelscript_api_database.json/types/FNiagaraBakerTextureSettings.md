# FNiagaraBakerTextureSettings

## 属性

### OutputName
- **类型**: `FName`
- **描述**: Optional output name, if left empty a name will be auto generated using the index of the texture/

### SourceBinding
- **类型**: `FNiagaraBakerTextureSource`
- **描述**: Source visualization we should capture, i.e. Scene Color, World Normal, etc

### FrameSize
- **类型**: `FIntPoint`
- **描述**: Size of each frame generated.

### TextureSize
- **类型**: `FIntPoint`
- **描述**: Overall texture size that will be generated.

### GeneratedTexture
- **类型**: `UTexture2D`
- **描述**: Final texture generated, an existing entry will be updated with new capture data.

### bUseFrameSize
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FNiagaraBakerTextureSettings& opAssign(FNiagaraBakerTextureSettings Other)
```

