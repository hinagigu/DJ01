# UDJ01HeroComponent

**继承自**: `UPawnComponent`

UDJ01HeroComponent

设置玩家控制的 Pawn（或模拟玩家的 Bot）的输入和相机处理的组件
此组件依赖于 PawnExtensionComponent 来协调初始化

对齐 Lyra 的 HeroComponent，提供：
- 输入绑定管理
- 相机模式控制
- 与 GameFeature 系统的集成
- 能力系统的输入处理

## 属性

### DefaultInputMappings
- **类型**: `TArray<FInputMappingContextAndPriority>`
- **描述**: 初始化此玩家时应添加的输入映射。这些配置
不会在设置中注册，因为它们是在运行时添加的。如果希望配置
出现在设置中，则通过 GameFeatureAction_AddInputConfig 添加

注意：只有在无法访问游戏功能插件时才应添加到此处。
如果可以，请使用 GameFeatureAction_AddInputConfig 代替。

