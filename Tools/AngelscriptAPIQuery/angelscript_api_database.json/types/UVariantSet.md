# UVariantSet

**继承自**: `UObject`

## 方法

### GetDisplayText
```angelscript
FText GetDisplayText()
```

### GetNumVariants
```angelscript
int GetNumVariants()
```

### GetParent
```angelscript
ULevelVariantSets GetParent()
```

### GetThumbnail
```angelscript
UTexture2D GetThumbnail()
```
Gets the thumbnail currently used for this variant set

### GetVariant
```angelscript
UVariant GetVariant(int VariantIndex)
```

### GetVariantByName
```angelscript
UVariant GetVariantByName(FString VariantName)
```

### SetDisplayText
```angelscript
void SetDisplayText(FText NewDisplayText)
```

### SetThumbnailFromCamera
```angelscript
void SetThumbnailFromCamera(FTransform CameraTransform, float32 FOVDegrees, float32 MinZ, float32 Gamma)
```

### SetThumbnailFromEditorViewport
```angelscript
void SetThumbnailFromEditorViewport()
```
Sets the thumbnail from the active editor viewport. Doesn't do anything if the Editor is not available

### SetThumbnailFromFile
```angelscript
void SetThumbnailFromFile(FString FilePath)
```

### SetThumbnailFromTexture
```angelscript
void SetThumbnailFromTexture(UTexture2D NewThumbnail)
```
Sets the thumbnail to use for this variant set. Can receive nullptr to clear it

