# __NiagaraDataInterfaceArray

## 方法

### GetNiagaraArrayBool
```angelscript
TArray<bool> GetNiagaraArrayBool(UNiagaraComponent NiagaraSystem, FName OverrideName)
```
Gets a copy of Niagara Bool Data.

### GetNiagaraArrayBoolValue
```angelscript
bool GetNiagaraArrayBoolValue(UNiagaraComponent NiagaraSystem, FName OverrideName, int Index)
```
Gets a single value within a Niagara Array Bool.

### GetNiagaraArrayColor
```angelscript
TArray<FLinearColor> GetNiagaraArrayColor(UNiagaraComponent NiagaraSystem, FName OverrideName)
```
Gets a copy of Niagara FLinearColor Data.

### GetNiagaraArrayColorValue
```angelscript
FLinearColor GetNiagaraArrayColorValue(UNiagaraComponent NiagaraSystem, FName OverrideName, int Index)
```
Gets a single value within a Niagara Array FLinearColor.

### GetNiagaraArrayFloat
```angelscript
TArray<float32> GetNiagaraArrayFloat(UNiagaraComponent NiagaraSystem, FName OverrideName)
```
Gets a copy of Niagara Float Data.

### GetNiagaraArrayFloatValue
```angelscript
float32 GetNiagaraArrayFloatValue(UNiagaraComponent NiagaraSystem, FName OverrideName, int Index)
```
Gets a single value within a Niagara Array Float.

### GetNiagaraArrayInt32
```angelscript
TArray<int> GetNiagaraArrayInt32(UNiagaraComponent NiagaraSystem, FName OverrideName)
```
Gets a copy of Niagara Int32 Data.

### GetNiagaraArrayInt32Value
```angelscript
int GetNiagaraArrayInt32Value(UNiagaraComponent NiagaraSystem, FName OverrideName, int Index)
```
Gets a single value within a Niagara Array Int32.

### GetNiagaraArrayMatrix
```angelscript
TArray<FMatrix> GetNiagaraArrayMatrix(UNiagaraComponent NiagaraSystem, FName OverrideName, bool bApplyLWCRebase)
```
Gets a copy of Niagara FMatrix Data.
@param bApplyLWCRebase When enabled the matrix translation will have the simulation tile offset added to it

### GetNiagaraArrayMatrixValue
```angelscript
FMatrix GetNiagaraArrayMatrixValue(UNiagaraComponent NiagaraSystem, FName OverrideName, int Index, bool bApplyLWCRebase)
```
Gets a single value within a Niagara Array FMatrix.
@param bApplyLWCRebase When enabled the matrix translation will have the simulation tile offset added to it

### GetNiagaraArrayPosition
```angelscript
TArray<FVector> GetNiagaraArrayPosition(UNiagaraComponent NiagaraSystem, FName OverrideName)
```
Gets a copy of Niagara Position Data.

### GetNiagaraArrayPositionValue
```angelscript
FVector GetNiagaraArrayPositionValue(UNiagaraComponent NiagaraSystem, FName OverrideName, int Index)
```
Gets a single value within a Niagara Array Position.

### GetNiagaraArrayQuat
```angelscript
TArray<FQuat> GetNiagaraArrayQuat(UNiagaraComponent NiagaraSystem, FName OverrideName)
```
Gets a copy of Niagara FQuat Data.

### GetNiagaraArrayQuatValue
```angelscript
FQuat GetNiagaraArrayQuatValue(UNiagaraComponent NiagaraSystem, FName OverrideName, int Index)
```
Gets a single value within a Niagara Array FQuat.

### GetNiagaraArrayUInt8
```angelscript
TArray<int> GetNiagaraArrayUInt8(UNiagaraComponent NiagaraSystem, FName OverrideName)
```
Gets a copy of Niagara UInt8 Data.

### GetNiagaraArrayUInt8Value
```angelscript
int GetNiagaraArrayUInt8Value(UNiagaraComponent NiagaraSystem, FName OverrideName, int Index)
```
Gets a single value within a Niagara Array UInt8.

### GetNiagaraArrayVector
```angelscript
TArray<FVector> GetNiagaraArrayVector(UNiagaraComponent NiagaraSystem, FName OverrideName)
```
Gets a copy of Niagara FVector Data.

### GetNiagaraArrayVector2D
```angelscript
TArray<FVector2D> GetNiagaraArrayVector2D(UNiagaraComponent NiagaraSystem, FName OverrideName)
```
Gets a copy of Niagara FVector2D Data.

### GetNiagaraArrayVector2DValue
```angelscript
FVector2D GetNiagaraArrayVector2DValue(UNiagaraComponent NiagaraSystem, FName OverrideName, int Index)
```
Gets a single value within a Niagara Array FVector2D.

### GetNiagaraArrayVector4
```angelscript
TArray<FVector4> GetNiagaraArrayVector4(UNiagaraComponent NiagaraSystem, FName OverrideName)
```
Gets a copy of Niagara FVector4 Data.

### GetNiagaraArrayVector4Value
```angelscript
FVector4 GetNiagaraArrayVector4Value(UNiagaraComponent NiagaraSystem, FName OverrideName, int Index)
```
Gets a single value within a Niagara Array FVector4.

### GetNiagaraArrayVectorValue
```angelscript
FVector GetNiagaraArrayVectorValue(UNiagaraComponent NiagaraSystem, FName OverrideName, int Index)
```
Gets a single value within a Niagara Array FVector.

### SetNiagaraArrayBool
```angelscript
void SetNiagaraArrayBool(UNiagaraComponent NiagaraSystem, FName OverrideName, TArray<bool> ArrayData)
```
Sets Niagara Array Bool Data.

