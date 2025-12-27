# UVariant

**继承自**: `UObject`

## 方法

### GetActor
```angelscript
AActor GetActor(int ActorIndex)
```

### GetDependency
```angelscript
FVariantDependency& GetDependency(int Index)
```
Get the dependency at index 'Index' by value. Will crash if index is invalid

### GetDependents
```angelscript
TArray<UVariant> GetDependents(ULevelVariantSets LevelVariantSets, bool bOnlyEnabledDependencies)
```
Returns all the variants that have this variant as a dependency

### GetDisplayText
```angelscript
FText GetDisplayText()
```

### GetNumActors
```angelscript
int GetNumActors()
```

### GetNumDependencies
```angelscript
int GetNumDependencies()
```

### GetParent
```angelscript
UVariantSet GetParent()
```

### GetThumbnail
```angelscript
UTexture2D GetThumbnail()
```
Gets the thumbnail currently used for this variant

### IsActive
```angelscript
bool IsActive()
```
Returns true if none of our properties are dirty

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
Sets the thumbnail to use for this variant. Can receive nullptr to clear it

### SwitchOn
```angelscript
void SwitchOn()
```

