#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJ01 DataAsset Manager - 资产注册表
职责：管理所有资产的引用和依赖关系
"""

import json
import os
from typing import Dict, List, Optional
from dataclasses import dataclass, field, asdict
from datetime import datetime


@dataclass
class AssetReference:
    """资产引用信息"""
    asset_type: str
    asset_name: str
    asset_path: str = ""
    config_id: str = ""
    dependencies: List[str] = field(default_factory=list)
    dependents: List[str] = field(default_factory=list)
    created_at: str = ""
    updated_at: str = ""
    
    def to_dict(self) -> dict:
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: dict) -> 'AssetReference':
        return cls(**data)
    
    def get_key(self) -> str:
        """获取唯一键"""
        return f"{self.asset_type}:{self.asset_name}"


class AssetRegistry:
    """资产注册表"""
    
    def __init__(self, registry_path: str):
        self.registry_path = registry_path
        self.assets: Dict[str, AssetReference] = {}
        self._load()
    
    def _load(self):
        """加载注册表"""
        if not os.path.exists(self.registry_path):
            return
        
        try:
            with open(self.registry_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for key, value in data.get("assets", {}).items():
                    self.assets[key] = AssetReference.from_dict(value)
        except Exception as e:
            print(f"加载注册表失败: {e}")
    
    def save(self):
        """保存注册表"""
        data = {
            "version": "1.0",
            "updated_at": datetime.now().isoformat(),
            "assets": {k: v.to_dict() for k, v in self.assets.items()}
        }
        
        os.makedirs(os.path.dirname(self.registry_path), exist_ok=True)
        with open(self.registry_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def register(self, asset: AssetReference) -> str:
        """注册资产"""
        key = asset.get_key()
        now = datetime.now().isoformat()
        
        if key not in self.assets:
            asset.created_at = now
        asset.updated_at = now
        
        self.assets[key] = asset
        return key
    
    def unregister(self, asset_type: str, asset_name: str) -> bool:
        """注销资产"""
        key = f"{asset_type}:{asset_name}"
        if key in self.assets:
            del self.assets[key]
            return True
        return False
    
    def get(self, asset_type: str, asset_name: str) -> Optional[AssetReference]:
        """获取资产"""
        return self.assets.get(f"{asset_type}:{asset_name}")
    
    def get_by_type(self, asset_type: str) -> List[AssetReference]:
        """获取指定类型的所有资产"""
        return [a for a in self.assets.values() if a.asset_type == asset_type]
    
    def get_all_names(self, asset_type: str = None) -> List[str]:
        """获取所有资产名称"""
        if asset_type:
            return [a.asset_name for a in self.assets.values() if a.asset_type == asset_type]
        return [a.asset_name for a in self.assets.values()]
    
    def get_count(self, asset_type: str = None) -> int:
        """获取资产数量"""
        if asset_type:
            return len([a for a in self.assets.values() if a.asset_type == asset_type])
        return len(self.assets)