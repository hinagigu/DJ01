# 🗺️ DJ01 项目开发路标

> **定位**: UE5 动作战斗系统技术研究项目  
> **核心方向**: 动作系统深度优化 (Motion Warping + 连招取消)  
> **时间规划**: 2026.01 - 2027.01 (一年期)  
> **版本**: v4.0 | **日期**: 2026-01-18

---

## 📊 项目状态一览

```
基础框架 ████████████████████████░░ 85%
动作系统 ████████████░░░░░░░░░░░░░░ 45%  ← 深挖方向
```

| 领域 | 完成度 | 说明 |
|------|--------|------|
| GAS 战斗框架 | ✅ 95% | ASC + 三层属性 + DamageExecution |
| 开发工具链 | ✅ 100% | 4 个 Python 工具 |
| 连招系统 (基础) | ✅ 90% | ComboGraph + 输入缓冲 |
| 动画层架构 | ✅ 90% | Lyra 风格 + BindingSet |
| **Motion Warping** | ⬜ 0% | 🎯 下一步 |
| **连招取消系统** | ⬜ 0% | 🎯 核心目标 |
| **受击反馈** | ⬜ 10% | 🎯 打击感 |
| 敌人 AI | ⬜ 10% | 后期完善 |

---

## 🎯 核心目标：动作系统深挖

### 为什么选择这个方向？

```
┌────────────────────────────────────────────────────────────────┐
│  GAS 基础功能 → 引擎内置，大多数人都能做                        │
│  连招 + 动画层 → 你已经做了，但还不够深                         │
│  Motion Warping + Cancel System → 专业动作游戏核心技术 ✅       │
└────────────────────────────────────────────────────────────────┘
```

**目标产出**:
- 专业级动作战斗手感
- 可演示的技术 Demo 视频
- 完整的技术文档

---

## 📅 一年期开发规划

```
2026.01 ─────────────────────────────────────────────── 2027.01
    │                                                      │
    ├── Q1: 动作系统基础 ──┬── Motion Warping             │
    │                      └── 受击反馈 (Hit Stop)         │
    │                                                      │
    ├── Q2: 连招取消系统 ──┬── Cancel Window 架构          │
    │                      ├── 闪避取消                    │
    │                      └── 技能取消                    │
    │                                                      │
    ├── Q3: 系统完善 ──────┬── 敌人 AI                     │
    │                      ├── 完整战斗循环                │
    │                      └── Debug/调试工具              │
    │                                                      │
    └── Q4: Demo 制作 ─────┬── 场景搭建                    │
                           ├── 视频录制                    │
                           └── 文档整理                    │
```

---

## 🎮 Phase 2A: Motion Warping (Q1)

> **预计时间**: 2-3 周  
> **目标**: 让攻击动作自动追踪目标

### 什么是 Motion Warping?

在运行时动态调整 Root Motion 动画，使角色自动对齐目标：
- 攻击时自动转向敌人
- 冲刺攻击自动停在合适距离
- 翻滚朝向输入方向

### 任务分解

| # | 任务 | 说明 | 预估 |
|---|------|------|------|
| 2A.1 | 添加 MotionWarpingComponent | 角色集成 | 2h |
| 2A.2 | 目标检测系统 | 检测攻击范围内的敌人 | 4h |
| 2A.3 | Montage Warp Window | 配置动画扭曲窗口 | 4h |
| 2A.4 | 攻击朝向修正 | 自动转向目标 | 4h |
| 2A.5 | 冲刺攻击对齐 | 位移 + 朝向 | 4h |
| 2A.6 | 翻滚方向控制 | 朝输入方向翻滚 | 4h |
| 2A.7 | 测试调参 | 参数微调 | 4h |

### 技术要点

```cpp
// 核心代码结构
UPROPERTY()
UMotionWarpingComponent* MotionWarpingComp;

// 攻击时设置目标
FMotionWarpingTarget Target;
Target.Name = FName("AttackTarget");
Target.Location = Enemy->GetActorLocation();
Target.Rotation = (Enemy->GetActorLocation() - GetActorLocation()).Rotation();
MotionWarpingComp->AddOrUpdateWarpTarget(Target);
```

### 验收标准

- [ ] 轻攻击时自动转向 90° 范围内的敌人
- [ ] 冲刺攻击时自动冲向目标并停在攻击距离
- [ ] 翻滚时朝输入方向移动
- [ ] 无目标时保持原方向

