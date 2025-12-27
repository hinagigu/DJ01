# FVector

## 属性

### X
- **类型**: `float`

### Y
- **类型**: `float`

### Z
- **类型**: `float`

## 方法

### opAssign
```angelscript
FVector& opAssign(FVector Other)
```

### opAdd
```angelscript
FVector opAdd(FVector Other)
```

### opSub
```angelscript
FVector opSub(FVector Other)
```

### opMul
```angelscript
FVector opMul(FVector Other)
```

### opDiv
```angelscript
FVector opDiv(FVector Other)
```

### opMul
```angelscript
FVector opMul(float Scale)
```

### opDiv
```angelscript
FVector opDiv(float Scale)
```

### opNeg
```angelscript
FVector opNeg()
```

### opMulAssign
```angelscript
FVector opMulAssign(float Scale)
```

### opDivAssign
```angelscript
FVector opDivAssign(float Scale)
```

### opMulAssign
```angelscript
FVector opMulAssign(FVector Other)
```

### opDivAssign
```angelscript
FVector opDivAssign(FVector Other)
```

### opAddAssign
```angelscript
FVector opAddAssign(FVector Other)
```

### opSubAssign
```angelscript
FVector opSubAssign(FVector Other)
```

### opIndex
```angelscript
float& opIndex(int Index)
```

### opIndex
```angelscript
float opIndex(int Index)
```

### opEquals
```angelscript
bool opEquals(FVector Other)
```

### Equals
```angelscript
bool Equals(FVector Other, float Tolerance)
```

### CrossProduct
```angelscript
FVector CrossProduct(FVector Other)
```

### DotProduct
```angelscript
float DotProduct(FVector Other)
```

### AllComponentsEqual
```angelscript
bool AllComponentsEqual(float Tolerance)
```

### Parallel
```angelscript
bool Parallel(FVector Normal2, float ParallelCosineThreshold)
```
* See if two normal vectors are nearly parallel, meaning the angle between them is close to 0 degrees. 
* @param  Normal1 First normalized vector.
* @param  Normal1 Second normalized vector.
* @param  ParallelCosineThreshold Normals are parallel if absolute value of dot product (cosine of angle between them) is greater than or equal to this. For example: cos(1.0 degrees). 
* @return true if vectors are nearly parallel, false otherwise. 


### Coincident
```angelscript
bool Coincident(FVector Normal2, float ParallelCosineThreshold)
```
* See if two normal vectors are coincident (nearly parallel and point in the same direction).
* @param  Normal1 First normalized vector.
* @param  Normal2 Second normalized vector.
* @param  ParallelCosineThreshold Normals are coincident if dot product (cosine of angle between them) is greater than or equal to this. For example: cos(1.0 degrees).
* @return true if vectors are coincident (nearly parallel and point in the same direction), false otherwise.


### Orthogonal
```angelscript
bool Orthogonal(FVector Normal2, float OrthogonalCosineThreshold)
```
* See if two normal vectors are nearly orthogonal (perpendicular), meaning the angle between them is close to 90 degrees.
* @param  Normal1 First normalized vector.
* @param  Normal2 Second normalized vector.
* @param  OrthogonalCosineThreshold Normals are orthogonal if absolute value of dot product (cosine of angle between them) is less than or equal to this. For example: cos(89.0 degrees).
* @return true if vectors are orthogonal (perpendicular), false otherwise.


### GetMax
```angelscript
float GetMax()
```

### GetAbsMax
```angelscript
float GetAbsMax()
```

### GetMin
```angelscript
float GetMin()
```

### GetAbsMin
```angelscript
float GetAbsMin()
```

### ComponentMin
```angelscript
FVector ComponentMin(FVector Other)
```

### ComponentMax
```angelscript
FVector ComponentMax(FVector Other)
```

### ComponentClamp
```angelscript
FVector ComponentClamp(FVector Min, FVector Max)
```

### GetAbs
```angelscript
FVector GetAbs()
```

### Size
```angelscript
float Size()
```

### SizeSquared
```angelscript
float SizeSquared()
```

### Size2D
```angelscript
float Size2D()
```

### SizeSquared2D
```angelscript
float SizeSquared2D()
```

### IsNearlyZero
```angelscript
bool IsNearlyZero(float Tolerance)
```

### IsZero
```angelscript
bool IsZero()
```

### Normalize
```angelscript
bool Normalize(float Tolerance)
```

### IsNormalized
```angelscript
bool IsNormalized()
```

### ToDirectionAndLength
```angelscript
void ToDirectionAndLength(FVector& OutDir, float& OutLength)
```

### ToDirectionAndLength
```angelscript
void ToDirectionAndLength(FVector& OutDir, float32& OutLength)
```

### GetSignVector
```angelscript
FVector GetSignVector()
```

### Projection
```angelscript
FVector Projection()
```

