# UDJ01AbilityEffect

**继承自**: `UObject`

UDJ01AbilityEffect

技能效果基类，类似 ActorComponent 的设计理念。
每个效果负责一种具体行为（伤害、治疗、Buff等）。

使用方式：
1. 继承此类创建具体效果（UDJ01DamageEffect, UDJ01HealEffect 等）
2. 在 UDJ01GameplayAbility 的 Effects 数组中添加效果
3. 设置触发阶段，技能会在对应时机自动执行效果

## 属性

### DisplayName
- **类型**: `FText`

### Description
- **类型**: `FText`

### bEnabled
- **类型**: `bool`

## 方法

### Execute
```angelscript
bool Execute(FDJ01EffectContext& Context)
```
执行效果
@param Context - 执行上下文，包含施法者和目标信息
@return 是否成功执行

### GetEffectDescription
```angelscript
FString GetEffectDescription()
```
获取效果描述文本
用于技能提示 UI 显示