---

## ⚔️ Phase 2B: 连招取消系统 (Q2)

> **预计时间**: 4-6 周  
> **目标**: 实现专业的动作取消机制

### 核心概念

```
[攻击动画时间轴]
|----[不可取消]----[可闪避取消]----[可技能取消]----[可连招]----[收招]---|
     0%            25%            40%            60%        85%   100%

取消优先级: 受击打断 > 闪避取消 > 技能取消 > 连招衔接
```

### 2B.1 Cancel Window 架构 (Week 1-2)

| 任务 | 说明 | 预估 |
|------|------|------|
| 设计 CancelWindow 数据结构 | 定义取消窗口类型和时间 | 4h |
| 创建 DJ01CancelWindowComponent | 管理当前可用的取消选项 | 8h |
| AnimNotify_CancelWindow | Montage 中标记取消窗口 | 4h |
| 与 GAS 技能系统集成 | 技能激活时检查取消条件 | 6h |

```cpp
// Cancel Window 类型
UENUM()
enum class ECancelWindowType : uint8
{
    None,           // 不可取消
    DodgeCancel,    // 可闪避取消
    SkillCancel,    // 可技能取消
    ComboCancel,    // 可连招衔接
    AnyCancel       // 任意取消
};
```

### 2B.2 闪避取消 (Week 3)

| 任务 | 说明 | 预估 |
|------|------|------|
| 创建 GA_Dodge 技能 | 闪避/翻滚 Gameplay Ability | 4h |
| 闪避取消逻辑 | 检测 DodgeCancel 窗口 | 4h |
| 无敌帧实现 | 闪避期间的 i-frame | 4h |
| 动画配置 | 8 方向翻滚动画 | 6h |

### 2B.3 技能取消 (Week 4)

| 任务 | 说明 | 预估 |
|------|------|------|
| 技能取消检测 | SkillCancel 窗口判断 | 4h |
| 与 ComboGraph 集成 | 从连招分支到技能 | 6h |
| 资源消耗检查 | 蓝量/冷却判断 | 4h |

### 2B.4 受击打断 (Week 5)

| 任务 | 说明 | 预估 |
|------|------|------|
| 受击事件处理 | GE 触发中断 | 4h |
| 霸体状态 | 部分动作不可打断 | 4h |
| 受击硬直计算 | 根据伤害决定硬直时间 | 4h |

### 验收标准

- [ ] 攻击中按闪避键可取消当前动作并翻滚
- [ ] 攻击中按技能键可释放特殊技能
- [ ] 被攻击时正确打断当前动作
- [ ] 霸体状态下不被打断

---

## 💥 Phase 2C: 受击反馈系统 (Q1-Q2)

> **预计时间**: 2-3 周  
> **目标**: 让战斗有打击感

### 任务分解

| # | 任务 | 说明 | 预估 |
|---|------|------|------|
| 2C.1 | Hit Stop (顿帧) | 命中瞬间暂停 | 4h |
| 2C.2 | Camera Shake | 相机震动 | 2h |
| 2C.3 | 敌人受击动画 | 根据方向/力度播放 | 6h |
| 2C.4 | 击退效果 | 击退/击飞物理 | 6h |
| 2C.5 | GameplayCue 配置 | 特效/音效 | 4h |

### Hit Stop 实现

```cpp
// 命中时调用
void UDJ01HitStopManager::ApplyHitStop(float Duration, AActor* Attacker, AActor* Victim)
{
    // 暂停攻击者动画
    Attacker->CustomTimeDilation = 0.01f;
    // 暂停受击者动画  
    Victim->CustomTimeDilation = 0.01f;
    
    // 定时恢复
    GetWorld()->GetTimerManager().SetTimer(
        HitStopTimer, 
        [Attacker, Victim]() {
            Attacker->CustomTimeDilation = 1.0f;
            Victim->CustomTimeDilation = 1.0f;
        },
        Duration, false);
}
```

### 验收标准

- [ ] 攻击命中时有明显的顿帧感
- [ ] 相机随攻击类型震动
- [ ] 敌人根据攻击方向播放受击动画
- [ ] 重攻击有明显击退效果

---

## 🤖 Phase 3: 敌人与完整战斗循环 (Q3)

> **预计时间**: 4-6 周

### 任务概览

