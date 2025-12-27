# __ImportanceSampling

## 方法

### BreakImportanceTexture
```angelscript
void BreakImportanceTexture(FImportanceTexture ImportanceTexture, UTexture2D& Texture, EImportanceWeight& WeightingFunc)
```
Get texture used to create an ImportanceTexture object
@param ImportanceTexture - The source ImportanceTexture object
@outparam Texture - Texture object for this ImportanceTexture.
@param WeightingFunc - How to turn the texture data into probability weights
@return new ImportanceTexture object for use with ImportanceSample

### ImportanceSample
```angelscript
void ImportanceSample(FImportanceTexture Texture, FVector2D Rand, int Samples, float32 Intensity, FVector2D& SamplePosition, FLinearColor& SampleColor, float32& SampleIntensity, float32& SampleSize)
```
Distribute sample points proportional to Texture2D luminance.
@param Rand - Random 2D point with components evenly distributed between 0 and 1
@param Samples - Total number of samples that will be used
@param Intensity - Total intensity for light
@outparam SamplePosition - Importance sampled 2D output texture coordinate (0-1)
@outparam SampleColor - Representative color near Position from MIP level for SampleSize
@outparam SampleIntensity - Intensity of individual points, scaled by probability and number of samples
@outparam SampleSize - Local density of points near Position (scaled for 1x1 texture space)

### MakeImportanceTexture
```angelscript
FImportanceTexture MakeImportanceTexture(UTexture2D Texture, EImportanceWeight WeightingFunc)
```
Create an FImportanceTexture object for texture-driven importance sampling from a 2D RGBA8 texture
@param Texture - Texture object to use. Must be RGBA8 format.
@param WeightingFunc - How to turn the texture data into probability weights
@return new ImportanceTexture object for use with ImportanceSample

### NextSobolCell2D
```angelscript
FVector2D NextSobolCell2D(int Index, int NumCells, FVector2D PreviousValue)
```
@param Index - Which sequential point
@param NumCells - Size of cell grid, 1 to 32768. Rounded up to the next power of two
@param PreviousValue - The Sobol value for Index-1
@return Sobol-distributed random 2D position in the same grid cell

### NextSobolCell3D
```angelscript
FVector NextSobolCell3D(int Index, int NumCells, FVector PreviousValue)
```
@param Index - Which sequential point
@param NumCells - Size of cell grid, 1 to 1024. Rounded up to the next power of two
@param PreviousValue - The Sobol value for Index-1
@return Sobol-distributed random 3D position in the same grid cell

### NextSobolFloat
```angelscript
float32 NextSobolFloat(int Index, int Dimension, float32 PreviousValue)
```
@param Index - Which sequential point
@param Dimension - Which Sobol dimension (0 to 15)
@param PreviousValue - The Sobol value for Index-1
@return Sobol-distributed random number between 0 and 1

### RandomSobolCell2D
```angelscript
FVector2D RandomSobolCell2D(int Index, int NumCells, FVector2D Cell, FVector2D Seed)
```
@param Index - Which sequential point in the cell (starting at 0)
@param NumCells - Size of cell grid, 1 to 32768. Rounded up to the next power of two
@param Cell - Give a point from this integer grid cell
@param Seed - Random 2D seed (components in the range 0-1) to randomize across multiple sequences
@return Sobol-distributed random 2D position in the given grid cell

### RandomSobolCell3D
```angelscript
FVector RandomSobolCell3D(int Index, int NumCells, FVector Cell, FVector Seed)
```
@param Index - Which sequential point in the cell (starting at 0)
@param NumCells - Size of cell grid, 1 to 1024. Rounded up to the next power of two
@param Cell - Give a point from this integer grid cell
@param Seed - Random 3D seed (components in the range 0-1) to randomize across multiple sequences
@return Sobol-distributed random 3D vector in the given grid cell

### RandomSobolFloat
```angelscript
float32 RandomSobolFloat(int Index, int Dimension, float32 Seed)
```
@param Index - Which sequential point
@param Dimension - Which Sobol dimension (0 to 15)
@param Seed - Random seed (in the range 0-1) to randomize across multiple sequences
@return Sobol-distributed random number between 0 and 1

