# FCollisionQueryParams

## 属性

### TraceTag
- **类型**: `FName`

### OwnerTag
- **类型**: `FName`

### bTraceComplex
- **类型**: `bool`

### bFindInitialOverlaps
- **类型**: `bool`

### bReturnFaceIndex
- **类型**: `bool`

### bReturnPhysicalMaterial
- **类型**: `bool`

### bIgnoreBlocks
- **类型**: `bool`

### bIgnoreTouches
- **类型**: `bool`

### bSkipNarrowPhase
- **类型**: `bool`

### MobilityType
- **类型**: `EQueryMobilityType`

### IgnoreMask
- **类型**: `uint8`

## 方法

### GetIgnoredComponents
```angelscript
TArray<uint> GetIgnoredComponents()
```

### GetIgnoredActors
```angelscript
TArray<uint> GetIgnoredActors()
```

### ClearIgnoredComponents
```angelscript
void ClearIgnoredComponents()
```

### ClearIgnoredActors
```angelscript
void ClearIgnoredActors()
```

### SetNumIgnoredComponents
```angelscript
void SetNumIgnoredComponents(int NewNum)
```

### AddIgnoredActor
```angelscript
void AddIgnoredActor(const AActor InIgnoreActor)
```

### AddIgnoredActor
```angelscript
void AddIgnoredActor(uint InIgnoreActorID)
```

### AddIgnoredActors
```angelscript
void AddIgnoredActors(TArray<AActor> InIgnoreActors)
```

### AddIgnoredActors
```angelscript
void AddIgnoredActors(TArray<const AActor> InIgnoreActors)
```

### AddIgnoredComponent
```angelscript
void AddIgnoredComponent(const UPrimitiveComponent InIgnoreComponent)
```

### AddIgnoredComponents
```angelscript
void AddIgnoredComponents(TArray<UPrimitiveComponent> InIgnoreComponents)
```

### AddIgnoredComponent_LikelyDuplicatedRoot
```angelscript
void AddIgnoredComponent_LikelyDuplicatedRoot(const UPrimitiveComponent InIgnoreComponent)
```

### ToString
```angelscript
FString ToString()
```

