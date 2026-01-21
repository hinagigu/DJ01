# __DJ01Widget

## 方法

### AddChildToCanvas
```angelscript
bool AddChildToCanvas(UWidget CanvasPanel, UWidget Child, FVector2D Position, FVector2D Size)
```
将控件添加到 CanvasPanel
@param CanvasPanel - CanvasPanel 控件
@param Child - 要添加的子控件
@param Position - 位置
@param Size - 大小
@return 是否添加成功

### AddChildToPanel
```angelscript
bool AddChildToPanel(UWidget Parent, UWidget Child)
```
将子控件添加到父控件
@param Parent - 父控件（必须是 PanelWidget）
@param Child - 要添加的子控件
@return 是否添加成功

### CreateCanvasPanel
```angelscript
UWidget CreateCanvasPanel(UWidgetBlueprint WidgetBlueprint, FName WidgetName)
```
创建 CanvasPanel 控件
@param WidgetBlueprint - Widget Blueprint 资产
@param WidgetName - 控件名称
@return 创建的 CanvasPanel

### CreateImage
```angelscript
UWidget CreateImage(UWidgetBlueprint WidgetBlueprint, FName WidgetName)
```
创建 Image 控件
@param WidgetBlueprint - Widget Blueprint 资产
@param WidgetName - 控件名称
@return 创建的 Image

### CreateProgressBar
```angelscript
UWidget CreateProgressBar(UWidgetBlueprint WidgetBlueprint, FName WidgetName)
```
创建 ProgressBar 控件
@param WidgetBlueprint - Widget Blueprint 资产
@param WidgetName - 控件名称
@return 创建的 ProgressBar

### CreateTextBlock
```angelscript
UWidget CreateTextBlock(UWidgetBlueprint WidgetBlueprint, FName WidgetName)
```
创建 TextBlock 控件
@param WidgetBlueprint - Widget Blueprint 资产
@param WidgetName - 控件名称
@return 创建的 TextBlock

### CreateWidget
```angelscript
UWidget CreateWidget(UWidgetBlueprint WidgetBlueprint, TSubclassOf<UWidget> WidgetClass, FName WidgetName)
```
在 WidgetTree 中创建一个新控件
@param WidgetBlueprint - Widget Blueprint 资产
@param WidgetClass - 要创建的控件类型
@param WidgetName - 控件名称（用于 BindWidget）
@return 创建的控件，如果失败返回 nullptr

### CreateWidgetsFromJson
```angelscript
bool CreateWidgetsFromJson(UWidgetBlueprint WidgetBlueprint, FString SchemaJson)
```
根据 Schema JSON 创建控件树
@param WidgetBlueprint - Widget Blueprint 资产
@param SchemaJson - Schema JSON 字符串
@return 是否创建成功

### FindWidgetByName
```angelscript
UWidget FindWidgetByName(UWidgetBlueprint WidgetBlueprint, FName WidgetName)
```
按名称查找控件
@param WidgetBlueprint - Widget Blueprint 资产
@param WidgetName - 控件名称
@return 找到的控件，如果没找到返回 nullptr

### GetAllWidgets
```angelscript
TArray<UWidget> GetAllWidgets(UWidgetBlueprint WidgetBlueprint)
```
获取所有控件
@param WidgetBlueprint - Widget Blueprint 资产
@return 所有控件的数组

### GetRootWidget
```angelscript
UWidget GetRootWidget(UWidgetBlueprint WidgetBlueprint)
```
获取 Widget Blueprint 的根控件
@param WidgetBlueprint - Widget Blueprint 资产
@return 根控件，如果没有返回 nullptr

### GetWidgetTree
```angelscript
UWidgetTree GetWidgetTree(UWidgetBlueprint WidgetBlueprint)
```
获取 Widget Blueprint 的 WidgetTree
@param WidgetBlueprint - Widget Blueprint 资产
@return WidgetTree 对象，如果失败返回 nullptr

### MarkDirty
```angelscript
void MarkDirty(UWidgetBlueprint WidgetBlueprint)
```
标记 Widget Blueprint 为已修改
@param WidgetBlueprint - Widget Blueprint 资产

### SaveWidgetBlueprint
```angelscript
bool SaveWidgetBlueprint(UWidgetBlueprint WidgetBlueprint)
```
保存 Widget Blueprint
@param WidgetBlueprint - Widget Blueprint 资产
@return 是否保存成功

### SetRootWidget
```angelscript
bool SetRootWidget(UWidgetBlueprint WidgetBlueprint, UWidget RootWidget)
```
设置 Widget Blueprint 的根控件
@param WidgetBlueprint - Widget Blueprint 资产
@param RootWidget - 要设置为根的控件
@return 是否设置成功

