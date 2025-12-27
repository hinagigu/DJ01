# UMetaSoundBuilderBase

**继承自**: `UObject`

Base implementation of MetaSound builder

## 方法

### AddGraphInputNode
```angelscript
FMetaSoundBuilderNodeOutputHandle AddGraphInputNode(FName Name, FName DataType, FMetasoundFrontendLiteral DefaultValue, EMetaSoundBuilderResult& OutResult, bool bIsConstructorInput)
```
Adds a graph input node with the given name, DataType, and sets the graph input to default value.
Returns the new input node's output handle if it was successfully created, or an invalid handle if it failed.

### AddGraphOutputNode
```angelscript
FMetaSoundBuilderNodeInputHandle AddGraphOutputNode(FName Name, FName DataType, FMetasoundFrontendLiteral DefaultValue, EMetaSoundBuilderResult& OutResult, bool bIsConstructorOutput)
```
Adds a graph output node with the given name, DataType, and sets output node's input to default value.
Returns the new output node's input handle if it was successfully created, or an invalid handle if it failed.

### AddInterface
```angelscript
void AddInterface(FName InterfaceName, EMetaSoundBuilderResult& OutResult)
```
Adds an interface registered with the given name to the graph, adding associated input and output nodes.

### AddNodeByClassName
```angelscript
FMetaSoundNodeHandle AddNodeByClassName(FMetasoundFrontendClassName ClassName, EMetaSoundBuilderResult& OutResult, int MajorVersion)
```
Adds node referencing the highest native class version of the given class name to the document.
Returns a node handle to the created node if successful, or an invalid handle if it failed.

### ConnectNodeInputsToMatchingGraphInterfaceInputs
```angelscript
TArray<FMetaSoundBuilderNodeOutputHandle> ConnectNodeInputsToMatchingGraphInterfaceInputs(FMetaSoundNodeHandle NodeHandle, EMetaSoundBuilderResult& OutResult)
```
Connects a given node's inputs to all graph inputs for shared interfaces implemented on both the node's referenced class and the builder's MetaSound graph. Returns outputs of connected input nodes.

### ConnectNodeInputToGraphInput
```angelscript
void ConnectNodeInputToGraphInput(FName GraphInputName, FMetaSoundBuilderNodeInputHandle NodeInputHandle, EMetaSoundBuilderResult& OutResult)
```
Connects a given node input to the graph input with the given name.

### ConnectNodeOutputsToMatchingGraphInterfaceOutputs
```angelscript
TArray<FMetaSoundBuilderNodeInputHandle> ConnectNodeOutputsToMatchingGraphInterfaceOutputs(FMetaSoundNodeHandle NodeHandle, EMetaSoundBuilderResult& OutResult)
```
Connects a given node's outputs to all graph outputs for shared interfaces implemented on both the node's referenced class and the builder's MetaSound graph. Returns inputs of connected output nodes.

### ConnectNodeOutputToGraphOutput
```angelscript
void ConnectNodeOutputToGraphOutput(FName GraphOutputName, FMetaSoundBuilderNodeOutputHandle NodeOutputHandle, EMetaSoundBuilderResult& OutResult)
```
Connects a given node output to the graph output with the given name.

### ConnectNodes
```angelscript
void ConnectNodes(FMetaSoundBuilderNodeOutputHandle NodeOutputHandle, FMetaSoundBuilderNodeInputHandle NodeInputHandle, EMetaSoundBuilderResult& OutResult)
```
Connects node output to a node input. Does *NOT* provide loop detection for performance reasons.  Loop detection is checked on class registration when built or played.
Returns succeeded if connection made, failed if connection already exists with input, the data types do not match, or the connection is not supported due to access type
incompatibility (ex. constructor input to non-constructor input).

### ConnectNodesByInterfaceBindings
```angelscript
void ConnectNodesByInterfaceBindings(FMetaSoundNodeHandle FromNodeHandle, FMetaSoundNodeHandle ToNodeHandle, EMetaSoundBuilderResult& OutResult)
```
Connects two nodes using defined MetaSound Interface Bindings registered with the MetaSound Interface registry.

### ContainsNode
```angelscript
bool ContainsNode(FMetaSoundNodeHandle Node)
```
Returns whether node exists.

### ContainsNodeInput
```angelscript
bool ContainsNodeInput(FMetaSoundBuilderNodeInputHandle Input)
```
Returns whether node input exists.

### ContainsNodeOutput
```angelscript
bool ContainsNodeOutput(FMetaSoundBuilderNodeOutputHandle Output)
```
Returns whether node output exists.

### ConvertFromPreset
```angelscript
void ConvertFromPreset(EMetaSoundBuilderResult& OutResult)
```
Converts this preset to a fully accessible MetaSound; sets result to succeeded if it was converted successfully and failed if it was not.

