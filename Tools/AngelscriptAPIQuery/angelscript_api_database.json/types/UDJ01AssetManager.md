# UDJ01AssetManager

**继承自**: `UAssetManager`

DJ01 资产管理器

游戏的资产管理器，负责：
- 管理PrimaryAssets的加载和卸载
- 处理Bundle的加载策略
- 管理GameFeature的资产

使用方式：
1. 在DefaultEngine.ini中配置: AssetManagerClassName=/Script/DJ01.DJ01AssetManager
2. 配置PrimaryAssetTypes和PrimaryAssetRules

