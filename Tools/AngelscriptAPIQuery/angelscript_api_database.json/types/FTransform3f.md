# FTransform3f

## 方法

### opAssign
```angelscript
FTransform3f& opAssign(FTransform3f Other)
```

### Inverse
```angelscript
FTransform3f Inverse()
```

### Blend
```angelscript
void Blend(FTransform3f Atom1, FTransform3f Atom2, float32 Alpha)
```

### BlendWith
```angelscript
void BlendWith(FTransform3f OtherAtom, float32 Alpha)
```

### opMul
```angelscript
FTransform3f opMul(FTransform3f Other)
```

### opMul
```angelscript
FTransform3f opMul(FQuat4f Other)
```

### opMulAssign
```angelscript
void opMulAssign(FTransform3f Other)
```

### opMulAssign
```angelscript
void opMulAssign(FQuat4f Other)
```

### ScaleTranslation
```angelscript
void ScaleTranslation(FVector3f InScale3D)
```

### ScaleTranslation
```angelscript
void ScaleTranslation(float32 Scale)
```

### RemoveScaling
```angelscript
void RemoveScaling(float32 Tolerance)
```

### SetToRelativeTransform
```angelscript
void SetToRelativeTransform(FTransform3f Other)
```

### Accumulate
```angelscript
void Accumulate(FTransform3f SourceAtom)
```
Accumulates another transform with this one
Rotation is accumulated multiplicatively (Rotation = SourceAtom.Rotation * Rotation)
Translation is accumulated additively (Translation += SourceAtom.Translation)
Scale3D is accumulated multiplicatively (Scale3D *= SourceAtom.Scale3D)
@param SourceAtom The other transform to accumulate into this one

### GetMaximumAxisScale
```angelscript
float32 GetMaximumAxisScale()
```

### GetMinimumAxisScale
```angelscript
float32 GetMinimumAxisScale()
```

### GetRelativeTransform
```angelscript
FTransform3f GetRelativeTransform(FTransform3f Other)
```

### GetRelativeTransformReverse
```angelscript
FTransform3f GetRelativeTransformReverse(FTransform3f Other)
```

### TransformPosition
```angelscript
FVector3f TransformPosition(FVector3f V)
```

### TransformPositionNoScale
```angelscript
FVector3f TransformPositionNoScale(FVector3f V)
```

### InverseTransformPosition
```angelscript
FVector3f InverseTransformPosition(FVector3f V)
```

### InverseTransformPositionNoScale
```angelscript
FVector3f InverseTransformPositionNoScale(FVector3f V)
```

### TransformVector
```angelscript
FVector3f TransformVector(FVector3f V)
```

### TransformVectorNoScale
```angelscript
FVector3f TransformVectorNoScale(FVector3f V)
```

### InverseTransformVector
```angelscript
FVector3f InverseTransformVector(FVector3f V)
```

### InverseTransformVectorNoScale
```angelscript
FVector3f InverseTransformVectorNoScale(FVector3f V)
```

### TransformRotation
```angelscript
FQuat4f TransformRotation(FQuat4f Q)
```

### InverseTransformRotation
```angelscript
FQuat4f InverseTransformRotation(FQuat4f Q)
```

### SubtractTranslations
```angelscript
FVector3f SubtractTranslations(FTransform3f B)
```

### NormalizeRotation
```angelscript
void NormalizeRotation()
```

### IsRotationNormalized
```angelscript
bool IsRotationNormalized()
```

### TranslationEquals
```angelscript
bool TranslationEquals(FTransform3f Other, float32 Tolerance)
```

### EqualsNoScale
```angelscript
bool EqualsNoScale(FTransform3f Other, float32 Tolerance)
```

### Equals
```angelscript
bool Equals(FTransform3f Other, float32 Tolerance)
```

### GetLocation
```angelscript
FVector3f GetLocation()
```

### ContainsNaN
```angelscript
bool ContainsNaN()
```

### IsValid
```angelscript
bool IsValid()
```

### GetDeterminant
```angelscript
float32 GetDeterminant()
```

### Rotator
```angelscript
FRotator3f Rotator()
```

### GetTranslation
```angelscript
FVector3f GetTranslation()
```

### GetScale3D
```angelscript
FVector3f GetScale3D()
```

### GetRotation
```angelscript
FQuat4f GetRotation()
```

### SetLocation
```angelscript
void SetLocation(FVector3f Origin)
```

### SetTranslation
```angelscript
void SetTranslation(FVector3f Origin)
```

### AddToTranslation
```angelscript
void AddToTranslation(FVector3f Origin)
```

### ConcatenateRotation
```angelscript
void ConcatenateRotation(FQuat4f DeltaRotation)
```
Concatenates another rotation to this transformation
@param DeltaRotation The rotation to concatenate in the following fashion: Rotation = Rotation * DeltaRotation

### SetRotation
```angelscript
void SetRotation(FQuat4f NewRotation)
```

### SetScale3D
```angelscript
void SetScale3D(FVector3f NewScale3D)
```

### SetTranslationAndScale3D
```angelscript
void SetTranslationAndScale3D(FVector3f NewTranslation, FVector3f NewScale3D)
```

### InitFromString
```angelscript
bool InitFromString(FString SourceString)
```

### ToString
```angelscript
FString ToString()
```

### InverseTransformRotation
```angelscript
FRotator3f InverseTransformRotation(FRotator3f R)
```

### SetRotation
```angelscript
void SetRotation(FRotator3f NewRotation)
```

### TransformRotation
```angelscript
FRotator3f TransformRotation(FRotator3f R)
```

