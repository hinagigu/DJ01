#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DataAssetManager 打包脚本
使用方法：在此目录运行 python build_exe.py
"""

import os
import subprocess
import sys
import shutil

# 获取当前目录
TOOL_DIR = os.path.dirname(os.path.abspath(__file__))
MAIN_SCRIPT = os.path.join(TOOL_DIR, "main.py")
DIST_DIR = os.path.join(TOOL_DIR, "dist")
BUILD_DIR = os.path.join(TOOL_DIR, "build")

# 需要打包的数据文件/目录
DATA_DIRS = [
    "configs",
    "ue_scripts",
]

def build():
    """执行打包"""
    print("=" * 60)
    print("DataAssetManager 打包工具")
    print("=" * 60)
    
    # 清理旧的构建目录
    for d in [DIST_DIR, BUILD_DIR]:
        if os.path.exists(d):
            print(f"清理: {d}")
            shutil.rmtree(d)
    
    # 构建 --add-data 参数
    add_data_args = []
    for data_dir in DATA_DIRS:
        src = os.path.join(TOOL_DIR, data_dir)
        if os.path.exists(src):
            # Windows 使用分号，Linux/Mac 使用冒号
            add_data_args.extend(["--add-data", f"{src};{data_dir}"])
    
    # PyInstaller 命令
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--name", "DataAssetManager",
        "--onedir",  # 打包成目录（文件更少，启动更快）
        # "--onefile",  # 如果需要单个 exe，取消此行注释并注释上行
        "--windowed",  # 无控制台窗口（GUI 应用）
        "--noconfirm",  # 覆盖已有文件
        "--clean",  # 清理临时文件
        *add_data_args,
        MAIN_SCRIPT,
    ]
    
    print(f"\n执行命令:")
    print(" ".join(cmd))
    print()
    
    # 执行打包
    result = subprocess.run(cmd, cwd=TOOL_DIR)
    
    if result.returncode == 0:
        print("\n" + "=" * 60)
        print("✅ 打包成功!")
        print(f"输出目录: {os.path.join(DIST_DIR, 'DataAssetManager')}")
        print("=" * 60)
        
        # 复制额外文件到输出目录
        output_dir = os.path.join(DIST_DIR, "DataAssetManager")
        
        # 确保 configs 和 ue_scripts 在正确位置
        for data_dir in DATA_DIRS:
            src = os.path.join(TOOL_DIR, data_dir)
            dst = os.path.join(output_dir, data_dir)
            if os.path.exists(src) and not os.path.exists(dst):
                print(f"复制: {data_dir} -> {dst}")
                shutil.copytree(src, dst)
        
        print("\n运行方式: 双击 dist/DataAssetManager/DataAssetManager.exe")
    else:
        print("\n❌ 打包失败!")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(build())