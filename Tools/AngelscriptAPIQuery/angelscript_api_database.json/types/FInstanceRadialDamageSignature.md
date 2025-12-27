# FInstanceRadialDamageSignature

## 方法

### opAssign
```angelscript
FInstanceRadialDamageSignature& opAssign(FInstanceRadialDamageSignature Other)
```

### IsBound
```angelscript
bool IsBound()
```

### Clear
```angelscript
void Clear()
```

### AddUFunction
```angelscript
void AddUFunction(const UObject Object, FName FunctionName)
```

### Unbind
```angelscript
void Unbind(UObject Object, FName FunctionName)
```

### UnbindObject
```angelscript
void UnbindObject(UObject Object)
```

### Broadcast
```angelscript
void Broadcast(const TArray<int>&in Instances, const TArray<float32>&in Damages, AController InstigatedBy, FVector Origin, float32 MaxRadius, const UDamageType DamageType, AActor DamageCauser)
```

