# FVector3f

## 属性

### X
- **类型**: `float32`

### Y
- **类型**: `float32`

### Z
- **类型**: `float32`

## 方法

### opAssign
```angelscript
FVector3f& opAssign(FVector3f Other)
```

### opAdd
```angelscript
FVector3f opAdd(FVector3f Other)
```

### opSub
```angelscript
FVector3f opSub(FVector3f Other)
```

### opMul
```angelscript
FVector3f opMul(FVector3f Other)
```

### opDiv
```angelscript
FVector3f opDiv(FVector3f Other)
```

### opMul
```angelscript
FVector3f opMul(float32 Scale)
```

### opDiv
```angelscript
FVector3f opDiv(float32 Scale)
```

### opNeg
```angelscript
FVector3f opNeg()
```

### opMulAssign
```angelscript
FVector3f opMulAssign(float32 Scale)
```

### opDivAssign
```angelscript
FVector3f opDivAssign(float32 Scale)
```

### opMulAssign
```angelscript
FVector3f opMulAssign(FVector3f Other)
```

### opDivAssign
```angelscript
FVector3f opDivAssign(FVector3f Other)
```

### opAddAssign
```angelscript
FVector3f opAddAssign(FVector3f Other)
```

### opSubAssign
```angelscript
FVector3f opSubAssign(FVector3f Other)
```

### opIndex
```angelscript
float32& opIndex(int Index)
```

### opIndex
```angelscript
float32 opIndex(int Index)
```

### opEquals
```angelscript
bool opEquals(FVector3f Other)
```

### Equals
```angelscript
bool Equals(FVector3f Other, float32 Tolerance)
```

### CrossProduct
```angelscript
FVector3f CrossProduct(FVector3f Other)
```

### DotProduct
```angelscript
float32 DotProduct(FVector3f Other)
```

### AllComponentsEqual
```angelscript
bool AllComponentsEqual(float32 Tolerance)
```

### Parallel
```angelscript
bool Parallel(FVector3f Normal2, float32 ParallelCosineThreshold)
```
* See if two normal vectors are nearly parallel, meaning the angle between them is close to 0 degrees. 
* @param  Normal1 First normalized vector.
* @param  Normal1 Second normalized vector.
* @param  ParallelCosineThreshold Normals are parallel if absolute value of dot product (cosine of angle between them) is greater than or equal to this. For example: cos(1.0 degrees). 
* @return true if vectors are nearly parallel, false otherwise. 


### Coincident
```angelscript
bool Coincident(FVector3f Normal2, float32 ParallelCosineThreshold)
```
* See if two normal vectors are coincident (nearly parallel and point in the same direction).
* @param  Normal1 First normalized vector.
* @param  Normal2 Second normalized vector.
* @param  ParallelCosineThreshold Normals are coincident if dot product (cosine of angle between them) is greater than or equal to this. For example: cos(1.0 degrees).
* @return true if vectors are coincident (nearly parallel and point in the same direction), false otherwise.


### Orthogonal
```angelscript
bool Orthogonal(FVector3f Normal2, float32 OrthogonalCosineThreshold)
```
* See if two normal vectors are nearly orthogonal (perpendicular), meaning the angle between them is close to 90 degrees.
* @param  Normal1 First normalized vector.
* @param  Normal2 Second normalized vector.
* @param  OrthogonalCosineThreshold Normals are orthogonal if absolute value of dot product (cosine of angle between them) is less than or equal to this. For example: cos(89.0 degrees).
* @return true if vectors are orthogonal (perpendicular), false otherwise.


### GetMax
```angelscript
float32 GetMax()
```

### GetAbsMax
```angelscript
float32 GetAbsMax()
```

### GetMin
```angelscript
float32 GetMin()
```

### GetAbsMin
```angelscript
float32 GetAbsMin()
```

### ComponentMin
```angelscript
FVector3f ComponentMin(FVector3f Other)
```

### ComponentMax
```angelscript
FVector3f ComponentMax(FVector3f Other)
```

### ComponentClamp
```angelscript
FVector3f ComponentClamp(FVector3f Min, FVector3f Max)
```

### GetAbs
```angelscript
FVector3f GetAbs()
```

### Size
```angelscript
float32 Size()
```

### SizeSquared
```angelscript
float32 SizeSquared()
```

### Size2D
```angelscript
float32 Size2D()
```

### SizeSquared2D
```angelscript
float32 SizeSquared2D()
```

### IsNearlyZero
```angelscript
bool IsNearlyZero(float32 Tolerance)
```

### IsZero
```angelscript
bool IsZero()
```

### Normalize
```angelscript
bool Normalize(float32 Tolerance)
```

### IsNormalized
```angelscript
bool IsNormalized()
```

### ToDirectionAndLength
```angelscript
void ToDirectionAndLength(FVector3f& OutDir, float32& OutLength)
```

### GetSignVector
```angelscript
FVector3f GetSignVector()
```