### DisconnectNodeInput
```angelscript
void DisconnectNodeInput(FMetaSoundBuilderNodeInputHandle NodeInputHandle, EMetaSoundBuilderResult& OutResult)
```
Removes connection to a given node input. Returns success if connection was removed, failed if not.

### DisconnectNodeOutput
```angelscript
void DisconnectNodeOutput(FMetaSoundBuilderNodeOutputHandle NodeOutputHandle, EMetaSoundBuilderResult& OutResult)
```
Removes all connections from a given node output. Returns success if all connections were removed, failed if not.

### DisconnectNodes
```angelscript
void DisconnectNodes(FMetaSoundBuilderNodeOutputHandle NodeOutputHandle, FMetaSoundBuilderNodeInputHandle NodeInputHandle, EMetaSoundBuilderResult& OutResult)
```
Disconnects node output to a node input. Returns success if connection was removed, failed if not.

### DisconnectNodesByInterfaceBindings
```angelscript
void DisconnectNodesByInterfaceBindings(FMetaSoundNodeHandle FromNodeHandle, FMetaSoundNodeHandle ToNodeHandle, EMetaSoundBuilderResult& OutResult)
```
Disconnects two nodes using defined MetaSound Interface Bindings registered with the MetaSound Interface registry. Returns success if
all connections were found and removed, failed if any connections were not.

### FindGraphInputNode
```angelscript
FMetaSoundNodeHandle FindGraphInputNode(FName InputName, EMetaSoundBuilderResult& OutResult)
```
Returns graph input node by the given name if it exists, or an invalid handle if not found.

### FindGraphOutputNode
```angelscript
FMetaSoundNodeHandle FindGraphOutputNode(FName OutputName, EMetaSoundBuilderResult& OutResult)
```
Returns graph output node by the given name if it exists, or an invalid handle if not found.

### FindInterfaceInputNodes
```angelscript
TArray<FMetaSoundNodeHandle> FindInterfaceInputNodes(FName InterfaceName, EMetaSoundBuilderResult& OutResult)
```
Returns input nodes associated with a given interface.

### FindInterfaceOutputNodes
```angelscript
TArray<FMetaSoundNodeHandle> FindInterfaceOutputNodes(FName InterfaceName, EMetaSoundBuilderResult& OutResult)
```
Returns output nodes associated with a given interface.

### FindNodeClassVersion
```angelscript
FMetasoundFrontendVersion FindNodeClassVersion(FMetaSoundNodeHandle NodeHandle, EMetaSoundBuilderResult& OutResult)
```
Returns output's parent node if the input is valid, otherwise returns invalid node handle.

### FindNodeInputByName
```angelscript
FMetaSoundBuilderNodeInputHandle FindNodeInputByName(FMetaSoundNodeHandle NodeHandle, FName InputName, EMetaSoundBuilderResult& OutResult)
```
Returns node input by the given name if it exists, or an invalid handle if not found.

### FindNodeInputParent
```angelscript
FMetaSoundNodeHandle FindNodeInputParent(FMetaSoundBuilderNodeInputHandle InputHandle, EMetaSoundBuilderResult& OutResult)
```
Returns input's parent node if the input is valid, otherwise returns invalid node handle.

### FindNodeInputs
```angelscript
TArray<FMetaSoundBuilderNodeInputHandle> FindNodeInputs(FMetaSoundNodeHandle NodeHandle, EMetaSoundBuilderResult& OutResult)
```
Returns all node inputs.

### FindNodeInputsByDataType
```angelscript
TArray<FMetaSoundBuilderNodeInputHandle> FindNodeInputsByDataType(FMetaSoundNodeHandle NodeHandle, EMetaSoundBuilderResult& OutResult, FName DataType)
```
Returns node inputs by the given DataType (ex. "Audio", "Trigger", "String", "Bool", "Float", "Int32", etc.).

### FindNodeOutputByName
```angelscript
FMetaSoundBuilderNodeOutputHandle FindNodeOutputByName(FMetaSoundNodeHandle NodeHandle, FName OutputName, EMetaSoundBuilderResult& OutResult)
```
Returns node output by the given name.

### FindNodeOutputParent
```angelscript
FMetaSoundNodeHandle FindNodeOutputParent(FMetaSoundBuilderNodeOutputHandle OutputHandle, EMetaSoundBuilderResult& OutResult)
```
Returns output's parent node if the input is valid, otherwise returns invalid node handle.

### FindNodeOutputs
```angelscript
TArray<FMetaSoundBuilderNodeOutputHandle> FindNodeOutputs(FMetaSoundNodeHandle NodeHandle, EMetaSoundBuilderResult& OutResult)
```
Returns all node outputs.

