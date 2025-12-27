# __ETextureImportPNGInfill

When should RGB colors be spread into neighboring fully transparent white pixels, replacing their RGB.
  By default, this is done OnlyOnBinaryTransparency, not on PNG's with non-binary-transparency alpha channels.
  The PNG format has two different ways of storing alpha, either as 1-bit binary transparency, or as full 8/16 bit alpha channels.

  Used to be set from the TextureImporter/FillPNGZeroAlpha config value.  Setting this option will supercede that.

## 属性

### Default
- **类型**: `ETextureImportPNGInfill`

### Never
- **类型**: `ETextureImportPNGInfill`

### OnlyOnBinaryTransparency
- **类型**: `ETextureImportPNGInfill`

### Always
- **类型**: `ETextureImportPNGInfill`

### ETextureImportPNGInfill_MAX
- **类型**: `ETextureImportPNGInfill`

