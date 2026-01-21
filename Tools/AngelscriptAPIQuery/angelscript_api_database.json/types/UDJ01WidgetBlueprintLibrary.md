# UDJ01WidgetBlueprintLibrary

**继承自**: `UBlueprintFunctionLibrary`

Widget Blueprint 操作库
提供 Python 可调用的函数来操作 Widget Blueprint

使用示例 (Python):
```python
import unreal

# 加载 Widget Blueprint
widget_bp = unreal.EditorAssetLibrary.load_asset("/Game/UI/MyWidget")

# 获取 WidgetTree
tree = unreal.DJ01WidgetBlueprintLibrary.get_widget_tree(widget_bp)

# 添加控件
canvas = unreal.DJ01WidgetBlueprintLibrary.add_widget_to_tree(
    widget_bp, unreal.CanvasPanel, "RootCanvas")

# 设置根控件
unreal.DJ01WidgetBlueprintLibrary.set_root_widget(widget_bp, canvas)
```

