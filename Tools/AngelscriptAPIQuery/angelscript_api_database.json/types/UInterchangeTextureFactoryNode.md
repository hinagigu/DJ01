# UInterchangeTextureFactoryNode

**继承自**: `UInterchangeFactoryBaseNode`

## 方法

### GetCustomAdjustBrightness
```angelscript
bool GetCustomAdjustBrightness(float32& AttributeValue)
```
Return false if the Attribute was not set previously.

### GetCustomAdjustBrightnessCurve
```angelscript
bool GetCustomAdjustBrightnessCurve(float32& AttributeValue)
```
Return false if the Attribute was not set previously.

### GetCustomAdjustHue
```angelscript
bool GetCustomAdjustHue(float32& AttributeValue)
```
Return false if the Attribute was not set previously.

### GetCustomAdjustMaxAlpha
```angelscript
bool GetCustomAdjustMaxAlpha(float32& AttributeValue)
```
Return false if the Attribute was not set previously.

### GetCustomAdjustMinAlpha
```angelscript
bool GetCustomAdjustMinAlpha(float32& AttributeValue)
```
Return false if the Attribute was not set previously.

### GetCustomAdjustRGBCurve
```angelscript
bool GetCustomAdjustRGBCurve(float32& AttributeValue)
```
Return false if the Attribute was not set previously.

### GetCustomAdjustSaturation
```angelscript
bool GetCustomAdjustSaturation(float32& AttributeValue)
```
Return false if the Attribute was not set previously.

### GetCustomAdjustVibrance
```angelscript
bool GetCustomAdjustVibrance(float32& AttributeValue)
```
Return false if the Attribute was not set previously.

### GetCustomAllowNonPowerOfTwo
```angelscript
bool GetCustomAllowNonPowerOfTwo(bool& AttributeValue)
```
Return false if the Attribute was not set previously.

### GetCustomAlphaCoverageThresholds
```angelscript
bool GetCustomAlphaCoverageThresholds(FVector4& AttributeValue)
```
Return false if the Attribute was not set previously.

### GetCustombChromaKeyTexture
```angelscript
bool GetCustombChromaKeyTexture(bool& AttributeValue)
```
Return false if the Attribute was not set previously.

### GetCustombDoScaleMipsForAlphaCoverage
```angelscript
bool GetCustombDoScaleMipsForAlphaCoverage(bool& AttributeValue)
```
Return false if the Attribute was not set previously.

### GetCustombFlipGreenChannel
```angelscript
bool GetCustombFlipGreenChannel(bool& AttributeValue)
```
Return false if the Attribute was not set previously.

### GetCustombPreserveBorder
```angelscript
bool GetCustombPreserveBorder(bool& AttributeValue)
```
Return false if the Attribute was not set previously.

### GetCustombUseLegacyGamma
```angelscript
bool GetCustombUseLegacyGamma(bool& AttributeValue)
```
Return false if the Attribute was not set previously.

### GetCustomChromaKeyColor
```angelscript
bool GetCustomChromaKeyColor(FColor& AttributeValue)
```
Return false if the Attribute was not set previously.

### GetCustomChromaKeyThreshold
```angelscript
bool GetCustomChromaKeyThreshold(float32& AttributeValue)
```
Return false if the Attribute was not set previously.

### GetCustomCompositePower
```angelscript
bool GetCustomCompositePower(float32& AttributeValue)
```
Return false if the Attribute was not set previously.

### GetCustomCompositeTextureMode
```angelscript
bool GetCustomCompositeTextureMode(uint8& AttributeValue)
```
Return false if the Attribute was not set previously.

### GetCustomCompressionNoAlpha
```angelscript
bool GetCustomCompressionNoAlpha(bool& AttributeValue)
```
Return false if the Attribute was not set previously.

### GetCustomCompressionQuality
```angelscript
bool GetCustomCompressionQuality(uint8& AttributeValue)
```
Return false if the Attribute was not set previously.

### GetCustomCompressionSettings
```angelscript
bool GetCustomCompressionSettings(uint8& AttributeValue)
```
Return false if the Attribute was not set previously.

### GetCustomDeferCompression
```angelscript
bool GetCustomDeferCompression(bool& AttributeValue)
```
Return false if the Attribute was not set previously.

### GetCustomDownscale
```angelscript
bool GetCustomDownscale(float32& AttributeValue)
```
Return false if the Attribute was not set previously.

### GetCustomDownscaleOptions
```angelscript
bool GetCustomDownscaleOptions(uint8& AttributeValue)
```
Return false if the Attribute was not set previously.

