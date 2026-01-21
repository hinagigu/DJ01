# UDJ01ViewModelBase

**继承自**: `UMVVMViewModelBase`

DJ01 ViewModel 基类

所有游戏 ViewModel 的基类，提供：
- 与 GAS 属性系统的集成（通过 BindingSet）
- 玩家上下文获取
- 通用的初始化/清理逻辑

使用方式：
1. 继承此类创建具体的 ViewModel
2. 使用 DJ01_DECLARE_BINDING_SET(Name) 声明需要的绑定
3. 在 InitializeViewModel_Implementation 中调用 DJ01_INIT_BINDING_SET
4. 在 UninitializeViewModel_Implementation 中调用 DJ01_CLEANUP_BINDING_SET

@see DJ01HealthViewModel 完整使用示例

## 方法

### GetAbilitySystemComponent
```angelscript
UAbilitySystemComponent GetAbilitySystemComponent()
```
获取绑定的 ASC

### InitializeViewModel
```angelscript
void InitializeViewModel(UAbilitySystemComponent ASC)
```
初始化 ViewModel
子类应重写此函数以调用 DJ01_INIT_BINDING_SET

### IsInitialized
```angelscript
bool IsInitialized()
```
检查 ViewModel 是否已初始化

### UninitializeViewModel
```angelscript
void UninitializeViewModel()
```
清理 ViewModel
子类应重写此函数以调用 DJ01_CLEANUP_BINDING_SET

