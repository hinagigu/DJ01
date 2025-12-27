# __UAnimationCurveIdentifierExtensions

## 方法

### GetName
```angelscript
FName GetName(FAnimationCurveIdentifier& Identifier)
```
@return       The name used for displaying the Curve Identifier

### GetTransformChildCurveIdentifier
```angelscript
bool GetTransformChildCurveIdentifier(FAnimationCurveIdentifier& InOutIdentifier, ETransformCurveChannel Channel, EVectorCurveChannel Axis)
```
Converts a valid FAnimationCurveIdentifier instance with RCT_Transform curve type to target a child curve.

@param        InOutIdentifier         [out] Identifier to be converted
@param        Channel                         Channel to target
@param        Axis                            Axis within channel to target

@return       Valid FAnimationCurveIdentifier if the operation was successful

### GetType
```angelscript
ERawCurveTrackTypes GetType(FAnimationCurveIdentifier& Identifier)
```
@return       The animation curve type for the curve represented by the Curve Identifier

### IsValid
```angelscript
bool IsValid(FAnimationCurveIdentifier& Identifier)
```
@return       Whether or not the Curve Identifier is valid

### SetCurveIdentifier
```angelscript
void SetCurveIdentifier(FAnimationCurveIdentifier& InOutIdentifier, FName Name, ERawCurveTrackTypes CurveType)
```
Constructs a valid FAnimationCurveIdentifier instance.

@param        InOutIdentifier         The identifier to set up
@param        Name                            Name of the curve to find or add
@param        CurveType                       Type of the curve to find or add

### StaticClass
```angelscript
UClass StaticClass()
```

