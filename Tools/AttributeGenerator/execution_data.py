#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJ01 GAS 代码生成器 - Execution 数据模型
"""


class ExecutionData:
    """Execution 数据模型"""
    
    def __init__(self, name="", description=""):
        self.name = name
        self.description = description
        self.captures = []  # [{"source": "Source", "set": "StatSet", "attr": "AttackPower", "layer": "Total"}]
        self.outputs = []   # [{"set": "ResourceSet", "attr": "Health", "op": "Additive"}]
        self.tag_conditions = []  # [{"source": "Target", "tag": "Immunity.Fire", "effect": "Skip", "value": 0}]
        self.formula = ""

    def to_dict(self):
        """转换为字典格式"""
        return {
            'Name': self.name,
            'Description': self.description,
            'Captures': self.captures,
            'Outputs': self.outputs,
            'TagConditions': self.tag_conditions,
            'Formula': self.formula
        }

    @staticmethod
    def from_dict(d):
        """从字典创建 ExecutionData"""
        exe = ExecutionData(d.get('Name', ''), d.get('Description', ''))
        exe.captures = d.get('Captures', [])
        exe.outputs = d.get('Outputs', [])
        exe.tag_conditions = d.get('TagConditions', [])
        exe.formula = d.get('Formula', '')
        return exe#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJ01 GAS 代码生成器 - Execution 数据模型
"""


class ExecutionData:
    """Execution 数据模型"""
    def __init__(self, name="", description=""):
        self.name = name
        self.description = description
        self.captures = []  # [{"source": "Source", "set": "StatSet", "attr": "AttackPower", "layer": "Total"}]
        self.outputs = []   # [{"set": "ResourceSet", "attr": "Health", "op": "Additive"}]
        self.tag_conditions = []  # [{"source": "Target", "tag": "Immunity.Fire", "effect": "Skip", "value": 0}]
        self.formula = ""

    def to_dict(self):
        return {
            'Name': self.name,
            'Description': self.description,
            'Captures': self.captures,
            'Outputs': self.outputs,
            'TagConditions': self.tag_conditions,
            'Formula': self.formula
        }

    @staticmethod
    def from_dict(d):
        exe = ExecutionData(d.get('Name', ''), d.get('Description', ''))
        exe.captures = d.get('Captures', [])
        exe.outputs = d.get('Outputs', [])
        exe.tag_conditions = d.get('TagConditions', [])
        exe.formula = d.get('Formula', '')
        return exe