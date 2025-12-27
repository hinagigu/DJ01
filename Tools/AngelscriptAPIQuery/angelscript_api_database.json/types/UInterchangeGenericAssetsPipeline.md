# UInterchangeGenericAssetsPipeline

**继承自**: `UInterchangePipelineBase`

This pipeline is the generic option for all types of meshes. It should be called before specialized mesh pipelines like the generic static mesh or skeletal mesh pipelines.
All import options that are shared between mesh types should be added here.

## 属性

### PipelineDisplayName
- **类型**: `FString`

### ReimportStrategy
- **类型**: `EReimportStrategyFlags`

### bUseSourceNameForAsset
- **类型**: `bool`

### AssetName
- **类型**: `FString`

### ImportOffsetTranslation
- **类型**: `FVector`

### ImportOffsetRotation
- **类型**: `FRotator`

### ImportOffsetUniformScale
- **类型**: `float32`

### CommonMeshesProperties
- **类型**: `UInterchangeGenericCommonMeshesProperties`

### CommonSkeletalMeshesAndAnimationsProperties
- **类型**: `UInterchangeGenericCommonSkeletalMeshesAndAnimationsProperties`

### MeshPipeline
- **类型**: `UInterchangeGenericMeshPipeline`

### AnimationPipeline
- **类型**: `UInterchangeGenericAnimationPipeline`

### MaterialPipeline
- **类型**: `UInterchangeGenericMaterialPipeline`

