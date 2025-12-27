# UE Python 开发经验总结

## 📋 概述

本文档记录了在开发 DataAssetManager 工具时遇到的 UE Python API 相关坑点和解决方案。

---

## 🔥 常见坑点

### 1. UPROPERTY 访问权限

**问题**: 使用 `EditDefaultsOnly` 标记的属性无法通过 Python 修改

```
Exception: Property 'InputAction' cannot be edited on instances
```

**原因**: `EditDefaultsOnly` 限制属性只能在类默认值中编辑，Python 设置被视为实例编辑。

**解决方案**: 将 C++ 中的 `EditDefaultsOnly` 改为 `EditAnywhere`

```cpp
// 修改前
UPROPERTY(EditDefaultsOnly, BlueprintReadOnly)
TObjectPtr<const UInputAction> InputAction = nullptr;

// 修改后
UPROPERTY(EditAnywhere, BlueprintReadOnly)
TObjectPtr<const UInputAction> InputAction = nullptr;
```

---

### 2. GameplayTag 操作

**问题**: GameplayTag 没有 `tag_name` 属性

```python
# ❌ 错误
tag.tag_name

# ✅ 正确 - 使用 str() 或 import_text()
str(tag)
tag.import_text("InputTag.Move")
```

**设置 GameplayTag 的正确方式**:
```python
def set_struct_gameplay_tag(struct_instance, property_name: str, tag_name: str) -> bool:
    try:
        tag = struct_instance.get_editor_property(property_name)
        tag.import_text(tag_name)  # 使用 import_text 设置值
        struct_instance.set_editor_property(property_name, tag)
        return True
    except Exception as e:
        return False
```

---

### 3. 结构体 (USTRUCT) 的 Python 命名

**规则**: Python 中结构体名称去掉 `F` 前缀

```cpp
// C++
USTRUCT(BlueprintType)
struct FDJ01InputAction { ... };
```

```python
# Python
struct_instance = unreal.DJ01InputAction()  # 注意没有 F 前缀
```

---

### 4. DataAsset 路径约定

**资产路径 vs 类路径**:
- 资产路径: `/Game/Path/To/Asset` (不带后缀)
- 蓝图类路径: `/Game/Path/To/BP_Class.BP_Class_C` (带 `_C` 后缀)

```python
# 加载资产
asset = unreal.load_asset("/Game/Input/Actions/IA_Move")

# 加载蓝图类
bp_class = unreal.load_class(None, "/Game/Characters/BP_Hero.BP_Hero_C")
```

---

### 5. 保存资产

**基本保存**:
```python
unreal.EditorAssetLibrary.save_asset(package_path, only_if_is_dirty=False)
```

**保存所有脏资产**:
```python
unreal.EditorLoadingAndSavingUtils.save_dirty_packages(True, True)
```

**注意**: 某些 API 如 `sync_asset`、`mark_package_dirty` 可能不存在或有版本差异。

---

### 6. UE 日志系统

**日志级别**:
```python
unreal.log("普通信息")           # 可能被过滤
unreal.log_warning("警告信息")   # 更容易看到
unreal.log_error("错误信息")     # 最高优先级
```

**坑点**: Output Log 可能截断或过滤普通日志，调试时建议使用 `log_warning`。

---

### 7. JSON 配置文件 Key 约定

**大小写一致性**: 确保 JSON key 与代码中的查找 key 一致

```json
{
  "inputconfig": {  // 小写
    "InputConfig_Base": { ... }
  }
}
```

```python
# 代码中使用相同的 key
input_data = config.get("inputconfig", {})  # 匹配小写
```

---

## 📁 文件路径处理

### Windows 路径问题

UE 返回的路径可能混合使用 `/` 和 `\`:
```
../../../../../UnrealProjects/DJ01\Tools\DataAssetManager\configs\
```

**建议**: 使用 `os.path.join()` 和 `os.path.normpath()` 规范化路径。

---

## 🔄 远程执行注意事项

### 文件监控模式

1. GUI 工具通过写入 JSON 命令文件与 UE 通信
2. UE 中的监控脚本使用 `exec()` 执行 Python 文件
3. **每次执行都重新读取文件**，修改脚本后无需重启

### 主线程限制

UE 资产操作**必须在主线程执行**:
- 后台线程不能直接调用 `unreal.*` API
- 使用标志变量进行线程间通信

---

## ✅ 最佳实践

1. **修改 C++ 后重新编译** - UPROPERTY 变更需要重启编辑器
2. **使用 log_warning 调试** - 普通 log 可能被过滤
3. **验证数据设置** - 设置属性后立即读取验证
4. **处理异常** - 捕获所有可能的异常并记录详细信息
5. **测试蓝图类加载** - 确保路径带 `_C` 后缀

---

## 📚 参考资源

- [Unreal Engine Python API 文档](https://docs.unrealengine.com/5.0/en-US/PythonAPI/)
- [UE Python 编辑器脚本指南](https://docs.unrealengine.com/5.0/en-US/scripting-the-unreal-editor-using-python/)