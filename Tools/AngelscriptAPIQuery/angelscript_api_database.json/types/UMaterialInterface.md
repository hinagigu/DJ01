# UMaterialInterface

**继承自**: `UObject`

## 属性

### SubsurfaceProfile
- **类型**: `USubsurfaceProfile`

### NeuralProfile
- **类型**: `UNeuralProfile`

### LightmassSettings
- **类型**: `FLightmassMaterialInterfaceSettings`
- **描述**: The Lightmass settings for this object.

### AssetUserData
- **类型**: `TArray<TObjectPtr<UAssetUserData>>`
- **描述**: Array of user data stored with the asset

### PreviewMesh
- **类型**: `FSoftObjectPath`
- **描述**: The mesh used by the material editor to preview the material.

### ThumbnailInfo
- **类型**: `UThumbnailInfo`
- **描述**: Information for thumbnail rendering

### AssetImportData
- **类型**: `UAssetImportData`
- **描述**: Importing data and options used for this material

## 方法

### GetBaseMaterial
```angelscript
UMaterial GetBaseMaterial()
```
Walks up parent chain and finds the base Material that this is an instance of. Just calls the virtual GetMaterial()

### GetBlendMode
```angelscript
EBlendMode GetBlendMode()
```

### GetNaniteOverideMaterial
```angelscript
UMaterialInterface GetNaniteOverideMaterial()
```
Get the associated nanite override material.

### GetParameterInfo
```angelscript
FMaterialParameterInfo GetParameterInfo(EMaterialParameterAssociation Association, FName ParameterName, UMaterialFunctionInterface LayerFunction)
```

### GetPhysicalMaterial
```angelscript
UPhysicalMaterial GetPhysicalMaterial()
```
Return a pointer to the physical material used by this material instance.
@return The physical material.

### GetPhysicalMaterialFromMap
```angelscript
UPhysicalMaterial GetPhysicalMaterialFromMap(int Index)
```
Return a pointer to the physical material from mask map at given index.
@return The physical material.

### GetPhysicalMaterialMask
```angelscript
UPhysicalMaterialMask GetPhysicalMaterialMask()
```
Return a pointer to the physical material mask used by this material instance.
@return The physical material.

### SetForceMipLevelsToBeResident
```angelscript
void SetForceMipLevelsToBeResident(bool OverrideForceMiplevelsToBeResident, bool bForceMiplevelsToBeResidentValue, float32 ForceDuration, int CinematicTextureGroups, bool bFastResponse)
```
Force the streaming system to disregard the normal logic for the specified duration and
instead always load all mip-levels for all textures used by this material.

@param OverrideForceMiplevelsToBeResident    - Whether to use (true) or ignore (false) the bForceMiplevelsToBeResidentValue parameter.
@param bForceMiplevelsToBeResidentValue              - true forces all mips to stream in. false lets other factors decide what to do with the mips.
@param ForceDuration                                                 - Number of seconds to keep all mip-levels in memory, disregarding the normal priority logic. Negative value turns it off.
@param CinematicTextureGroups                                - Bitfield indicating texture groups that should use extra high-resolution mips
@param bFastResponse                                                 - USE WITH EXTREME CAUTION! Fast response textures incur sizable GT overhead and disturb streaming metric calculation. Avoid whenever possible.

