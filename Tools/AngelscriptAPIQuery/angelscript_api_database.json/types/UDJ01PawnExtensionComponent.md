# UDJ01PawnExtensionComponent

**继承自**: `UPawnComponent`

UDJ01PawnExtensionComponent

为所有 Pawn 类添加功能的组件，可用于角色/载具等
协调其他组件的初始化顺序，管理 Pawn 的整个生命周期

初始化状态链：Spawned -> DataAvailable -> DataInitialized -> GameplayReady

## 属性

### PawnData
- **类型**: `const UDJ01PawnData`
- **描述**: 用于创建 Pawn 的 PawnData。从生成函数指定或在已放置的实例上指定

## 方法

### GetDJ01AbilitySystemComponent
```angelscript
UDJ01AbilitySystemComponent GetDJ01AbilitySystemComponent()
```
获取当前的 AbilitySystem 组件，可能由不同的 Actor 拥有

