# __Math

## 方法

### RandHelper
```angelscript
int RandHelper(int Max)
```

### RandRange
```angelscript
int RandRange(int Min, int Max)
```
Returns a random integer >= Min and <= Max

### RandRange
```angelscript
float RandRange(float Min, float Max)
```

### RandRange
```angelscript
float32 RandRange(float32 Min, float32 Max)
```

### RandBool
```angelscript
bool RandBool()
```

### VRand
```angelscript
FVector VRand()
```
Returns a random vector with length of 1

### VRandCone
```angelscript
FVector VRandCone(FVector DDir, float32 HorizontalConeHalfAngleRad, float32 VerticalConeHalfAngleRad)
```
Returns a random unit vector, uniformly distributed, within the specified cone
ConeHalfAngleRad is the half-angle of cone, in radians.  Returns a normalized vector.

### VRandCone
```angelscript
FVector VRandCone(FVector DDir, float32 ConeHalfAngleRad)
```

### RandPointInCircle
```angelscript
FVector2D RandPointInCircle(float32 Radius)
```
Get a random point on a unit circle, evenly spread across the circumference.

### GetReflectionVector
```angelscript
FVector GetReflectionVector(FVector Direction, FVector SurfaceNormal)
```
Given a direction vector and a surface normal, returns the vector reflected across the surface normal.
Produces a result like shining a laser at a mirror!
@param Direction Direction vector the ray is coming from.
@param SurfaceNormal A normal of the surface the ray should be reflected on.
@returns Reflected vector.

### MakePulsatingValue
```angelscript
float32 MakePulsatingValue(float InCurrentTime, float32 InPulsesPerSecond, float32 InPhase)
```
Simple function to create a pulsating scalar value
@param  InCurrentTime  Current absolute time
@param  InPulsesPerSecond  How many full pulses per second?
@param  InPhase  Optional phase amount, between 0.0 and 1.0 (to synchronize pulses)
@return  Pulsating value (0.0-1.0)

### IsNearlyEqual
```angelscript
bool IsNearlyEqual(float A, float B, float ErrorTolerance)
```

### IsNearlyEqual
```angelscript
bool IsNearlyEqual(float32 A, float32 B, float32 ErrorTolerance)
```

### IsNearlyZero
```angelscript
bool IsNearlyZero(float Value, float ErrorTolerance)
```

### IsNearlyZero
```angelscript
bool IsNearlyZero(float32 Value, float32 ErrorTolerance)
```

### IsPowerOfTwo
```angelscript
bool IsPowerOfTwo(int Value)
```

### SmoothStep
```angelscript
float SmoothStep(float A, float B, float X)
```
Returns a smooth Hermite interpolation between 0 and 1 for the value X (where X ranges between A and B)
Clamped to 0 for X <= A and 1 for X >= B.
@param A Minimum value of X
@param B Maximum value of X
@param X Parameter
@return Smoothed value between 0 and 1


### SmoothStep
```angelscript
float32 SmoothStep(float32 A, float32 B, float32 X)
```
Returns a smooth Hermite interpolation between 0 and 1 for the value X (where X ranges between A and B)
Clamped to 0 for X <= A and 1 for X >= B.
@param A Minimum value of X
@param B Maximum value of X
@param X Parameter
@return Smoothed value between 0 and 1


### Clamp
```angelscript
float Clamp(float X, float Min, float Max)
```
Clamps X to be between Min and Max, inclusive

### Clamp
```angelscript
float32 Clamp(float32 X, float32 Min, float32 Max)
```
Clamps X to be between Min and Max, inclusive

### Clamp
```angelscript
int Clamp(int X, int Min, int Max)
```
Clamps X to be between Min and Max, inclusive

### Clamp
```angelscript
uint Clamp(uint X, uint Min, uint Max)
```
Clamps X to be between Min and Max, inclusive

### FastAsin
```angelscript
float FastAsin(float Value)
```

### FastAsin
```angelscript
float32 FastAsin(float32 Value)
```

### RadiansToDegrees
```angelscript
float RadiansToDegrees(float RadVal)
```

### DegreesToRadians
```angelscript
float DegreesToRadians(float DegVal)
```

### RadiansToDegrees
```angelscript
float32 RadiansToDegrees(float32 RadVal)
```

### DegreesToRadians
```angelscript
float32 DegreesToRadians(float32 DegVal)
```

