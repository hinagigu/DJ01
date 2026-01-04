"""
日志工具
"""
import tkinter as tk
from tkinter import scrolledtext
from typing import Optional, Callable
from datetime import datetime


class Logger:
    """日志管理器"""
    
    LEVELS = {
        "info": "ℹ️",
        "warning": "⚠️", 
        "error": "❌",
        "success": "✅",
        "debug": "🔍"
    }
    
    def __init__(self, text_widget: Optional[scrolledtext.ScrolledText] = None):
        self.text_widget = text_widget
        self.callbacks: list[Callable[[str, str], None]] = []
        self._buffer: list[tuple[str, str, datetime]] = []
    
    def set_widget(self, widget: scrolledtext.ScrolledText):
        """设置日志输出控件"""
        self.text_widget = widget
        # 输出缓冲的日志
        for msg, level, _ in self._buffer:
            self._write(msg, level)
        self._buffer.clear()
    
    def add_callback(self, callback: Callable[[str, str], None]):
        """添加日志回调"""
        self.callbacks.append(callback)
    
    def log(self, message: str, level: str = "info"):
        """记录日志"""
        timestamp = datetime.now()
        
        if self.text_widget:
            self._write(message, level)
        else:
            self._buffer.append((message, level, timestamp))
        
        # 触发回调
        for cb in self.callbacks:
            try:
                cb(message, level)
            except:
                pass
    
    def _write(self, message: str, level: str):
        """写入到控件"""
        prefix = self.LEVELS.get(level, "")
        self.text_widget.insert(tk.END, f"{prefix} {message}\n")
        self.text_widget.see(tk.END)
    
    def info(self, message: str):
        self.log(message, "info")
    
    def warning(self, message: str):
        self.log(message, "warning")
    
    def error(self, message: str):
        self.log(message, "error")
    
    def success(self, message: str):
        self.log(message, "success")
    
    def debug(self, message: str):
        self.log(message, "debug")
    
    def separator(self):
        """输出分隔线"""
        self.log("-" * 40, "info")