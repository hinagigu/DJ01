# FNiagaraRendererMaterialParameters

Parameters to apply to the material, these are both constant and dynamic bindings
Having any bindings set will cause a MID to be generated

## 属性

### AttributeBindings
- **类型**: `TArray<FNiagaraMaterialAttributeBinding>`

### ScalarParameters
- **类型**: `TArray<FNiagaraRendererMaterialScalarParameter>`

### VectorParameters
- **类型**: `TArray<FNiagaraRendererMaterialVectorParameter>`

### TextureParameters
- **类型**: `TArray<FNiagaraRendererMaterialTextureParameter>`

### StaticBoolParameters
- **类型**: `TArray<FNiagaraRendererMaterialStaticBoolParameter>`

## 方法

### opAssign
```angelscript
FNiagaraRendererMaterialParameters& opAssign(FNiagaraRendererMaterialParameters Other)
```

