# UChaosClothingInteractor

**继承自**: `UClothingInteractor`

## 方法

### ResetAndTeleport
```angelscript
void ResetAndTeleport(bool bReset, bool bTeleport)
```

### SetAerodynamics
```angelscript
void SetAerodynamics(float32 DragCoefficient, float32 LiftCoefficient, FVector WindVelocity)
```
Deprecated. This function cannot set different Low and High values for the Drag and Lift weight maps. Use SetWind instead.

### SetAnimDrive
```angelscript
void SetAnimDrive(FVector2D AnimDriveStiffness, FVector2D AnimDriveDamping)
```

### SetAnimDriveLinear
```angelscript
void SetAnimDriveLinear(float32 AnimDriveStiffness)
```

### SetBackstop
```angelscript
void SetBackstop(bool bEnabled)
```

### SetCollision
```angelscript
void SetCollision(float32 CollisionThickness, float32 FrictionCoefficient, bool bUseCCD, float32 SelfCollisionThickness)
```

### SetDamping
```angelscript
void SetDamping(float32 DampingCoefficient, float32 LocalDampingCoefficient)
```

### SetGravity
```angelscript
void SetGravity(float32 GravityScale, bool bIsGravityOverridden, FVector GravityOverride)
```

### SetLongRangeAttachment
```angelscript
void SetLongRangeAttachment(FVector2D TetherStiffness, FVector2D TetherScale)
```

### SetLongRangeAttachmentLinear
```angelscript
void SetLongRangeAttachmentLinear(float32 TetherStiffness, float32 TetherScale)
```

### SetMaterial
```angelscript
void SetMaterial(FVector2D EdgeStiffness, FVector2D BendingStiffness, FVector2D AreaStiffness)
```

### SetMaterialLinear
```angelscript
void SetMaterialLinear(float32 EdgeStiffness, float32 BendingStiffness, float32 AreaStiffness)
```

### SetPressure
```angelscript
void SetPressure(FVector2D Pressure)
```

### SetVelocityScale
```angelscript
void SetVelocityScale(FVector LinearVelocityScale, float32 AngularVelocityScale, float32 FictitiousAngularScale)
```

### SetWind
```angelscript
void SetWind(FVector2D Drag, FVector2D Lift, float32 AirDensity, FVector WindVelocity)
```

