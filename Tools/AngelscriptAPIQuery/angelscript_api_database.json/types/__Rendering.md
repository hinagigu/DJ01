# __Rendering

## 方法

### BeginDrawCanvasToRenderTarget
```angelscript
void BeginDrawCanvasToRenderTarget(UTextureRenderTarget2D TextureRenderTarget, UCanvas& Canvas, FVector2D& Size, FDrawToRenderTargetContext& Context)
```
Returns a Canvas object that can be used to draw to the specified render target.
Canvas has functions like DrawMaterial with size parameters that can be used to draw to a specific area of a render target.
Be sure to call EndDrawCanvasToRenderTarget to complete the rendering!

### BreakSkinWeightInfo
```angelscript
void BreakSkinWeightInfo(FSkelMeshSkinWeightInfo InWeight, int& Bone0, uint8& Weight0, int& Bone1, uint8& Weight1, int& Bone2, uint8& Weight2, int& Bone3, uint8& Weight3)
```
Break FSkelMeshSkinWeightInfo

### CalculateProjectionMatrix
```angelscript
FMatrix CalculateProjectionMatrix(FMinimalViewInfo MinimalViewInfo)
```
Calculates the projection matrix using this view info's aspect ratio (regardless of bConstrainAspectRatio)

### ClearRenderTarget2D
```angelscript
void ClearRenderTarget2D(UTextureRenderTarget2D TextureRenderTarget, FLinearColor ClearColor)
```
Clears the specified render target with the given ClearColor.

### ConvertRenderTargetToTexture2DArrayEditorOnly
```angelscript
void ConvertRenderTargetToTexture2DArrayEditorOnly(UTextureRenderTarget2DArray RenderTarget, UTexture2DArray Texture)
```
Copies the contents of a UTextureRenderTarget2DArray to a UTexture2DArray
Only works in the editor

### ConvertRenderTargetToTexture2DEditorOnly
```angelscript
void ConvertRenderTargetToTexture2DEditorOnly(UTextureRenderTarget2D RenderTarget, UTexture2D Texture)
```
Copies the contents of a UTextureRenderTarget2D to a UTexture2D
Only works in the editor

### ConvertRenderTargetToTextureCubeEditorOnly
```angelscript
void ConvertRenderTargetToTextureCubeEditorOnly(UTextureRenderTargetCube RenderTarget, UTextureCube Texture)
```
Copies the contents of a UTextureRenderTargetCube to a UTextureCube
Only works in the editor

### ConvertRenderTargetToTextureVolumeEditorOnly
```angelscript
void ConvertRenderTargetToTextureVolumeEditorOnly(UTextureRenderTargetVolume RenderTarget, UVolumeTexture Texture)
```
Copies the contents of a UTextureRenderTargetVolume to a UVolumeTexture
Only works in the editor

### CreateRenderTarget2D
```angelscript
UTextureRenderTarget2D CreateRenderTarget2D(int Width, int Height, ETextureRenderTargetFormat Format, FLinearColor ClearColor, bool bAutoGenerateMipMaps, bool bSupportUAVs)
```
Creates a new render target and initializes it to the specified dimensions

### CreateRenderTarget2DArray
```angelscript
UTextureRenderTarget2DArray CreateRenderTarget2DArray(int Width, int Height, int Slices, ETextureRenderTargetFormat Format, FLinearColor ClearColor, bool bAutoGenerateMipMaps, bool bSupportUAVs)
```
Creates a new render target array and initializes it to the specified dimensions

### CreateRenderTargetVolume
```angelscript
UTextureRenderTargetVolume CreateRenderTargetVolume(int Width, int Height, int Depth, ETextureRenderTargetFormat Format, FLinearColor ClearColor, bool bAutoGenerateMipMaps, bool bSupportUAVs)
```
Creates a new volume render target and initializes it to the specified dimensions

