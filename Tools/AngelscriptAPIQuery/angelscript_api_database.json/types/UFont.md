# UFont

**继承自**: `UObject`

A font object, for use by Slate, UMG, and Canvas.

A font can either be:
  * Runtime cached - The font contains a series of TTF files that combine to form a composite font. The glyphs are cached on demand when required at runtime.
  * Offline cached - The font contains a series of textures containing pre-baked cached glyphs and their associated texture coordinates.

## 属性

### FontCacheType
- **类型**: `EFontCacheType`
- **描述**: What kind of font caching should we use? This controls which options we see

### FontRasterizationMode
- **类型**: `EFontRasterizationMode`
- **描述**: The preferred rasterization method for this font (enable / disable MSDF)

### SdfSettings
- **类型**: `FFontSdfSettings`
- **描述**: Settings for rendering this font using the sdf pipeline

### Characters
- **类型**: `TArray<FFontCharacter>`
- **描述**: List of characters in the font.  For a MultiFont, this will include all characters in all sub-fonts!  Thus,
              the number of characters in this array isn't necessary the number of characters available in the font

### EmScale
- **类型**: `float32`
- **描述**: Font metrics.

### Ascent
- **类型**: `float32`
- **描述**: @todo document

### Descent
- **类型**: `float32`
- **描述**: @todo document

### Leading
- **类型**: `float32`
- **描述**: @todo document

### Kerning
- **类型**: `int`
- **描述**: Default horizontal spacing between characters when rendering text with this font

### ImportOptions
- **类型**: `FFontImportOptionsData`
- **描述**: Options used when importing this font

### ScalingFactor
- **类型**: `float32`
- **描述**: Scale to apply to the font.

### LegacyFontSize
- **类型**: `int`
- **描述**: The default size of the font used for legacy Canvas APIs that don't specify a font size

### LegacyFontName
- **类型**: `FName`
- **描述**: The default font name to use for legacy Canvas APIs that don't specify a font name

### CompositeFont
- **类型**: `FCompositeFont`
- **描述**: Embedded composite font data

