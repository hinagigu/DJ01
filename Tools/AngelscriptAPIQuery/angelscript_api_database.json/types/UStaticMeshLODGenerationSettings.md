# UStaticMeshLODGenerationSettings

**继承自**: `UObject`

UStaticMeshLODGenerationSettings is intended to be a stored version of the settings used
by UGenerateStaticMeshLODProcess (and the associated UGenerateStaticMeshLODAssetTool).
This UObject is exposed as an Asset type in the Editor via UStaticMeshLODGenerationSettingsFactory.

The Tool uses these serialized settings as a 'Preset', ie the user can save a set
of configured settings, or load previously-saved settings.

## 属性

### Preprocessing
- **类型**: `FGenerateStaticMeshLODProcess_PreprocessSettings`

### MeshGeneration
- **类型**: `FGenerateStaticMeshLODProcessSettings`

### Simplification
- **类型**: `FGenerateStaticMeshLODProcess_SimplifySettings`

### Normals
- **类型**: `FGenerateStaticMeshLODProcess_NormalsSettings`

### TextureBaking
- **类型**: `FGenerateStaticMeshLODProcess_TextureSettings`

### UVGeneration
- **类型**: `FGenerateStaticMeshLODProcess_UVSettings`

### SimpleCollision
- **类型**: `FGenerateStaticMeshLODProcess_CollisionSettings`

