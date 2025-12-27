# USplineMeshComponent

**继承自**: `UStaticMeshComponent`

A Spline Mesh Component is a derivation of a Static Mesh Component which can be deformed using a spline. Only a start and end position (and tangent) can be specified.
@see https://docs.unrealengine.com/latest/INT/Resources/ContentExamples/Blueprint_Splines

## 属性

### SplineParams
- **类型**: `FSplineMeshParams`
- **描述**: Spline that is used to deform mesh

### SplineBoundaryMin
- **类型**: `float32`
- **描述**: Minimum coordinate along the spline forward axis which corresponds to start of spline. If set to 0.0, will use bounding box to determine bounds

### SplineBoundaryMax
- **类型**: `float32`
- **描述**: Maximum coordinate along the spline forward axis which corresponds to end of spline. If set to 0.0, will use bounding box to determine bounds

### bAllowSplineEditingPerInstance
- **类型**: `bool`

### bSmoothInterpRollScale
- **类型**: `bool`

### bNeverNeedsCookedCollisionData
- **类型**: `bool`

## 方法

### GetBoundaryMax
```angelscript
float32 GetBoundaryMax()
```
Get the boundary max

### GetBoundaryMin
```angelscript
float32 GetBoundaryMin()
```
Get the boundary min

### GetEndOffset
```angelscript
FVector2D GetEndOffset()
```
Get the end offset

### GetEndPosition
```angelscript
FVector GetEndPosition()
```
Get the end position of spline in local space

### GetEndRoll
```angelscript
float32 GetEndRoll()
```
Get the end roll, in radians

### GetEndScale
```angelscript
FVector2D GetEndScale()
```
Get the end scaling

### GetEndTangent
```angelscript
FVector GetEndTangent()
```
Get the end tangent vector of spline in local space

### GetForwardAxis
```angelscript
ESplineMeshAxis GetForwardAxis()
```
Get the forward axis

### GetSplineUpDir
```angelscript
FVector GetSplineUpDir()
```
Get the spline up direction

### GetStartOffset
```angelscript
FVector2D GetStartOffset()
```
Get the start offset

### GetStartPosition
```angelscript
FVector GetStartPosition()
```
Get the start position of spline in local space

### GetStartRoll
```angelscript
float32 GetStartRoll()
```
Get the start roll, in radians

### GetStartScale
```angelscript
FVector2D GetStartScale()
```
Get the start scaling

### GetStartTangent
```angelscript
FVector GetStartTangent()
```
Get the start tangent vector of spline in local space

### SetBoundaryMax
```angelscript
void SetBoundaryMax(float32 InBoundaryMax, bool bUpdateMesh)
```
Set the boundary max

### SetBoundaryMin
```angelscript
void SetBoundaryMin(float32 InBoundaryMin, bool bUpdateMesh)
```
Set the boundary min

### SetEndOffset
```angelscript
void SetEndOffset(FVector2D EndOffset, bool bUpdateMesh)
```
Set the end offset

### SetEndPosition
```angelscript
void SetEndPosition(FVector EndPos, bool bUpdateMesh)
```
Set the end position of spline in local space

### SetEndRoll
```angelscript
void SetEndRoll(float32 EndRoll, bool bUpdateMesh)
```
Set the end roll, in radians

### SetEndRollDegrees
```angelscript
void SetEndRollDegrees(float32 EndRollDegrees, bool bUpdateMesh)
```
Set the end roll in degrees

### SetEndScale
```angelscript
void SetEndScale(FVector2D EndScale, bool bUpdateMesh)
```
Set the end scaling

### SetEndTangent
```angelscript
void SetEndTangent(FVector EndTangent, bool bUpdateMesh)
```
Set the end tangent vector of spline in local space

### SetForwardAxis
```angelscript
void SetForwardAxis(ESplineMeshAxis InForwardAxis, bool bUpdateMesh)
```
Set the forward axis

### SetSplineUpDir
```angelscript
void SetSplineUpDir(FVector InSplineUpDir, bool bUpdateMesh)
```
Set the spline up direction

### SetStartAndEnd
```angelscript
void SetStartAndEnd(FVector StartPos, FVector StartTangent, FVector EndPos, FVector EndTangent, bool bUpdateMesh)
```
Set the start and end, position and tangent, all in local space

### SetStartOffset
```angelscript
void SetStartOffset(FVector2D StartOffset, bool bUpdateMesh)
```
Set the start offset

### SetStartPosition
```angelscript
void SetStartPosition(FVector StartPos, bool bUpdateMesh)
```
Set the start position of spline in local space

### SetStartRoll
```angelscript
void SetStartRoll(float32 StartRoll, bool bUpdateMesh)
```
Set the start roll, in radians

### SetStartRollDegrees
```angelscript
void SetStartRollDegrees(float32 StartRollDegrees, bool bUpdateMesh)
```
Set the start roll in degrees

### SetStartScale
```angelscript
void SetStartScale(FVector2D StartScale, bool bUpdateMesh)
```
Set the start scaling

### SetStartTangent
```angelscript
void SetStartTangent(FVector StartTangent, bool bUpdateMesh)
```
Set the start tangent vector of spline in local space

### UpdateMesh
```angelscript
void UpdateMesh()
```
Update the collision and render state on the spline mesh following changes to its geometry

