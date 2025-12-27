#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJ01 DataAsset Manager - GameFeatureAction 类型定义
定义各种 Action 类型的属性 schema
"""

# Action 类型的属性定义
ACTION_PROPERTIES = {
    "UGameFeatureAction_AddAbilities": {
        "display_name": "添加技能 (Add Abilities)",
        "description": "向指定 Actor 授予技能、属性集和 AbilitySet",
        "properties": {
            "AbilitiesList": {
                "display_name": "技能配置列表",
                "type": "array",
                "item_schema": {
                    "ActorClass": {
                        "display_name": "目标 Actor 类",
                        "type": "class",
                        "options_source": "pawn_classes",
                        "required": True
                    },
                    "GrantedAbilities": {
                        "display_name": "授予的技能",
                        "type": "array",
                        "item_schema": {
                            "AbilityType": {
                                "display_name": "技能类",
                                "type": "class",
                                "options_source": "gameplay_abilities"
                            }
                        }
                    },
                    "GrantedAttributes": {
                        "display_name": "授予的属性集",
                        "type": "array",
                        "item_schema": {
                            "AttributeSetType": {
                                "display_name": "属性集类",
                                "type": "class",
                                "options_source": "attribute_sets"
                            },
                            "AttributeSetTag": {
                                "display_name": "属性集标签",
                                "type": "string"
                            },
                            "InitializationData": {
                                "display_name": "初始化数据表",
                                "type": "asset",
                                "allow_empty": True
                            }
                        }
                    },
                    "GrantedAbilitySets": {
                        "display_name": "授予的 AbilitySet",
                        "type": "array",
                        "item_type": "asset",
                        "options_source": "ability_sets"
                    }
                }
            }
        }
    },
    "UGameFeatureAction_AddInputBinding": {
        "display_name": "添加输入绑定 (Add Input Binding)",
        "description": "添加输入配置到 Pawn",
        "properties": {
            "InputConfigs": {
                "display_name": "输入配置列表",
                "type": "array",
                "item_type": "asset",
                "options_source": "input_configs"
            }
        }
    },
    "UGameFeatureAction_AddInputContextMapping": {
        "display_name": "添加输入上下文 (Add Input Context)",
        "description": "添加 InputMappingContext",
        "properties": {
            "InputMappings": {
                "display_name": "输入映射列表",
                "type": "array",
                "item_schema": {
                    "InputMappingContext": {
                        "display_name": "输入映射上下文",
                        "type": "asset",
                        "options_source": "input_mapping_contexts"
                    },
                    "Priority": {
                        "display_name": "优先级",
                        "type": "integer",
                        "default": 0
                    }
                }
            }
        }
    },
    "UGameFeatureAction_AddWidgets": {
        "display_name": "添加 UI 控件 (Add Widgets)",
        "description": "添加 HUD 布局和 UI 控件",
        "properties": {
            "Layout": {
                "display_name": "布局列表",
                "type": "array",
                "item_schema": {
                    "LayoutClass": {
                        "display_name": "布局类",
                        "type": "class",
                        "options_source": "activatable_widgets"
                    },
                    "LayerID": {
                        "display_name": "UI 层级",
                        "type": "tag",
                        "options_source": "ui_layer_tags"
                    }
                }
            },
            "Widgets": {
                "display_name": "控件列表",
                "type": "array",
                "item_schema": {
                    "WidgetClass": {
                        "display_name": "控件类",
                        "type": "class",
                        "options_source": "widget_classes"
                    },
                    "SlotID": {
                        "display_name": "插槽 ID",
                        "type": "tag",
                        "options_source": "ui_slot_tags"
                    }
                }
            }
        }
    },
    "UGameFeatureAction_AddWidget": {
        "display_name": "添加 UI 控件 (Add Widget)",
        "description": "添加 HUD 布局和 UI 控件",
        "properties": {
            "Layout": {
                "display_name": "布局列表",
                "type": "array",
                "item_schema": {
                    "LayoutClass": {
                        "display_name": "布局类",
                        "type": "class",
                        "options_source": "activatable_widgets"
                    },
                    "LayerID": {
                        "display_name": "UI 层级",
                        "type": "tag",
                        "options_source": "ui_layer_tags"
                    }
                }
            },
            "Widgets": {
                "display_name": "控件列表",
                "type": "array",
                "item_schema": {
                    "WidgetClass": {
                        "display_name": "控件类",
                        "type": "class",
                        "options_source": "widget_classes"
                    },
                    "SlotID": {
                        "display_name": "插槽 ID",
                        "type": "tag",
                        "options_source": "ui_slot_tags"
                    }
                }
            }
        }
    }
}


def get_action_def(type_name: str) -> dict:
    """获取 Action 类型定义"""
    return ACTION_PROPERTIES.get(type_name, {})


def get_action_display_name(type_name: str) -> str:
    """获取 Action 显示名称"""
    action_def = ACTION_PROPERTIES.get(type_name, {})
    return action_def.get("display_name", type_name)


def get_action_description(type_name: str) -> str:
    """获取 Action 描述"""
    action_def = ACTION_PROPERTIES.get(type_name, {})
    return action_def.get("description", "")


def get_action_properties(type_name: str) -> dict:
    """获取 Action 属性定义"""
    action_def = ACTION_PROPERTIES.get(type_name, {})
    return action_def.get("properties", {})