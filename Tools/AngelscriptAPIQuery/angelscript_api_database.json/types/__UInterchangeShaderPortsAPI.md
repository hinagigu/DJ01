# __UInterchangeShaderPortsAPI

## 方法

### ConnectDefaultOuputToInput
```angelscript
bool ConnectDefaultOuputToInput(UInterchangeBaseNode InterchangeNode, FString InputName, FString ExpressionUid)
```
Adds an input connection attribute.
@param InterchangeNode       The node to create the input on.
@param InputName                     The name to give to the input.
@param ExpressionUid         The unique ID of the node to connect to the input.
@return                                      True if the input connection was successfully added to the node.

### ConnectOuputToInputByIndex
```angelscript
bool ConnectOuputToInputByIndex(UInterchangeBaseNode InterchangeNode, FString InputName, FString ExpressionUid, int OutputIndex)
```
Adds an input connection attribute.
@param InterchangeNode       The node to create the input on.
@param InputName                     The name to give to the input.
@param ExpressionUid         The unique ID of the node to connect to the input.
@param OutputIndex           The index of the output from ExpressionUid to connect to the input.
@return                                      True if the input connection was successfully added to the node.
OutputIndex is encoded in a string in the following pattern: ExpressionUid:OutputByIndex:FString::FromInt(OutputIndex)
The index should be retrieved using UInterchangeShaderPortsAPI::GetOutputIndexFromName().

### ConnectOuputToInputByName
```angelscript
bool ConnectOuputToInputByName(UInterchangeBaseNode InterchangeNode, FString InputName, FString ExpressionUid, FString OutputName)
```
Adds an input connection attribute.
@param InterchangeNode       The node to create the input on.
@param InputName                     The name to give to the input.
@param ExpressionUid         The unique ID of the node to connect to the input.
@param OutputName            The name of the output from ExpressionUid to connect to the input.
@return                                      True if the input connection was successfully added to the node.

### GatherInputs
```angelscript
void GatherInputs(const UInterchangeBaseNode InterchangeNode, TArray<FString>& OutInputNames)
```
Retrieves the names of all the inputs for a given node.

### GetInputConnection
```angelscript
bool GetInputConnection(const UInterchangeBaseNode InterchangeNode, FString InputName, FString& OutExpressionUid, FString& OutputName)
```
Retrieves the node unique id and the output name connected to a given input, if any.

### HasInput
```angelscript
bool HasInput(const UInterchangeBaseNode InterchangeNode, FName InInputName)
```
Checks whether a particular input exists on a given node.

### HasParameter
```angelscript
bool HasParameter(const UInterchangeBaseNode InterchangeNode, FName InInputName)
```
Checks whether a particular input exists as a parameter on a given node.

### IsAnInput
```angelscript
bool IsAnInput(FString AttributeKey)
```
Returns true if the attribute key is associated with an input (starts with "Inputs:").

### IsAParameter
```angelscript
bool IsAParameter(FString AttributeKey)
```
Returns true if the attribute key is an input that represents parameters (ends with ":Parameter").

### MakeInputConnectionKey
```angelscript
FString MakeInputConnectionKey(FString InputName)
```
Makes an attribute key to represent a node being connected to an input (that is, Inputs:InputName:Connect).

### MakeInputName
```angelscript
FString MakeInputName(FString InputKey)
```
From an attribute key associated with an input (that is, Inputs:InputName:Value), retrieves the input name.

### MakeInputParameterKey
```angelscript
FString MakeInputParameterKey(FString InputName)
```
Makes an attribute key to represent a parameter being given to an input (that is, Inputs:InputName:Parameter).
This is more relevant to Materials, but could be used to differentiate between constant values and parameters.

### MakeInputValueKey
```angelscript
FString MakeInputValueKey(FString InputName)
```
Makes an attribute key to represent a value being given to an input (that is, Inputs:InputName:Value).

### StaticClass
```angelscript
UClass StaticClass()
```

