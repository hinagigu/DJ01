# UMaterialExpressionSceneTexture

**继承自**: `UMaterialExpression`

## 属性

### SceneTextureId
- **类型**: `ESceneTextureId`
- **描述**: Which scene texture (screen aligned texture) we want to make a lookup into

### bFiltered
- **类型**: `bool`
- **描述**: Whether to use point sampled texture lookup (default) or using [bi-linear] filtered (can be slower, avoid faceted lock with distortions), some SceneTextures cannot be filtered