### ClampAngle
```angelscript
float32 ClampAngle(float32 AngleDegrees, float32 MinAngleDegrees, float32 MaxAngleDegrees)
```

### ClampAngle
```angelscript
float ClampAngle(float AngleDegrees, float MinAngleDegrees, float MaxAngleDegrees)
```

### FindDeltaAngleDegrees
```angelscript
float FindDeltaAngleDegrees(float A1, float A2)
```

### FindDeltaAngleRadians
```angelscript
float FindDeltaAngleRadians(float A1, float A2)
```

### FindDeltaAngleDegrees
```angelscript
float32 FindDeltaAngleDegrees(float32 A1, float32 A2)
```

### FindDeltaAngleRadians
```angelscript
float32 FindDeltaAngleRadians(float32 A1, float32 A2)
```

### UnwindDegrees
```angelscript
float UnwindDegrees(float A)
```
Utility to ensure angle is between +/- 180 degrees by unwinding.

### UnwindRadians
```angelscript
float UnwindRadians(float A)
```
Utility to ensure angle is between +/- 180 degrees by unwinding.

### UnwindDegrees
```angelscript
float32 UnwindDegrees(float32 A)
```
Utility to ensure angle is between +/- 180 degrees by unwinding.

### UnwindRadians
```angelscript
float32 UnwindRadians(float32 A)
```
Utility to ensure angle is between +/- 180 degrees by unwinding.

### LerpStable
```angelscript
float LerpStable(float A, float B, float Alpha)
```

### LerpStable
```angelscript
float32 LerpStable(float32 A, float32 B, float32 Alpha)
```

### Lerp
```angelscript
float Lerp(float A, float B, float Alpha)
```

### Lerp
```angelscript
float32 Lerp(float32 A, float32 B, float32 Alpha)
```

### Lerp
```angelscript
FVector Lerp(FVector A, FVector B, float Alpha)
```

### Lerp
```angelscript
FVector2D Lerp(FVector2D A, FVector2D B, float Alpha)
```

### Lerp
```angelscript
FVector3f Lerp(FVector3f A, FVector3f B, float32 Alpha)
```

### Lerp
```angelscript
FVector2f Lerp(FVector2f A, FVector2f B, float32 Alpha)
```

### VLerp
```angelscript
FVector VLerp(FVector A, FVector B, FVector Alpha)
```

### Lerp
```angelscript
FLinearColor Lerp(FLinearColor A, FLinearColor B, float32 Alpha)
```

### IsWithin
```angelscript
bool IsWithin(float TestValue, float MinValue, float MaxValue)
```

### IsWithin
```angelscript
bool IsWithin(float32 TestValue, float32 MinValue, float32 MaxValue)
```

### IsWithin
```angelscript
bool IsWithin(int TestValue, int MinValue, int MaxValue)
```

### IsWithinInclusive
```angelscript
bool IsWithinInclusive(float TestValue, float MinValue, float MaxValue)
```

### IsWithinInclusive
```angelscript
bool IsWithinInclusive(float32 TestValue, float32 MinValue, float32 MaxValue)
```

### IsWithinInclusive
```angelscript
bool IsWithinInclusive(int TestValue, int MinValue, int MaxValue)
```

### CubicInterp
```angelscript
FVector CubicInterp(FVector Point0, FVector Tangent0, FVector Point1, FVector Tangent1, float Alpha)
```

### CubicInterp
```angelscript
FQuat CubicInterp(FQuat Point0, FQuat Tangent0, FQuat Point1, FQuat Tangent1, float Alpha)
```

### CubicInterp
```angelscript
FVector CubicInterp(FVector Point0, FVector Tangent0, FVector Point1, FVector Tangent1, float32 Alpha)
```

### CubicInterp
```angelscript
FQuat CubicInterp(FQuat Point0, FQuat Tangent0, FQuat Point1, FQuat Tangent1, float32 Alpha)
```

### CubicInterp
```angelscript
FVector3f CubicInterp(FVector3f Point0, FVector3f Tangent0, FVector3f Point1, FVector3f Tangent1, float32 Alpha)
```

### CubicInterp
```angelscript
FQuat4f CubicInterp(FQuat4f Point0, FQuat4f Tangent0, FQuat4f Point1, FQuat4f Tangent1, float32 Alpha)
```

