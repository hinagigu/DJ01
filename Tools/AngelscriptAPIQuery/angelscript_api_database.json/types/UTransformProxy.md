# UTransformProxy

**继承自**: `UObject`

UTransformProxy is used to transform a set of sub-objects. An internal
FTransform is generated based on the sub-object set, and the relative
FTransform of each sub-object is stored. Then as this main transform
is updated, the sub-objects are also updated.

Currently only USceneComponent sub-objects are supported.

If only one sub-object is set, the main transform is the sub-object transform.
Otherwise the main transform is centered at the average origin and
has no rotation.

