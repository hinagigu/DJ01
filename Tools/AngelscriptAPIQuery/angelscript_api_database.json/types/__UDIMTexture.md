# __UDIMTexture

## 方法

### MakeUDIMVirtualTextureFromTexture2Ds
```angelscript
UTexture2D MakeUDIMVirtualTextureFromTexture2Ds(FString OutputPathName, TArray<UTexture2D> SourceTextures, TArray<FIntPoint> BlockCoords, bool bKeepExistingSettings, bool bCheckOutAndSave)
```
Make a UDIM virtual texture from a list of regular 2D textures
@param OutputPathName                 Path name of the UDIM texture (e.g. /Game/MyTexture)
@param SourceTextures                 List of regular 2D textures to be packed into the atlas
@param BlockCoords                    Coordinates of the corresponding texture in the atlas
@param bKeepExistingSettings  Whether to keep existing settings if a texture with the same path name exists. Otherwise, settings will be copied from the first source texture
@param bCheckOutAndSave               Whether to check out and save the UDIM texture
@return UTexture2D*                   Pointer to the UDIM texture or null if failed

