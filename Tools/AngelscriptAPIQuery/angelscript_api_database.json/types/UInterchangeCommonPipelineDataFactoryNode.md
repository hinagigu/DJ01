# UInterchangeCommonPipelineDataFactoryNode

**继承自**: `UInterchangeFactoryBaseNode`

This factory node is where pipelines can set global data that can be used by factories.

## 方法

### GetBakeMeshes
```angelscript
bool GetBakeMeshes(bool& AttributeValue)
```
Return the value of the Bake Meshes setting set by the pipelines.

### GetCustomGlobalOffsetTransform
```angelscript
bool GetCustomGlobalOffsetTransform(FTransform& AttributeValue)
```
Return the global offset transform set by the pipelines.

### SetBakeMeshes
```angelscript
bool SetBakeMeshes(const UInterchangeBaseNodeContainer NodeContainer, bool AttributeValue)
```
Pipelines can set this Bake Meshes setting. Factories use this to identify whether they should apply global transforms to static meshes and skeletal meshes.

### SetCustomGlobalOffsetTransform
```angelscript
bool SetCustomGlobalOffsetTransform(const UInterchangeBaseNodeContainer NodeContainer, FTransform AttributeValue)
```
Pipelines can set a global transform. Factories will use this global offset when importing assets.

