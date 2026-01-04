# UE5 Python API 限制与 C++ Bridge 解决方案

> **文档版本**: 1.0  
> **创建日期**: 2024-12-30  
> **相关模块**: DJ01Editor, UIGenerator  
> **关键词**: UE5, Python API, WidgetBlueprint, WidgetTree, C++ Bridge

---

## 目录

1. [问题背景](#问题背景)
2. [问题分析](#问题分析)
3. [解决方案探索](#解决方案探索)
4. [最终实现](#最终实现)
5. [使用指南](#使用指南)
6. [经验总结](#经验总结)

---

## 问题背景

### 项目目标

我们希望创建一套**可视化 UI Schema 工具链**，让设计师能够：

1. 通过 JSON Schema 定义 UI 结构
2. 自动生成对应的 C++ Widget 基类（带 `BindWidget` 绑定）
3. 自动生成 Widget Blueprint 资产，并创建好控件层级

### 遇到的问题

在实现第 3 步时，我们使用 Python 脚本在 UE 编辑器内运行，尝试自动创建 Widget Blueprint 中的控件层级。然而遇到了严重障碍：

```python
# 尝试获取 WidgetTree
widget_bp = unreal.EditorAssetLibrary.load_asset("/Game/UI/WBP_Test")
widget_tree = widget_bp.get_editor_property("widget_tree")  # ❌ 失败！
```

**错误信息**：
```
LogPython: Error: WidgetBlueprint: Failed to find property 'widget_tree'
```

---

## 问题分析

### 1. 为什么 Python 无法访问 `widget_tree`？

通过测试脚本验证，我们发现：

| 属性/方法 | Python 可访问 | 原因 |
|-----------|--------------|------|
| `UWidgetBlueprint.widget_tree` | ❌ | 没有 `UPROPERTY` 暴露给反射系统 |
| `UWidgetTree.RootWidget` | ❌ | 同上 |
| `UWidgetTree.ConstructWidget()` | ❌ | 没有 `UFUNCTION` 标记 |
| `UCanvasPanel.AddChild()` | ✅ | 有正确的 UMG 暴露 |

**根本原因**：UE 的 Python API 是基于反射系统的，只有标记了 `UPROPERTY(BlueprintReadWrite)` 或 `UFUNCTION(BlueprintCallable)` 的成员才会暴露给 Python。

而 `UWidgetBlueprint::WidgetTree` 在引擎源码中的定义是：

```cpp
// Engine/Source/Editor/UMGEditor/Public/WidgetBlueprint.h
UPROPERTY()  // 注意：没有 BlueprintReadWrite！
TObjectPtr<UWidgetTree> WidgetTree;
```

### 2. 这是 Epic 的设计决策

`WidgetTree` 是**编辑器专用**的数据结构，Epic 有意不将其暴露给蓝图/脚本，原因可能包括：

- 防止运行时误操作编辑器资产
- WidgetTree 的操作需要配合编辑器事务系统
- 复杂的生命周期管理

### 3. AngelScript 也无法解决

我们检查了 AngelScript API 数据库（`Tools/AngelscriptAPIQuery`），发现：

```json
// UWidgetTree.json
{
  "name": "UWidgetTree",
  "properties": {},  // 空！没有暴露属性
  "methods": []      // 空！没有暴露方法
}
```

AngelScript 同样依赖反射系统，所以也无法访问这些内部 API。

---

## 解决方案探索

### 方案 1：纯 Python（失败）

```python
# 尝试各种方式访问 WidgetTree
widget_bp.get_editor_property("widget_tree")  # ❌
widget_bp.widget_tree  # ❌
getattr(widget_bp, "widget_tree")  # ❌
```

**结论**：不可行，Python 反射层无法访问未暴露的属性。

### 方案 2：使用 `create_widgets_from_json` 蓝图节点（不适用）

UE 有一些 Widget 运行时创建 API，但它们是用于**运行时**创建实例，而不是**编辑器**中修改资产。

**结论**：不适用于我们的场景。

### 方案 3：C++ Editor Module + Python Bridge（✅ 最终方案）

创建一个 C++ Editor 模块，暴露一个 `UBlueprintFunctionLibrary`，将 WidgetTree 操作封装为 `UFUNCTION(BlueprintCallable)` 函数，从而让 Python 可以调用。

```
┌─────────────┐     ┌─────────────────────────┐     ┌────────────────┐
│   Python    │────>│ DJ01WidgetBlueprintLib  │────>│  UWidgetTree   │
│   Script    │     │    (C++ Bridge)         │     │  (Internal)    │
└─────────────┘     └─────────────────────────┘     └────────────────┘
     反射调用              直接 C++ 访问
```

**结论**：可行！这是最干净的解决方案。

---

## 最终实现

### 1. 创建 Editor Module

**文件结构**：
```
Source/DJ01Editor/
├── DJ01Editor.Build.cs
├── Public/
│   ├── DJ01EditorModule.h
│   └── DJ01WidgetBlueprintLibrary.h
└── Private/
    ├── DJ01EditorModule.cpp
    └── DJ01WidgetBlueprintLibrary.cpp
```

### 2. Build.cs 配置

```csharp
// DJ01Editor.Build.cs
public class DJ01Editor : ModuleRules
{
    public DJ01Editor(ReadOnlyTargetRules Target) : base(Target)
    {
        PCHUsage = PCHUsageMode.UseExplicitOrSharedPCHs;
        
        PublicDependencyModuleNames.AddRange(new string[] { 
            "Core", "CoreUObject", "Engine", "DJ01"
        });

        PrivateDependencyModuleNames.AddRange(new string[] { 
            "Slate", "SlateCore",
            "UnrealEd",    // 编辑器核心
            "UMG",         // Widget 运行时
            "UMGEditor",   // Widget 编辑器（UWidgetBlueprint, UWidgetTree）
            "Blutility",
            "BlueprintGraph",
            "Json", "JsonUtilities"
        });
    }
}
```

### 3. C++ Bridge 实现

```cpp
// DJ01WidgetBlueprintLibrary.h
UCLASS()
class DJ01EDITOR_API UDJ01WidgetBlueprintLibrary : public UBlueprintFunctionLibrary
{
    GENERATED_BODY()
    
public:
    // ===== 基础操作 =====
    UFUNCTION(BlueprintCallable, Category = "DJ01|WidgetBlueprint")
    static UWidgetTree* GetWidgetTree(UWidgetBlueprint* WidgetBlueprint);
    
    UFUNCTION(BlueprintCallable, Category = "DJ01|WidgetBlueprint")
    static UWidget* GetRootWidget(UWidgetBlueprint* WidgetBlueprint);
    
    UFUNCTION(BlueprintCallable, Category = "DJ01|WidgetBlueprint")
    static bool SetRootWidget(UWidgetBlueprint* WidgetBlueprint, UWidget* RootWidget);
    
    // ===== 控件创建 =====
    UFUNCTION(BlueprintCallable, Category = "DJ01|WidgetBlueprint")
    static UWidget* CreateWidget(UWidgetBlueprint* WidgetBlueprint, 
                                  TSubclassOf<UWidget> WidgetClass, FName WidgetName);
    
    UFUNCTION(BlueprintCallable, Category = "DJ01|WidgetBlueprint")
    static UWidget* CreateCanvasPanel(UWidgetBlueprint* WidgetBlueprint, FName WidgetName);
    
    UFUNCTION(BlueprintCallable, Category = "DJ01|WidgetBlueprint")
    static UWidget* CreateProgressBar(UWidgetBlueprint* WidgetBlueprint, FName WidgetName);
    
    UFUNCTION(BlueprintCallable, Category = "DJ01|WidgetBlueprint")
    static UWidget* CreateTextBlock(UWidgetBlueprint* WidgetBlueprint, FName WidgetName);
    
    // ===== 层级操作 =====
    UFUNCTION(BlueprintCallable, Category = "DJ01|WidgetBlueprint")
    static bool AddChildToPanel(UWidget* Parent, UWidget* Child);
    
    UFUNCTION(BlueprintCallable, Category = "DJ01|WidgetBlueprint")
    static bool AddChildToCanvas(UWidget* CanvasPanel, UWidget* Child, 
                                  FVector2D Position, FVector2D Size);
    
    // ===== 保存操作 =====
    UFUNCTION(BlueprintCallable, Category = "DJ01|WidgetBlueprint")
    static bool SaveWidgetBlueprint(UWidgetBlueprint* WidgetBlueprint);
    
    // ===== 批量操作 =====
    UFUNCTION(BlueprintCallable, Category = "DJ01|WidgetBlueprint")
    static bool CreateWidgetsFromJson(UWidgetBlueprint* WidgetBlueprint, 
                                       const FString& SchemaJson);
};
```

### 4. 关键实现细节

```cpp
// 获取 WidgetTree（Python 原本无法访问）
UWidgetTree* UDJ01WidgetBlueprintLibrary::GetWidgetTree(UWidgetBlueprint* WidgetBlueprint)
{
    if (!WidgetBlueprint) return nullptr;
    return WidgetBlueprint->WidgetTree;  // C++ 可以直接访问！
}

// 创建控件到 WidgetTree
UWidget* UDJ01WidgetBlueprintLibrary::CreateWidget(
    UWidgetBlueprint* WidgetBlueprint, 
    TSubclassOf<UWidget> WidgetClass, 
    FName WidgetName)
{
    if (!WidgetBlueprint || !WidgetBlueprint->WidgetTree || !WidgetClass)
        return nullptr;
    
    WidgetBlueprint->Modify();  // 标记为脏，支持撤销
    
    // 使用 WidgetTree 的模板方法创建
    return WidgetBlueprint->WidgetTree->ConstructWidget<UWidget>(WidgetClass, WidgetName);
}

// 添加子控件到 Canvas 并设置布局
bool UDJ01WidgetBlueprintLibrary::AddChildToCanvas(
    UWidget* CanvasPanelWidget, 
    UWidget* Child, 
    FVector2D Position, 
    FVector2D Size)
{
    UCanvasPanel* CanvasPanel = Cast<UCanvasPanel>(CanvasPanelWidget);
    if (!CanvasPanel || !Child) return false;
    
    UCanvasPanelSlot* Slot = Cast<UCanvasPanelSlot>(CanvasPanel->AddChild(Child));
    if (Slot)
    {
        Slot->SetPosition(Position);
        Slot->SetSize(Size);
        Slot->SetAnchors(FAnchors(0.0f, 0.0f, 0.0f, 0.0f));  // 左上角锚点
        return true;
    }
    return false;
}
```

### 5. Python 调用示例

```python
import unreal

# 获取 C++ Bridge
lib = unreal.DJ01WidgetBlueprintLibrary

# 加载 Widget Blueprint
wb = unreal.EditorAssetLibrary.load_asset('/Game/UI/WBP_Test')

# 现在可以操作 WidgetTree 了！
widget_tree = lib.get_widget_tree(wb)  # ✅ 成功！

# 创建控件
canvas = lib.create_canvas_panel(wb, "RootCanvas")
progress = lib.create_progress_bar(wb, "HealthBar")
text = lib.create_text_block(wb, "HealthText")

# 设置层级
lib.set_root_widget(wb, canvas)
lib.add_child_to_canvas(canvas, progress, unreal.Vector2D(50, 50), unreal.Vector2D(200, 30))
lib.add_child_to_canvas(canvas, text, unreal.Vector2D(50, 100), unreal.Vector2D(150, 25))

# 保存
lib.save_widget_blueprint(wb)
```

---

## 使用指南

### 前置条件

1. `DJ01Editor` 模块已编译
2. 在 `.uproject` 中正确配置了模块

### 测试 Bridge 是否可用

在 UE 编辑器 Python 控制台运行：

```python
py "D:/UnrealProjects/DJ01/Tools/UIGenerator/ue_scripts/test_widget_bridge.py"
```

### 生成 Widget Blueprint

```python
py "D:/UnrealProjects/DJ01/Tools/UIGenerator/ue_scripts/generate_widget_bp.py"
```

或指定 Schema：

```python
from generate_widget_bp import generate_from_schema
generate_from_schema("D:/UnrealProjects/DJ01/Tools/UIGenerator/schemas/widgets/HealthBar.json")
```

---

## 经验总结

### 技术收获

1. **理解 UE 反射系统的边界**
   - Python/蓝图只能访问显式暴露的 API
   - 编辑器内部 API 通常不暴露，需要 C++ 桥接

2. **C++ Bridge 模式**
   - 当脚本语言无法访问某些 API 时，创建 `UBlueprintFunctionLibrary` 作为桥梁
   - 这是 UE 开发中的常见模式

3. **Editor Module vs Runtime Module**
   - Editor 模块只在编辑器中加载
   - 可以安全地依赖 `UnrealEd`、`UMGEditor` 等编辑器模块

4. **WidgetTree 的正确操作方式**
   - 使用 `WidgetBlueprint->Modify()` 支持撤销
   - 使用 `WidgetTree->ConstructWidget<T>()` 创建控件
   - 手动管理父子关系和 Slot

### 方法论收获

1. **问题定位**
   - 先写测试脚本验证假设
   - 检查引擎源码确认 API 暴露情况
   - 查阅 AngelScript API 数据库对比

2. **方案评估**
   - 先列出所有可能方案
   - 评估每个方案的可行性和复杂度
   - 选择最干净、可维护的方案

3. **文档化**
   - 记录问题、分析、解决过程
   - 为团队成员提供参考
   - 避免重复踩坑

### 可复用的模式

这个 C++ Bridge 模式可以应用于其他场景：

- 访问 `UBlueprint` 内部结构
- 操作 `UDataTable` 编辑器功能
- 自动化 `UMaterial` 节点图
- 任何 Python API 无法访问的编辑器功能

---

## C++ Bridge 搭建详解

### 第一步：创建 Editor Module

#### 1.1 创建目录结构

```
Source/
├── DJ01/                    # 主模块（已存在）
└── DJ01Editor/              # 新建 Editor 模块
    ├── DJ01Editor.Build.cs
    ├── Public/
    │   ├── DJ01EditorModule.h
    │   └── DJ01WidgetBlueprintLibrary.h
    └── Private/
        ├── DJ01EditorModule.cpp
        └── DJ01WidgetBlueprintLibrary.cpp
```

#### 1.2 配置 .uproject 文件

在 `DJ01.uproject` 的 `Modules` 数组中添加 Editor 模块：

```json
{
    "Modules": [
        {
            "Name": "DJ01",
            "Type": "Runtime",
            "LoadingPhase": "Default"
        },
        {
            "Name": "DJ01Editor",
            "Type": "Editor",
            "LoadingPhase": "Default"
        }
    ]
}
```

> **注意**: `Type: "Editor"` 表示此模块仅在编辑器中加载，打包后不包含。

#### 1.3 创建 Build.cs

```csharp
// DJ01Editor.Build.cs
using UnrealBuildTool;

public class DJ01Editor : ModuleRules
{
    public DJ01Editor(ReadOnlyTargetRules Target) : base(Target)
    {
        PCHUsage = PCHUsageMode.UseExplicitOrSharedPCHs;
        
        // 公共依赖
        PublicDependencyModuleNames.AddRange(new string[] { 
            "Core", 
            "CoreUObject", 
            "Engine",
            "DJ01"  // 依赖主模块
        });

        // 私有依赖（编辑器专用模块）
        PrivateDependencyModuleNames.AddRange(new string[] { 
            "Slate",
            "SlateCore",
            "UnrealEd",        // 编辑器核心 API
            "UMG",             // Widget 运行时（UWidget, UCanvasPanel 等）
            "UMGEditor",       // Widget 编辑器（UWidgetBlueprint, UWidgetTree）
            "Blutility",       // Editor Utility
            "BlueprintGraph",  // 蓝图图表
            "Json",            // JSON 解析
            "JsonUtilities"
        });
    }
}
```

#### 1.4 创建模块入口

```cpp
// Public/DJ01EditorModule.h
#pragma once

#include "CoreMinimal.h"
#include "Modules/ModuleManager.h"

class FDJ01EditorModule : public IModuleInterface
{
public:
    virtual void StartupModule() override;
    virtual void ShutdownModule() override;
};
```

```cpp
// Private/DJ01EditorModule.cpp
#include "DJ01EditorModule.h"

#define LOCTEXT_NAMESPACE "FDJ01EditorModule"

void FDJ01EditorModule::StartupModule()
{
    UE_LOG(LogTemp, Log, TEXT("DJ01Editor Module Started"));
}

void FDJ01EditorModule::ShutdownModule()
{
}

#undef LOCTEXT_NAMESPACE

IMPLEMENT_MODULE(FDJ01EditorModule, DJ01Editor)
```

### 第二步：创建 Blueprint Function Library

#### 2.1 头文件定义

```cpp
// Public/DJ01WidgetBlueprintLibrary.h
#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "DJ01WidgetBlueprintLibrary.generated.h"

class UWidgetBlueprint;
class UWidgetTree;
class UWidget;

UCLASS()
class DJ01EDITOR_API UDJ01WidgetBlueprintLibrary : public UBlueprintFunctionLibrary
{
    GENERATED_BODY()
    
public:
    // ==================== 基础操作 ====================
    
    /** 获取 WidgetBlueprint 的 WidgetTree（Python 原本无法访问） */
    UFUNCTION(BlueprintCallable, Category = "DJ01|WidgetBlueprint")
    static UWidgetTree* GetWidgetTree(UWidgetBlueprint* WidgetBlueprint);
    
    /** 获取根控件 */
    UFUNCTION(BlueprintCallable, Category = "DJ01|WidgetBlueprint")
    static UWidget* GetRootWidget(UWidgetBlueprint* WidgetBlueprint);
    
    /** 设置根控件 */
    UFUNCTION(BlueprintCallable, Category = "DJ01|WidgetBlueprint")
    static bool SetRootWidget(UWidgetBlueprint* WidgetBlueprint, UWidget* RootWidget);
    
    // ==================== 控件创建 ====================
    
    /** 创建任意类型的控件 */
    UFUNCTION(BlueprintCallable, Category = "DJ01|WidgetBlueprint")
    static UWidget* CreateWidget(UWidgetBlueprint* WidgetBlueprint, 
                                  TSubclassOf<UWidget> WidgetClass, 
                                  FName WidgetName);
    
    /** 创建 CanvasPanel */
    UFUNCTION(BlueprintCallable, Category = "DJ01|WidgetBlueprint")
    static UWidget* CreateCanvasPanel(UWidgetBlueprint* WidgetBlueprint, FName WidgetName);
    
    /** 创建 ProgressBar */
    UFUNCTION(BlueprintCallable, Category = "DJ01|WidgetBlueprint")
    static UWidget* CreateProgressBar(UWidgetBlueprint* WidgetBlueprint, FName WidgetName);
    
    /** 创建 TextBlock */
    UFUNCTION(BlueprintCallable, Category = "DJ01|WidgetBlueprint")
    static UWidget* CreateTextBlock(UWidgetBlueprint* WidgetBlueprint, FName WidgetName);
    
    /** 创建 Image */
    UFUNCTION(BlueprintCallable, Category = "DJ01|WidgetBlueprint")
    static UWidget* CreateImage(UWidgetBlueprint* WidgetBlueprint, FName WidgetName);
    
    // ==================== 层级操作 ====================
    
    /** 添加子控件到 PanelWidget */
    UFUNCTION(BlueprintCallable, Category = "DJ01|WidgetBlueprint")
    static bool AddChildToPanel(UWidget* Parent, UWidget* Child);
    
    /** 添加子控件到 CanvasPanel（带位置和大小） */
    UFUNCTION(BlueprintCallable, Category = "DJ01|WidgetBlueprint")
    static bool AddChildToCanvas(UWidget* CanvasPanelWidget, UWidget* Child, 
                                  FVector2D Position, FVector2D Size);
    
    // ==================== 查找操作 ====================
    
    /** 按名称查找控件 */
    UFUNCTION(BlueprintCallable, Category = "DJ01|WidgetBlueprint")
    static UWidget* FindWidgetByName(UWidgetBlueprint* WidgetBlueprint, FName WidgetName);
    
    /** 获取所有控件 */
    UFUNCTION(BlueprintCallable, Category = "DJ01|WidgetBlueprint")
    static TArray<UWidget*> GetAllWidgets(UWidgetBlueprint* WidgetBlueprint);
    
    // ==================== 保存操作 ====================
    
    /** 标记为脏（需要保存） */
    UFUNCTION(BlueprintCallable, Category = "DJ01|WidgetBlueprint")
    static void MarkDirty(UWidgetBlueprint* WidgetBlueprint);
    
    /** 保存 WidgetBlueprint 到磁盘 */
    UFUNCTION(BlueprintCallable, Category = "DJ01|WidgetBlueprint")
    static bool SaveWidgetBlueprint(UWidgetBlueprint* WidgetBlueprint);
    
    // ==================== 批量操作 ====================
    
    /** 从 JSON Schema 批量创建控件 */
    UFUNCTION(BlueprintCallable, Category = "DJ01|WidgetBlueprint")
    static bool CreateWidgetsFromJson(UWidgetBlueprint* WidgetBlueprint, 
                                       const FString& SchemaJson);
};
```

#### 2.2 实现文件

```cpp
// Private/DJ01WidgetBlueprintLibrary.cpp
#include "DJ01WidgetBlueprintLibrary.h"
#include "WidgetBlueprint.h"
#include "Blueprint/WidgetTree.h"
#include "Components/Widget.h"
#include "Components/PanelWidget.h"
#include "Components/CanvasPanel.h"
#include "Components/CanvasPanelSlot.h"
#include "Components/ProgressBar.h"
#include "Components/TextBlock.h"
#include "Components/Image.h"
#include "UObject/Package.h"
#include "UObject/SavePackage.h"
#include "Dom/JsonObject.h"
#include "Serialization/JsonReader.h"
#include "Serialization/JsonSerializer.h"

// ==================== 基础操作 ====================

UWidgetTree* UDJ01WidgetBlueprintLibrary::GetWidgetTree(UWidgetBlueprint* WidgetBlueprint)
{
    if (!WidgetBlueprint)
    {
        UE_LOG(LogTemp, Warning, TEXT("GetWidgetTree: WidgetBlueprint is null"));
        return nullptr;
    }
    return WidgetBlueprint->WidgetTree;
}

UWidget* UDJ01WidgetBlueprintLibrary::GetRootWidget(UWidgetBlueprint* WidgetBlueprint)
{
    if (!WidgetBlueprint || !WidgetBlueprint->WidgetTree)
    {
        return nullptr;
    }
    return WidgetBlueprint->WidgetTree->RootWidget;
}

bool UDJ01WidgetBlueprintLibrary::SetRootWidget(UWidgetBlueprint* WidgetBlueprint, UWidget* RootWidget)
{
    if (!WidgetBlueprint || !WidgetBlueprint->WidgetTree)
    {
        return false;
    }
    
    WidgetBlueprint->Modify();  // 支持撤销
    WidgetBlueprint->WidgetTree->RootWidget = RootWidget;
    return true;
}

// ==================== 控件创建 ====================

UWidget* UDJ01WidgetBlueprintLibrary::CreateWidget(
    UWidgetBlueprint* WidgetBlueprint, 
    TSubclassOf<UWidget> WidgetClass, 
    FName WidgetName)
{
    if (!WidgetBlueprint || !WidgetBlueprint->WidgetTree || !WidgetClass)
    {
        return nullptr;
    }
    
    WidgetBlueprint->Modify();
    return WidgetBlueprint->WidgetTree->ConstructWidget<UWidget>(WidgetClass, WidgetName);
}

UWidget* UDJ01WidgetBlueprintLibrary::CreateCanvasPanel(UWidgetBlueprint* WidgetBlueprint, FName WidgetName)
{
    return CreateWidget(WidgetBlueprint, UCanvasPanel::StaticClass(), WidgetName);
}

UWidget* UDJ01WidgetBlueprintLibrary::CreateProgressBar(UWidgetBlueprint* WidgetBlueprint, FName WidgetName)
{
    return CreateWidget(WidgetBlueprint, UProgressBar::StaticClass(), WidgetName);
}

UWidget* UDJ01WidgetBlueprintLibrary::CreateTextBlock(UWidgetBlueprint* WidgetBlueprint, FName WidgetName)
{
    return CreateWidget(WidgetBlueprint, UTextBlock::StaticClass(), WidgetName);
}

UWidget* UDJ01WidgetBlueprintLibrary::CreateImage(UWidgetBlueprint* WidgetBlueprint, FName WidgetName)
{
    return CreateWidget(WidgetBlueprint, UImage::StaticClass(), WidgetName);
}

// ==================== 层级操作 ====================

bool UDJ01WidgetBlueprintLibrary::AddChildToPanel(UWidget* Parent, UWidget* Child)
{
    UPanelWidget* PanelWidget = Cast<UPanelWidget>(Parent);
    if (!PanelWidget || !Child)
    {
        return false;
    }
    
    return PanelWidget->AddChild(Child) != nullptr;
}

bool UDJ01WidgetBlueprintLibrary::AddChildToCanvas(
    UWidget* CanvasPanelWidget, 
    UWidget* Child, 
    FVector2D Position, 
    FVector2D Size)
{
    UCanvasPanel* CanvasPanel = Cast<UCanvasPanel>(CanvasPanelWidget);
    if (!CanvasPanel || !Child)
    {
        return false;
    }
    
    UCanvasPanelSlot* Slot = Cast<UCanvasPanelSlot>(CanvasPanel->AddChild(Child));
    if (Slot)
    {
        Slot->SetPosition(Position);
        Slot->SetSize(Size);
        Slot->SetAnchors(FAnchors(0.0f, 0.0f, 0.0f, 0.0f));  // 左上角锚点
        return true;
    }
    return false;
}

// ==================== 查找操作 ====================

UWidget* UDJ01WidgetBlueprintLibrary::FindWidgetByName(UWidgetBlueprint* WidgetBlueprint, FName WidgetName)
{
    if (!WidgetBlueprint || !WidgetBlueprint->WidgetTree)
    {
        return nullptr;
    }
    return WidgetBlueprint->WidgetTree->FindWidget(WidgetName);
}

TArray<UWidget*> UDJ01WidgetBlueprintLibrary::GetAllWidgets(UWidgetBlueprint* WidgetBlueprint)
{
    TArray<UWidget*> AllWidgets;
    if (WidgetBlueprint && WidgetBlueprint->WidgetTree)
    {
        WidgetBlueprint->WidgetTree->GetAllWidgets(AllWidgets);
    }
    return AllWidgets;
}

// ==================== 保存操作 ====================

void UDJ01WidgetBlueprintLibrary::MarkDirty(UWidgetBlueprint* WidgetBlueprint)
{
    if (WidgetBlueprint)
    {
        WidgetBlueprint->Modify();
    }
}

bool UDJ01WidgetBlueprintLibrary::SaveWidgetBlueprint(UWidgetBlueprint* WidgetBlueprint)
{
    if (!WidgetBlueprint)
    {
        return false;
    }
    
    UPackage* Package = WidgetBlueprint->GetOutermost();
    if (!Package)
    {
        return false;
    }
    
    Package->MarkPackageDirty();
    
    FString PackageFileName = FPackageName::LongPackageNameToFilename(
        Package->GetName(), 
        FPackageName::GetAssetPackageExtension()
    );
    
    return UPackage::SavePackage(
        Package, 
        WidgetBlueprint, 
        RF_Standalone,
        *PackageFileName,
        GError,
        nullptr,
        false,
        true,
        SAVE_None
    );
}

// ==================== 批量操作 ====================

bool UDJ01WidgetBlueprintLibrary::CreateWidgetsFromJson(
    UWidgetBlueprint* WidgetBlueprint, 
    const FString& SchemaJson)
{
    // 解析 JSON 并递归创建控件...
    // （完整实现见源码）
}
```

### 第三步：重新生成项目并编译

```bash
# 1. 重新生成 VS 项目文件
右键 .uproject -> Generate Visual Studio project files

# 2. 打开 VS 编译
# 或者直接启动 UE 编辑器，会自动编译
```

---

## API 参考

### Python 调用方式

```python
import unreal

# 获取 Bridge
lib = unreal.DJ01WidgetBlueprintLibrary
```

### 完整 API 列表

| 函数 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `get_widget_tree(wb)` | `WidgetBlueprint` | `WidgetTree` | 获取 WidgetTree（核心功能） |
| `get_root_widget(wb)` | `WidgetBlueprint` | `Widget` | 获取根控件 |
| `set_root_widget(wb, widget)` | `WidgetBlueprint`, `Widget` | `bool` | 设置根控件 |
| `create_widget(wb, class, name)` | `WidgetBlueprint`, `Class`, `FName` | `Widget` | 创建任意类型控件 |
| `create_canvas_panel(wb, name)` | `WidgetBlueprint`, `FName` | `CanvasPanel` | 创建画布面板 |
| `create_progress_bar(wb, name)` | `WidgetBlueprint`, `FName` | `ProgressBar` | 创建进度条 |
| `create_text_block(wb, name)` | `WidgetBlueprint`, `FName` | `TextBlock` | 创建文本块 |
| `create_image(wb, name)` | `WidgetBlueprint`, `FName` | `Image` | 创建图片 |
| `add_child_to_panel(parent, child)` | `Widget`, `Widget` | `bool` | 添加子控件到面板 |
| `add_child_to_canvas(canvas, child, pos, size)` | `CanvasPanel`, `Widget`, `Vector2D`, `Vector2D` | `bool` | 添加到画布（带布局） |
| `find_widget_by_name(wb, name)` | `WidgetBlueprint`, `FName` | `Widget` | 按名称查找控件 |
| `get_all_widgets(wb)` | `WidgetBlueprint` | `Array<Widget>` | 获取所有控件 |
| `mark_dirty(wb)` | `WidgetBlueprint` | `void` | 标记需要保存 |
| `save_widget_blueprint(wb)` | `WidgetBlueprint` | `bool` | 保存到磁盘 |
| `create_widgets_from_json(wb, json)` | `WidgetBlueprint`, `String` | `bool` | 从 JSON 批量创建 |

### 使用示例

#### 示例 1：创建简单控件层级

```python
import unreal

lib = unreal.DJ01WidgetBlueprintLibrary
wb = unreal.EditorAssetLibrary.load_asset('/Game/UI/WBP_Test')

# 创建层级: Canvas -> ProgressBar + TextBlock
canvas = lib.create_canvas_panel(wb, "RootCanvas")
health_bar = lib.create_progress_bar(wb, "HealthBar")
health_text = lib.create_text_block(wb, "HealthText")

# 设置根控件
lib.set_root_widget(wb, canvas)

# 添加子控件（带位置和大小）
lib.add_child_to_canvas(canvas, health_bar, 
    unreal.Vector2D(50, 50),    # Position
    unreal.Vector2D(200, 30))   # Size

lib.add_child_to_canvas(canvas, health_text,
    unreal.Vector2D(50, 90),
    unreal.Vector2D(100, 25))

# 保存
lib.save_widget_blueprint(wb)
```

#### 示例 2：从 JSON Schema 批量创建

```python
import unreal
import json

lib = unreal.DJ01WidgetBlueprintLibrary
wb = unreal.EditorAssetLibrary.load_asset('/Game/UI/WBP_HUD')

schema = {
    "components": [
        {
            "name": "RootCanvas",
            "type": "CanvasPanel",
            "children": [
                {"name": "HealthBar", "type": "ProgressBar"},
                {"name": "HealthText", "type": "TextBlock"},
                {"name": "ManaBar", "type": "ProgressBar"},
                {"name": "ManaText", "type": "TextBlock"},
                {"name": "Portrait", "type": "Image"}
            ]
        }
    ]
}

lib.create_widgets_from_json(wb, json.dumps(schema))
lib.save_widget_blueprint(wb)
```

#### 示例 3：查询现有控件

```python
import unreal

lib = unreal.DJ01WidgetBlueprintLibrary
wb = unreal.EditorAssetLibrary.load_asset('/Game/UI/WBP_Test')

# 获取所有控件
all_widgets = lib.get_all_widgets(wb)
for w in all_widgets:
    print(f"  - {w.get_name()} ({type(w).__name__})")

# 按名称查找
health_bar = lib.find_widget_by_name(wb, "HealthBar")
if health_bar:
    print(f"Found: {health_bar}")
```

---

## 相关文件

| 文件 | 说明 |
|------|------|
| `Source/DJ01Editor/` | C++ Bridge 模块 |
| `Tools/UIGenerator/ue_scripts/generate_widget_bp.py` | 更新后的生成脚本 |
| `Tools/UIGenerator/ue_scripts/test_widget_bridge.py` | Bridge 测试脚本 |
| `Tools/UIGenerator/ue_scripts/test_widget_creation.py` | 原始问题发现脚本 |

---

## 参考资料

- [UE5 Python API Documentation](https://docs.unrealengine.com/5.0/en-US/PythonAPI/)
- [Unreal Engine Source: WidgetBlueprint.h](https://github.com/EpicGames/UnrealEngine)
- [UBlueprintFunctionLibrary](https://docs.unrealengine.com/5.0/en-US/API/Runtime/Engine/Kismet/UBlueprintFunctionLibrary/)