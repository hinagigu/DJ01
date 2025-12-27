# UMaterialParameterCollection

**继承自**: `UObject`

Asset class that contains a list of parameter names and their default values.
Any number of materials can reference these parameters and get new values when the parameter values are changed.

## 属性

### ScalarParameters
- **类型**: `TArray<FCollectionScalarParameter>`

### VectorParameters
- **类型**: `TArray<FCollectionVectorParameter>`

## 方法

### GetScalarParameterDefaultValue
```angelscript
float32 GetScalarParameterDefaultValue(FName ParameterName, bool& bParameterFound)
```
Gets the default value of a scalar parameter from a material collection.
@param ParameterName - The name of the value to get the value of
@param bParameterFound - if a parameter with the input name was found
@returns the value of the parameter

### GetScalarParameterNames
```angelscript
TArray<FName> GetScalarParameterNames()
```
Returns an array of the names of all the scalar parameters in this Material Parameter Collection *

### GetVectorParameterDefaultValue
```angelscript
FLinearColor GetVectorParameterDefaultValue(FName ParameterName, bool& bParameterFound)
```
Gets the default value of a scalar parameter from a material collection.
@param ParameterName - The name of the value to get the value of
@param bParameterFound - if a parameter with the input name was found
@returns the value of the parameter

### GetVectorParameterNames
```angelscript
TArray<FName> GetVectorParameterNames()
```
Returns an array of the names of all the vector parameters in this Material Parameter Collection *