### CubicInterpDerivative
```angelscript
FVector CubicInterpDerivative(FVector Point0, FVector Tangent0, FVector Point1, FVector Tangent1, float Alpha)
```

### CubicInterpDerivative
```angelscript
FRotator CubicInterpDerivative(FRotator Point0, FRotator Tangent0, FRotator Point1, FRotator Tangent1, float Alpha)
```

### CubicInterpDerivative
```angelscript
FVector CubicInterpDerivative(FVector Point0, FVector Tangent0, FVector Point1, FVector Tangent1, float32 Alpha)
```

### CubicInterpDerivative
```angelscript
FRotator CubicInterpDerivative(FRotator Point0, FRotator Tangent0, FRotator Point1, FRotator Tangent1, float32 Alpha)
```

### CubicInterpDerivative
```angelscript
FVector3f CubicInterpDerivative(FVector3f Point0, FVector3f Tangent0, FVector3f Point1, FVector3f Tangent1, float32 Alpha)
```

### CubicInterpDerivative
```angelscript
FRotator3f CubicInterpDerivative(FRotator3f Point0, FRotator3f Tangent0, FRotator3f Point1, FRotator3f Tangent1, float32 Alpha)
```

### VInterpNormalRotationTo
```angelscript
FVector VInterpNormalRotationTo(FVector Current, FVector Target, float32 DeltaTime, float32 RotationSpeedDegrees)
```

### VInterpConstantTo
```angelscript
FVector VInterpConstantTo(FVector Current, FVector Target, float32 DeltaTime, float32 InterpSpeed)
```

### VInterpTo
```angelscript
FVector VInterpTo(FVector Current, FVector Target, float32 DeltaTime, float32 InterpSpeed)
```

### Vector2DInterpConstantTo
```angelscript
FVector2D Vector2DInterpConstantTo(FVector2D Current, FVector2D Target, float32 DeltaTime, float32 InterpSpeed)
```

### Vector2DInterpTo
```angelscript
FVector2D Vector2DInterpTo(FVector2D Current, FVector2D Target, float32 DeltaTime, float32 InterpSpeed)
```

### RInterpConstantTo
```angelscript
FRotator RInterpConstantTo(FRotator Current, FRotator Target, float32 DeltaTime, float32 InterpSpeed)
```

### RInterpTo
```angelscript
FRotator RInterpTo(FRotator Current, FRotator Target, float32 DeltaTime, float32 InterpSpeed)
```

### RotatorFromAxisAndAngle
```angelscript
FRotator RotatorFromAxisAndAngle(FVector Axis, float32 Angle)
```

### RandomPointInBoundingBox
```angelscript
FVector RandomPointInBoundingBox(FVector Center, FVector HalfSize)
```

### RandomRotator
```angelscript
FRotator RandomRotator(bool bRoll)
```

### QInterpConstantTo
```angelscript
FQuat QInterpConstantTo(FQuat Current, FQuat Target, float32 DeltaTime, float32 InterpSpeed)
```

### QInterpTo
```angelscript
FQuat QInterpTo(FQuat Current, FQuat Target, float32 DeltaTime, float32 InterpSpeed)
```

### QInterpConstantTo
```angelscript
FQuat4f QInterpConstantTo(FQuat4f Current, FQuat4f Target, float32 DeltaTime, float32 InterpSpeed)
```

### QInterpTo
```angelscript
FQuat4f QInterpTo(FQuat4f Current, FQuat4f Target, float32 DeltaTime, float32 InterpSpeed)
```

### FInterpConstantTo
```angelscript
float32 FInterpConstantTo(float32 Current, float32 Target, float32 DeltaTime, float32 InterpSpeed)
```

### FInterpTo
```angelscript
float32 FInterpTo(float32 Current, float32 Target, float32 DeltaTime, float32 InterpSpeed)
```

### FInterpConstantTo
```angelscript
float FInterpConstantTo(float Current, float Target, float DeltaTime, float InterpSpeed)
```

### FInterpTo
```angelscript
float FInterpTo(float Current, float Target, float DeltaTime, float InterpSpeed)
```

### CInterpTo
```angelscript
FLinearColor CInterpTo(FLinearColor Current, FLinearColor Target, float32 DeltaTime, float32 InterpSpeed)
```

### SphereAABBIntersection
```angelscript
bool SphereAABBIntersection(FVector SphereCenter, float RadiusSquared, FBox AABB)
```

