# __UAnimationAttributeIdentifierExtensions

## 方法

### CreateAttributeIdentifier
```angelscript
FAnimationAttributeIdentifier CreateAttributeIdentifier(UAnimationAsset AnimationAsset, FName AttributeName, FName BoneName, UScriptStruct AttributeType, bool bValidateExistsOnAsset)
```
Constructs a valid FAnimationAttributeIdentifier instance. Ensuring that the underlying BoneName exists on the Skeleton for the provided AnimationAsset.

@param        AnimationAsset                  Animation asset to retrieve Skeleton from
@param        AttributeName                   Name of the attribute
@param        BoneName                                Name of the bone this attribute should be attributed to
@param        AttributeType                   Type of the underlying data (to-be) stored by this attribute
@param        bValidateExistsOnAsset  Whether or not the attribute should exist on the AnimationAsset. False by default.

@return       Valid FAnimationCurveIdentifier if the operation was successful

### IsValid
```angelscript
bool IsValid(FAnimationAttributeIdentifier& Identifier)
```
@return       Whether or not the Attribute Identifier is valid

### StaticClass
```angelscript
UClass StaticClass()
```

