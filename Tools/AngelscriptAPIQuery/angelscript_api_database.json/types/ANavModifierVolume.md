# ANavModifierVolume

**继承自**: `AVolume`

Allows applying selected AreaClass to navmesh, using Volume's shape

## 属性

### bMaskFillCollisionUnderneathForNavmesh
- **类型**: `bool`
- **描述**: Experimental: if set, the 2D space occupied by the volume box will ignore FillCollisionUnderneathForNavmesh

### NavMeshResolution
- **类型**: `ENavigationDataResolution`
- **描述**: Experimental: When not set to None, the navmesh tiles touched by the navigation modifier volume will be built
using the highest resolution found.

### AreaClass
- **类型**: `TSubclassOf<UNavArea>`

## 方法

### SetAreaClass
```angelscript
void SetAreaClass(TSubclassOf<UNavArea> NewAreaClass)
```

