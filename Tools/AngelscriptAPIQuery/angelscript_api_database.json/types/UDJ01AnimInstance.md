# UDJ01AnimInstance

**继承自**: `UAnimInstance`

UDJ01AnimInstance

DJ01项目的基础动画实例类

功能特性：
- 与GAS（Gameplay Ability System）集成
- 支持GameplayTag到蓝图变量的自动映射
- 提供地面距离信息用于动画状态控制

## 属性

### GameplayTagPropertyMap
- **类型**: `FDJ01GameplayTagPropertyMap`
- **描述**: GameplayTag到蓝图变量的映射配置
当对应的Tag添加或移除时，映射的变量会自动更新
映射在构造函数中自动配置，由 Tag Manager 生成

### GroundSpeed
- **类型**: `float32`
- **描述**: 实际地面移动速度 (XY平面)
用于 BlendSpace 混合: Idle(0) -> Walk(150) -> Run(600)

### GroundDistance
- **类型**: `float32`
- **描述**: 角色到地面的距离，用于跳跃/降落动画控制

