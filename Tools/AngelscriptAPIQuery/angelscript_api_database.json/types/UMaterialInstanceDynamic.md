# UMaterialInstanceDynamic

**继承自**: `UMaterialInstance`

## 方法

### CopyParameterOverrides
```angelscript
void CopyParameterOverrides(UMaterialInstance MaterialInstance)
```
Copy parameter values from another material instance. This will copy only
parameters explicitly overridden in that material instance!!

### InitializeScalarParameterAndGetIndex
```angelscript
bool InitializeScalarParameterAndGetIndex(FName ParameterName, float32 Value, int& OutParameterIndex)
```
Use this function to set an initial value and fetch the index for use in SetScalarParameterByIndex.  This
function should only be called once for a particular name, and then use SetScalarParameterByIndex for subsequent
calls.  However, beware using this except in cases where optimization is critical, which is generally only if
you're using an unusually high number of parameters in a material and setting a large number of parameters in the
same frame.  Also, if the material is changed in any way that can change the parameter list, the index can be
invalidated.

### CopyMaterialInstanceParameters
```angelscript
void CopyMaterialInstanceParameters(UMaterialInterface Source, bool bQuickParametersOnly)
```
Copies over parameters given a material interface (copy each instance following the hierarchy)
Very slow implementation, avoid using at runtime. Hopefully we can replace it later with something like CopyInterpParameters()
The output is the object itself (this). Copying 'quick parameters only' will result in a much
faster copy process but will only copy dynamic scalar, vector and texture parameters on clients.
@param bQuickParametersOnly Copy scalar, vector and texture parameters only. Much faster but may not include required data

### GetScalarParameterValue
```angelscript
float32 GetScalarParameterValue(FName ParameterName)
```
Get the current scalar (float) parameter value from an MID

### GetScalarParameterValueByInfo
```angelscript
float32 GetScalarParameterValueByInfo(FMaterialParameterInfo ParameterInfo)
```
Get the current scalar (float) parameter value from an MID, using MPI (to allow access to layer parameters)

### GetTextureParameterValue
```angelscript
UTexture GetTextureParameterValue(FName ParameterName)
```
Get the current MID texture parameter value

### GetTextureParameterValueByInfo
```angelscript
UTexture GetTextureParameterValueByInfo(FMaterialParameterInfo ParameterInfo)
```
Get the current MID texture parameter value, using MPI (to allow access to layer parameters)

### GetVectorParameterValue
```angelscript
FLinearColor GetVectorParameterValue(FName ParameterName)
```
Get the current MID vector parameter value

### GetVectorParameterValueByInfo
```angelscript
FLinearColor GetVectorParameterValueByInfo(FMaterialParameterInfo ParameterInfo)
```
Get the current MID vector parameter value, using MPI (to allow access to layer parameters)

### InterpolateMaterialInstanceParameters
```angelscript
void InterpolateMaterialInstanceParameters(UMaterialInstance SourceA, UMaterialInstance SourceB, float32 Alpha)
```
Interpolates the scalar and vector parameters of this material instance based on two other material instances, and an alpha blending factor
The output is the object itself (this).
Supports the case SourceA==this || SourceB==this
Both material have to be from the same base material
@param SourceA value that is used for Alpha=0, silently ignores the case if 0
@param SourceB value that is used for Alpha=1, silently ignores the case if 0
@param Alpha usually in the range 0..1, values outside the range extrapolate

### SetDoubleVectorParameterValue
```angelscript
void SetDoubleVectorParameterValue(FName ParameterName, FVector4 Value)
```
Set an MID vector parameter value

### SetRuntimeVirtualTextureParameterValue
```angelscript
void SetRuntimeVirtualTextureParameterValue(FName ParameterName, URuntimeVirtualTexture Value)
```
Set an MID texture parameter value

### SetRuntimeVirtualTextureParameterValueByInfo
```angelscript
void SetRuntimeVirtualTextureParameterValueByInfo(FMaterialParameterInfo ParameterInfo, URuntimeVirtualTexture Value)
```
Set an MID texture parameter value using MPI (to allow access to layer parameters)

### SetScalarParameterByIndex
```angelscript
bool SetScalarParameterByIndex(int ParameterIndex, float32 Value)
```
Use the cached value of OutParameterIndex from InitializeScalarParameterAndGetIndex to set the scalar parameter
ONLY on the exact same MID.  Do NOT presume the index can be used from one instance on another.  Only use this
pair of functions when optimization is critical; otherwise use either SetScalarParameterValueByInfo or
SetScalarParameterValue.

### SetScalarParameterValue
```angelscript
void SetScalarParameterValue(FName ParameterName, float32 Value)
```
Set a MID scalar (float) parameter value

### SetScalarParameterValueByInfo
```angelscript
void SetScalarParameterValueByInfo(FMaterialParameterInfo ParameterInfo, float32 Value)
```
Set a MID scalar (float) parameter value using MPI (to allow access to layer parameters)

### SetSparseVolumeTextureParameterValue
```angelscript
void SetSparseVolumeTextureParameterValue(FName ParameterName, USparseVolumeTexture Value)
```
Set an MID texture parameter value

### SetTextureParameterValue
```angelscript
void SetTextureParameterValue(FName ParameterName, UTexture Value)
```
Set an MID texture parameter value

### SetTextureParameterValueByInfo
```angelscript
void SetTextureParameterValueByInfo(FMaterialParameterInfo ParameterInfo, UTexture Value)
```
Set an MID texture parameter value using MPI (to allow access to layer parameters)

### SetVectorParameterValue
```angelscript
void SetVectorParameterValue(FName ParameterName, FLinearColor Value)
```
Set an MID vector parameter value

### SetVectorParameterValueByInfo
```angelscript
void SetVectorParameterValueByInfo(FMaterialParameterInfo ParameterInfo, FLinearColor Value)
```
Set an MID vector parameter value, using MPI (to allow access to layer parameters)

