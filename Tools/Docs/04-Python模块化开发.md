# 04 - Python 模块化开发

## 🎯 核心概念

Python 的模块化系统是组织大型项目的基础。理解它能帮助你更好地阅读和维护 AI 生成的代码。

---

## 📐 基本概念

### 模块 (Module)
一个 `.py` 文件就是一个模块。

```python
# utils.py - 这是一个模块
def helper():
    pass
```

### 包 (Package)
包含 `__init__.py` 的目录就是一个包。

```
my_package/
├── __init__.py      # 使目录成为包
├── module_a.py
└── module_b.py
```

---

## 🔑 项目中的模块结构

### DataAssetManager 的包结构

```
DataAssetManager/
├── main.py              # 入口模块
├── config.py            # 配置模块
│
├── core/                # core 包
│   ├── __init__.py     # 包初始化，导出公开接口
│   ├── data_manager.py
│   ├── options_scanner.py
│   └── schema_loader.py
│
├── ui/                  # ui 包
│   ├── __init__.py
│   ├── editors/         # 子包
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── experience.py
│   └── widgets/         # 子包
│       ├── __init__.py
│       ├── factory.py
│       └── text.py
│
└── configs/             # 纯数据目录（非包）
    └── schema/
```

---

## 📦 `__init__.py` 的作用

### 1. 标识包

```python
# core/__init__.py
# 空文件也可以，只是标识这是一个包
```

### 2. 控制导出

```python
# core/__init__.py
from .data_manager import DataManager
from .options_scanner import OptionsScanner

__all__ = ['DataManager', 'OptionsScanner']
```

使用时：
```python
from core import DataManager  # 简洁的导入
```

### 3. 包级别初始化

```python
# core/__init__.py
print("Core 包被加载")  # 首次导入时执行

# 可以做包级别的配置
_default_config = {...}
```

---

## 🔄 导入方式

### 绝对导入

```python
# 从项目根目录开始
from core.data_manager import DataManager
from ui.widgets.factory import WidgetFactory
```

### 相对导入

```python
# 在 ui/editors/experience.py 中
from .base import BaseEditor          # 同级目录
from ..widgets.factory import WidgetFactory  # 上级的同级目录
```

### 项目中的实际例子

```python
# ui/widgets/factory.py

# 相对导入：同包内的模块
from ui.widgets.base import PropertyWidget
from ui.widgets.text import TextInputWidget

# 绝对导入：其他包的模块
from core.schema import PropertyDef
from core.options_scanner import OptionsScanner
```

---

## ⚠️ 常见问题

### 问题1：ModuleNotFoundError

```python
# 错误
from core.data_manager import DataManager
# ModuleNotFoundError: No module named 'core'
```

**原因**：Python 找不到 `core` 包

**解决**：确保项目根目录在 `sys.path` 中

```python
import os
import sys

# 添加项目根目录到 Python 路径
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# 现在可以导入了
from core.data_manager import DataManager
```

### 问题2：循环导入

```python
# module_a.py
from module_b import func_b

# module_b.py
from module_a import func_a  # 循环导入！
```

**解决方法**：

1. **延迟导入**
   ```python
   def my_function():
       from module_b import func_b  # 函数内导入
       func_b()
   ```

2. **重构**：把共享代码提取到第三个模块

### 问题3：相对导入失败

```python
# 直接运行子模块时
python ui/editors/experience.py
# ImportError: attempted relative import with no known parent package
```

**原因**：直接运行模块时，Python 不知道包结构

**解决**：
```bash
# 从项目根目录运行
python -m ui.editors.experience
```

或使用绝对导入 + 路径修复。

---

## 💡 最佳实践

### 1. 入口文件的路径处理

```python
# main.py
import os
import sys

# 确保能找到同级的包
_current_dir = os.path.dirname(os.path.abspath(__file__))
if _current_dir not in sys.path:
    sys.path.insert(0, _current_dir)

# 现在可以安全导入
from core import DataManager
from ui import MainWindow
```

### 2. 子模块的路径处理

```python
# ui/widgets/factory.py
import os
import sys

# 获取工具根目录（向上两级）
_tool_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _tool_dir not in sys.path:
    sys.path.insert(0, _tool_dir)
```

### 3. `__init__.py` 的推荐写法

```python
# core/__init__.py
"""
Core 模块 - 业务逻辑层

提供数据管理、项目扫描等核心功能。
"""

from .data_manager import DataManager
from .options_scanner import OptionsScanner
from .schema_loader import SchemaLoader

__all__ = [
    'DataManager',
    'OptionsScanner', 
    'SchemaLoader',
]
```

---

## 📊 导入顺序规范 (PEP 8)

```python
# 1. 标准库
import os
import sys
import json
from typing import List, Dict

# 2. 第三方库
import tkinter as tk
from tkinter import ttk

# 3. 本项目模块
from core.data_manager import DataManager
from ui.widgets import WidgetFactory
```

每组之间空一行，每组内按字母排序。

---

## 🧪 练习

**问题**：以下目录结构，在 `editor.py` 中如何导入 `helper.py` 的函数？

```
project/
├── main.py
├── utils/
│   ├── __init__.py
│   └── helper.py      # 包含 format_name()
└── ui/
    ├── __init__.py
    └── editor.py      # 需要使用 format_name()
```

**答案**：

```python
# ui/editor.py

# 方法1：绝对导入
from utils.helper import format_name

# 方法2：如果 utils/__init__.py 导出了
from utils import format_name
```