### DrawMaterialToRenderTarget
```angelscript
void DrawMaterialToRenderTarget(UTextureRenderTarget2D TextureRenderTarget, UMaterialInterface Material)
```
Renders a quad with the material applied to the specified render target.
This sets the render target even if it is already set, which is an expensive operation.
Use BeginDrawCanvasToRenderTarget / EndDrawCanvasToRenderTarget instead if rendering multiple primitives to the same render target.

### EnablePathTracing
```angelscript
void EnablePathTracing(bool bEnablePathTracer)
```
Enables or disables the path tracer for the current Game Viewport.
This command is equivalent to setting ShowFlag.PathTracing, but is accessible even from shipping builds.

### EndDrawCanvasToRenderTarget
```angelscript
void EndDrawCanvasToRenderTarget(FDrawToRenderTargetContext Context)
```
Must be paired with a BeginDrawCanvasToRenderTarget to complete rendering to a render target.

### ExportRenderTarget
```angelscript
void ExportRenderTarget(UTextureRenderTarget2D TextureRenderTarget, FString FilePath, FString FileName)
```
Exports a render target as a HDR or PNG image onto the disk (depending on the format of the render target)

### ExportTexture2D
```angelscript
void ExportTexture2D(UTexture2D Texture, FString FilePath, FString FileName)
```
Exports a Texture2D as a HDR image onto the disk.

### ImportBufferAsTexture2D
```angelscript
UTexture2D ImportBufferAsTexture2D(TArray<uint8> Buffer)
```
Imports a texture from a buffer and creates Texture2D from it.

### ImportFileAsTexture2D
```angelscript
UTexture2D ImportFileAsTexture2D(FString Filename)
```
Imports a texture file from disk and creates Texture2D from it.

### MakeSkinWeightInfo
```angelscript
FSkelMeshSkinWeightInfo MakeSkinWeightInfo(int Bone0, uint8 Weight0, int Bone1, uint8 Weight1, int Bone2, uint8 Weight2, int Bone3, uint8 Weight3)
```
Create FSkelMeshSkinWeightInfo

### ReadRenderTarget
```angelscript
bool ReadRenderTarget(UTextureRenderTarget2D TextureRenderTarget, TArray<FColor>& OutSamples, bool bNormalize)
```
Incredibly inefficient and slow operation! Reads entire render target as sRGB color and returns a linear array of sRGB colors.
LDR render targets are assumed to be in sRGB space. HDR ones are assumed to be in linear space.
Result whether the operation succeeded.  If successful, OutSamples will an entry per pixel, where each is 8-bit per channel [0,255] BGRA in sRGB space.

### ReadRenderTargetPixel
```angelscript
FColor ReadRenderTargetPixel(UTextureRenderTarget2D TextureRenderTarget, int X, int Y)
```
Incredibly inefficient and slow operation! Read a value as sRGB color from a render target using integer pixel coordinates.
LDR render targets are assumed to be in sRGB space. HDR ones are assumed to be in linear space.
Result is 8-bit per channel [0,255] BGRA in sRGB space.

### ReadRenderTargetRaw
```angelscript
bool ReadRenderTargetRaw(UTextureRenderTarget2D TextureRenderTarget, TArray<FLinearColor>& OutLinearSamples, bool bNormalize)
```
Incredibly inefficient and slow operation! Read entire texture as-is from a render target.

### ReadRenderTargetRawPixel
```angelscript
FLinearColor ReadRenderTargetRawPixel(UTextureRenderTarget2D TextureRenderTarget, int X, int Y, bool bNormalize)
```
Incredibly inefficient and slow operation! Read a value as-is from a render target using integer pixel coordinates.

### ReadRenderTargetRawPixelArea
```angelscript
TArray<FLinearColor> ReadRenderTargetRawPixelArea(UTextureRenderTarget2D TextureRenderTarget, int MinX, int MinY, int MaxX, int MaxY, bool bNormalize)
```
Incredibly inefficient and slow operation! Read an area of values as-is from a render target using a rectangle defined by integer pixel coordinates.

