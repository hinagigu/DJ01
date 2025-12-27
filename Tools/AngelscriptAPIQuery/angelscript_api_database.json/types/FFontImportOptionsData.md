# FFontImportOptionsData

Font import options

## 属性

### FontName
- **类型**: `FString`
- **描述**: Name of the typeface for the font to import

### Height
- **类型**: `float32`
- **描述**: Height of font (point size)

### CharacterSet
- **类型**: `EFontImportCharacterSet`
- **描述**: Character set for this font

### Chars
- **类型**: `FString`
- **描述**: Explicit list of characters to include in the font

### UnicodeRange
- **类型**: `FString`
- **描述**: Range of Unicode character values to include in the font.  You can specify ranges using hyphens and/or commas (e.g. '400-900')

### CharsFilePath
- **类型**: `FString`
- **描述**: Path on disk to a folder where files that contain a list of characters to include in the font

### CharsFileWildcard
- **类型**: `FString`
- **描述**: File mask wildcard that specifies which files within the CharsFilePath to scan for characters in include in the font

### ForegroundColor
- **类型**: `FLinearColor`
- **描述**: Color of the foreground font pixels.  Usually you should leave this white and instead use the UI Styles editor to change the color of the font on the fly

### TexturePageWidth
- **类型**: `int`
- **描述**: Horizontal size of each texture page for this font in pixels

### TexturePageMaxHeight
- **类型**: `int`
- **描述**: The maximum vertical size of a texture page for this font in pixels.  The actual height of a texture page may be less than this if the font can fit within a smaller sized texture page.

### XPadding
- **类型**: `int`
- **描述**: Horizontal padding between each font character on the texture page in pixels

### YPadding
- **类型**: `int`
- **描述**: Vertical padding between each font character on the texture page in pixels

### ExtendBoxTop
- **类型**: `int`
- **描述**: How much to extend the top of the UV coordinate rectangle for each character in pixels

### ExtendBoxBottom
- **类型**: `int`
- **描述**: How much to extend the bottom of the UV coordinate rectangle for each character in pixels

### ExtendBoxRight
- **类型**: `int`
- **描述**: How much to extend the right of the UV coordinate rectangle for each character in pixels

### ExtendBoxLeft
- **类型**: `int`
- **描述**: How much to extend the left of the UV coordinate rectangle for each character in pixels

### Kerning
- **类型**: `int`
- **描述**: The initial horizontal spacing adjustment between rendered characters.  This setting will be copied directly into the generated Font object's properties.

### DistanceFieldScaleFactor
- **类型**: `int`
- **描述**: Scale factor determines how big to scale the font bitmap during import when generating distance field values
Note that higher values give better quality but importing will take much longer.

### DistanceFieldScanRadiusScale
- **类型**: `float32`
- **描述**: Shrinks or expands the scan radius used to determine the silhouette of the font edges.

### bEnableAntialiasing
- **类型**: `bool`

### bEnableBold
- **类型**: `bool`

### bEnableItalic
- **类型**: `bool`

### bEnableUnderline
- **类型**: `bool`

### bAlphaOnly
- **类型**: `bool`

### bCreatePrintableOnly
- **类型**: `bool`

### bIncludeASCIIRange
- **类型**: `bool`

### bEnableDropShadow
- **类型**: `bool`

### bEnableLegacyMode
- **类型**: `bool`

### bUseDistanceFieldAlpha
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FFontImportOptionsData& opAssign(FFontImportOptionsData Other)
```