### SphereAABBIntersection
```angelscript
bool SphereAABBIntersection(FSphere Sphere, FBox AABB)
```

### SphereAABBIntersection
```angelscript
bool SphereAABBIntersection(FVector3f SphereCenter, float32 RadiusSquared, FBox3f AABB)
```

### SphereAABBIntersection
```angelscript
bool SphereAABBIntersection(FSphere3f Sphere, FBox3f AABB)
```

### RayPlaneIntersection
```angelscript
FVector RayPlaneIntersection(FVector RayOrigin, FVector RayDirection, FPlane Plane)
```

### LinePlaneIntersection
```angelscript
FVector LinePlaneIntersection(FVector Point1, FVector Point2, FVector PlaneOrigin, FVector PlaneNormal)
```

### LinePlaneIntersection
```angelscript
FVector3f LinePlaneIntersection(FVector3f Point1, FVector3f Point2, FVector3f PlaneOrigin, FVector3f PlaneNormal)
```

### LineSphereIntersection
```angelscript
bool LineSphereIntersection(FVector3f Start, FVector3f Dir, float32 Length, FVector3f Origin, float32 Radius)
```

### LineSphereIntersection
```angelscript
bool LineSphereIntersection(FVector Start, FVector Dir, float Length, FVector Origin, float Radius)
```

### LineBoxIntersection
```angelscript
bool LineBoxIntersection(FBox Box, FVector Start, FVector End, FVector StartToEnd)
```

### ClosestPointOnLine
```angelscript
FVector ClosestPointOnLine(FVector LineStart, FVector LineEnd, FVector Point)
```

### ClosestPointOnInfiniteLine
```angelscript
FVector ClosestPointOnInfiniteLine(FVector LineStart, FVector LineEnd, FVector Point)
```

### ComputeBoundingSphereForCone
```angelscript
FSphere ComputeBoundingSphereForCone(FVector ConeOrigin, FVector ConeDirection, float ConeRadius, float CosConeAngle, float SinConeAngle)
```

### ComputeBoundingSphereForCone
```angelscript
FSphere3f ComputeBoundingSphereForCone(FVector3f ConeOrigin, FVector3f ConeDirection, float32 ConeRadius, float32 CosConeAngle, float32 SinConeAngle)
```

### TruncToInt
```angelscript
int TruncToInt(float F)
```

### TruncToInt
```angelscript
int TruncToInt(float32 F)
```

### TruncToFloat
```angelscript
float TruncToFloat(float F)
```

### TruncToFloat
```angelscript
float32 TruncToFloat(float32 F)
```

### TruncToDouble
```angelscript
float TruncToDouble(float F)
```

### RoundToInt
```angelscript
int RoundToInt(float F)
```

### RoundToInt
```angelscript
int RoundToInt(float32 F)
```

### RoundToFloat
```angelscript
float RoundToFloat(float F)
```

### RoundToFloat
```angelscript
float32 RoundToFloat(float32 F)
```

### RoundToDouble
```angelscript
float RoundToDouble(float F)
```

### FloorToInt
```angelscript
int FloorToInt(float F)
```

### FloorToInt
```angelscript
int FloorToInt(float32 F)
```

### FloorToFloat
```angelscript
float FloorToFloat(float F)
```

### FloorToFloat
```angelscript
float32 FloorToFloat(float32 F)
```

### FloorToDouble
```angelscript
float FloorToDouble(float F)
```

### CeilToInt
```angelscript
int CeilToInt(float F)
```

### CeilToInt
```angelscript
int CeilToInt(float32 F)
```

### CeilToFloat
```angelscript
float CeilToFloat(float F)
```

### CeilToFloat
```angelscript
float32 CeilToFloat(float32 F)
```

### RoundFromZero
```angelscript
float RoundFromZero(float F)
```

### RoundFromZero
```angelscript
float32 RoundFromZero(float32 F)
```

### IsNaN
```angelscript
bool IsNaN(float F)
```

### IsFinite
```angelscript
bool IsFinite(float F)
```

### InvSqrt
```angelscript
float InvSqrt(float F)
```

### InvSqrtEst
```angelscript
float InvSqrtEst(float F)
```

### Fractional
```angelscript
float Fractional(float Value)
```

### Frac
```angelscript
float Frac(float Value)
```

### IsNaN
```angelscript
bool IsNaN(float32 F)
```

