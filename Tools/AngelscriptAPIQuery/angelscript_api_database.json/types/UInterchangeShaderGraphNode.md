# UInterchangeShaderGraphNode

**继承自**: `UInterchangeShaderNode`

A shader graph has its own set of inputs on which shader nodes can be connected to.

## 方法

### GetCustomBlendMode
```angelscript
bool GetCustomBlendMode(int& AttributeValue)
```
Set the Blend Mode using EBlendMode to avoid a dependency on the Engine.

### GetCustomIsAShaderFunction
```angelscript
bool GetCustomIsAShaderFunction(bool& AttributeValue)
```

### GetCustomOpacityMaskClipValue
```angelscript
bool GetCustomOpacityMaskClipValue(float32& AttributeValue)
```

### GetCustomScreenSpaceReflections
```angelscript
bool GetCustomScreenSpaceReflections(bool& AttributeValue)
```

### GetCustomTwoSided
```angelscript
bool GetCustomTwoSided(bool& AttributeValue)
```

### GetCustomTwoSidedTransmission
```angelscript
bool GetCustomTwoSidedTransmission(bool& AttributeValue)
```
Forces two-sided even for Transmission materials.

### SetCustomBlendMode
```angelscript
bool SetCustomBlendMode(int AttributeValue)
```

### SetCustomIsAShaderFunction
```angelscript
bool SetCustomIsAShaderFunction(bool AttributeValue)
```
Set whether this shader graph should be considered as a material (false), or a material function (true).

### SetCustomOpacityMaskClipValue
```angelscript
bool SetCustomOpacityMaskClipValue(float32 AttributeValue, bool bAddApplyDelegate)
```
The shader is transparent if its alpha value is lower than the clip value, or opaque if it is higher.

### SetCustomScreenSpaceReflections
```angelscript
bool SetCustomScreenSpaceReflections(bool AttributeValue)
```

### SetCustomTwoSided
```angelscript
bool SetCustomTwoSided(bool AttributeValue)
```
Set if this shader graph should be rendered two-sided or not. Defaults to off.

### SetCustomTwoSidedTransmission
```angelscript
bool SetCustomTwoSidedTransmission(bool AttributeValue)
```

