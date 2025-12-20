#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MMC 数据模型
"""


class MMCData:
    """MMC (Modifier Magnitude Calculation) 数据模型"""
    
    def __init__(self, name="", description=""):
        self.name = name
        self.description = description
        self.captures = []  # [{"source": "Target", "set": "MoveMent", "attr": "SlowResistance", "layer": "Total"}]
        self.set_by_callers = []  # [{"tag": "Data.SlowPercent", "default": -0.3, "description": "基础减速值"}]
        self.formula = ""

    def to_dict(self):
        return {
            'Name': self.name,
            'Description': self.description,
            'Captures': self.captures,
            'SetByCallers': self.set_by_callers,
            'Formula': self.formula
        }

    @staticmethod
    def from_dict(d):
        mmc = MMCData(d.get('Name', ''), d.get('Description', ''))
        mmc.captures = d.get('Captures', [])
        mmc.set_by_callers = d.get('SetByCallers', [])
        mmc.formula = d.get('Formula', '')
        return mmc