# UPaperSpriteComponent

**继承自**: `UMeshComponent`

A component that handles rendering and collision for a single instance of a UPaperSprite asset.

This component is created when you drag a sprite asset from the content browser into a Blueprint, or
contained inside of the actor created when you drag one into the level.

@see UPrimitiveComponent, UPaperSprite

## 属性

### SourceSprite
- **类型**: `UPaperSprite`

### SpriteColor
- **类型**: `FLinearColor`

## 方法

### GetSprite
```angelscript
UPaperSprite GetSprite()
```
Gets the PaperSprite used by this instance.

### SetSprite
```angelscript
bool SetSprite(UPaperSprite NewSprite)
```
Change the PaperSprite used by this instance.

### SetSpriteColor
```angelscript
void SetSpriteColor(FLinearColor NewColor)
```
Set color of the sprite