### ReadRenderTargetRawUV
```angelscript
FLinearColor ReadRenderTargetRawUV(UTextureRenderTarget2D TextureRenderTarget, float32 U, float32 V, bool bNormalize)
```
Incredibly inefficient and slow operation! Read a value as-is from a render target using UV [0,1]x[0,1] coordinates.

### ReadRenderTargetRawUVArea
```angelscript
TArray<FLinearColor> ReadRenderTargetRawUVArea(UTextureRenderTarget2D TextureRenderTarget, FBox2D Area, bool bNormalize)
```
Incredibly inefficient and slow operation! Read an area of values as-is from a render target using a rectangle defined by UV [0,1]x[0,1] coordinates.

### ReadRenderTargetUV
```angelscript
FColor ReadRenderTargetUV(UTextureRenderTarget2D TextureRenderTarget, float32 U, float32 V)
```
Incredibly inefficient and slow operation! Read a value as sRGB color from a render target using UV [0,1]x[0,1] coordinates.
LDR render targets are assumed to be in sRGB space. HDR ones are assumed to be in linear space.
Result is 8-bit per channel [0,255] BGRA in sRGB space.

### RefreshPathTracingOutput
```angelscript
void RefreshPathTracingOutput()
```
Forces the path tracer to restart sample accumulation.
This can be used to force the path tracer to compute a new frame in situations where it can not detect a change in the scene automatically.

### ReleaseRenderTarget2D
```angelscript
void ReleaseRenderTarget2D(UTextureRenderTarget2D TextureRenderTarget)
```
Manually releases GPU resources of a render target. This is useful for blueprint creating a lot of render target that would
normally be released too late by the garbage collector that can be problematic on platforms that have tight GPU memory constrains.

### RenderTargetCreateStaticTexture2DArrayEditorOnly
```angelscript
UTexture2DArray RenderTargetCreateStaticTexture2DArrayEditorOnly(UTextureRenderTarget2DArray RenderTarget, FString Name, TextureCompressionSettings CompressionSettings, TextureMipGenSettings MipSettings)
```
Creates a new Static Texture 2D Array from a Render Target 2D Array.
Only works in the editor

### RenderTargetCreateStaticTexture2DEditorOnly
```angelscript
UTexture2D RenderTargetCreateStaticTexture2DEditorOnly(UTextureRenderTarget2D RenderTarget, FString Name, TextureCompressionSettings CompressionSettings, TextureMipGenSettings MipSettings)
```
Creates a new Static Texture from a Render Target 2D.
Only works in the editor

### RenderTargetCreateStaticTextureCubeEditorOnly
```angelscript
UTextureCube RenderTargetCreateStaticTextureCubeEditorOnly(UTextureRenderTargetCube RenderTarget, FString Name, TextureCompressionSettings CompressionSettings, TextureMipGenSettings MipSettings)
```
Creates a new Static Texture Cube from a Render Target Cube.
Only works in the editor

### RenderTargetCreateStaticVolumeTextureEditorOnly
```angelscript
UVolumeTexture RenderTargetCreateStaticVolumeTextureEditorOnly(UTextureRenderTargetVolume RenderTarget, FString Name, TextureCompressionSettings CompressionSettings, TextureMipGenSettings MipSettings)
```
Creates a new Static Volume Texture from a Render Target Volume.
Only works in the editor

### ResizeRenderTarget2D
```angelscript
void ResizeRenderTarget2D(UTextureRenderTarget2D TextureRenderTarget, int Width, int Height)
```
Changes the resolution of a render target. This is useful for when you need to resize the game viewport or change the in-game resolution during runtime
and thus need to update the sizes of all the render targets in the game accordingly.

### SetCastInsetShadowForAllAttachments
```angelscript
void SetCastInsetShadowForAllAttachments(UPrimitiveComponent PrimitiveComponent, bool bCastInsetShadow, bool bLightAttachmentsAsGroup)
```
Set the inset shadow casting state of the given component and all its child attachments.
    Also choose if all attachments should be grouped for the inset shadow rendering. If enabled, one depth target will be shared for all attachments.

