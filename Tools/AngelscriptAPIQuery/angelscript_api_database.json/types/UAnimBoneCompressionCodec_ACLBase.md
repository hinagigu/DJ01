# UAnimBoneCompressionCodec_ACLBase

**继承自**: `UAnimBoneCompressionCodec`

The base codec implementation for ACL support.

## 属性

### CompressionLevel
- **类型**: `ACLCompressionLevel`
- **描述**: The compression level to use. Higher levels will be slower to compress but yield a lower memory footprint.

### PhantomTrackMode
- **类型**: `ACLPhantomTrackMode`
- **描述**: How to treat phantom tracks. Phantom tracks are not mapped to a skeleton bone.

### DefaultVirtualVertexDistance
- **类型**: `float32`
- **描述**: The default virtual vertex distance for normal bones.

### SafeVirtualVertexDistance
- **类型**: `float32`
- **描述**: The virtual vertex distance for bones that requires extra accuracy.

### ErrorThreshold
- **类型**: `float32`
- **描述**: The error threshold to use when optimizing and compressing the animation sequence.