### GetUnsafeNormal
```angelscript
FVector GetUnsafeNormal()
```

### GridSnap
```angelscript
FVector GridSnap(float GridSize)
```

### BoundToCube
```angelscript
FVector BoundToCube(float Radius)
```

### BoundToBox
```angelscript
FVector BoundToBox(FVector Min, FVector Max)
```

### GetClampedToSize
```angelscript
FVector GetClampedToSize(float Min, float Max)
```

### GetClampedToSize2D
```angelscript
FVector GetClampedToSize2D(float Min, float Max)
```

### GetClampedToMaxSize
```angelscript
FVector GetClampedToMaxSize(float Max)
```

### GetClampedToMaxSize2D
```angelscript
FVector GetClampedToMaxSize2D(float Max)
```

### AddBounded
```angelscript
void AddBounded(FVector V, float Radius)
```

### Reciprocal
```angelscript
FVector Reciprocal()
```

### IsUniform
```angelscript
bool IsUniform(float Tolerance)
```

### MirrorByVector
```angelscript
FVector MirrorByVector(FVector MirrorNormal)
```

### VectorPlaneProject
```angelscript
FVector VectorPlaneProject(FVector PlaneNormal)
```

### RotateAngleAxis
```angelscript
FVector RotateAngleAxis(float AngleDeg, FVector Axis)
```

### GetSafeNormal
```angelscript
FVector GetSafeNormal(float Tolerance, FVector ResultIfZero)
```

### GetSafeNormal2D
```angelscript
FVector GetSafeNormal2D(float Tolerance, FVector ResultIfZero)
```

### CosineAngle2D
```angelscript
float CosineAngle2D(FVector B)
```

### ProjectOnTo
```angelscript
FVector ProjectOnTo(FVector A)
```
Gets a copy of this vector projected onto the input vector.

@param A	Vector to project onto, does not assume it is normalized.
@return Projected vector.

### ProjectOnToNormal
```angelscript
FVector ProjectOnToNormal(FVector Normal)
```
Gets a copy of this vector projected onto the input vector, which is assumed to be unit length.

@param A	Normal vector to project onto (assumed to be unit length).
@return Projected vector.

### FindBestAxisVectors
```angelscript
void FindBestAxisVectors(FVector& Axis1, FVector& Axis2)
```

### UnwindEuler
```angelscript
void UnwindEuler()
```

### ContainsNaN
```angelscript
bool ContainsNaN()
```

### IsUnit
```angelscript
bool IsUnit(float LengthSquaredTolerance)
```

### HeadingAngle
```angelscript
float HeadingAngle()
```

### PointsAreSame
```angelscript
bool PointsAreSame(FVector P2)
```

### PointsAreNear
```angelscript
bool PointsAreNear(FVector P2, float Dist)
```

### Distance
```angelscript
float Distance(FVector Other)
```

### DistSquared
```angelscript
float DistSquared(FVector Other)
```

### Dist2D
```angelscript
float Dist2D(FVector Other)
```

### DistXY
```angelscript
float DistXY(FVector Other)
```

### DistSquaredXY
```angelscript
float DistSquaredXY(FVector Other)
```

### DistSquared2D
```angelscript
float DistSquared2D(FVector Other)
```

### ToOrientationRotator
```angelscript
FRotator ToOrientationRotator()
```

### ToOrientationQuat
```angelscript
FQuat ToOrientationQuat()
```

### Rotation
```angelscript
FRotator Rotation()
```

### InitFromString
```angelscript
bool InitFromString(FString SourceString)
```

### ToString
```angelscript
FString ToString()
```

### AngularDistance
```angelscript
float AngularDistance(FVector B)
```
Get the angle in radians between two vectors. Vectors are not assumed to be normalized.

### AngularDistanceForNormals
```angelscript
float AngularDistanceForNormals(FVector B)
```
Get the angle in radians between two normal vectors. Both vectors are assumed to be unit length, or a wrong value will be returned.

### ConstrainToDirection
```angelscript
FVector ConstrainToDirection(FVector Direction)
```

### ConstrainToPlane
```angelscript
FVector ConstrainToPlane(FVector PlaneUp)
```

### Dist2D
```angelscript
float Dist2D(FVector Other, FVector UpDirection)
```

### DistSquared2D
```angelscript
float DistSquared2D(FVector Other, FVector UpDirection)
```

### MoveTowards
```angelscript
FVector MoveTowards(FVector Target, float StepSize)
```

### PointPlaneProject
```angelscript
FVector PointPlaneProject(FVector PlaneBase, FVector PlaneNormal)
```

### Size2D
```angelscript
float Size2D(FVector UpDirection)
```

### SizeSquared2D
```angelscript
float SizeSquared2D(FVector UpDirection)
```

### ToColorString
```angelscript
FString ToColorString()
```

