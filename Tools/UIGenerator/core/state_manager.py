"""
生成状态管理
"""
import os
import json
from enum import Enum
from typing import List, Optional
from datetime import datetime

from utils.paths import paths


class GenerationStage(Enum):
    """生成阶段"""
    IDLE = "idle"                           # 空闲
    CPP_GENERATED = "cpp_generated"         # C++ 已生成，等待编译
    READY_FOR_BLUEPRINT = "ready_for_bp"    # 可以生成蓝图


class StateManager:
    """生成状态管理器"""
    
    def __init__(self):
        self.stage = GenerationStage.IDLE
        self.pending_schemas: List[str] = []
        self.cpp_generated_time: Optional[datetime] = None
        self._callbacks: list = []
    
    def add_stage_callback(self, callback):
        """添加阶段变化回调"""
        self._callbacks.append(callback)
    
    def set_stage(self, stage: GenerationStage):
        """设置生成阶段"""
        self.stage = stage
        for cb in self._callbacks:
            try:
                cb(stage)
            except:
                pass
    
    def add_pending_schema(self, schema_path: str):
        """添加待处理的 Schema"""
        if schema_path not in self.pending_schemas:
            self.pending_schemas.append(schema_path)
    
    def set_pending_schemas(self, schemas: List[str]):
        """设置待处理的 Schema 列表"""
        self.pending_schemas = schemas.copy()
    
    def clear_pending(self):
        """清空待处理列表"""
        self.pending_schemas.clear()
    
    def mark_cpp_generated(self):
        """标记 C++ 已生成"""
        self.cpp_generated_time = datetime.now()
        self.set_stage(GenerationStage.CPP_GENERATED)
    
    def mark_compiled(self):
        """标记编译完成"""
        self.set_stage(GenerationStage.READY_FOR_BLUEPRINT)
    
    def reset(self):
        """重置状态"""
        self.set_stage(GenerationStage.IDLE)
        self.pending_schemas.clear()
        self.cpp_generated_time = None
    
    def save(self):
        """保存状态到文件"""
        os.makedirs(os.path.dirname(paths.state_file), exist_ok=True)
        
        state = {
            "stage": self.stage.value,
            "pending_schemas": self.pending_schemas,
            "cpp_generated_time": self.cpp_generated_time.isoformat() if self.cpp_generated_time else None
        }
        
        with open(paths.state_file, 'w', encoding='utf-8') as f:
            json.dump(state, f, indent=2)
    
    def load(self) -> bool:
        """从文件加载状态"""
        if not os.path.exists(paths.state_file):
            return False
        
        try:
            with open(paths.state_file, 'r', encoding='utf-8') as f:
                state = json.load(f)
            
            self.stage = GenerationStage(state.get("stage", "idle"))
            self.pending_schemas = state.get("pending_schemas", [])
            
            if state.get("cpp_generated_time"):
                self.cpp_generated_time = datetime.fromisoformat(state["cpp_generated_time"])
            
            # 触发回调
            for cb in self._callbacks:
                try:
                    cb(self.stage)
                except:
                    pass
            
            return True
        except Exception:
            return False