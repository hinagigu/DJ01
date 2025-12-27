# 08 - UE Python API 详解

## 🎯 概述

Unreal Engine 提供了 Python API (`unreal` 模块) 用于编辑器脚本开发。本文介绍 DataAssetManager 中用到的核心 API。

---

## 📐 模块结构

```python
import unreal

# 主要功能分类
unreal.Paths          # 路径工具
unreal.EditorAssetLibrary   # 资产操作
unreal.AssetToolsHelpers    # 资产创建
unreal.BlueprintFactory     # 蓝图工厂
unreal.log()          # 日志输出
unreal.register_slate_post_tick_callback()  # Tick 回调
```

---

## 🔑 核心 API 详解

### 1. 路径工具 (Paths)

```python
import unreal

# 获取项目目录 (绝对路径)
project_dir = unreal.Paths.project_dir()
# 返回: "D:/UnrealProjects/DJ01/"

# 获取内容目录
content_dir = unreal.Paths.project_content_dir()
# 返回: "D:/UnrealProjects/DJ01/Content/"

# 转换为游戏内路径
game_path = unreal.Paths.convert_relative_path_to_full("/Game/MyAsset")
```

### 2. 资产库操作 (EditorAssetLibrary)

```python
# 检查资产是否存在
exists = unreal.EditorAssetLibrary.does_asset_exist("/Game/MyFolder/MyAsset")

# 加载资产
asset = unreal.EditorAssetLibrary.load_asset("/Game/MyFolder/MyAsset")

# 保存资产
unreal.EditorAssetLibrary.save_asset("/Game/MyFolder/MyAsset")

# 删除资产
unreal.EditorAssetLibrary.delete_asset("/Game/MyFolder/MyAsset")

# 复制资产
unreal.EditorAssetLibrary.duplicate_asset(
    "/Game/Source/Asset",
    "/Game/Dest/AssetCopy"
)

# 重命名资产
unreal.EditorAssetLibrary.rename_asset(
    "/Game/OldName",
    "/Game/NewName"
)

# 获取资产的类
asset_class = asset.get_class()
class_name = asset_class.get_name()
```

### 3. 创建蓝图资产

```python
# 获取资产工具
asset_tools = unreal.AssetToolsHelpers.get_asset_tools()

# 创建蓝图工厂
factory = unreal.BlueprintFactory()
factory.set_editor_property("parent_class", unreal.DJ01ExperienceDefinition)

# 创建蓝图资产
blueprint = asset_tools.create_asset(
    asset_name="BP_MyExperience",
    package_path="/Game/Experiences",
    asset_class=unreal.Blueprint,
    factory=factory
)
```

### 4. 获取蓝图的生成类 (CDO)

```python
# 方法1：直接获取属性 (UE5)
generated_class = blueprint.get_editor_property("generated_class")

# 方法2：通过 GeneratedClass 属性
generated_class = getattr(blueprint, 'GeneratedClass', None)

# 方法3：作为属性访问
if hasattr(blueprint, 'generated_class'):
    generated_class = blueprint.generated_class

# 获取 CDO (Class Default Object)
cdo = unreal.get_default_object(generated_class)
```

### 5. 设置资产属性

```python
# 设置简单属性
cdo.set_editor_property("PropertyName", value)

# 设置对象引用
pawn_data = unreal.EditorAssetLibrary.load_asset("/Game/PawnData/PD_Hero")
cdo.set_editor_property("DefaultPawnData", pawn_data)

# 设置数组属性
tags = unreal.Array(unreal.GameplayTag)
tags.append(unreal.GameplayTag.request_gameplay_tag("Ability.Jump"))
cdo.set_editor_property("AbilityTags", tags)

# 设置软引用
soft_ref = unreal.SoftObjectPath("/Game/MyAsset.MyAsset")
cdo.set_editor_property("SoftReference", soft_ref)
```

### 6. Gameplay Tags

```python
# 获取已有标签
tag = unreal.GameplayTag.request_gameplay_tag("Character.Hero")

# 检查标签是否有效
if tag.is_valid():
    print(f"标签有效: {tag.get_tag_name()}")

# 创建标签容器
tag_container = unreal.GameplayTagContainer()
tag_container.add_tag(tag)
```

