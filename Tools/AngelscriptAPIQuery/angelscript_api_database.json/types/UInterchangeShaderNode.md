# UInterchangeShaderNode

**继承自**: `UInterchangeBaseNode`

A shader node is a named set of inputs and outputs. It can be connected to other shader nodes and finally to a shader graph input.

## 方法

### AddFloatInput
```angelscript
bool AddFloatInput(FString InputName, float32 AttributeValue, bool bIsAParameter)
```
Set the Float Attribute on the Shader Node. If bIsAParameter is set to true, it would be treated as a ScalarParameter
when the Material Pipeline creates the materials. Otherwise it would be a constant expression in the shader graph.
Note: It is assumed that the input name would be the parameter name when bIsAParameter is true.

### AddLinearColorInput
```angelscript
bool AddLinearColorInput(FString InputName, FLinearColor AttributeValue, bool bIsAParameter)
```
Set the Linear Color Attribute on the Shader Node. If bIsAParameter is set to true, it would be treated as a VectorParameter
when the Material Pipeline creates the materials. Otherwise it would be a constant 3 vector expression in the shader graph.
Note: It is assumed that the input name would be the parameter name when bIsAParameter is true.

### AddStringInput
```angelscript
bool AddStringInput(FString InputName, FString AttributeValue, bool bIsAParameter)
```
Set the String Attribute on the Shader Node. If bIsAParameter is set to true, it would be treated as a overridable Texture
or else it should be treated as a LUT Texture.
Note: It is assumed that the input name would be the parameter name when bIsAParameter is true.

### GetCustomShaderType
```angelscript
bool GetCustomShaderType(FString& AttributeValue)
```

### SetCustomShaderType
```angelscript
bool SetCustomShaderType(FString AttributeValue)
```
Sets which type of shader this nodes represents. Can be arbitrary or one of the predefined shader types.
The material pipeline handling the shader node should be aware of the shader type that is being set here.

