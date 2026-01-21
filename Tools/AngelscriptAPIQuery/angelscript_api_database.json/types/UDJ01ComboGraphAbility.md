# UDJ01ComboGraphAbility

**继承自**: `UDJ01GameplayAbility`

UDJ01ComboGraphAbility

连招技能中间层
- 继承自 UDJ01GameplayAbility，保留项目技能系统的所有特性
- 封装 ComboGraph 插件的使用，提供简洁的接口

使用方式：
1. 创建蓝图子类
2. 设置 ComboGraph 资产
3. 像普通 GA 一样授予和触发

## 属性

### ComboGraph
- **类型**: `UComboGraph`

### InitialInputAction
- **类型**: `UInputAction`

### bBroadcastInternalEvents
- **类型**: `bool`

### bEndAbilityOnGraphEnd
- **类型**: `bool`

## 方法

### GetCurrentComboNode
```angelscript
UComboGraphNodeAnimBase GetCurrentComboNode()
```
获取当前正在执行的节点

### GetPreviousComboNode
```angelscript
UComboGraphNodeAnimBase GetPreviousComboNode()
```
获取上一个执行的节点

### IsComboGraphRunning
```angelscript
bool IsComboGraphRunning()
```
ComboGraph 是否正在运行

### OnComboEventReceived
```angelscript
void OnComboEventReceived(FGameplayTag EventTag, FGameplayEventData EventData)
```
当接收到 Gameplay Event 时调用

### OnComboGraphEnded
```angelscript
void OnComboGraphEnded(bool bWasCancelled)
```
当 ComboGraph 结束时调用

### OnComboGraphStarted
```angelscript
void OnComboGraphStarted()
```
当 ComboGraph 开始执行时调用

### OnComboNodeChanged
```angelscript
void OnComboNodeChanged(UComboGraphNodeAnimBase PreviousNode, UComboGraphNodeAnimBase NewNode)
```
当节点切换时调用

