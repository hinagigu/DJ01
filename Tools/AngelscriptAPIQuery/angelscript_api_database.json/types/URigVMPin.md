# URigVMPin

**继承自**: `UObject`

The Pin represents a single connector / pin on a node in the RigVM model.
Pins can be connected based on rules. Pins also provide access to a 'PinPath',
which essentially represents . separated list of names to reach the pin within
the owning graph. PinPaths are unique.
In comparison to the EdGraph Pin the URigVMPin supports the concept of 'SubPins',
so child / parent relationships between pins. A FVector Pin for example might
have its X, Y and Z components as SubPins. Array Pins will have its elements as
SubPins, and so on.
A URigVMPin is owned solely by a URigVMNode.

## 方法

### ContainsWildCardSubPin
```angelscript
bool ContainsWildCardSubPin()
```
Returns true if any of the subpins is a wildcard

### FindLinkForPin
```angelscript
URigVMLink FindLinkForPin(const URigVMPin InOtherPin)
```
Returns the link that represents the connection
between this pin and InOtherPin. nullptr is returned
if the pins are not connected.

### FindSubPin
```angelscript
URigVMPin FindSubPin(FString InPinPath)
```
Returns a SubPin given a name / path or nullptr.

### GetAbsolutePinIndex
```angelscript
int GetAbsolutePinIndex()
```
Returns the absolute index of the Pin within the node / parent Pin

### GetArrayElementCppType
```angelscript
FString GetArrayElementCppType()
```
Returns the C++ data type of an element of the Pin array

### GetArraySize
```angelscript
int GetArraySize()
```
Returns the number of elements within an array Pin

### GetCPPType
```angelscript
FString GetCPPType()
```
Returns the C++ data type of the pin

### GetCPPTypeObject
```angelscript
UObject GetCPPTypeObject()
```
Returns the struct of the data type of the Pin,
or nullptr otherwise.

### GetCustomWidgetName
```angelscript
FName GetCustomWidgetName()
```
Returns the name of a custom widget to be used
for editing the Pin.

### GetDefaultValue
```angelscript
FString GetDefaultValue()
```
Returns the default value of the Pin as a string.
Note that this value is computed based on the Pin's
SubPins - so for example for a FVector typed Pin
the default value is actually composed out of the
default values of the X, Y and Z SubPins.

### GetDirection
```angelscript
ERigVMPinDirection GetDirection()
```
Returns the direction of the pin

### GetDisplayName
```angelscript
FName GetDisplayName()
```
Returns the display label of the pin

### GetEnum
```angelscript
UEnum GetEnum()
```
Returns the enum of the data type of the Pin,
or nullptr otherwise.

### GetGraph
```angelscript
URigVMGraph GetGraph()
```
Returns the graph of this Pin.

### GetLinkedSourcePins
```angelscript
TArray<URigVMPin> GetLinkedSourcePins(bool bRecursive)
```
Returns all of the linked source Pins,
using this Pin as the target.

### GetLinkedTargetPins
```angelscript
TArray<URigVMPin> GetLinkedTargetPins(bool bRecursive)
```
Returns all of the linked target Pins,
using this Pin as the source.

### GetLinks
```angelscript
TArray<URigVMLink> GetLinks()
```
Returns all of the links linked to this Pin.

### GetMetaData
```angelscript
FString GetMetaData(FName InKey)
```
Returns the keyed metadata associated with this pin, if any

### GetNode
```angelscript
URigVMNode GetNode()
```
Returns the node of this Pin.

### GetOriginalPinFromInjectedNode
```angelscript
URigVMPin GetOriginalPinFromInjectedNode()
```
Returns the original pin for a pin on an injected
node. This can be used to determine where a link
should go in the user interface

### GetParentPin
```angelscript
URigVMPin GetParentPin()
```
Returns the parent Pin - or nullptr if the Pin
is nested directly below a node.

### GetPinForLink
```angelscript
URigVMPin GetPinForLink()
```
Returns the pin to be used for a link.
This might differ from this actual pin, since
the pin might contain injected nodes.

### GetPinIndex
```angelscript
int GetPinIndex()
```
Returns the index of the Pin within the node / parent Pin

### GetPinPath
```angelscript
FString GetPinPath(bool bUseNodePath)
```
Returns a . separated path containing all names of the pin and its owners,
this includes the node name, for example "Node.Color.R"