### FindNodeOutputsByDataType
```angelscript
TArray<FMetaSoundBuilderNodeOutputHandle> FindNodeOutputsByDataType(FMetaSoundNodeHandle NodeHandle, EMetaSoundBuilderResult& OutResult, FName DataType)
```
Returns node outputs by the given DataType (ex. "Audio", "Trigger", "String", "Bool", "Float", "Int32", etc.).

### GetNodeInputClassDefault
```angelscript
FMetasoundFrontendLiteral GetNodeInputClassDefault(FMetaSoundBuilderNodeInputHandle InputHandle, EMetaSoundBuilderResult& OutResult)
```
Returns node input's class literal value if set, otherwise fails and returns default literal.

### GetNodeInputData
```angelscript
void GetNodeInputData(FMetaSoundBuilderNodeInputHandle InputHandle, FName& Name, FName& DataType, EMetaSoundBuilderResult& OutResult)
```
Returns node input's data if valid (including things like name and datatype).

### GetNodeInputDefault
```angelscript
FMetasoundFrontendLiteral GetNodeInputDefault(FMetaSoundBuilderNodeInputHandle InputHandle, EMetaSoundBuilderResult& OutResult)
```
Returns node input's literal value if set on graph, otherwise fails and returns default literal.

### GetNodeInputIsConstructorPin
```angelscript
bool GetNodeInputIsConstructorPin(FMetaSoundBuilderNodeInputHandle InputHandle)
```
Returns whether the given node input is a constructor pin

### GetNodeOutputData
```angelscript
void GetNodeOutputData(FMetaSoundBuilderNodeOutputHandle OutputHandle, FName& Name, FName& DataType, EMetaSoundBuilderResult& OutResult)
```
Returns node output's data if valid (including things like name and datatype).

### GetNodeOutputIsConstructorPin
```angelscript
bool GetNodeOutputIsConstructorPin(FMetaSoundBuilderNodeOutputHandle OutputHandle)
```
Returns whether the given node output is a constructor pin

### GetReferencedPresetAsset
```angelscript
UObject GetReferencedPresetAsset()
```
Return the asset referenced by this preset builder. Returns nullptr if the builder is not a preset.

### InterfaceIsDeclared
```angelscript
bool InterfaceIsDeclared(FName InterfaceName)
```
Returns if a given interface is declared.

### IsPreset
```angelscript
bool IsPreset()
```
Returns whether this is a preset.

### NodeInputIsConnected
```angelscript
bool NodeInputIsConnected(FMetaSoundBuilderNodeInputHandle InputHandle)
```
Returns if a given node input has connections.

### NodeOutputIsConnected
```angelscript
bool NodeOutputIsConnected(FMetaSoundBuilderNodeOutputHandle OutputHandle)
```
Returns if a given node output is connected.

### NodesAreConnected
```angelscript
bool NodesAreConnected(FMetaSoundBuilderNodeOutputHandle OutputHandle, FMetaSoundBuilderNodeInputHandle InputHandle)
```
Returns if a given node output and node input are connected.

### RemoveGraphInput
```angelscript
void RemoveGraphInput(FName Name, EMetaSoundBuilderResult& OutResult)
```
Removes graph input if it exists; sets result to succeeded if it was removed and failed if it was not.

### RemoveGraphOutput
```angelscript
void RemoveGraphOutput(FName Name, EMetaSoundBuilderResult& OutResult)
```
Removes graph output if it exists; sets result to succeeded if it was removed and failed if it was not.

### RemoveInterface
```angelscript
void RemoveInterface(FName InterfaceName, EMetaSoundBuilderResult& OutResult)
```
Removes the interface with the given name from the builder's MetaSound. Removes any graph inputs
and outputs associated with the given interface and their respective connections (if any).

### RemoveNode
```angelscript
void RemoveNode(FMetaSoundNodeHandle NodeHandle, EMetaSoundBuilderResult& OutResult)
```
Removes node and any associated connections from the builder's MetaSound.

### RemoveNodeInputDefault
```angelscript
void RemoveNodeInputDefault(FMetaSoundBuilderNodeInputHandle InputHandle, EMetaSoundBuilderResult& OutResult)
```
Removes node input literal default if set, reverting the value to be whatever the node class defaults the value to.
Returns success if value was removed, false if not removed (i.e. wasn't set to begin with).

### SetGraphInputDefault
```angelscript
void SetGraphInputDefault(FName InputName, FMetasoundFrontendLiteral Literal, EMetaSoundBuilderResult& OutResult)
```
Sets the input node's default value, overriding the default provided by the referenced graph if the graph is a preset.

### SetNodeInputDefault
```angelscript
void SetNodeInputDefault(FMetaSoundBuilderNodeInputHandle NodeInputHandle, FMetasoundFrontendLiteral Literal, EMetaSoundBuilderResult& OutResult)
```
Sets the node's input default value (used if no connection to the given node input is present)

