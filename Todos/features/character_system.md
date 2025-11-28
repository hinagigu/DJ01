# 角色系统设计文档

## 核心特性

### 1. 属性系统
```cpp
// 基础属性结构
struct FCharacterAttributes
{
    float Health;
    float Mana;
    float Stamina;
    float AttackPower;
    float Defense;
    float CriticalRate;
    float CriticalDamage;
};
```

### 2. 移动系统
- 基础移动速度：600
- 跑步速度：900
- 翻滚距离：500
- 跳跃高度：400

### 3. 状态系统
- Idle
- Walking
- Running
- Jumping
- Rolling
- Attacking
- Blocking
- Dead

## 技术实现

### 1. 组件结构
- DJ01HeroComponent：核心角色组件
- AttributeComponent：属性管理
- CombatComponent：战斗相关
- InventoryComponent：物品系统

### 2. 动画系统
- 状态机设计
- 动画通知
- 蒙太奇系统

### 3. 输入系统
- 移动：WASD
- 跳跃：Space
- 翻滚：Left Shift
- 攻击：Left Mouse
- 格挡：Right Mouse
- 技能：1234

## 开发优先级
1. 基础移动系统
2. 属性系统
3. 动画状态机
4. 战斗系统
5. 装备系统

## 参考资料
- Lyra角色系统实现
- UE5官方文档
- 常见RPG游戏角色设计