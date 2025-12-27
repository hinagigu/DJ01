# ADJ01CharacterWithAbilities

**继承自**: `ADJ01Character`

ADJ01CharacterWithAbilities

ADJ01Character 通常从控制它的 PlayerState 获取 AbilitySystemComponent。
这个类代表一个带有自包含 AbilitySystemComponent 的角色。

使用场景：
- AI 控制的角色（没有 PlayerState）
- 不需要持久化技能状态的角色
- 单机游戏中的简化角色

注意：属性集（HealthSet, CombatSet 等）现在通过 GameFeatureAction_AddAbilities 动态添加，
而非在此类中硬编码。请在对应的 GameFeature 配置中添加属性集。

## 属性

### AbilitySystemComponent
- **类型**: `UDJ01AbilitySystemComponent`
- **描述**: 此角色使用的 AbilitySystemComponent（自包含，不依赖 PlayerState）

## 方法

### GetDJ01AbilitySystemComponent
```angelscript
UDJ01AbilitySystemComponent GetDJ01AbilitySystemComponent()
```
获取 DJ01 版本的 AbilitySystemComponent

