# Unreal AngelScript API 查询工具

本工具用于从运行中的 Unreal Engine 项目中查询 AngelScript API 信息。当你在编写 AngelScript 代码时遇到问题（如不确定某个类有哪些方法、属性的类型是什么等），可以使用此工具快速获取准确的 API 信息。

## 前提条件

1. **Unreal Engine 项目必须正在运行**（编辑器模式即可）
2. **项目必须启用了 AngelScript 插件**
3. 工具通过 TCP 端口 `27099` 与 Unreal Engine 通信

## 快速开始

### 基本用法

```bash
# 进入工具目录
cd d:\UnrealProjects\DJ01\Tools\AngelscriptAPIQuery

# 列出所有可用类型
python batch_query.py --list-types

# 按名称筛选类型
python batch_query.py --list-types --filter "Actor"

# 搜索 API（类、方法、属性）
python batch_query.py --search "GetAllActors"

# 查看特定类型的详细信息
python batch_query.py --type "AActor"

# 以 Markdown 格式输出类型文档
python batch_query.py --type "AActor" --format markdown

# 导出整个 API 数据库到 JSON 文件
python batch_query.py --export --output api_database.json
```

## 命令行参数详解

| 参数 | 说明 | 示例 |
|------|------|------|
| `--list-types` | 列出所有可用类型 | `--list-types` |
| `--filter <关键词>` | 配合 `--list-types` 使用，筛选类型名 | `--filter "Component"` |
| `--search <关键词>` | 搜索类名、方法名、属性名 | `--search "SetActorLocation"` |
| `--type <类型名>` | 查看指定类型的完整信息 | `--type "USceneComponent"` |
| `--format <格式>` | 输出格式：`table`（默认）、`json`、`markdown` | `--format markdown` |
| `--export` | 导出整个 API 数据库 | `--export` |
| `--output <文件路径>` | 指定导出文件路径 | `--output my_api.json` |
| `--host <IP>` | Unreal Engine 主机地址（默认 127.0.0.1） | `--host 192.168.1.100` |
| `--port <端口>` | 端口号（默认 27099） | `--port 27099` |

## 常见使用场景

### 场景 1：查找某个类有哪些方法

```bash
# 查看 AActor 的所有方法和属性
python batch_query.py --type "AActor" --format markdown
```

### 场景 2：搜索如何获取某个功能

```bash
# 搜索与 "Overlap" 相关的 API
python batch_query.py --search "Overlap"

# 搜索与 "Damage" 相关的 API
python batch_query.py --search "Damage"
```

### 场景 3：查找特定组件

```bash
# 列出所有组件类型
python batch_query.py --list-types --filter "Component"

# 查看特定组件的详情
python batch_query.py --type "UCharacterMovementComponent"
```

### 场景 4：查找命名空间下的函数

AngelScript 的全局函数和静态方法通常以 `__` 前缀命名：

```bash
# 搜索 Gameplay 命名空间的函数
python batch_query.py --search "__Gameplay"

# 搜索数学相关函数
python batch_query.py --search "__Math"
```

### 场景 5：导出完整 API 供离线查阅

```bash
# 导出到 JSON 文件
python batch_query.py --export --output angelscript_api.json
```

## 输出格式示例

### 搜索结果（默认 table 格式）

```
找到 3 个结果:

[方法] void AActor.SetActorLocation(FVector NewLocation)
        Move the Actor to the specified location...
[方法] bool AActor.SetActorLocation(FVector NewLocation, bool bSweep, ...)
        Move the Actor to the specified location...
[属性] FVector AActor.ActorLocation
```

### 类型详情（Markdown 格式）

```markdown
# USceneComponent

**继承自**: `UActorComponent`

A SceneComponent has a transform and supports attachment...

## 属性

### RelativeLocation
- **类型**: `FVector`
- **描述**: Location of the component relative to its parent

## 方法

### GetWorldLocation
\`\`\`angelscript
FVector GetWorldLocation()
\`\`\`
Return location of the component, in world space.
```

## 故障排除

### 错误：无法连接到 Unreal Engine

**原因**：Unreal Engine 编辑器未运行，或 AngelScript 插件未启用。

**解决方案**：
1. 确保 Unreal Engine 编辑器已打开项目
2. 确认 AngelScript 插件已启用
3. 检查端口 27099 是否被防火墙阻止

### 错误：找到 0 个类型

**原因**：连接成功但数据解析失败。

**解决方案**：
1. 确保 Unreal Engine 项目正在运行
2. 尝试重启 Unreal Engine 编辑器

### 搜索无结果

**提示**：
1. 尝试使用更短的关键词
2. 类名通常以 `A`（Actor）、`U`（UObject）、`F`（结构体）开头
3. 全局函数以 `__` 开头

## 技术细节

- **通信协议**：TCP，端口 27099
- **数据格式**：JSON（从 Unreal Engine 运行时获取）
- **数据来源**：AngelScript VSCode 插件使用的相同接口

## 文件结构

```
Tools/AngelscriptAPIQuery/
├── README.md          # 本文档
├── api_query.py       # 核心 API 查询库
└── batch_query.py     # 命令行工具
```

## 供 LLM/AI 助手使用的指南

当用户在 AngelScript 代码中遇到问题时，AI 助手可以按以下流程使用此工具：

1. **识别问题类型**：用户是在询问某个类的用法、查找某个功能、还是调试代码错误？

2. **选择合适的查询方式**：
   - 如果用户问"AActor 有哪些方法"：使用 `--type "AActor"`
   - 如果用户问"怎么获取所有 Actor"：使用 `--search "GetAllActor"`
   - 如果用户问"有哪些组件类型"：使用 `--list-types --filter "Component"`

3. **执行查询命令**：
   ```bash
   cd d:\UnrealProjects\DJ01\Tools\AngelscriptAPIQuery && python batch_query.py <参数>
   ```

4. **分析输出结果**：根据查询结果为用户提供准确的 API 使用建议。

### 常用查询命令模板

```bash
# 查看类的完整文档
cd d:\UnrealProjects\DJ01\Tools\AngelscriptAPIQuery && python batch_query.py --type "<类名>" --format markdown

# 搜索功能
cd d:\UnrealProjects\DJ01\Tools\AngelscriptAPIQuery && python batch_query.py --search "<关键词>"

# 列出类型
cd d:\UnrealProjects\DJ01\Tools\AngelscriptAPIQuery && python batch_query.py --list-types --filter "<关键词>"
```

### 注意事项

- 必须在 Unreal Engine 编辑器运行时才能查询
- 类名区分大小写，建议使用精确名称
- 搜索关键词不区分大小写
