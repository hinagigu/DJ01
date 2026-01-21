# ComboGraph 学习文档

本目录包含对 ComboGraph 插件的深度分析，旨在帮助 UE 新手从中学习游戏开发和插件架构知识。

## 📚 文档目录

| 文档 | 内容 | 适合阅读顺序 |
|------|------|-------------|
| [01-设计思想与架构概述](./01-DesignPhilosophy.md) | 插件的设计理念、解决的问题、整体架构 | ⭐ 第一个读 |
| [02-核心类解析](./02-CoreClasses.md) | 关键类的职责、继承关系、交互方式 | ⭐⭐ |
| [03-图编辑器系统](./03-GraphEditorSystem.md) | 自定义编辑器的实现，学习 UE 编辑器扩展 | ⭐⭐⭐ |
| [04-运行时执行流程](./04-RuntimeExecution.md) | 连招如何在游戏中实际执行 | ⭐⭐⭐ |
| [05-GAS集成详解](./05-GASIntegration.md) | 与 Gameplay Ability System 的深度整合 | ⭐⭐⭐⭐ |
| [06-网络同步机制](./06-NetworkReplication.md) | 多人游戏中的同步策略 | ⭐⭐⭐⭐ |
| [07-设计难点与解决方案](./07-DesignChallenges.md) | 开发中的技术挑战及解决思路 | ⭐⭐⭐⭐⭐ |
| [08-学习收获总结](./08-LearningPoints.md) | 从插件中可以学到的 UE 知识点 | 最后总结 |
| [09-调试实战案例](./09-DebugCaseStudy.md) | DJ01项目集成时的调试经验 | 实战参考 |

## 🎯 学习目标

通过研究 ComboGraph，你将学到：

1. **UE 资产系统**：如何创建自定义资产类型
2. **图编辑器开发**：自定义 EdGraph、Schema、节点渲染
3. **GAS 深度集成**：AbilityTask、GameplayEffect、GameplayCue
4. **增强输入系统**：Enhanced Input 在复杂场景的应用
5. **网络编程**：Gameplay 事件的网络同步
6. **动画系统**：AnimNotify、Montage 动态控制
7. **插件架构**：模块划分、编辑器/运行时分离

---

*文档版本：1.0 | 基于 ComboGraph 1.4.0 分析*