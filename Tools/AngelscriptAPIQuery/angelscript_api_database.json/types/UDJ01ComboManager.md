# UDJ01ComboManager

**继承自**: `UActorComponent`

UDJ01ComboManager

连招管理器 - 协调输入缓冲、GAS、动画系统

职责：
- 管理输入缓冲
- 控制连招窗口（是否可接受输入）
- 追踪当前连招状态
- 与 ASC 协调技能激活

## 属性

### OnComboWindowStateChanged
- **类型**: `FOnComboWindowStateChanged`

### OnComboAdvanced
- **类型**: `FOnComboAdvanced`

### InputBuffer
- **类型**: `FDJ01ComboInputBuffer`
- **描述**: 输入缓冲配置

## 方法

### AdvanceComboIndex
```angelscript
void AdvanceComboIndex()
```
推进连招索引

### BufferInput
```angelscript
void BufferInput(FGameplayTag AbilityTag, int Priority)
```
缓冲输入
由输入系统调用（EnhancedInput / AngelScript）

@param AbilityTag 技能标签
@param Priority 优先级（越小越高）

### ClearInputBuffer
```angelscript
void ClearInputBuffer()
```
清空输入缓冲

### CloseComboWindow
```angelscript
void CloseComboWindow()
```
仅关闭连招窗口（不消费输入）

### CloseComboWindowAndConsume
```angelscript
bool CloseComboWindowAndConsume()
```
关闭连招窗口并尝试消费输入
由 AnimNotify 调用

@return 是否成功消费输入并激活下一段

### GetCurrentComboChainTag
```angelscript
FGameplayTag GetCurrentComboChainTag()
```
获取当前连招链 Tag

### GetCurrentComboIndex
```angelscript
int GetCurrentComboIndex()
```
获取当前连招索引

### HasBufferedInput
```angelscript
bool HasBufferedInput()
```
检查是否有缓冲输入

### IsComboWindowOpen
```angelscript
bool IsComboWindowOpen()
```
连招窗口是否打开

### OpenComboWindow
```angelscript
void OpenComboWindow(FGameplayTag ComboChainTag)
```
打开连招窗口
由 AnimNotify 调用，标记可以接受下一段输入

@param ComboChainTag 当前连招链标识（可选）

### RequestAutoChain
```angelscript
void RequestAutoChain(FGameplayTag NextAbilityTag)
```
请求自动衔接下一段
无需玩家输入，自动触发下一个技能

@param NextAbilityTag 下一个技能的 Tag

### ResetComboState
```angelscript
void ResetComboState()
```
重置连招状态

### TryActivateOrBuffer
```angelscript
bool TryActivateOrBuffer(FGameplayTag AbilityTag, int Priority)
```
尝试立即激活或缓冲输入
如果当前无技能执行，立即激活；否则缓冲

@param AbilityTag 技能标签
@param Priority 优先级
@return 是否立即激活成功

