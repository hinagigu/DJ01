# UUVLayoutProperties

**继承自**: `UInteractiveToolPropertySet`

UV Layout Settings

## 属性

### LayoutType
- **类型**: `EUVLayoutType`
- **描述**: Type of layout applied to input UVs

### TextureResolution
- **类型**: `int`
- **描述**: Expected resolution of the output textures; this controls spacing left between UV islands to avoid interpolation artifacts

### Scale
- **类型**: `float32`
- **描述**: Uniform scale applied to UVs after packing

### Translation
- **类型**: `FVector2D`
- **描述**: Translation applied to UVs after packing, and after scaling

### bAllowFlips
- **类型**: `bool`
- **描述**: Allow the Repack layout type to flip the orientation of UV islands to save space. Note that this may cause problems for downstream operations, and therefore is disabled by default.

### bEnableUDIMLayout
- **类型**: `bool`
- **描述**: Enable UDIM aware layout and keep islands within their originating UDIM tiles when laying out.