### GetRootPin
```angelscript
URigVMPin GetRootPin()
```
Returns the top-most parent Pin, so for example
for "Node.Transform.Translation.X" this returns
the Pin for "Node.Transform".

### GetScriptStruct
```angelscript
UScriptStruct GetScriptStruct()
```
Returns the struct of the data type of the Pin,
or nullptr otherwise.

### GetSegmentPath
```angelscript
FString GetSegmentPath(bool bIncludeRootPin)
```
Returns a . separated path containing all names of the pin within its main
memory owner / storage. This is typically used to create an offset pointer
within memory (FRigVMRegisterOffset).
So for example for a PinPath such as "Node.Transform.Translation.X" the
corresponding SegmentPath is "Translation.X", since the transform is the
storage / memory.

### GetSourceLinks
```angelscript
TArray<URigVMLink> GetSourceLinks(bool bRecursive)
```
Returns all of the source pins
using this Pin as the target.

### GetSubPinPath
```angelscript
FString GetSubPinPath(const URigVMPin InParentPin, bool bIncludeParentPinName)
```
Returns a . separated path containing all names of the pin and its owners
until we hit the provided parent pin.

### GetSubPins
```angelscript
TArray<URigVMPin> GetSubPins()
```
Returns all of the SubPins of this one.

### GetTargetLinks
```angelscript
TArray<URigVMLink> GetTargetLinks(bool bRecursive)
```
Returns all of the target links,
using this Pin as the source.

### GetToolTipText
```angelscript
FText GetToolTipText()
```
Returns the tooltip of this pin

### IsArray
```angelscript
bool IsArray()
```
Returns true if the data type of the Pin is an array

### IsArrayElement
```angelscript
bool IsArrayElement()
```
Returns true if the Pin is a SubPin within an array

### IsDecoratorPin
```angelscript
bool IsDecoratorPin()
```
Returns true if this pin represents a decorator

### IsDefinedAsConstant
```angelscript
bool IsDefinedAsConstant()
```
Returns true if the pin is defined as a constant value / literal

### IsDynamicArray
```angelscript
bool IsDynamicArray()
```
Returns true if this pin represents a dynamic array

### IsEnum
```angelscript
bool IsEnum()
```
Returns true if the data type of the Pin is a enum

### IsExecuteContext
```angelscript
bool IsExecuteContext()
```
Returns true if the C++ data type is an execute context

### IsExpanded
```angelscript
bool IsExpanded()
```
Returns true if the pin is currently expanded

### IsFixedSizeArray
```angelscript
bool IsFixedSizeArray()
```
Returns true if this pin is an array that should be displayed as elements only

### IsInterface
```angelscript
bool IsInterface()
```
Returns true if the data type of the Pin is a interface

### IsLazy
```angelscript
bool IsLazy()
```
Returns true if this pin's value may be executed lazily

### IsLinkedTo
```angelscript
bool IsLinkedTo(const URigVMPin InPin)
```
Returns true if this Pin is linked to another Pin

### IsReferenceCountedContainer
```angelscript
bool IsReferenceCountedContainer()
```
Returns true if this data type is referenced counted

### IsRootPin
```angelscript
bool IsRootPin()
```
Returns true if this pin is a root pin

### IsStringType
```angelscript
bool IsStringType()
```
Returns true if the C++ data type is FString or FName

### IsStruct
```angelscript
bool IsStruct()
```
Returns true if the data type of the Pin is a struct

### IsStructMember
```angelscript
bool IsStructMember()
```
Returns true if the Pin is a SubPin within a struct

### IsUObject
```angelscript
bool IsUObject()
```
Returns true if the data type of the Pin is a uobject

### IsWildCard
```angelscript
bool IsWildCard()
```
Returns true if the C++ data type is unknown

### RequiresWatch
```angelscript
bool RequiresWatch(bool bCheckExposedPinChain)
```
Returns true if the pin should be watched

### ShouldHideSubPins
```angelscript
bool ShouldHideSubPins()
```
Returns true if this pin's subpins should be hidden in the UI

### ShouldOnlyShowSubPins
```angelscript
bool ShouldOnlyShowSubPins()
```
Returns true if this pin is an array that should be displayed as elements only

