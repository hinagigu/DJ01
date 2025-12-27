# UMeshComponent

**继承自**: `UPrimitiveComponent`

MeshComponent is an abstract base for any component that is an instance of a renderable collection of triangles.

@see UStaticMeshComponent
@see USkeletalMeshComponent

## 属性

### OverrideMaterials
- **类型**: `TArray<TObjectPtr<UMaterialInterface>>`
- **描述**: Material overrides.

### bEnableMaterialParameterCaching
- **类型**: `bool`

## 方法

### GetMaterials
```angelscript
TArray<UMaterialInterface> GetMaterials()
```

### GetOverlayMaterial
```angelscript
UMaterialInterface GetOverlayMaterial()
```
Get the overlay material used by this instance

### GetOverlayMaterialMaxDrawDistance
```angelscript
float32 GetOverlayMaterialMaxDrawDistance()
```
Get the overlay material used by this instance

### PrestreamMeshLODs
```angelscript
bool PrestreamMeshLODs(float32 Seconds)
```
Tell the streaming system to start streaming in all LODs for the mesh.
 Note: this function may set bIgnoreStreamingMipBias on this component enable the FastForceResident system.
@return bool                                                        True if streaming was successfully requested
@param Seconds                                                  Number of seconds to force all LODs to be resident

### PrestreamTextures
```angelscript
void PrestreamTextures(float32 Seconds, bool bPrioritizeCharacterTextures, int CinematicTextureGroups)
```
Tell the streaming system to start loading all textures with all mip-levels.
@param Seconds                                                  Number of seconds to force all mip-levels to be resident
@param bPrioritizeCharacterTextures             Whether character textures should be prioritized for a while by the streaming system
@param CinematicTextureGroups                   Bitfield indicating which texture groups that use extra high-resolution mips

### SetOverlayMaterial
```angelscript
void SetOverlayMaterial(UMaterialInterface NewOverlayMaterial)
```
Change the overlay material used by this instance

### SetOverlayMaterialMaxDrawDistance
```angelscript
void SetOverlayMaterialMaxDrawDistance(float32 InMaxDrawDistance)
```
Change the overlay material max draw distance used by this instance

### SetScalarParameterValueOnMaterials
```angelscript
void SetScalarParameterValueOnMaterials(FName ParameterName, float32 ParameterValue)
```
Set all occurrences of Scalar Material Parameters with ParameterName in the set of materials of the SkeletalMesh to ParameterValue

### SetVectorParameterValueOnMaterials
```angelscript
void SetVectorParameterValueOnMaterials(FName ParameterName, FVector ParameterValue)
```
Set all occurrences of Vector Material Parameters with ParameterName in the set of materials of the SkeletalMesh to ParameterValue

