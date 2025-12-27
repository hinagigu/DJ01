# UFbxImportUI

**继承自**: `UObject`

## 属性

### bIsObjImport
- **类型**: `bool`
- **描述**: Whether or not the imported file is in OBJ format

### OriginalImportType
- **类型**: `EFBXImportType`
- **描述**: The original detected type of this import

### MeshTypeToImport
- **类型**: `EFBXImportType`
- **描述**: Type of asset to import from the FBX file

### bImportAsSkeletal
- **类型**: `bool`

### bImportMesh
- **类型**: `bool`

### Skeleton
- **类型**: `USkeleton`

### PhysicsAsset
- **类型**: `UPhysicsAsset`

### LodDistance0
- **类型**: `float32`

### LodDistance1
- **类型**: `float32`

### LodDistance2
- **类型**: `float32`

### LodDistance3
- **类型**: `float32`

### LodDistance4
- **类型**: `float32`

### LodDistance5
- **类型**: `float32`

### LodDistance6
- **类型**: `float32`

### LodDistance7
- **类型**: `float32`

### MinimumLodNumber
- **类型**: `int`

### LodNumber
- **类型**: `int`

### OverrideAnimationName
- **类型**: `FString`

### StaticMeshImportData
- **类型**: `UFbxStaticMeshImportData`

### SkeletalMeshImportData
- **类型**: `UFbxSkeletalMeshImportData`

### AnimSequenceImportData
- **类型**: `UFbxAnimSequenceImportData`

### TextureImportData
- **类型**: `UFbxTextureImportData`

### bAutomatedImportShouldDetectType
- **类型**: `bool`
- **描述**: If true the automated import path should detect the import type.  If false the import type was specified by the user

### bOverrideFullName
- **类型**: `bool`

### bCreatePhysicsAsset
- **类型**: `bool`

### bAutoComputeLodDistances
- **类型**: `bool`

### bImportAnimations
- **类型**: `bool`

### bImportRigidMesh
- **类型**: `bool`

### bImportMaterials
- **类型**: `bool`

### bImportTextures
- **类型**: `bool`

### bResetToFbxOnMaterialConflict
- **类型**: `bool`

## 方法

### ResetToDefault
```angelscript
void ResetToDefault()
```