### SetNiagaraArrayBoolValue
```angelscript
void SetNiagaraArrayBoolValue(UNiagaraComponent NiagaraSystem, FName OverrideName, int Index, bool Value, bool bSizeToFit)
```
Sets a single value within a Niagara Array Bool.

### SetNiagaraArrayColor
```angelscript
void SetNiagaraArrayColor(UNiagaraComponent NiagaraSystem, FName OverrideName, TArray<FLinearColor> ArrayData)
```
Sets Niagara Array FLinearColor Data.

### SetNiagaraArrayColorValue
```angelscript
void SetNiagaraArrayColorValue(UNiagaraComponent NiagaraSystem, FName OverrideName, int Index, FLinearColor Value, bool bSizeToFit)
```
Sets a single value within a Niagara Array FLinearColor.

### SetNiagaraArrayFloat
```angelscript
void SetNiagaraArrayFloat(UNiagaraComponent NiagaraSystem, FName OverrideName, TArray<float32> ArrayData)
```
Sets Niagara Array Float Data.

### SetNiagaraArrayFloatValue
```angelscript
void SetNiagaraArrayFloatValue(UNiagaraComponent NiagaraSystem, FName OverrideName, int Index, float32 Value, bool bSizeToFit)
```
Sets a single value within a Niagara Array Float.

### SetNiagaraArrayInt32
```angelscript
void SetNiagaraArrayInt32(UNiagaraComponent NiagaraSystem, FName OverrideName, TArray<int> ArrayData)
```
Sets Niagara Array Int32 Data.

### SetNiagaraArrayInt32Value
```angelscript
void SetNiagaraArrayInt32Value(UNiagaraComponent NiagaraSystem, FName OverrideName, int Index, int Value, bool bSizeToFit)
```
Sets a single value within a Niagara Array Int32.

### SetNiagaraArrayMatrix
```angelscript
void SetNiagaraArrayMatrix(UNiagaraComponent NiagaraSystem, FName OverrideName, TArray<FMatrix> ArrayData, bool bApplyLWCRebase)
```
Sets Niagara Array FMatrix Data.
@param bApplyLWCRebase When enabled the matrix translation will have the simulation tile offset subtracted from it

### SetNiagaraArrayMatrixValue
```angelscript
void SetNiagaraArrayMatrixValue(UNiagaraComponent NiagaraSystem, FName OverrideName, int Index, FMatrix Value, bool bSizeToFit, bool bApplyLWCRebase)
```
Sets a single value within a Niagara Array FMatrix.
@param bApplyLWCRebase When enabled the matrix translation will have the simulation tile offset subtracted from it

### SetNiagaraArrayPosition
```angelscript
void SetNiagaraArrayPosition(UNiagaraComponent NiagaraSystem, FName OverrideName, TArray<FVector> ArrayData)
```
Sets Niagara Array FVector Data.

### SetNiagaraArrayPositionValue
```angelscript
void SetNiagaraArrayPositionValue(UNiagaraComponent NiagaraSystem, FName OverrideName, int Index, FVector Value, bool bSizeToFit)
```

### SetNiagaraArrayQuat
```angelscript
void SetNiagaraArrayQuat(UNiagaraComponent NiagaraSystem, FName OverrideName, TArray<FQuat> ArrayData)
```
Sets Niagara Array FQuat Data.

### SetNiagaraArrayQuatValue
```angelscript
void SetNiagaraArrayQuatValue(UNiagaraComponent NiagaraSystem, FName OverrideName, int Index, FQuat Value, bool bSizeToFit)
```
Sets a single value within a Niagara Array FQuat.

### SetNiagaraArrayUInt8
```angelscript
void SetNiagaraArrayUInt8(UNiagaraComponent NiagaraSystem, FName OverrideName, TArray<int> ArrayData)
```
Sets Niagara Array UInt8 Data.

### SetNiagaraArrayUInt8Value
```angelscript
void SetNiagaraArrayUInt8Value(UNiagaraComponent NiagaraSystem, FName OverrideName, int Index, int Value, bool bSizeToFit)
```
Sets a single value within a Niagara Array UInt8.

### SetNiagaraArrayVector
```angelscript
void SetNiagaraArrayVector(UNiagaraComponent NiagaraSystem, FName OverrideName, TArray<FVector> ArrayData)
```
Sets Niagara Array FVector Data.

### SetNiagaraArrayVector2D
```angelscript
void SetNiagaraArrayVector2D(UNiagaraComponent NiagaraSystem, FName OverrideName, TArray<FVector2D> ArrayData)
```
Sets Niagara Array FVector2D Data.

### SetNiagaraArrayVector2DValue
```angelscript
void SetNiagaraArrayVector2DValue(UNiagaraComponent NiagaraSystem, FName OverrideName, int Index, FVector2D Value, bool bSizeToFit)
```
Sets a single value within a Niagara Array FVector2D.

### SetNiagaraArrayVector4
```angelscript
void SetNiagaraArrayVector4(UNiagaraComponent NiagaraSystem, FName OverrideName, TArray<FVector4> ArrayData)
```
Sets Niagara Array FVector4 Data.

### SetNiagaraArrayVector4Value
```angelscript
void SetNiagaraArrayVector4Value(UNiagaraComponent NiagaraSystem, FName OverrideName, int Index, FVector4 Value, bool bSizeToFit)
```
Sets a single value within a Niagara Array FVector4.

### SetNiagaraArrayVectorValue
```angelscript
void SetNiagaraArrayVectorValue(UNiagaraComponent NiagaraSystem, FName OverrideName, int Index, FVector Value, bool bSizeToFit)
```
Sets a single value within a Niagara Array FVector.

