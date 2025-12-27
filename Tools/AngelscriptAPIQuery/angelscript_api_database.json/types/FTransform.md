# FTransform

## 方法

### opAssign
```angelscript
FTransform& opAssign(FTransform Other)
```

### Inverse
```angelscript
FTransform Inverse()
```

### Blend
```angelscript
void Blend(FTransform Atom1, FTransform Atom2, float32 Alpha)
```

### BlendWith
```angelscript
void BlendWith(FTransform OtherAtom, float32 Alpha)
```

### opMul
```angelscript
FTransform opMul(FTransform Other)
```

### opMul
```angelscript
FTransform opMul(FQuat Other)
```

### opMulAssign
```angelscript
void opMulAssign(FTransform Other)
```

### opMulAssign
```angelscript
void opMulAssign(FQuat Other)
```

### ScaleTranslation
```angelscript
void ScaleTranslation(FVector InScale3D)
```

### ScaleTranslation
```angelscript
void ScaleTranslation(float Scale)
```

### RemoveScaling
```angelscript
void RemoveScaling(float Tolerance)
```

### SetToRelativeTransform
```angelscript
void SetToRelativeTransform(FTransform Other)
```

### Accumulate
```angelscript
void Accumulate(FTransform SourceAtom)
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
FTransform GetRelativeTransform(FTransform Other)
```

### GetRelativeTransformReverse
```angelscript
FTransform GetRelativeTransformReverse(FTransform Other)
```

### TransformPosition
```angelscript
FVector TransformPosition(FVector V)
```

### TransformPositionNoScale
```angelscript
FVector TransformPositionNoScale(FVector V)
```

### InverseTransformPosition
```angelscript
FVector InverseTransformPosition(FVector V)
```

### InverseTransformPositionNoScale
```angelscript
FVector InverseTransformPositionNoScale(FVector V)
```

### TransformVector
```angelscript
FVector TransformVector(FVector V)
```

### TransformVectorNoScale
```angelscript
FVector TransformVectorNoScale(FVector V)
```

### InverseTransformVector
```angelscript
FVector InverseTransformVector(FVector V)
```

### InverseTransformVectorNoScale
```angelscript
FVector InverseTransformVectorNoScale(FVector V)
```

### TransformRotation
```angelscript
FQuat TransformRotation(FQuat Q)
```

### InverseTransformRotation
```angelscript
FQuat InverseTransformRotation(FQuat Q)
```

### SubtractTranslations
```angelscript
FVector SubtractTranslations(FTransform B)
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
bool TranslationEquals(FTransform Other, float Tolerance)
```

### EqualsNoScale
```angelscript
bool EqualsNoScale(FTransform Other, float Tolerance)
```

### Equals
```angelscript
bool Equals(FTransform Other, float Tolerance)
```

### GetLocation
```angelscript
FVector GetLocation()
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
float GetDeterminant()
```

### Rotator
```angelscript
FRotator Rotator()
```

### GetTranslation
```angelscript
FVector GetTranslation()
```

### GetScale3D
```angelscript
FVector GetScale3D()
```

### GetRotation
```angelscript
FQuat GetRotation()
```

### ToMatrixWithScale
```angelscript
FMatrix ToMatrixWithScale()
```

### ToMatrixNoScale
```angelscript
FMatrix ToMatrixNoScale()
```

### ToInverseMatrixWithScale
```angelscript
FMatrix ToInverseMatrixWithScale()
```

### SetLocation
```angelscript
void SetLocation(FVector Origin)
```

### SetTranslation
```angelscript
void SetTranslation(FVector Origin)
```

### AddToTranslation
```angelscript
void AddToTranslation(FVector Origin)
```

### ConcatenateRotation
```angelscript
void ConcatenateRotation(FQuat DeltaRotation)
```
Concatenates another rotation to this transformation
@param DeltaRotation The rotation to concatenate in the following fashion: Rotation = Rotation * DeltaRotation

### SetRotation
```angelscript
void SetRotation(FQuat NewRotation)
```

### SetScale3D
```angelscript
void SetScale3D(FVector NewScale3D)
```

### SetTranslationAndScale3D
```angelscript
void SetTranslationAndScale3D(FVector NewTranslation, FVector NewScale3D)
```

### InitFromString
```angelscript
bool InitFromString(FString SourceString)
```

### ToString
```angelscript
FString ToString()
```

### Blend
```angelscript
void Blend(FTransform Atom1, FTransform Atom2, float Alpha)
```

### BlendWith
```angelscript
void BlendWith(FTransform OtherAtom, float Alpha)
```

### InverseTransformRotation
```angelscript
FRotator InverseTransformRotation(FRotator R)
```

### SetRotation
```angelscript
void SetRotation(FRotator NewRotation)
```

### TransformRotation
```angelscript
FRotator TransformRotation(FRotator R)
```

