# UPropertyBag

**继承自**: `UScriptStruct`

A script struct that is used to store the value of the property bag instance.
References to UPropertyBag cannot be serialized, instead the array of the properties
is serialized and new class is create on load based on the composition of the properties.

Note: Should not be used directly.

