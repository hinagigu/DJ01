# UInterchangeUserDefinedAttributesAPI

**继承自**: `UObject`

UInterchangeUserDefinedAttributesAPI is used to store and retrieve user-defined attributes such as DCC node attributes, so that pipelines have access to those attributes.
Every user-defined attribute has a name, a value, and an optional AnimationPayloadKey: an FRichCurve that is a float curve.
The value type must be supported by the UE::Interchange::EAttributeTypes enumeration.

