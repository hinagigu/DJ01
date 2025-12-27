#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJ01 DataAsset Manager - 资产注册表
统一管理所有 DataAsset 的引用和依赖关系
"""

import json
import os
from typing import Dict, List, Optional, Set
from dataclasses import dataclass, field, asdict
from datetime import datetime


@dataclass
class AssetReference:
    """资产引用信息"""
    asset_type: str  # Experience, PawnData, InputConfig, AbilitySet, AbilityTemplate
    asset_name: str
    asset_path: str  # UE 资产路径
    config_id: str   # 配置文件中的 ID
    dependencies: List[str] = field(default_factory=list)  # 依赖的其他资产
    dependents: List[str] = field(default_factory=list)    # 被哪些资产依赖
    created_at: str = ""
    updated_at: str = ""
    
    def to_dict(self):
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)


class AssetRegistry:
    """
    资产注册表
    管理所有 DataAsset 的配置和依赖关系
    """
    
    def __init__(self, registry_path: str):
        self.registry_path = registry_path
        self.assets: Dict[str, AssetReference] = {}
        self._load()
    
    def _load(self):
        """从文件加载注册表"""
        if os.path.exists(self.registry_path):
            try:
                with open(self.registry_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for key, value in data.get("assets", {}).items():
                        self.assets[key] = AssetReference.from_dict(value)
            except Exception as e:
                print(f"加载资产注册表失败: {e}")
                self.assets = {}
    
    def save(self):
        """保存注册表到文件"""
        data = {
            "version": "1.0",
            "updated_at": datetime.now().isoformat(),
            "assets": {key: asset.to_dict() for key, asset in self.assets.items()}
        }
        os.makedirs(os.path.dirname(self.registry_path), exist_ok=True)
        with open(self.registry_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def _make_key(self, asset_type: str, asset_name: str) -> str:
        """生成资产唯一键"""
        return f"{asset_type}:{asset_name}"
    
    def register(self, asset: AssetReference) -> str:
        """注册新资产"""
        key = self._make_key(asset.asset_type, asset.asset_name)
        now = datetime.now().isoformat()
        if key not in self.assets:
            asset.created_at = now
        asset.updated_at = now
        self.assets[key] = asset
        self.save()
        return key
    
    def unregister(self, asset_type: str, asset_name: str) -> bool:
        """注销资产"""
        key = self._make_key(asset_type, asset_name)
        if key in self.assets:
            # 移除所有依赖关系
            asset = self.assets[key]
            for dep_key in asset.dependencies:
                if dep_key in self.assets:
                    dep_asset = self.assets[dep_key]
                    if key in dep_asset.dependents:
                        dep_asset.dependents.remove(key)
            del self.assets[key]
            self.save()
            return True
        return False
    
    def get(self, asset_type: str, asset_name: str) -> Optional[AssetReference]:
        """获取资产"""
        key = self._make_key(asset_type, asset_name)
        return self.assets.get(key)
    
    def get_by_type(self, asset_type: str) -> List[AssetReference]:
        """获取指定类型的所有资产"""
        return [
            asset for key, asset in self.assets.items()
            if asset.asset_type == asset_type
        ]
    
    def add_dependency(self, from_type: str, from_name: str, 
                       to_type: str, to_name: str):
        """添加依赖关系"""
        from_key = self._make_key(from_type, from_name)
        to_key = self._make_key(to_type, to_name)
        
        if from_key in self.assets and to_key in self.assets:
            from_asset = self.assets[from_key]
            to_asset = self.assets[to_key]
            
            if to_key not in from_asset.dependencies:
                from_asset.dependencies.append(to_key)
            if from_key not in to_asset.dependents:
                to_asset.dependents.append(from_key)
            
            self.save()
    
    def get_dependencies(self, asset_type: str, asset_name: str) -> List[AssetReference]:
        """获取资产的所有依赖"""
        key = self._make_key(asset_type, asset_name)
        if key not in self.assets:
            return []
        
        return [
            self.assets[dep_key] for dep_key in self.assets[key].dependencies
            if dep_key in self.assets
        ]
    
    def get_dependents(self, asset_type: str, asset_name: str) -> List[AssetReference]:
        """获取依赖此资产的所有资产"""
        key = self._make_key(asset_type, asset_name)
        if key not in self.assets:
            return []
        
        return [
            self.assets[dep_key] for dep_key in self.assets[key].dependents
            if dep_key in self.assets
        ]
    
    def validate_dependencies(self) -> List[str]:
        """验证所有依赖关系，返回错误列表"""
        errors = []
        for key, asset in self.assets.items():
            for dep_key in asset.dependencies:
                if dep_key not in self.assets:
                    errors.append(f"{key} 依赖的 {dep_key} 不存在")
        return errors
    
    def get_all_asset_names(self, asset_type: str = None) -> List[str]:
        """获取所有资产名称"""
        if asset_type:
            return [asset.asset_name for asset in self.assets.values() 
                    if asset.asset_type == asset_type]
        return [asset.asset_name for asset in self.assets.values()]