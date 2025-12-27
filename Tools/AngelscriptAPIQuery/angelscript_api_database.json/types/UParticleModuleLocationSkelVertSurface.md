# UParticleModuleLocationSkelVertSurface

**继承自**: `UParticleModuleLocationBase`

## 属性

### SourceType
- **类型**: `ELocationSkelVertSurfaceSource`
- **描述**: Whether the module uses Verts or Surfaces for locations.

VERTSURFACESOURCE_Vert          - Use Verts as the source locations.
VERTSURFACESOURCE_Surface       - Use Surfaces as the source locations.

### UniversalOffset
- **类型**: `FVector`
- **描述**: An offset to apply to each vert/surface

### InheritVelocityScale
- **类型**: `float32`
- **描述**: A scale on how much of the bone's velocity a particle will inherit.

### SkelMeshActorParamName
- **类型**: `FName`
- **描述**: The parameter name of the skeletal mesh actor that supplies the SkelMeshComponent for in-game.

### EditorSkelMesh
- **类型**: `USkeletalMesh`
- **描述**: The name of the skeletal mesh to use in the editor

### ValidAssociatedBones
- **类型**: `TArray<FName>`
- **描述**: This module will only spawn from verts or surfaces associated with the bones in this list

### NormalToCompare
- **类型**: `FVector`
- **描述**: Use this normal to restrict spawning locations

### NormalCheckToleranceDegrees
- **类型**: `float32`
- **描述**: Normal tolerance.  0 degrees means it must be an exact match, 180 degrees means it can be any angle.

### ValidMaterialIndices
- **类型**: `TArray<int>`
- **描述**: Array of material indices that are valid materials to spawn from.
If empty, any material will be considered valid

### InheritUVChannel
- **类型**: `uint`
- **描述**: UV channel to inherit from the spawn mesh, internally clamped to those available.

### bUpdatePositionEachFrame
- **类型**: `bool`

### bOrientMeshEmitters
- **类型**: `bool`

### bInheritBoneVelocity
- **类型**: `bool`

### bEnforceNormalCheck
- **类型**: `bool`

### bInheritVertexColor
- **类型**: `bool`

### bInheritUV
- **类型**: `bool`