### GetCustomFilter
```angelscript
bool GetCustomFilter(uint8& AttributeValue)
```
Return false if the Attribute was not set previously.

### GetCustomLODBias
```angelscript
bool GetCustomLODBias(int& AttributeValue)
```
Return false if the Attribute was not set previously.

### GetCustomLODGroup
```angelscript
bool GetCustomLODGroup(uint8& AttributeValue)
```
Return false if the Attribute was not set previously.

### GetCustomLossyCompressionAmount
```angelscript
bool GetCustomLossyCompressionAmount(uint8& AttributeValue)
```
Return false if the Attribute was not set previously.

### GetCustomMaxTextureSize
```angelscript
bool GetCustomMaxTextureSize(int& AttributeValue)
```
Return false if the Attribute was not set previously.

### GetCustomMipGenSettings
```angelscript
bool GetCustomMipGenSettings(uint8& AttributeValue)
```
Return false if the Attribute was not set previously.

### GetCustomMipLoadOptions
```angelscript
bool GetCustomMipLoadOptions(uint8& AttributeValue)
```
Return false if the Attribute was not set previously.

### GetCustomPaddingColor
```angelscript
bool GetCustomPaddingColor(FColor& AttributeValue)
```
Return false if the Attribute was not set previously.

### GetCustomPowerOfTwoMode
```angelscript
bool GetCustomPowerOfTwoMode(uint8& AttributeValue)
```
Return false if the Attribute was not set previously.

### GetCustomPreferCompressedSourceData
```angelscript
bool GetCustomPreferCompressedSourceData(bool& AttributeValue)
```
Return false if the Attribute was not set previously.

### GetCustomSRGB
```angelscript
bool GetCustomSRGB(bool& AttributeValue)
```
Return false if the Attribute was not set previously.

### GetCustomTranslatedTextureNodeUid
```angelscript
bool GetCustomTranslatedTextureNodeUid(FString& AttributeValue)
```
Get the unique ID of the translated texture node.

### GetCustomVirtualTextureStreaming
```angelscript
bool GetCustomVirtualTextureStreaming(bool& AttributeValue)
```
Return false if the Attribute was not set previously.

### GetObjectClass
```angelscript
UClass GetObjectClass()
```
Get the class this node creates.

### InitializeTextureNode
```angelscript
void InitializeTextureNode(FString UniqueID, FString DisplayLabel, FString InAssetName)
```
Initialize node data.
@param: UniqueID - The unique ID for this node.
@param DisplayLabel - The name of the node.
@param InAssetClass - The class the texture factory will create for this node.

### SetCustomAdjustBrightness
```angelscript
bool SetCustomAdjustBrightness(float32 AttributeValue, bool bAddApplyDelegate)
```

### SetCustomAdjustBrightnessCurve
```angelscript
bool SetCustomAdjustBrightnessCurve(float32 AttributeValue, bool bAddApplyDelegate)
```

### SetCustomAdjustHue
```angelscript
bool SetCustomAdjustHue(float32 AttributeValue, bool bAddApplyDelegate)
```

### SetCustomAdjustMaxAlpha
```angelscript
bool SetCustomAdjustMaxAlpha(float32 AttributeValue, bool bAddApplyDelegate)
```

### SetCustomAdjustMinAlpha
```angelscript
bool SetCustomAdjustMinAlpha(float32 AttributeValue, bool bAddApplyDelegate)
```

### SetCustomAdjustRGBCurve
```angelscript
bool SetCustomAdjustRGBCurve(float32 AttributeValue, bool bAddApplyDelegate)
```

### SetCustomAdjustSaturation
```angelscript
bool SetCustomAdjustSaturation(float32 AttributeValue, bool bAddApplyDelegate)
```

### SetCustomAdjustVibrance
```angelscript
bool SetCustomAdjustVibrance(float32 AttributeValue, bool bAddApplyDelegate)
```

### SetCustomAllowNonPowerOfTwo
```angelscript
bool SetCustomAllowNonPowerOfTwo(bool AttributeValue)
```
* Should the factory allow the import of texture that would have a resolution that is not a power of two
* By default this is not allowed

### SetCustomAlphaCoverageThresholds
```angelscript
bool SetCustomAlphaCoverageThresholds(FVector4 AttributeValue, bool bAddApplyDelegate)
```

### SetCustombChromaKeyTexture
```angelscript
bool SetCustombChromaKeyTexture(bool AttributeValue, bool bAddApplyDelegate)
```