### IsFinite
```angelscript
bool IsFinite(float32 F)
```

### InvSqrt
```angelscript
float32 InvSqrt(float32 F)
```

### InvSqrtEst
```angelscript
float32 InvSqrtEst(float32 F)
```

### Fractional
```angelscript
float32 Fractional(float32 Value)
```

### Frac
```angelscript
float32 Frac(float32 Value)
```

### Exp
```angelscript
float Exp(float Value)
```

### Exp2
```angelscript
float Exp2(float Value)
```

### Loge
```angelscript
float Loge(float Value)
```

### Log2
```angelscript
float Log2(float Value)
```

### LogX
```angelscript
float LogX(float Base, float Value)
```

### Fmod
```angelscript
float Fmod(float X, float Y)
```

### Sin
```angelscript
float Sin(float Value)
```

### Asin
```angelscript
float Asin(float Value)
```

### Sinh
```angelscript
float Sinh(float Value)
```

### Cos
```angelscript
float Cos(float Value)
```

### Acos
```angelscript
float Acos(float Value)
```

### Tan
```angelscript
float Tan(float Value)
```

### Atan
```angelscript
float Atan(float Value)
```

### Atan2
```angelscript
float Atan2(float Y, float X)
```

### Sqrt
```angelscript
float Sqrt(float Value)
```

### Pow
```angelscript
float Pow(float A, float B)
```

### Exp
```angelscript
float32 Exp(float32 Value)
```

### Exp2
```angelscript
float32 Exp2(float32 Value)
```

### Loge
```angelscript
float32 Loge(float32 Value)
```

### Log2
```angelscript
float32 Log2(float32 Value)
```

### LogX
```angelscript
float32 LogX(float32 Base, float32 Value)
```

### Fmod
```angelscript
float32 Fmod(float32 X, float32 Y)
```

### Sin
```angelscript
float32 Sin(float32 Value)
```

### Asin
```angelscript
float32 Asin(float32 Value)
```

### Sinh
```angelscript
float32 Sinh(float32 Value)
```

### Cos
```angelscript
float32 Cos(float32 Value)
```

### Acos
```angelscript
float32 Acos(float32 Value)
```

### Tan
```angelscript
float32 Tan(float32 Value)
```

### Atan
```angelscript
float32 Atan(float32 Value)
```

### Atan2
```angelscript
float32 Atan2(float32 Y, float32 X)
```

### Sqrt
```angelscript
float32 Sqrt(float32 Value)
```

### Pow
```angelscript
float32 Pow(float32 A, float32 B)
```

### Rand
```angelscript
int Rand()
```

### FRand
```angelscript
float32 FRand()
```

### Abs
```angelscript
float Abs(float Value)
```

### Abs
```angelscript
float32 Abs(float32 Value)
```

### Abs
```angelscript
int Abs(int Value)
```

### Sign
```angelscript
float Sign(float Value)
```

### Sign
```angelscript
float32 Sign(float32 Value)
```

### Sign
```angelscript
int Sign(int Value)
```

### Min
```angelscript
float Min(float A, float B)
```

### Min
```angelscript
float32 Min(float32 A, float32 B)
```

### Min
```angelscript
int Min(int A, int B)
```

### Min
```angelscript
uint Min(uint A, uint B)
```

### Max3
```angelscript
float Max3(float A, float B, float C)
```

### Max3
```angelscript
float32 Max3(float32 A, float32 B, float32 C)
```

### Max
```angelscript
float Max(float A, float B)
```

### Max
```angelscript
float32 Max(float32 A, float32 B)
```

### Max
```angelscript
int Max(int A, int B)
```

### Max
```angelscript
uint Max(uint A, uint B)
```

### Square
```angelscript
float Square(float Value)
```

### Square
```angelscript
float32 Square(float32 Value)
```

### Square
```angelscript
int Square(int Value)
```

### Square
```angelscript
uint Square(uint Value)
```

### GetMappedRangeValueClamped
```angelscript
float GetMappedRangeValueClamped(FVector2D InputRange, FVector2D OutputRange, float Value)
```

### GetMappedRangeValueUnclamped
```angelscript
float GetMappedRangeValueUnclamped(FVector2D InputRange, FVector2D OutputRange, float Value)
```

### GetMappedRangeValueClamped
```angelscript
float32 GetMappedRangeValueClamped(FVector2f InputRange, FVector2f OutputRange, float32 Value)
```

