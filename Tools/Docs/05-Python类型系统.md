# 05 - Python 类型系统

## 🎯 为什么需要类型提示？

Python 是动态类型语言，变量不需要声明类型。但在大型项目中，类型提示能：

1. **提高可读性** - 一眼看出函数期望什么参数
2. **IDE 支持** - 自动补全、错误检查
3. **减少 bug** - 静态分析工具可以发现类型错误
4. **便于 AI 理解** - AI 更容易理解代码意图

---

## 📐 基本语法

### 变量类型注解

```python
# 基本类型
name: str = "Experience"
count: int = 10
ratio: float = 0.5
is_enabled: bool = True

# 可以只注解不赋值
result: str  # 声明类型，稍后赋值
```

### 函数类型注解

```python
def greet(name: str) -> str:
    """
    参数 name: 字符串类型
    返回值: 字符串类型
    """
    return f"Hello, {name}"

def process(data: dict) -> None:
    """返回 None"""
    print(data)
```

---

## 🔑 typing 模块

### 常用类型

```python
from typing import List, Dict, Tuple, Set, Optional, Any, Union

# 列表（指定元素类型）
names: List[str] = ["Alice", "Bob"]
numbers: List[int] = [1, 2, 3]

# 字典（指定键和值类型）
config: Dict[str, Any] = {"name": "test", "count": 10}
scores: Dict[str, int] = {"math": 90, "english": 85}

# 元组（固定长度和类型）
point: Tuple[int, int] = (10, 20)
record: Tuple[str, int, bool] = ("name", 100, True)

# 集合
tags: Set[str] = {"tag1", "tag2"}

# 可选（可以是指定类型或 None）
result: Optional[str] = None  # 等同于 Union[str, None]

# 任意类型
data: Any = get_unknown_data()

# 联合类型（多种可能）
value: Union[int, str] = 10  # 可以是 int 或 str
```

### 项目中的实际例子

```python
# core/options_scanner.py
from typing import List, Dict, Optional, Callable, Any

class OptionsScanner:
    def __init__(self, project_root: str = None):
        self.project_root: str = project_root or self._detect_root()
        self.options_data: Dict[str, Any] = {}
    
    def get_options(self, source: str) -> List[Dict[str, str]]:
        """
        获取指定来源的选项列表
        
        Args:
            source: 选项来源标识，如 "pawn_data"
        
        Returns:
            选项列表，每项包含 name, display_name, description
        """
        return self.options_data.get(source, {}).get("items", [])
    
    def scan_directory(
        self, 
        path: str, 
        filter_func: Optional[Callable[[str], bool]] = None
    ) -> List[str]:
        """
        扫描目录，可选过滤函数
        
        Args:
            path: 目录路径
            filter_func: 可选的过滤函数，接收文件名返回是否保留
        """
        ...
```

---

## 🔄 Callable 类型

用于表示函数/回调的类型：

```python
from typing import Callable

# 无参数，返回 None
callback: Callable[[], None]

# 接收两个 str，返回 bool
comparator: Callable[[str, str], bool]

# 项目中的例子
class WidgetFactory:
    def __init__(self):
        # 标签提供器：无参数，返回字符串列表
        self._tag_provider: Callable[[], List[str]] = None
        
        # 变化回调：接收属性名和值，无返回值
        self._on_change: Callable[[str, Any], None] = None
    
    def set_on_change(self, callback: Callable[[str, Any], None]):
        self._on_change = callback
```

---

## 📦 TypedDict（结构化字典）

当字典有固定结构时，使用 TypedDict：

```python
from typing import TypedDict, List

class AssetOption(TypedDict):
    name: str
    display_name: str
    description: str

class ScanConfig(TypedDict):
    blueprint_paths: List[str]
    prefixes: List[str]
    keywords: List[str]

# 使用
def get_options() -> List[AssetOption]:
    return [
        {"name": "/Game/PD_Hero", "display_name": "英雄", "description": "主角数据"}
    ]
```

---

## 🏷️ 类型别名

为复杂类型创建别名，提高可读性：

```python
from typing import Dict, List, Any, Callable

# 定义类型别名
AssetConfig = Dict[str, Any]
OptionsList = List[Dict[str, str]]
ChangeCallback = Callable[[str, Any], None]

# 使用别名
def load_config(path: str) -> AssetConfig:
    ...

def get_all_options() -> OptionsList:
    ...

class Editor:
    def __init__(self, on_change: ChangeCallback = None):
        self.on_change = on_change
```

---

## 🔍 泛型 (Generic)

创建可复用的类型模板：

```python
from typing import TypeVar, Generic, List

T = TypeVar('T')  # 定义类型变量

class Container(Generic[T]):
    def __init__(self):
        self.items: List[T] = []
    
    def add(self, item: T) -> None:
        self.items.append(item)
    
    def get_all(self) -> List[T]:
        return self.items

# 使用
str_container: Container[str] = Container()
str_container.add("hello")  # OK
str_container.add(123)      # 类型检查器会警告

int_container: Container[int] = Container()
int_container.add(42)  # OK
```

---

## ⚠️ 注意事项

### 1. 类型提示是可选的

```python
# 这两种写法都有效
def func1(x: int) -> int:
    return x + 1

def func2(x):  # 无类型提示
    return x + 1
```

### 2. 运行时不检查类型

```python
def greet(name: str) -> str:
    return f"Hello, {name}"

greet(123)  # 运行时不会报错！类型提示只是"提示"
```

需要 mypy 等工具进行静态检查：
```bash
pip install mypy
mypy my_script.py
```

### 3. 前向引用

当类型还未定义时，使用字符串：

```python
class Node:
    def __init__(self, child: "Node" = None):  # 引用自己
        self.child = child

# 或者使用 annotations（Python 3.10+）
from __future__ import annotations

class Node:
    def __init__(self, child: Node = None):  # 直接使用
        self.child = child
```

---

## 💡 最佳实践

### 1. 公开 API 必须有类型提示

```python
# core/schema_loader.py

class SchemaLoader:
    def get_schema(self, asset_type: str) -> Dict[str, Any]:
        """公开方法，必须有类型提示"""
        ...
    
    def _parse_file(self, path):
        """私有方法，类型提示可选"""
        ...
```

### 2. 返回值类型要明确

```python
# ❌ 不明确
def get_data(key):
    return self.data.get(key)  # 可能返回任何类型

# ✓ 明确
def get_data(key: str) -> Optional[Dict[str, Any]]:
    return self.data.get(key)
```

### 3. 使用 Optional 表示可能为 None

```python
# ❌ 隐藏了 None 的可能性
def find_user(id: int) -> User:
    ...

# ✓ 明确表示可能返回 None
def find_user(id: int) -> Optional[User]:
    ...
```

---

## 📊 项目中的类型提示统计

DataAssetManager 中大量使用了类型提示：

```python
# core/options_scanner.py
def _update_options_list(self, key: str, items: List[Dict[str, str]]) -> int:
    ...

# ui/widgets/factory.py
def create(self, parent: tk.Widget, prop: PropertyDef,
           on_change: Callable[[str, Any], None] = None) -> Optional[PropertyWidget]:
    ...

# core/ue_remote.py
def execute_file(self, script_path: str, timeout: float = 30.0) -> Tuple[bool, str]:
    ...
```

这使得代码更易读、更易维护，也更容易被 AI 理解和修改。