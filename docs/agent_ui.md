# DJ01 UI/BindingSet 系统开发指引

## CONTEXT

项目: Unreal Engine 5.3 Action RPG
模块: DJ01
工作目录: D:\UnrealProjects\DJ01

## SYSTEM_ARCHITECTURE

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              UI 生产管线                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  [JSON Schema] ──► [C++ Generator] ──► [Compile] ──► [UE Python] ──► [UMG] │
│                                                                             │
│  Tools/UIGenerator/                    Source/DJ01/UI/                      │
│  └─ schemas/*.json                     ├─ Public/*.h                        │
│  └─ core/cpp_generator.py              └─ Private/*.cpp                     │
│  └─ ue_scripts/generate_widget_bp.py                                        │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                            GAS 绑定系统                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  [BindingSet JSON] ──► [Generator] ──► [Macro Headers] ──► [C++ Class]     │
│                                                                             │
│  Config/BindingSetDefinitions.json     Generated/BindingSets.h              │
│  Tools/AttributeGenerator/             DJ01_DECLARE_BINDING_SET(Name)       │
│  └─ bindingset/generator.py            DJ01_INIT_BINDING_SET(Name, ASC)     │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                              MVVM 层                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  UDJ01ViewModelBase ◄─── UDJ01HealthViewModel                               │
│  (接收 ASC, 管理生命周期)   (DJ01_DECLARE_BINDING_SET + FieldNotify)        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## KEY_PATHS

```yaml
BindingSet:
  config: Source/DJ01/AbilitySystem/Attributes/BindingSets/Config/BindingSetDefinitions.json
  output: Source/DJ01/AbilitySystem/Attributes/BindingSets/Generated/
  generator: Tools/AttributeGenerator/bindingset/generator.py
  include: "DJ01/AbilitySystem/Attributes/BindingSets/Generated/BindingSets.h"

UIGenerator:
  tool: Tools/UIGenerator/
  schemas: Tools/UIGenerator/schemas/
  cpp_gen: Tools/UIGenerator/core/cpp_generator.py
  ue_script: Tools/UIGenerator/ue_scripts/generate_widget_bp.py

ViewModel:
  base_h: Source/DJ01/UI/Public/DJ01ViewModelBase.h
  base_cpp: Source/DJ01/UI/Private/DJ01ViewModelBase.cpp
  health_h: Source/DJ01/UI/Public/ViewModels/DJ01HealthViewModel.h
  health_cpp: Source/DJ01/UI/Private/ViewModels/DJ01HealthViewModel.cpp

Attributes:
  config: Source/DJ01/AbilitySystem/Attributes/Config/AttributeDefinitions.csv
  generated_h: Source/DJ01/AbilitySystem/Attributes/Public/DJ01GeneratedAttributes.h
  generator: Tools/AttributeGenerator/attribute/generator.py

CommonUI:
  hud: Source/DJ01/UI/Public/DJ01HUD.h
  game_feature: Source/GameFeatureActions/GameFeatureAction_AddWidgets.h
```

## INCLUDE_PATH_CONVENTION

所有 include 必须从模块名开始:
```cpp
#include "DJ01/[Subsystem]/Public/[FileName].h"
#include "DJ01/[Subsystem]/Private/[FileName].h"

// Examples:
#include "DJ01/UI/Public/DJ01ViewModelBase.h"
#include "DJ01/AbilitySystem/Public/DJ01AbilitySystemComponent.h"
#include "DJ01/AbilitySystem/Attributes/BindingSets/Generated/BindingSets.h"
```

## CURRENT_STATE

### Completed
- [x] BindingSet 宏系统 (DJ01_DECLARE/INIT/CLEANUP_BINDING_SET)
- [x] BindingSet Generator (Python)
- [x] Test BindingSet (CurrentHealth, CurrentMana, 5 status tags)
- [x] MVVM Plugin 启用 (ModelViewViewModel, FieldNotification)
- [x] UDJ01ViewModelBase 基类
- [x] UDJ01HealthViewModel (使用 BindingSet)
- [x] UIGenerator 基础框架 (schema, cpp_generator)

### Pending
- [ ] BindingSet: 添加 MaxHealth 绑定 (ValueType: Max)
- [ ] BindingSet: 创建专用 Health/HUD BindingSet
- [ ] ViewModel: CurrentHealth 变化时自动调用 UpdateDerivedProperties
- [ ] UIGenerator: 完善 UE Python 脚本 (WidgetTree 操作)
- [ ] UIGenerator: Schema 支持 ViewModel 绑定定义
- [ ] UIGenerator: 两步流程 GUI (C++ Gen → Compile → BP Gen)
- [ ] CommonUI: ActivatableWidget 基类集成

## BINDINGSET_SCHEMA

```json
{
  "BindingSets": [
    {
      "Name": "BindingSetName",
      "Description": "描述",
      "TagBindings": [
        {
          "Type": "Tag",
          "Tag": "Status.Condition.Stunned",
          "VariableName": "bStunned",
          "EventType": "NewOrRemoved",
          "Description": ""
        }
      ],
      "AttributeBindings": [
        {
          "Type": "Attribute",
          "AttributeSet": "ResourceSet",
          "AttributeName": "Health",
          "VariableName": "CurrentHealth",
          "VarType": "float",
          "ValueType": "Current|Max|Base|Total",
          "Description": ""
        }
      ]
    }
  ]
}
```

## VIEWMODEL_PATTERN

```cpp
// Header (.h)
UCLASS(BlueprintType)
class DJ01_API UMyViewModel : public UDJ01ViewModelBase
{
    GENERATED_BODY()
public:
    virtual void InitializeViewModel_Implementation(UAbilitySystemComponent* ASC) override;
    virtual void UninitializeViewModel_Implementation() override;

    // BindingSet 声明 - 自动生成变量
    DJ01_DECLARE_BINDING_SET(BindingSetName)

    // 派生属性 - 需要 FieldNotify
    UPROPERTY(BlueprintReadOnly, FieldNotify, Category = "...")
    float DerivedValue;
};

// Source (.cpp)
void UMyViewModel::InitializeViewModel_Implementation(UAbilitySystemComponent* ASC)
{
    Super::InitializeViewModel_Implementation(ASC);
    if (ASC)
    {
        DJ01_INIT_BINDING_SET(BindingSetName, ASC)
        UpdateDerivedProperties();
    }
}

void UMyViewModel::UninitializeViewModel_Implementation()
{
    if (BoundASC.IsValid())
    {
        DJ01_CLEANUP_BINDING_SET(BindingSetName, BoundASC.Get())
    }
    Super::UninitializeViewModel_Implementation();
}
```

## TASKS

### Task 1: 扩展 Health BindingSet
目标: 在 BindingSetDefinitions.json 添加 MaxHealth
```json
{
  "Type": "Attribute",
  "AttributeSet": "ResourceSet", 
  "AttributeName": "Health",
  "VariableName": "MaxHealth",
  "VarType": "float",
  "ValueType": "Max",
  "Description": "最大生命值"
}
```
然后运行 Tools/AttributeGenerator 重新生成代码

### Task 2: ViewModel 属性变化回调
问题: BindingSet 的 CurrentHealth 变化时，ViewModel 的 UpdateDerivedProperties 不会自动调用
方案: 
1. 修改 BindingSet Generator，支持生成自定义回调钩子
2. 或在 ViewModel 中覆盖 BindingSet 回调函数

### Task 3: UIGenerator Schema 扩展
目标: 支持在 JSON 中定义 ViewModel 绑定
```json
{
  "widget_name": "WBP_HealthBar",
  "viewmodel": {
    "class": "UDJ01HealthViewModel",
    "bindings": [
      {"property": "HealthPercent", "target": "ProgressBar_Health.Percent"},
      {"property": "HealthDisplayText", "target": "Text_Health.Text"}
    ]
  }
}
```

### Task 4: CommonUI ActivatableWidget 集成
目标: 创建支持 InputConfig 的 Widget 基类
文件: Source/DJ01/UI/Public/DJ01ActivatableWidget.h
功能:
- GetDesiredInputConfig() 返回输入配置
- NativeOnActivated/Deactivated 生命周期
- 与 CommonUI Layer 系统集成

## CODE_GENERATION_RULES

1. 新建 C++ 文件时，include 路径从 "DJ01/" 开始
2. .cpp 文件放 Private/, .h 文件放 Public/
3. 使用 SEARCH/REPLACE 格式修改现有文件
4. BindingSet 变量自动生成，不要在 ViewModel 中重复声明
5. FieldNotify 属性需要手动调用 BroadcastFieldValueChanged

## DEPENDENCIES

```cpp
// Build.cs 已包含
"CommonUI"
"CommonGame" 
"UIExtension"
"GameplayMessageRouter"
"ModelViewViewModel"
"FieldNotification"
"GameplayAbilities"
"GameplayTags"
```

## VALIDATION_CHECKLIST

修改代码后验证:
- [ ] Include 路径正确 (从 DJ01/ 开始)
- [ ] GENERATED_BODY() 存在
- [ ] _Implementation 后缀用于 BlueprintNativeEvent
- [ ] BindingSet 宏在 GENERATED_BODY() 之后
- [ ] 编译通过