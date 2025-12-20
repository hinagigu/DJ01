#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tag 数据模型
"""


class TagData:
    """Tag 数据模型"""
    
    def __init__(self, category="", tag="", variable_name="", description=""):
        self.category = category
        self.tag = tag
        self.variable_name = variable_name
        self.description = description

    def to_dict(self):
        return {
            'Category': self.category,
            'Tag': self.tag,
            'VariableName': self.variable_name,
            'Description': self.description
        }

    @staticmethod
    def from_dict(d):
        return TagData(
            category=d.get('Category', ''),
            tag=d.get('Tag', ''),
            variable_name=d.get('VariableName', ''),
            description=d.get('Description', '')
        )