### GetMappedRangeValueUnclamped
```angelscript
float32 GetMappedRangeValueUnclamped(FVector2f InputRange, FVector2f OutputRange, float32 Value)
```

### PerlinNoise1D
```angelscript
float32 PerlinNoise1D(float32 X)
```
Generates a 1D Perlin noise from the given value.  Returns a continuous random value between -1.0 and 1.0.
@param	Value	The input value that Perlin noise will be generated from.  This is usually a steadily incrementing time value.
@return	Perlin noise in the range of -1.0 to 1.0

### PerlinNoise2D
```angelscript
float32 PerlinNoise2D(FVector2D Location)
```
Generates a 1D Perlin noise sample at the given location.  Returns a continuous random value between -1.0 and 1.0.
@param	Location	Where to sample
@return	Perlin noise in the range of -1.0 to 1.0


### PerlinNoise3D
```angelscript
float32 PerlinNoise3D(FVector Location)
```
Generates a 3D Perlin noise sample at the given location.  Returns a continuous random value between -1.0 and 1.0.
@param	Location	Where to sample
@return	Perlin noise in the range of -1.0 to 1.0

### GridSnap
```angelscript
float GridSnap(float Location, float Grid)
```

### GridSnap
```angelscript
float32 GridSnap(float32 Location, float32 Grid)
```

### SegmentIntersection2D
```angelscript
bool SegmentIntersection2D(FVector SegmentStartA, FVector SegmentEndA, FVector SegmentStartB, FVector SegmentEndB, FVector& out_IntersectionPoint)
```
Returns true if there is an intersection between the segment specified by SegmentStartA and SegmentEndA, and
the segment specified by SegmentStartB and SegmentEndB, in 2D space. If there is an intersection, the point is placed in out_IntersectionPoint
@param SegmentStartA - start point of first segment
@param SegmentEndA   - end point of first segment
@param SegmentStartB - start point of second segment
@param SegmentEndB   - end point of second segment
@param out_IntersectionPoint - out var for the intersection point (if any)
@return true if intersection occurred

### FloatSpringInterp
```angelscript
float32 FloatSpringInterp(float32 Current, float32 Target, FFloatSpringState& SpringState, float32 Stiffness, float32 CriticalDampingFactor, float32 DeltaTime, float32 Mass, float32 TargetVelocityAmount)
```
Uses a simple spring model to interpolate a float32 from Current to Target.
@param Current				Current value
@param Target				Target value
@param SpringState			Data related to spring model (velocity, error, etc..) - Create a unique variable per spring
@param Stiffness				How stiff the spring model is (more stiffness means more oscillation around the target value)
@param CriticalDampingFactor	How much damping to apply to the spring (0 means no damping, 1 means critically damped which means no oscillation)
@param Mass					Multiplier that acts like mass on a spring
@param TargetVelocityAmount	If 1 then the target velocity will be calculated and used, which results following the target more closely/without lag. Values down to zero (recommended when using this to smooth data) will progressively disable this effect.

### VectorSpringInterp
```angelscript
FVector VectorSpringInterp(FVector Current, FVector Target, FVectorSpringState& SpringState, float32 Stiffness, float32 CriticalDampingFactor, float32 DeltaTime, float32 Mass, float32 TargetVelocityAmount)
```
Uses a simple spring model to interpolate a vector from Current to Target.
@param Current				Current value
@param Target				Target value
@param SpringState			Data related to spring model (velocity, error, etc..) - Create a unique variable per spring
@param Stiffness				How stiff the spring model is (more stiffness means more oscillation around the target value)
@param CriticalDampingFactor	How much damping to apply to the spring (0 means no damping, 1 means critically damped which means no oscillation)
@param Mass					Multiplier that acts like mass on a spring
@param TargetVelocityAmount	If 1 then the target velocity will be calculated and used, which results following the target more closely/without lag. Values down to zero (recommended when using this to smooth data) will progressively disable this effect.