| 模块 | 说明 | 预估 |
|------|------|------|
| BP_TestEnemy | 基础敌人 Pawn | 1 周 |
| 敌人 ASC + 属性 | HealthSet, StatSet | 3 天 |
| 行为树 AI | 巡逻/追击/攻击 | 2 周 |
| 敌人攻击技能 | GA_Enemy_Attack | 1 周 |
| 战斗调试工具 | Debug 显示/日志 | 1 周 |

---

## 🎬 Phase 4: Demo 制作 (Q4)

> **预计时间**: 4-6 周

### 任务概览

| 模块 | 说明 | 预估 |
|------|------|------|
| Demo 场景 | 战斗竞技场 | 2 周 |
| 视觉打磨 | 特效/UI | 2 周 |
| 视频录制 | 1-2 分钟技术 Demo | 1 周 |
| 文档整理 | README/技术文档 | 1 周 |

---

## ✅ 已完成模块

### Phase 0-1: 基础框架 (已完成)

| 模块 | 路径 | 亮点 |
|------|------|------|
| **GAS 系统** | `AbilitySystem/` | 三层属性、DamageExecution、BindingSet |
| **角色系统** | `Character/` | DJ01CharacterWithAbilities |
| **Experience** | `Experience/` | Lyra 风格异步加载 |
| **输入系统** | `Input/` | Enhanced Input + 输入缓冲 |
| **相机系统** | `Camera/` | 第三人称 + 战斗相机 |
| **连招系统** | ComboGraph | 4 段连招 + 分支 |
| **动画层** | `Animation/` | 武器动画层 + 状态机 |

### 开发工具 (已完成)

| 工具 | 功能 | 技术亮点 |
|------|------|----------|
| **AttributeGenerator** | GAS 代码生成 | 属性/Tag/Execution/MMC |
| **DataAssetManager** | 数据资产管理 | Python ↔ UE Remote Execution |
| **UIGenerator** | UI 代码生成 | Schema 驱动 + MVVM |
| **AngelscriptAPIQuery** | API 查询 | 运行时反射 + 文档导出 |

---

## 📚 文档索引

| 分类 | 路径 | 篇数 |
|------|------|------|
| GAS 架构 | `Source/DJ01/AbilitySystem/*.md` | 2 篇 |
| 连招教程 | `docs/ComBoFirst/` | 13 篇 |
| 动画系统 | `docs/Now/Animation/` | 5 篇 |
| AngelScript | `docs/AngelscriptGuide/` | 12 篇 |
| ComboGraph 源码 | `docs/ComboGraph/` | 10 篇 |

---

## 💼 求职亮点 (预期)

### 完成后的技术展示

| 特性 | 专业度 | 说明 |
|------|--------|------|
| **Motion Warping** | ⭐⭐⭐⭐⭐ | 现代动作游戏标配 |
| **Cancel System** | ⭐⭐⭐⭐⭐ | 《鬼泣》《战神》核心机制 |
| **Hit Stop** | ⭐⭐⭐⭐ | 打击感的关键 |
| **GAS 三层属性** | ⭐⭐⭐⭐ | 自定义架构 |
| **4 个开发工具** | ⭐⭐⭐⭐⭐ | 工程化能力 |
| **输入缓冲** | ⭐⭐⭐⭐ | 操作手感 |

### 面试话术

> "我的动作战斗系统基于 Lyra 架构，实现了 Motion Warping 自动追踪、多层取消窗口（闪避取消/技能取消/受击打断）、Hit Stop 顿帧系统。
> 
> 技能系统使用 GAS，采用三层属性架构（Base/Flat/Percent），伤害计算使用自定义 ExecutionCalculation。
> 
> 为了提升开发效率，我还开发了 4 个 Python 工具来自动生成 GAS 代码、管理数据资产。"

---

## 🔮 长期愿景 (暂缓)

> 保留为创意文档，有团队后继续

- 世界构建（格兰维尔）
- NPC/对话/任务系统
- ~~元素反应~~ (已废弃)
- 游戏完整流程

---

## 📝 更新记录

| 日期 | 版本 | 变更 |
|------|------|------|
| 2026-01-18 | v4.0 | 一年期长期规划，聚焦动作系统深挖 |
| 2026-01-18 | v3.0 | 项目重新定位为技术 Demo |
| 2025-12 | - | 完成 GAS 工具链 |
| 2025-11 | - | 项目启动，Lyra 适配 |

---

*一年后，这将是一份专业级的动作战斗系统技术展示。*