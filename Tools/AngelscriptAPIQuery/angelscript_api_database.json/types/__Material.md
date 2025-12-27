# __Material

## 方法

### CreateDynamicMaterialInstance
```angelscript
UMaterialInstanceDynamic CreateDynamicMaterialInstance(UMaterialInterface Parent, FName OptionalName, EMIDCreationFlags CreationFlags)
```
Creates a Dynamic Material Instance which you can modify during gameplay.

### GetScalarParameterValue
```angelscript
float32 GetScalarParameterValue(UMaterialParameterCollection Collection, FName ParameterName)
```
Gets a scalar parameter value from the material collection instance. Logs if ParameterName is invalid.

### GetVectorParameterValue
```angelscript
FLinearColor GetVectorParameterValue(UMaterialParameterCollection Collection, FName ParameterName)
```
Gets a vector parameter value from the material collection instance. Logs if ParameterName is invalid.

### SetScalarParameterValue
```angelscript
void SetScalarParameterValue(UMaterialParameterCollection Collection, FName ParameterName, float32 ParameterValue)
```
Sets a scalar parameter value on the material collection instance. Logs if ParameterName is invalid.

### SetVectorParameterValue
```angelscript
void SetVectorParameterValue(UMaterialParameterCollection Collection, FName ParameterName, FLinearColor ParameterValue)
```
Sets a vector parameter value on the material collection instance. Logs if ParameterName is invalid.

