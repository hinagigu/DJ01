# USkeletalMeshSocket

**继承自**: `UObject`

## 属性

### SocketName
- **类型**: `FName`
- **描述**: Defines a named attachment location on the USkeletalMesh.
These are set up in editor and used as a shortcut instead of specifying
everything explicitly to AttachComponent in the SkeletalMeshComponent.
The Outer of a SkeletalMeshSocket should always be the USkeletalMesh.

### BoneName
- **类型**: `FName`

### RelativeLocation
- **类型**: `FVector`

### RelativeRotation
- **类型**: `FRotator`

### RelativeScale
- **类型**: `FVector`

### bForceAlwaysAnimated
- **类型**: `bool`

## 方法

### GetSocketLocation
```angelscript
FVector GetSocketLocation(const USkeletalMeshComponent SkelComp)
```

### InitializeSocketFromLocation
```angelscript
void InitializeSocketFromLocation(const USkeletalMeshComponent SkelComp, FVector WorldLocation, FVector WorldNormal)
```
Sets BoneName, RelativeLocation and RelativeRotation based on closest bone to WorldLocation and WorldNormal

