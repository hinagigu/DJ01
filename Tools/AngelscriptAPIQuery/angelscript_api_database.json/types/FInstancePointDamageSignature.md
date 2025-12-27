# FInstancePointDamageSignature

## 方法

### opAssign
```angelscript
FInstancePointDamageSignature& opAssign(FInstancePointDamageSignature Other)
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
void Broadcast(int InstanceIndex, float32 Damage, AController InstigatedBy, FVector HitLocation, FVector ShotFromDirection, const UDamageType DamageType, AActor DamageCauser)
```