### QuaternionSpringInterp
```angelscript
FQuat QuaternionSpringInterp(FQuat Current, FQuat Target, FQuaternionSpringState& SpringState, float32 Stiffness, float32 CriticalDampingFactor, float32 DeltaTime, float32 Mass, float32 TargetVelocityAmount)
```
Uses a simple spring model to interpolate a quaternion from Current to Target.
@param Current				Current value
@param Target				Target value
@param SpringState			Data related to spring model (velocity, error, etc..) - Create a unique variable per spring
@param Stiffness				How stiff the spring model is (more stiffness means more oscillation around the target value)
@param CriticalDampingFactor	How much damping to apply to the spring (0 means no damping, 1 means critically damped which means no oscillation)
@param Mass					Multiplier that acts like mass on a spring
@param TargetVelocityAmount	If 1 then the target velocity will be calculated and used, which results following the target more closely/without lag. Values down to zero (recommended when using this to smooth data) will progressively disable this effect.

### EaseIn
```angelscript
float EaseIn(float A, float B, float Alpha, float Exp)
```

### EaseOut
```angelscript
float EaseOut(float A, float B, float Alpha, float Exp)
```

### EaseInOut
```angelscript
float EaseInOut(float A, float B, float Alpha, float Exp)
```

### SinusoidalIn
```angelscript
float SinusoidalIn(float A, float B, float Alpha)
```

### SinusoidalOut
```angelscript
float SinusoidalOut(float A, float B, float Alpha)
```

### SinusoidalInOut
```angelscript
float SinusoidalInOut(float A, float B, float Alpha)
```

### ExpoIn
```angelscript
float ExpoIn(float A, float B, float Alpha)
```

### ExpoOut
```angelscript
float ExpoOut(float A, float B, float Alpha)
```

### ExpoInOut
```angelscript
float ExpoInOut(float A, float B, float Alpha)
```

### CircularIn
```angelscript
float CircularIn(float A, float B, float Alpha)
```

### CircularOut
```angelscript
float CircularOut(float A, float B, float Alpha)
```

### CircularInOut
```angelscript
float CircularInOut(float A, float B, float Alpha)
```

### EaseIn
```angelscript
float32 EaseIn(float32 A, float32 B, float32 Alpha, float32 Exp)
```

### EaseOut
```angelscript
float32 EaseOut(float32 A, float32 B, float32 Alpha, float32 Exp)
```

### EaseInOut
```angelscript
float32 EaseInOut(float32 A, float32 B, float32 Alpha, float32 Exp)
```

### SinusoidalIn
```angelscript
float32 SinusoidalIn(float32 A, float32 B, float32 Alpha)
```

### SinusoidalOut
```angelscript
float32 SinusoidalOut(float32 A, float32 B, float32 Alpha)
```

### SinusoidalInOut
```angelscript
float32 SinusoidalInOut(float32 A, float32 B, float32 Alpha)
```

### ExpoIn
```angelscript
float32 ExpoIn(float32 A, float32 B, float32 Alpha)
```

### ExpoOut
```angelscript
float32 ExpoOut(float32 A, float32 B, float32 Alpha)
```

### ExpoInOut
```angelscript
float32 ExpoInOut(float32 A, float32 B, float32 Alpha)
```

### CircularIn
```angelscript
float32 CircularIn(float32 A, float32 B, float32 Alpha)
```

### CircularOut
```angelscript
float32 CircularOut(float32 A, float32 B, float32 Alpha)
```

### CircularInOut
```angelscript
float32 CircularInOut(float32 A, float32 B, float32 Alpha)
```

### EaseIn
```angelscript
FVector EaseIn(FVector A, FVector B, float32 Alpha, float32 Exp)
```

### EaseOut
```angelscript
FVector EaseOut(FVector A, FVector B, float32 Alpha, float32 Exp)
```

### EaseInOut
```angelscript
FVector EaseInOut(FVector A, FVector B, float32 Alpha, float32 Exp)
```

### SinusoidalIn
```angelscript
FVector SinusoidalIn(FVector A, FVector B, float32 Alpha)
```

### SinusoidalOut
```angelscript
FVector SinusoidalOut(FVector A, FVector B, float32 Alpha)
```

### SinusoidalInOut
```angelscript
FVector SinusoidalInOut(FVector A, FVector B, float32 Alpha)
```

### ExpoIn
```angelscript
FVector ExpoIn(FVector A, FVector B, float32 Alpha)
```

### ExpoOut
```angelscript
FVector ExpoOut(FVector A, FVector B, float32 Alpha)
```

### ExpoInOut
```angelscript
FVector ExpoInOut(FVector A, FVector B, float32 Alpha)
```

### CircularIn
```angelscript
FVector CircularIn(FVector A, FVector B, float32 Alpha)
```

