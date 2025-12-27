# UParticleModuleLocationBoneSocket

**继承自**: `UParticleModuleLocationBase`

## 属性

### SourceType
- **类型**: `ELocationBoneSocketSource`
- **描述**: Whether the module uses Bones or Sockets for locations.

BONESOCKETSOURCE_Bones          - Use Bones as the source locations.
BONESOCKETSOURCE_Sockets        - Use Sockets as the source locations.

### UniversalOffset
- **类型**: `FVector`
- **描述**: An offset to apply to each bone/socket

### SourceLocations
- **类型**: `TArray<FLocationBoneSocketInfo>`
- **描述**: The name(s) of the bone/socket(s) to position at. If this is empty, the module will attempt to spawn from all bones or sockets.

### SelectionMethod
- **类型**: `ELocationBoneSocketSelectionMethod`
- **描述**: The method by which to select the bone/socket to spawn at.

SEL_Sequential                  - loop through the bone/socket array in order
SEL_Random                              - randomly select a bone/socket from the array

### InheritVelocityScale
- **类型**: `float32`
- **描述**: A scale on how much of the bone's velocity a particle will inherit.

### SkelMeshActorParamName
- **类型**: `FName`
- **描述**: The parameter name of the skeletal mesh actor that supplies the SkelMeshComponent for in-game.

### NumPreSelectedIndices
- **类型**: `int`
- **描述**: When we have no source locations and we need to track bone velocities due to bInheritBoneVelocity, we pre select a set of bones to use each frame. This property determines how big the list is.
Too low and the randomness of selection may suffer, too high and memory will be wasted.

### EditorSkelMesh
- **类型**: `USkeletalMesh`
- **描述**: The name of the skeletal mesh to use in the editor

### bUpdatePositionEachFrame
- **类型**: `bool`

### bInheritBoneVelocity
- **类型**: `bool`

