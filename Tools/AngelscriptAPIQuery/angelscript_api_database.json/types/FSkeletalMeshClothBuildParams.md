# FSkeletalMeshClothBuildParams

Struct holding parameters needed when creating a new clothing asset or sub asset (LOD)

## 属性

### TargetAsset
- **类型**: `TWeakObjectPtr<UClothingAssetBase>`
- **描述**: Target asset when importing LODs

### TargetLod
- **类型**: `int`
- **描述**: Target LOD to import to when importing LODs

### bRemapParameters
- **类型**: `bool`
- **描述**: If reimporting, this will map the old LOD parameters to the new LOD mesh.
If adding a new LOD this will map the parameters from the preceeding LOD.

### AssetName
- **类型**: `FString`
- **描述**: Name of the clothing asset

### LodIndex
- **类型**: `int`
- **描述**: LOD to extract the section from

### SourceSection
- **类型**: `int`
- **描述**: Section within the specified LOD to extract

### bRemoveFromMesh
- **类型**: `bool`
- **描述**: Whether or not to leave this section behind (if driving a mesh with itself). Enable this if driving a high poly mesh with a low poly

### PhysicsAsset
- **类型**: `TSoftObjectPtr<UPhysicsAsset>`
- **描述**: Physics asset to extract collisions from, note this will only extract spheres and Sphyls, as that is what the simulation supports.

## 方法

### opAssign
```angelscript
FSkeletalMeshClothBuildParams& opAssign(FSkeletalMeshClothBuildParams Other)
```

