# UPaperSprite

**继承自**: `UObject`

Sprite Asset

Stores the data necessary to render a single 2D sprite (from a region of a texture)
Can also contain collision shapes for the sprite.

@see UPaperSpriteComponent

## 属性

### OriginInSourceImageBeforeTrimming
- **类型**: `FVector2D`
- **描述**: Origin within SourceImage, prior to atlasing

### SourceImageDimensionBeforeTrimming
- **类型**: `FVector2D`
- **描述**: Dimensions of SourceImage

### bTrimmedInSourceImage
- **类型**: `bool`
- **描述**: This texture is trimmed, consider the values above

### bRotatedInSourceImage
- **类型**: `bool`
- **描述**: This texture is rotated in the atlas

### SourceTextureDimension
- **类型**: `FVector2D`
- **描述**: Dimension of the texture when this sprite was created
Used when the sprite is resized at some point

### SourceUV
- **类型**: `FVector2D`
- **描述**: Position within SourceTexture (in pixels)

### SourceDimension
- **类型**: `FVector2D`
- **描述**: Dimensions within SourceTexture (in pixels)

### SourceTexture
- **类型**: `TSoftObjectPtr<UTexture2D>`
- **描述**: The source texture that the sprite comes from

### AdditionalSourceTextures
- **类型**: `TArray<TObjectPtr<UTexture>>`
- **描述**: Additional source textures for other slots

### DefaultMaterial
- **类型**: `UMaterialInterface`

### AlternateMaterial
- **类型**: `UMaterialInterface`

### Sockets
- **类型**: `TArray<FPaperSpriteSocket>`
- **描述**: List of sockets on this sprite

### SpriteCollisionDomain
- **类型**: `ESpriteCollisionMode`
- **描述**: Collision domain (no collision, 2D, or 3D)

### PixelsPerUnrealUnit
- **类型**: `float32`
- **描述**: The scaling factor between pixels and Unreal units (cm) (e.g., 0.64 would make a 64 pixel wide sprite take up 100 cm)

### BodySetup
- **类型**: `UBodySetup`
- **描述**: Baked physics data.

### PivotMode
- **类型**: `ESpritePivotMode`
- **描述**: Pivot mode

### CustomPivotPoint
- **类型**: `FVector2D`
- **描述**: Custom pivot point (relative to the sprite rectangle)

### bSnapPivotToPixelGrid
- **类型**: `bool`
- **描述**: Should the pivot be snapped to a pixel boundary?

### CollisionGeometry
- **类型**: `FSpriteGeometryCollection`
- **描述**: Custom collision geometry polygons (in texture space)

### CollisionThickness
- **类型**: `float32`
- **描述**: The extrusion thickness of collision geometry when using a 3D collision domain

### RenderGeometry
- **类型**: `FSpriteGeometryCollection`
- **描述**: Custom render geometry polygons (in texture space)

### AtlasGroup
- **类型**: `UPaperSpriteAtlas`
- **描述**: Spritesheet group that this sprite belongs to

