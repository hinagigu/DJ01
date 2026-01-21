# UDJ01HealthBarBase

**继承自**: `UCommonUserWidget`

DJ01HealthBar 基类



使用方式：
1. 创建继承此类的 Widget Blueprint
2. 在 Designer 中添加对应名称的控件
3. 调整布局和样式

## 属性

### RootCanvas
- **类型**: `UCanvasPanel`
- **描述**: ===== UI 组件 (BindWidget) =====

### HealthBar
- **类型**: `UProgressBar`

### HealthText
- **类型**: `UTextBlock`
- **描述**: 血量进度条

### HealthPercent
- **类型**: `float32`

## 方法

### BindToASC
```angelscript
void BindToASC(UAbilitySystemComponent InASC)
```
绑定到 AbilitySystemComponent

### UnbindFromASC
```angelscript
void UnbindFromASC()
```
解除绑定