### CircularOut
```angelscript
FVector CircularOut(FVector A, FVector B, float32 Alpha)
```

### CircularInOut
```angelscript
FVector CircularInOut(FVector A, FVector B, float32 Alpha)
```

### IsPointInBox
```angelscript
bool IsPointInBox(FVector Point, FVector BoxOrigin, FVector BoxExtent)
```

### IsPointInBoxWithTransform
```angelscript
bool IsPointInBoxWithTransform(FVector Point, FTransform BoxWorldTransform, FVector BoxExtent)
```

### FindNearestPointsOnLineSegments
```angelscript
void FindNearestPointsOnLineSegments(FVector Segment1Start, FVector Segment1End, FVector Segment2Start, FVector Segment2End, FVector& Segment1Point, FVector& Segment2Point)
```

### NormalizeToRange
```angelscript
float NormalizeToRange(float Value, float RangeMin, float RangeMax)
```

### IntegerDivisionTrunc
```angelscript
int IntegerDivisionTrunc(int Value, int DivideBy)
```
Divide integer Value by DivideBy, truncating any decimals from the result.

### IntegerDivisionTrunc
```angelscript
int64 IntegerDivisionTrunc(int64 Value, int64 DivideBy)
```
Divide integer Value by DivideBy, truncating any decimals from the result.

### IntegerDivisionTrunc
```angelscript
uint IntegerDivisionTrunc(uint Value, uint DivideBy)
```
Divide integer Value by DivideBy, truncating any decimals from the result.

### IntegerDivisionTrunc
```angelscript
uint64 IntegerDivisionTrunc(uint64 Value, uint64 DivideBy)
```
Divide integer Value by DivideBy, truncating any decimals from the result.

### LerpShortestPath
```angelscript
FRotator LerpShortestPath(FRotator A, FRotator B, float Alpha)
```
Lerp between two rotators along the shortest path between them. Uses a quaternion slerp internally.

### LineBoxIntersection
```angelscript
bool LineBoxIntersection(FBox Box, FVector Start, FVector End)
```

### Modf
```angelscript
float32 Modf(float32 InValue, float32& OutIntPart)
```

### Modf
```angelscript
float Modf(float InValue, float& OutIntPart)
```

### RInterpConstantShortestPathTo
```angelscript
FRotator RInterpConstantShortestPathTo(FRotator Current, FRotator Target, float32 DeltaTime, float32 InterpSpeedDegrees)
```
Interp with constant speed between two rotators along the shortest path between them. Uses a quaternion interp internally.

### RInterpShortestPathTo
```angelscript
FRotator RInterpShortestPathTo(FRotator Current, FRotator Target, float32 DeltaTime, float32 InterpSpeed)
```
Interp between two rotators along the shortest path between them. Uses a quaternion interp internally.

### SinCos
```angelscript
void SinCos(float32& ScalarSin, float32& ScalarCos, float32 Value)
```

### SinCos
```angelscript
void SinCos(float& ScalarSin, float& ScalarCos, float Value)
```

### TInterpTo
```angelscript
FTransform TInterpTo(FTransform Current, FTransform Target, float32 DeltaTime, float32 InterpSpeed)
```

### Wrap
```angelscript
float Wrap(float X, float Min, float Max)
```
Wraps X to be between Min and Max, inclusive.
When X can wrap to both Min and Max, it will wrap to Min if it lies below the range and wrap to Max if it is above the range.

### Wrap
```angelscript
float32 Wrap(float32 X, float32 Min, float32 Max)
```
Wraps X to be between Min and Max, inclusive.
When X can wrap to both Min and Max, it will wrap to Min if it lies below the range and wrap to Max if it is above the range.

### WrapIndex
```angelscript
int WrapIndex(int Value, int Min, int Max)
```
Wrap the index so it is always [>= Min, < Max)
Values lower than Min are wrapped below Max.
Values Max or higher are wrapped to Min.

This differs from Math::Wrap() in that the Max boundary is exclusive,
rather than inclusive.

### WrapIndex
```angelscript
uint WrapIndex(uint Value, uint Min, uint Max)
```
Wrap the index so it is always [>= Min, < Max)
Values lower than Min are wrapped below Max.
Values Max or higher are wrapped to Min.

This differs from Math::Wrap() in that the Max boundary is exclusive,
rather than inclusive.

