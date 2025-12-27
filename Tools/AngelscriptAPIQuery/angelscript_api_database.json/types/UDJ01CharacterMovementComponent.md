# UDJ01CharacterMovementComponent

**继承自**: `UCharacterMovementComponent`

UDJ01CharacterMovementComponent

为 RPG 项目优化的角色移动组件

功能特性：
- 基础移动（走/跑/跳跃）
- 地面信息检测（用于播放地面特效和音效）
- 预留 GAS 集成接口（用于技能系统控制移动）

设计理念：
- 简化的实现，适合 RPG 游戏的移动需求
- 相比 Lyra 移除了复杂的网络优化（RPG 通常移动较慢）
- 保留可扩展性，便于后续添加冲刺、翻滚等功能

## 方法

### GetGroundInfo
```angelscript
FDJ01CharacterGroundInfo GetGroundInfo()
```
获取当前地面信息
会自动缓存结果，同一帧内多次调用不会重复检测

使用场景：
- 脚步声系统：根据地面材质播放不同声音
- 粒子特效：根据地面类型生成灰尘、水花等
- 游戏逻辑：检测角色是否在特殊地面上（岩浆、冰面等）

