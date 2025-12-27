#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJ01 DataAsset Manager - 数据管理器
职责：统一管理配置数据的加载和保存
"""

import json
import os
import sys
from typing import Dict, Any, Optional

# 添加父目录到路径
_parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _parent_dir not in sys.path:
    sys.path.insert(0, _parent_dir)

from config import CONFIG_FILES, ASSET_TYPE_TO_CONFIG


class DataManager:
    """数据管理器"""
    
    def __init__(self):
        self._cache: Dict[str, Dict[str, Any]] = {}
    
    def get_config_path(self, asset_type: str) -> str:
        """获取配置文件路径"""
        config_key = ASSET_TYPE_TO_CONFIG.get(asset_type, asset_type.lower())
        return CONFIG_FILES.get(config_key, "")
    
    def load_assets(self, asset_type: str) -> Dict[str, Dict[str, Any]]:
        """加载指定类型的所有资产"""
        if asset_type in self._cache:
            return self._cache[asset_type]
        
        config_path = self.get_config_path(asset_type)
        if not config_path or not os.path.exists(config_path):
            return {}
        
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # 获取资产数据（兼容不同的键名）
                assets = data.get(asset_type.lower(), {})
                if not assets:
                    assets = data.get("assets", {})
                self._cache[asset_type] = assets
                return assets
        except Exception as e:
            print(f"加载 {asset_type} 配置失败: {e}")
            return {}
    
    def save_assets(self, asset_type: str, assets: Dict[str, Dict[str, Any]]) -> bool:
        """保存指定类型的所有资产"""
        config_path = self.get_config_path(asset_type)
        if not config_path:
            return False
        
        try:
            # 读取现有数据
            existing_data = {}
            if os.path.exists(config_path):
                with open(config_path, 'r', encoding='utf-8') as f:
                    existing_data = json.load(f)
            
            # 更新数据
            existing_data[asset_type.lower()] = assets
            existing_data["version"] = "1.0"
            
            # 确保目录存在
            os.makedirs(os.path.dirname(config_path), exist_ok=True)
            
            # 保存
            with open(config_path, 'w', encoding='utf-8') as f:
                json.dump(existing_data, f, indent=2, ensure_ascii=False)
            
            # 更新缓存
            self._cache[asset_type] = assets
            return True
            
        except Exception as e:
            print(f"保存 {asset_type} 配置失败: {e}")
            return False
    
    def get_asset(self, asset_type: str, asset_name: str) -> Optional[Dict[str, Any]]:
        """获取单个资产"""
        assets = self.load_assets(asset_type)
        return assets.get(asset_name)
    
    def save_asset(self, asset_type: str, asset_name: str, data: Dict[str, Any]) -> bool:
        """保存单个资产"""
        assets = self.load_assets(asset_type)
        assets[asset_name] = data
        return self.save_assets(asset_type, assets)
    
    def delete_asset(self, asset_type: str, asset_name: str) -> bool:
        """删除单个资产"""
        assets = self.load_assets(asset_type)
        if asset_name in assets:
            del assets[asset_name]
            return self.save_assets(asset_type, assets)
        return False
    
    def clear_cache(self, asset_type: str = None):
        """清除缓存"""
        if asset_type:
            self._cache.pop(asset_type, None)
        else:
            self._cache.clear()