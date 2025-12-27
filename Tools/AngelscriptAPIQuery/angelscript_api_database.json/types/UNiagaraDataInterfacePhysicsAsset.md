# UNiagaraDataInterfacePhysicsAsset

**继承自**: `UNiagaraDataInterface`

Data Interface for interacting with PhysicsAssets

## 属性

### DefaultSource
- **类型**: `UPhysicsAsset`
- **描述**: Skeletal Mesh from which the Physics Asset will be found.

### SoftSourceActor
- **类型**: `TSoftObjectPtr<AActor>`
- **描述**: The source actor from which to sample

### MeshUserParameter
- **类型**: `FNiagaraUserParameterBinding`
- **描述**: Reference to a user parameter if we're reading one.

