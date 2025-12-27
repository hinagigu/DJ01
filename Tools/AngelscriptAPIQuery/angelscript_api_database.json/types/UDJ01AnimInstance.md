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
- **类型**: `FGameplayTagBlueprintPropertyMap`
- **描述**: GameplayTag到蓝图变量的映射配置
当对应的Tag添加或移除时，映射的变量会自动更新
应使用此映射而非手动查询GameplayTag

### GroundSpeed
- **类型**: `float32`
- **描述**: 实际地面移动速度 (XY平面)
用于 BlendSpace 混合: Idle(0) -> Walk(150) -> Run(600)

### GroundDistance
- **类型**: `float32`
- **描述**: 角色到地面的距离，用于跳跃/降落动画控制

### bIsGrounded
- **类型**: `bool`
- **描述**: 是否在地面上 (映射自 Status.Movement.Grounded)

### bIsAttacking
- **类型**: `bool`
- **描述**: 是否在攻击中 (映射自 Status.Action.Attacking)

### bIsStunned
- **类型**: `bool`
- **描述**: 是否被眩晕 (映射自 Status.Condition.Stunned)

