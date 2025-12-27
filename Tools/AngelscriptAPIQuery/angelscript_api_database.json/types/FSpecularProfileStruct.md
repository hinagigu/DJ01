# FSpecularProfileStruct

struct with all the settings we want in USpecularProfile, separate to make it easer to pass this data around in the engine.

## 属性

### Format
- **类型**: `ESpecularProfileFormat`

### ViewColor
- **类型**: `FRuntimeCurveLinearColor`
- **描述**: Define the view facing color

### LightColor
- **类型**: `FRuntimeCurveLinearColor`
- **描述**: Define the light facing color

### Texture
- **类型**: `UTexture2D`

## 方法

### opAssign
```angelscript
FSpecularProfileStruct& opAssign(FSpecularProfileStruct Other)
```