### SetCustombDoScaleMipsForAlphaCoverage
```angelscript
bool SetCustombDoScaleMipsForAlphaCoverage(bool AttributeValue, bool bAddApplyDelegate)
```

### SetCustombFlipGreenChannel
```angelscript
bool SetCustombFlipGreenChannel(bool AttributeValue, bool bAddApplyDelegate)
```

### SetCustombPreserveBorder
```angelscript
bool SetCustombPreserveBorder(bool AttributeValue, bool bAddApplyDelegate)
```

### SetCustombUseLegacyGamma
```angelscript
bool SetCustombUseLegacyGamma(bool AttributeValue, bool bAddApplyDelegate)
```

### SetCustomChromaKeyColor
```angelscript
bool SetCustomChromaKeyColor(FColor AttributeValue, bool bAddApplyDelegate)
```

### SetCustomChromaKeyThreshold
```angelscript
bool SetCustomChromaKeyThreshold(float32 AttributeValue, bool bAddApplyDelegate)
```

### SetCustomCompositePower
```angelscript
bool SetCustomCompositePower(float32 AttributeValue, bool bAddApplyDelegate)
```

### SetCustomCompositeTextureMode
```angelscript
bool SetCustomCompositeTextureMode(uint8 AttributeValue, bool bAddApplyDelegate)
```

### SetCustomCompressionNoAlpha
```angelscript
bool SetCustomCompressionNoAlpha(bool AttributeValue, bool bAddApplyDelegate)
```

### SetCustomCompressionQuality
```angelscript
bool SetCustomCompressionQuality(uint8 AttributeValue, bool bAddApplyDelegate)
```

### SetCustomCompressionSettings
```angelscript
bool SetCustomCompressionSettings(uint8 AttributeValue, bool bAddApplyDelegate)
```

### SetCustomDeferCompression
```angelscript
bool SetCustomDeferCompression(bool AttributeValue, bool bAddApplyDelegate)
```

### SetCustomDownscale
```angelscript
bool SetCustomDownscale(float32 AttributeValue, bool bAddApplyDelegate)
```

### SetCustomDownscaleOptions
```angelscript
bool SetCustomDownscaleOptions(uint8 AttributeValue, bool bAddApplyDelegate)
```

### SetCustomFilter
```angelscript
bool SetCustomFilter(uint8 AttributeValue, bool bAddApplyDelegate)
```

### SetCustomLODBias
```angelscript
bool SetCustomLODBias(int AttributeValue, bool bAddApplyDelegate)
```

### SetCustomLODGroup
```angelscript
bool SetCustomLODGroup(uint8 AttributeValue, bool bAddApplyDelegate)
```

### SetCustomLossyCompressionAmount
```angelscript
bool SetCustomLossyCompressionAmount(uint8 AttributeValue, bool bAddApplyDelegate)
```

### SetCustomMaxTextureSize
```angelscript
bool SetCustomMaxTextureSize(int AttributeValue, bool bAddApplyDelegate)
```

### SetCustomMipGenSettings
```angelscript
bool SetCustomMipGenSettings(uint8 AttributeValue, bool bAddApplyDelegate)
```

### SetCustomMipLoadOptions
```angelscript
bool SetCustomMipLoadOptions(uint8 AttributeValue, bool bAddApplyDelegate)
```

### SetCustomPaddingColor
```angelscript
bool SetCustomPaddingColor(FColor AttributeValue, bool bAddApplyDelegate)
```

### SetCustomPowerOfTwoMode
```angelscript
bool SetCustomPowerOfTwoMode(uint8 AttributeValue, bool bAddApplyDelegate)
```

### SetCustomPreferCompressedSourceData
```angelscript
bool SetCustomPreferCompressedSourceData(bool AttributeValue)
```
* Determines whether the factory should tell the translator to provide a compressed source data payload when available.
* This will generally result in smaller assets. However, some operations like the texture build might be slower, because the source data first needs to be decompressed.

### SetCustomSRGB
```angelscript
bool SetCustomSRGB(bool AttributeValue, bool bAddApplyDelegate)
```

### SetCustomTranslatedTextureNodeUid
```angelscript
bool SetCustomTranslatedTextureNodeUid(FString AttributeValue)
```
Set the unique ID of the translated texture node. This is a reference to the node that was created by the translator. It is needed to get the texture payload.

### SetCustomVirtualTextureStreaming
```angelscript
bool SetCustomVirtualTextureStreaming(bool AttributeValue, bool bAddApplyDelegate)
```