### 7. 日志和通知

```python
# 输出日志 (显示在 Output Log)
unreal.log("普通消息")
unreal.log_warning("警告消息")
unreal.log_error("错误消息")

# 编辑器通知 (右下角弹窗)
unreal.EditorDialog.show_message(
    "标题",
    "消息内容",
    unreal.AppMsgType.OK
)
```

### 8. Tick 回调

```python
def my_tick_function(delta_time):
    """每帧调用"""
    # 你的逻辑
    pass

# 注册回调
handle = unreal.register_slate_post_tick_callback(my_tick_function)

# 取消注册
unreal.unregister_slate_post_tick_callback(handle)
```

---

## 📁 DataAssetManager 中的实际应用

### 创建 Experience 蓝图

```python
# ue_scripts/generate_experience.py

import unreal
import json
import os

def create_experience_blueprint(name, config):
    """创建 Experience 蓝图资产"""
    
    package_path = "/Game/Experiences"
    
    # 检查是否已存在
    full_path = f"{package_path}/{name}"
    if unreal.EditorAssetLibrary.does_asset_exist(full_path):
        unreal.log_warning(f"资产已存在: {full_path}")
        blueprint = unreal.EditorAssetLibrary.load_asset(full_path)
    else:
        # 创建新蓝图
        asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
        factory = unreal.BlueprintFactory()
        factory.set_editor_property("parent_class", unreal.DJ01ExperienceDefinition)
        
        blueprint = asset_tools.create_asset(
            asset_name=name,
            package_path=package_path,
            asset_class=unreal.Blueprint,
            factory=factory
        )
    
    # 获取 CDO
    generated_class = blueprint.get_editor_property("generated_class")
    cdo = unreal.get_default_object(generated_class)
    
    # 设置属性
    if "DefaultPawnData" in config:
        pawn_path = config["DefaultPawnData"]
        pawn_data = unreal.EditorAssetLibrary.load_asset(pawn_path)
        if pawn_data:
            cdo.set_editor_property("DefaultPawnData", pawn_data)
    
    # 保存
    unreal.EditorAssetLibrary.save_asset(full_path)
    unreal.log(f"Experience 创建成功: {full_path}")
    
    return blueprint

# 主执行逻辑
if __name__ == "__main__":
    config_path = os.path.join(os.path.dirname(__file__), "..", "configs", "experiences.json")
    with open(config_path, 'r', encoding='utf-8') as f:
        configs = json.load(f)
    
    for name, config in configs.items():
        create_experience_blueprint(name, config)
```

---

## 📊 常用类型对照表

| Python 类型 | UE 类型 | 说明 |
|-------------|---------|------|
| `str` | `FString` | 字符串 |
| `int` | `int32` | 整数 |
| `float` | `float` | 浮点数 |
| `bool` | `bool` | 布尔值 |
| `unreal.Array(T)` | `TArray<T>` | 数组 |
| `unreal.Map(K, V)` | `TMap<K, V>` | 字典 |
| `unreal.SoftObjectPath` | `TSoftObjectPtr` | 软引用 |
| `unreal.GameplayTag` | `FGameplayTag` | 游戏标签 |

---

## ⚠️ 注意事项

### 1. 属性名称

UE Python 中属性名使用 **snake_case**，而 C++ 中是 **PascalCase**：

```python
# Python
cdo.set_editor_property("default_pawn_data", value)

# 对应 C++
UPROPERTY()
UDJ01PawnData* DefaultPawnData;
```

### 2. 异步操作

某些资产操作需要等待完成：

```python
# 强制等待资产加载完成
asset = unreal.EditorAssetLibrary.load_asset(path)
if asset is None:
    unreal.log_error(f"无法加载: {path}")
```

### 3. 编辑器专用

`unreal` 模块只在**编辑器环境**可用，运行时不可用：

```python
import unreal  # 只在 Editor 中有效，打包后无法使用
```

---

## 📚 更多资源

- [UE Python API 官方文档](https://docs.unrealengine.com/5.0/en-US/PythonAPI/)
- [UE Editor Scripting](https://docs.unrealengine.com/5.0/en-US/scripting-the-unreal-editor-using-python/)