### Projection
```angelscript
FVector3f Projection()
```

### GetUnsafeNormal
```angelscript
FVector3f GetUnsafeNormal()
```

### GridSnap
```angelscript
FVector3f GridSnap(float32 GridSize)
```

### BoundToCube
```angelscript
FVector3f BoundToCube(float32 Radius)
```

### BoundToBox
```angelscript
FVector3f BoundToBox(FVector3f Min, FVector3f Max)
```

### GetClampedToSize
```angelscript
FVector3f GetClampedToSize(float32 Min, float32 Max)
```

### GetClampedToSize2D
```angelscript
FVector3f GetClampedToSize2D(float32 Min, float32 Max)
```

### GetClampedToMaxSize
```angelscript
FVector3f GetClampedToMaxSize(float32 Max)
```

### GetClampedToMaxSize2D
```angelscript
FVector3f GetClampedToMaxSize2D(float32 Max)
```

### AddBounded
```angelscript
void AddBounded(FVector3f V, float32 Radius)
```

### Reciprocal
```angelscript
FVector3f Reciprocal()
```

### IsUniform
```angelscript
bool IsUniform(float32 Tolerance)
```

### MirrorByVector
```angelscript
FVector3f MirrorByVector(FVector3f MirrorNormal)
```

### VectorPlaneProject
```angelscript
FVector3f VectorPlaneProject(FVector3f PlaneNormal)
```

### RotateAngleAxis
```angelscript
FVector3f RotateAngleAxis(float32 AngleDeg, FVector3f Axis)
```

### GetSafeNormal
```angelscript
FVector3f GetSafeNormal(float32 Tolerance, FVector3f ResultIfZero)
```

### GetSafeNormal2D
```angelscript
FVector3f GetSafeNormal2D(float32 Tolerance, FVector3f ResultIfZero)
```

### CosineAngle2D
```angelscript
float32 CosineAngle2D(FVector3f B)
```

### ProjectOnTo
```angelscript
FVector3f ProjectOnTo(FVector3f A)
```
Gets a copy of this vector projected onto the input vector.

@param A	Vector to project onto, does not assume it is normalized.
@return Projected vector.

### ProjectOnToNormal
```angelscript
FVector3f ProjectOnToNormal(FVector3f Normal)
```
Gets a copy of this vector projected onto the input vector, which is assumed to be unit length.

@param A	Normal vector to project onto (assumed to be unit length).
@return Projected vector.

### FindBestAxisVectors
```angelscript
void FindBestAxisVectors(FVector3f& Axis1, FVector3f& Axis2)
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
bool IsUnit(float32 LengthSquaredTolerance)
```

### HeadingAngle
```angelscript
float32 HeadingAngle()
```

### PointsAreSame
```angelscript
bool PointsAreSame(FVector3f P2)
```

### PointsAreNear
```angelscript
bool PointsAreNear(FVector3f P2, float32 Dist)
```

### Distance
```angelscript
float32 Distance(FVector3f Other)
```

### DistSquared
```angelscript
float32 DistSquared(FVector3f Other)
```

### Dist2D
```angelscript
float32 Dist2D(FVector3f Other)
```

### DistXY
```angelscript
float32 DistXY(FVector3f Other)
```

### DistSquaredXY
```angelscript
float32 DistSquaredXY(FVector3f Other)
```

### DistSquared2D
```angelscript
float32 DistSquared2D(FVector3f Other)
```

### ToOrientationRotator
```angelscript
FRotator3f ToOrientationRotator()
```

### ToOrientationQuat
```angelscript
FQuat4f ToOrientationQuat()
```

### Rotation
```angelscript
FRotator3f Rotation()
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
float32 AngularDistance(FVector3f B)
```
Get the angle in radians between two vectors. Vectors are not assumed to be normalized.

### AngularDistanceForNormals
```angelscript
float32 AngularDistanceForNormals(FVector3f B)
```
Get the angle in radians between two normal vectors. Both vectors are assumed to be unit length, or a wrong value will be returned.

### ConstrainToDirection
```angelscript
FVector3f ConstrainToDirection(FVector3f Direction)
```

### ConstrainToPlane
```angelscript
FVector3f ConstrainToPlane(FVector3f PlaneUp)
```

### Dist2D
```angelscript
float32 Dist2D(FVector3f Other, FVector3f UpDirection)
```

### DistSquared2D
```angelscript
float32 DistSquared2D(FVector3f Other, FVector3f UpDirection)
```

### PointPlaneProject
```angelscript
FVector3f PointPlaneProject(FVector3f PlaneBase, FVector3f PlaneNormal)
```

### Size2D
```angelscript
float32 Size2D(FVector3f UpDirection)
```

### SizeSquared2D
```angelscript
float32 SizeSquared2D(FVector3f UpDirection)
```

### ToColorString
```angelscript
FString ToColorString()
```

