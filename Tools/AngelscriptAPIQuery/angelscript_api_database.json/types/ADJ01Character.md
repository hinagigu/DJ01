# ADJ01Character

**继承自**: `AModularCharacter`

ADJ01Character

项目的基础角色类，使用模块化游戏框架
- 实现 IAbilitySystemInterface 以支持技能系统
- 实现 IGameplayTagAssetInterface 以支持 GameplayTag 查询
- 负责向 Pawn 组件发送事件
- 新行为应尽可能通过 Pawn 组件添加

注意：HeroComponent 不在这里创建，而是通过 Game Feature Data (GFD) 的 Action 动态添加

## 属性

### PawnExtComponent
- **类型**: `UDJ01PawnExtensionComponent`

### CameraComponent
- **类型**: `UDJ01CameraComponent`

