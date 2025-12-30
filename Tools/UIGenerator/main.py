#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UI Generator - Schema 驱动的 UI 生成工具
入口文件
"""

import os
import sys
import tkinter as tk

# 确保模块路径正确
TOOL_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, TOOL_ROOT)


def main():
    """主函数"""
    # 延迟导入以避免循环依赖
    from ui.app import UIGeneratorApp
    
    root = tk.Tk()
    app = UIGeneratorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()