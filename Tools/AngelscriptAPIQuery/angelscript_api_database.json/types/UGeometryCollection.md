# UGeometryCollection

**继承自**: `UObject`

UGeometryCollectionObject (UObject)

UObject wrapper for the FGeometryCollection

## 属性

### EnableClustering
- **类型**: `bool`

### ClusterGroupIndex
- **类型**: `int`
- **描述**: Maximum level for cluster breaks.

### MaxClusterLevel
- **类型**: `int`
- **描述**: Maximum level for cluster breaks.

### DamageModel
- **类型**: `EDamageModelTypeEnum`

### DamageThreshold
- **类型**: `TArray<float32>`
- **描述**: Damage threshold for clusters at different levels.

### bUseSizeSpecificDamageThreshold
- **类型**: `bool`
- **描述**: whether to use size specific damage threshold instead of level based ones ( see Size Specific Data array ).

### bUseMaterialDamageModifiers
- **类型**: `bool`

### PerClusterOnlyDamageThreshold
- **类型**: `bool`
- **描述**: compatibility check, when true, only cluster compute damage from parameters and propagate to direct children
when false, each child will compute it's damage threshold allowing for more precise and intuitive destruction behavior

### DamagePropagationData
- **类型**: `FGeometryCollectionDamagePropagationData`
- **描述**: Data about how damage propagation shoudl behave.

### ClusterConnectionType
- **类型**: `EClusterConnectionTypeEnum`

### ConnectionGraphBoundsFilteringMargin
- **类型**: `float32`

### GeometrySource
- **类型**: `TArray<FGeometryCollectionSource>`

### Materials
- **类型**: `TArray<TObjectPtr<UMaterialInterface>>`

### EmbeddedGeometryExemplar
- **类型**: `TArray<FGeometryCollectionEmbeddedExemplar>`
- **描述**: References for embedded geometry generation

### bUseFullPrecisionUVs
- **类型**: `bool`
- **描述**: Whether to use full precision UVs when rendering this geometry. (Does not apply to Nanite rendering)

### bStripOnCook
- **类型**: `bool`

### bStripRenderDataOnCook
- **类型**: `bool`

### CustomRendererType
- **类型**: `UClass`

### RootProxyData
- **类型**: `FGeometryCollectionProxyMeshData`

### AutoInstanceMeshes
- **类型**: `TArray<FGeometryCollectionAutoInstanceMesh>`
- **描述**: List of unique static mesh / materials pairs for auto instancing.

### PhysicsMaterial
- **类型**: `UPhysicalMaterial`

### bDensityFromPhysicsMaterial
- **类型**: `bool`

### bMassAsDensity
- **类型**: `bool`

### Mass
- **类型**: `float32`

### MinimumMassClamp
- **类型**: `float32`

### bImportCollisionFromSource
- **类型**: `bool`

### bOptimizeConvexes
- **类型**: `bool`

### bScaleOnRemoval
- **类型**: `bool`

### bRemoveOnMaxSleep
- **类型**: `bool`

### MaximumSleepTime
- **类型**: `FVector2D`

### RemovalDuration
- **类型**: `FVector2D`

### bSlowMovingAsSleeping
- **类型**: `bool`

### SlowMovingVelocityThreshold
- **类型**: `float32`

### SizeSpecificData
- **类型**: `TArray<FGeometryCollectionSizeSpecificData>`
- **描述**: * Size Specfic Data reflects the default geometry to bind to rigid bodies smaller
* than the max size volume. This can also be empty to reflect no collision geometry
* for the collection.

### AssetImportData
- **类型**: `UAssetImportData`

### ThumbnailInfo
- **类型**: `UThumbnailInfo`
- **描述**: Information for thumbnail rendering

### DataflowAsset
- **类型**: `UDataflow`

### DataflowTerminal
- **类型**: `FString`

### Overrides
- **类型**: `TMap<FString,FString>`

### AssetUserData
- **类型**: `TArray<TObjectPtr<UAssetUserData>>`
- **描述**: Array of user data stored with the asset

### bConvertVertexColorsToSRGB
- **类型**: `bool`

### EnableNanite
- **类型**: `bool`

## 方法

### SetConvertVertexColorsToSRGB
```angelscript
void SetConvertVertexColorsToSRGB(bool bValue)
```

### SetEnableNanite
```angelscript
void SetEnableNanite(bool bValue)
```

