"""
GameFeature UI 配置生成器

生成用于 GameFeature 系统的 UI 配置：
- UI.Layer / UI.Slot GameplayTag 定义
- PrimaryGameLayout Blueprint 结构
- GameFeatureData 资产配置

与 cpp_generator.py 配合使用，实现完整的 Lyra 风格 UI 架构。
"""

import json
import os
from typing import Dict, List, Optional
from datetime import datetime
from pathlib import Path


class GameFeatureUIGenerator:
    """GameFeature UI 配置生成器"""
    
    def __init__(self, widget_types_path: str, project_name: str = "DJ01"):
        """
        初始化生成器
        
        Args:
            widget_types_path: widget_types.json 路径
            project_name: 项目名称
        """
        with open(widget_types_path, 'r', encoding='utf-8') as f:
            self.widget_types = json.load(f)
        
        self.project_name = project_name
        self.ui_layers = self.widget_types.get('ui_layers', {})
        self.ui_slots = self.widget_types.get('ui_slots', {})
        self.gf_config = self.widget_types.get('gamefeature_integration', {})
    
    def generate_gameplay_tags_ini(self, output_path: str) -> str:
        """
        生成 GameplayTags 配置文件内容
        用于 Config/Tags/UITags.ini
        
        Args:
            output_path: 输出路径
            
        Returns:
            生成的文件路径
        """
        lines = []
        lines.append("; =============================================================================")
        lines.append(f"; UI GameplayTags - 自动生成")
        lines.append(f"; 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append("; =============================================================================")
        lines.append("")
        lines.append("[/Script/GameplayTags.GameplayTagsSettings]")
        lines.append("")
        
        # UI Layers
        lines.append("; ----- UI Layers (CommonUI 分层系统) -----")
        for layer_name, layer_info in self.ui_layers.items():
            if layer_name == '$comment':
                continue
            tag = layer_info.get('tag', f'UI.Layer.{layer_name}')
            desc = layer_info.get('description', '')
            lines.append(f'+GameplayTagList=(Tag="{tag}",DevComment="{desc}")')
        
        lines.append("")
        
        # UI Slots
        lines.append("; ----- UI Slots (UIExtension 插槽系统) -----")
        for slot_name, slot_info in self.ui_slots.items():
            if slot_name == '$comment':
                continue
            tag = slot_info.get('tag', f'UI.Slot.{slot_name}')
            desc = slot_info.get('description', '')
            lines.append(f'+GameplayTagList=(Tag="{tag}",DevComment="{desc}")')
        
        # 写入文件
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        
        return output_path
    
    def generate_primary_layout_header(self, output_dir: str) -> Dict[str, str]:
        """
        生成 PrimaryGameLayout C++ 基类
        这是 CommonUI 的核心布局 Widget，包含所有 UI Layer
        
        Args:
            output_dir: 输出目录
            
        Returns:
            生成的文件路径字典
        """
        class_name = f"U{self.project_name}PrimaryGameLayoutBase"
        
        # 生成头文件
        header_lines = []
        header_lines.append(self._generate_file_header("PrimaryGameLayout"))
        header_lines.append("")
        header_lines.append("#pragma once")
        header_lines.append("")
        header_lines.append('#include "CommonActivatableWidget.h"')
        header_lines.append('#include "GameplayTagContainer.h"')
        header_lines.append("")
        header_lines.append(f'#include "{self.project_name}PrimaryGameLayoutBase.generated.h"')
        header_lines.append("")
        header_lines.append("class UCommonActivatableWidgetContainerBase;")
        header_lines.append("")
        header_lines.append("/**")
        header_lines.append(" * 主游戏布局 Widget")
        header_lines.append(" * ")
        header_lines.append(" * 这是 CommonUI 分层系统的核心 Widget，负责管理所有 UI 层级。")
        header_lines.append(" * 通过 GameplayTag 标识不同的层，支持模块化的 UI 注入。")
        header_lines.append(" * ")
        header_lines.append(" * 层级说明：")
        for layer_name, layer_info in self.ui_layers.items():
            if layer_name == '$comment':
                continue
            desc = layer_info.get('description', '')
            header_lines.append(f" * - {layer_name}: {desc}")
        header_lines.append(" */")
        header_lines.append("UCLASS(Abstract, Blueprintable)")
        header_lines.append(f"class {self.project_name.upper()}_API {class_name} : public UCommonActivatableWidget")
        header_lines.append("{")
        header_lines.append("\tGENERATED_BODY()")
        header_lines.append("")
        header_lines.append("public:")
        header_lines.append(f"\t{class_name}(const FObjectInitializer& ObjectInitializer = FObjectInitializer::Get());")
        header_lines.append("")
        header_lines.append("\t/** 将 Widget 推送到指定的 UI 层 */")
        header_lines.append("\tUFUNCTION(BlueprintCallable, Category = \"UI|Layer\")")
        header_lines.append("\tUCommonActivatableWidget* PushWidgetToLayer(FGameplayTag LayerTag, TSubclassOf<UCommonActivatableWidget> WidgetClass);")
        header_lines.append("")
        header_lines.append("\t/** 根据 Tag 查找 Layer 容器 */")
        header_lines.append("\tUFUNCTION(BlueprintCallable, Category = \"UI|Layer\")")
        header_lines.append("\tUCommonActivatableWidgetContainerBase* GetLayerWidget(FGameplayTag LayerTag) const;")
        header_lines.append("")
        header_lines.append("protected:")
        header_lines.append("\t//~ Begin UUserWidget Interface")
        header_lines.append("\tvirtual void NativeConstruct() override;")
        header_lines.append("\t//~ End UUserWidget Interface")
        header_lines.append("")
        header_lines.append("\t/** 注册一个 Layer 容器 */")
        header_lines.append("\tUFUNCTION(BlueprintCallable, Category = \"UI|Layer\")")
        header_lines.append("\tvoid RegisterLayer(FGameplayTag LayerTag, UCommonActivatableWidgetContainerBase* Container);")
        header_lines.append("")
        header_lines.append("private:")
        header_lines.append("\t/** Tag -> Layer 容器映射 */")
        header_lines.append("\tUPROPERTY(Transient)")
        header_lines.append("\tTMap<FGameplayTag, TObjectPtr<UCommonActivatableWidgetContainerBase>> LayerMap;")
        header_lines.append("};")
        
        # 生成源文件
        source_lines = []
        source_lines.append(self._generate_file_header("PrimaryGameLayout"))
        source_lines.append("")
        source_lines.append(f'#include "{self.project_name}PrimaryGameLayoutBase.h"')
        source_lines.append('#include "Widgets/CommonActivatableWidgetContainerBase.h"')
        source_lines.append("")
        source_lines.append(f"{class_name}::{class_name}(const FObjectInitializer& ObjectInitializer)")
        source_lines.append("\t: Super(ObjectInitializer)")
        source_lines.append("{")
        source_lines.append("}")
        source_lines.append("")
        source_lines.append(f"void {class_name}::NativeConstruct()")
        source_lines.append("{")
        source_lines.append("\tSuper::NativeConstruct();")
        source_lines.append("")
        source_lines.append("\t// Blueprint 中应调用 RegisterLayer() 注册每个 Layer 容器")
        source_lines.append("}")
        source_lines.append("")
        source_lines.append(f"void {class_name}::RegisterLayer(FGameplayTag LayerTag, UCommonActivatableWidgetContainerBase* Container)")
        source_lines.append("{")
        source_lines.append("\tif (Container && LayerTag.IsValid())")
        source_lines.append("\t{")
        source_lines.append("\t\tLayerMap.Add(LayerTag, Container);")
        source_lines.append("\t}")
        source_lines.append("}")
        source_lines.append("")
        source_lines.append(f"UCommonActivatableWidgetContainerBase* {class_name}::GetLayerWidget(FGameplayTag LayerTag) const")
        source_lines.append("{")
        source_lines.append("\tconst TObjectPtr<UCommonActivatableWidgetContainerBase>* Found = LayerMap.Find(LayerTag);")
        source_lines.append("\treturn Found ? *Found : nullptr;")
        source_lines.append("}")
        source_lines.append("")
        source_lines.append(f"UCommonActivatableWidget* {class_name}::PushWidgetToLayer(FGameplayTag LayerTag, TSubclassOf<UCommonActivatableWidget> WidgetClass)")
        source_lines.append("{")
        source_lines.append("\tif (UCommonActivatableWidgetContainerBase* Layer = GetLayerWidget(LayerTag))")
        source_lines.append("\t{")
        source_lines.append("\t\treturn Layer->AddWidget(WidgetClass);")
        source_lines.append("\t}")
        source_lines.append("\treturn nullptr;")
        source_lines.append("}")
        
        # 写入文件
        os.makedirs(output_dir, exist_ok=True)
        header_path = os.path.join(output_dir, f"{self.project_name}PrimaryGameLayoutBase.h")
        source_path = os.path.join(output_dir, f"{self.project_name}PrimaryGameLayoutBase.cpp")
        
        with open(header_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(header_lines))
        
        with open(source_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(source_lines))
        
        return {'header': header_path, 'source': source_path}
    
    def generate_gamefeature_ui_config(self, schemas: List[Dict], output_path: str) -> str:
        """
        生成 GameFeature UI 配置 JSON
        用于描述哪些 Widget 应该注册到哪些 Layer/Slot
        
        Args:
            schemas: Widget schema 列表
            output_path: 输出路径
            
        Returns:
            生成的文件路径
        """
        config = {
            "$comment": "GameFeature UI 配置 - 用于 GameFeatureAction_AddWidgets",
            "generated_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "layouts": [],
            "widgets": []
        }
        
        for schema in schemas:
            widget_name = schema.get('name', '')
            parent_class = schema.get('parent_class', 'CommonUserWidget')
            gf_config = schema.get('gamefeature', {})
            
            if not gf_config:
                continue
            
            # 判断是 Layout 还是普通 Widget
            if gf_config.get('is_layout', False):
                # Layout 类型 - 推送到 Layer
                config['layouts'].append({
                    "widget_class": f"/Game/UI/Generated/WBP_{widget_name}.WBP_{widget_name}_C",
                    "layer": gf_config.get('layer', 'UI.Layer.Game'),
                    "comment": schema.get('description', '')
                })
            elif 'slot' in gf_config:
                # 普通 Widget - 注册到 Slot
                config['widgets'].append({
                    "widget_class": f"/Game/UI/Generated/WBP_{widget_name}.WBP_{widget_name}_C",
                    "slot": gf_config.get('slot'),
                    "comment": schema.get('description', '')
                })
        
        # 写入文件
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        
        return output_path
    
    def generate_ui_extension_point(self, slot_name: str, output_dir: str) -> Dict[str, str]:
        """
        生成 UIExtensionPoint Widget 基类
        用于在 Layout 中定义可扩展的插槽
        
        Args:
            slot_name: 插槽名称
            output_dir: 输出目录
            
        Returns:
            生成的文件路径字典
        """
        class_name = f"U{self.project_name}ExtensionPoint_{slot_name}Base"
        slot_info = self.ui_slots.get(slot_name, {})
        slot_tag = slot_info.get('tag', f'UI.Slot.{slot_name}')
        
        header_lines = []
        header_lines.append(self._generate_file_header(f"ExtensionPoint_{slot_name}"))
        header_lines.append("")
        header_lines.append("#pragma once")
        header_lines.append("")
        header_lines.append('#include "CommonUserWidget.h"')
        header_lines.append('#include "UIExtensionSystem.h"')
        header_lines.append("")
        header_lines.append(f'#include "{self.project_name}ExtensionPoint_{slot_name}Base.generated.h"')
        header_lines.append("")
        header_lines.append("/**")
        header_lines.append(f" * UI 扩展点: {slot_name}")
        header_lines.append(f" * Slot Tag: {slot_tag}")
        header_lines.append(f" * ")
        header_lines.append(f" * {slot_info.get('description', '')}")
        header_lines.append(" */")
        header_lines.append("UCLASS(Abstract, Blueprintable)")
        header_lines.append(f"class {self.project_name.upper()}_API {class_name} : public UCommonUserWidget")
        header_lines.append("{")
        header_lines.append("\tGENERATED_BODY()")
        header_lines.append("")
        header_lines.append("public:")
        header_lines.append(f"\t{class_name}(const FObjectInitializer& ObjectInitializer = FObjectInitializer::Get());")
        header_lines.append("")
        header_lines.append(f"\t/** 此扩展点的 Slot Tag */")
        header_lines.append(f"\tstatic FGameplayTag GetSlotTag();")
        header_lines.append("")
        header_lines.append("protected:")
        header_lines.append("\tvirtual void NativeConstruct() override;")
        header_lines.append("\tvirtual void NativeDestruct() override;")
        header_lines.append("")
        header_lines.append("private:")
        header_lines.append("\t/** 扩展点句柄 */")
        header_lines.append("\tFUIExtensionPointHandle ExtensionPointHandle;")
        header_lines.append("")
        header_lines.append("\t/** 容器 - 存放注册到此插槽的 Widget */")
        header_lines.append("\tUPROPERTY(meta = (BindWidget))")
        header_lines.append("\tTObjectPtr<UPanelWidget> ExtensionContainer;")
        header_lines.append("};")
        
        source_lines = []
        source_lines.append(self._generate_file_header(f"ExtensionPoint_{slot_name}"))
        source_lines.append("")
        source_lines.append(f'#include "{self.project_name}ExtensionPoint_{slot_name}Base.h"')
        source_lines.append('#include "Components/PanelWidget.h"')
        source_lines.append("")
        source_lines.append(f"{class_name}::{class_name}(const FObjectInitializer& ObjectInitializer)")
        source_lines.append("\t: Super(ObjectInitializer)")
        source_lines.append("{")
        source_lines.append("}")
        source_lines.append("")
        source_lines.append(f"FGameplayTag {class_name}::GetSlotTag()")
        source_lines.append("{")
        source_lines.append(f'\treturn FGameplayTag::RequestGameplayTag(FName("{slot_tag}"));')
        source_lines.append("}")
        source_lines.append("")
        source_lines.append(f"void {class_name}::NativeConstruct()")
        source_lines.append("{")
        source_lines.append("\tSuper::NativeConstruct();")
        source_lines.append("")
        source_lines.append("\tif (UUIExtensionSubsystem* ExtensionSubsystem = GetWorld()->GetSubsystem<UUIExtensionSubsystem>())")
        source_lines.append("\t{")
        source_lines.append("\t\tExtensionPointHandle = ExtensionSubsystem->RegisterExtensionPoint(")
        source_lines.append("\t\t\tGetSlotTag(),")
        source_lines.append("\t\t\tEUIExtensionPointMatch::ExactMatch,")
        source_lines.append("\t\t\tTArray<UClass*>(),")
        source_lines.append("\t\t\tFOnExtensionMutationDelegate::CreateWeakLambda(this, [this](EUIExtensionAction Action, const FUIExtensionRequest& Request)")
        source_lines.append("\t\t\t{")
        source_lines.append("\t\t\t\tif (Action == EUIExtensionAction::Added && ExtensionContainer)")
        source_lines.append("\t\t\t\t{")
        source_lines.append("\t\t\t\t\tif (UUserWidget* Widget = CreateWidget<UUserWidget>(GetOwningPlayer(), Request.WidgetClass))")
        source_lines.append("\t\t\t\t\t{")
        source_lines.append("\t\t\t\t\t\tExtensionContainer->AddChild(Widget);")
        source_lines.append("\t\t\t\t\t}")
        source_lines.append("\t\t\t\t}")
        source_lines.append("\t\t\t}));")
        source_lines.append("\t}")
        source_lines.append("}")
        source_lines.append("")
        source_lines.append(f"void {class_name}::NativeDestruct()")
        source_lines.append("{")
        source_lines.append("\tExtensionPointHandle.Unregister();")
        source_lines.append("\tSuper::NativeDestruct();")
        source_lines.append("}")
        
        # 写入文件
        os.makedirs(output_dir, exist_ok=True)
        header_path = os.path.join(output_dir, f"{self.project_name}ExtensionPoint_{slot_name}Base.h")
        source_path = os.path.join(output_dir, f"{self.project_name}ExtensionPoint_{slot_name}Base.cpp")
        
        with open(header_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(header_lines))
        
        with open(source_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(source_lines))
        
        return {'header': header_path, 'source': source_path}
    
    def _generate_file_header(self, name: str) -> str:
        """生成文件头注释"""
        return f"""// =============================================================================
// {name} - 自动生成的 GameFeature UI 组件
// 
// 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
// 
// ⚠️ 此文件由 UI Generator 自动生成，请勿手动修改
// ============================================================================="""