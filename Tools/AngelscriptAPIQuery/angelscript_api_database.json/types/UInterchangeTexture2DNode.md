# UInterchangeTexture2DNode

**继承自**: `UInterchangeTextureNode`

ns UE::Interchange

## 方法

### GetCustomWrapU
```angelscript
bool GetCustomWrapU(EInterchangeTextureWrapMode& AttributeValue)
```

### GetCustomWrapV
```angelscript
bool GetCustomWrapV(EInterchangeTextureWrapMode& AttributeValue)
```

### GetSourceBlocks
```angelscript
TMap<int,FString> GetSourceBlocks()
```
Get the source blocks for the texture.
If the map is empty, the texture is imported as a normal texture using the payload key.

### SetCustomWrapU
```angelscript
bool SetCustomWrapU(EInterchangeTextureWrapMode AttributeValue)
```

### SetCustomWrapV
```angelscript
bool SetCustomWrapV(EInterchangeTextureWrapMode AttributeValue)
```

