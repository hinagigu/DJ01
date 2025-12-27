# UNavigationPath

**继承自**: `UObject`

UObject wrapper for FNavigationPath

## 属性

### PathUpdatedNotifier
- **类型**: `FOnNavigationPathUpdated`

### PathPoints
- **类型**: `TArray<FVector>`

### RecalculateOnInvalidation
- **类型**: `ENavigationOptionFlag`

## 方法

### EnableDebugDrawing
```angelscript
void EnableDebugDrawing(bool bShouldDrawDebugData, FLinearColor PathColor)
```

### EnableRecalculationOnInvalidation
```angelscript
void EnableRecalculationOnInvalidation(ENavigationOptionFlag DoRecalculation)
```
if enabled path will request recalculation if it gets invalidated due to a change to underlying navigation

### GetDebugString
```angelscript
FString GetDebugString()
```
UObject end

### GetPathCost
```angelscript
float GetPathCost()
```

### GetPathLength
```angelscript
float GetPathLength()
```

### IsPartial
```angelscript
bool IsPartial()
```

### IsStringPulled
```angelscript
bool IsStringPulled()
```

### IsValid
```angelscript
bool IsValid()
```

