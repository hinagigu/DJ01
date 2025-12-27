# UAnimBoneCompressionSettings

**继承自**: `UObject`

* This object is used to wrap a bone compression codec. It allows a clean integration in the editor by avoiding the need
* to create asset types and factory wrappers for every codec.

## 属性

### Codecs
- **类型**: `TArray<TObjectPtr<UAnimBoneCompressionCodec>>`
- **描述**: A list of animation bone compression codecs to try. Empty entries are ignored but the array cannot be empty.

### ErrorThreshold
- **类型**: `float32`
- **描述**: When compressing, the best codec below this error threshold will be used.

### bForceBelowThreshold
- **类型**: `bool`
- **描述**: Any codec (even one that increases the size) with a lower error will be used until it falls below the threshold.

