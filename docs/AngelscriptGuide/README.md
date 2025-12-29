# UE-Angelscript 深度解析系列文档

> 本系列文档深入剖析 UE-Angelscript 插件的核心架构、绑定机制和运行原理。
> 适合想要深入理解 UE + AngelScript 集成的开发者。

## 📚 文档目录

| 章节 | 文件名 | 内容简介 |
|------|--------|----------|
| **第0章** | [00_概述与语言基础.md](./00_概述与语言基础.md) | UE-Angelscript 简介、语言基础语法、句柄与值类型 |
| **第1章** | [01_插件架构.md](./01_插件架构.md) | 目录结构、模块依赖、核心类关系 |
| **第2章** | [02_初始化流程.md](./02_初始化流程.md) | 引擎启动序列、PreInitialize/Initialize/PostInitialize |
| **第3章** | [03_类型系统.md](./03_类型系统.md) | FAngelscriptType、TypeUsage、TypeDatabase |
| **第4章** | [04_FBind机制.md](./04_FBind机制.md) | FBind 注册系统、绑定顺序（Early/Normal/Late） |
| **第5章** | [05_UObject绑定.md](./05_UObject绑定.md) | UClass 绑定流程、ShouldBindEngineType、成员绑定 |
| **第6章** | [06_UScriptStruct绑定.md](./06_UScriptStruct绑定.md) | 值类型绑定、ValueClass vs ReferenceClass |
| **第7章** | [07_手工绑定.md](./07_手工绑定.md) | 构造函数、属性、方法、运算符绑定详解 |
| **第8章** | [08_泛型模板绑定.md](./08_泛型模板绑定.md) | 模板类型声明、TemplateCallback、GenericMethod |
| **第9章** | [09_内存模型.md](./09_内存模型.md) | UObject/UScriptStruct 内存管理、asOBJ 标志 |
| **第10章** | [10_实战案例.md](./10_实战案例.md) | 自定义结构体绑定、Mixin 扩展、GAS 集成 |
| **第11章** | [11_附录.md](./11_附录.md) | 源码导航、官方文档链接、调试技巧 |

## 🚀 快速开始

如果你是初学者，建议按顺序阅读：
1. 先阅读 **第0章** 了解基本概念
2. 再阅读 **第1-2章** 了解架构和初始化
3. **第4-5章** 是理解绑定机制的核心

如果你需要解决具体问题：
- **GAS 能力不触发** → 直接看 **第10章** 案例3
- **自定义结构体绑定** → 看 **第7章** + **第10章** 案例1
- **理解类型系统** → 看 **第3章**

## 📝 关于版本

- **文档版本**: 1.0
- **适用引擎**: UnrealEngine-Angelscript 5.4.x
- **最后更新**: 2024年12月

---

*此系列文档基于 DJ01 项目中 GAS (Gameplay Ability System) 与 AngelScript 集成的实践经验整理*