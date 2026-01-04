"""
Dialog components for UI Generator
"""
import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from typing import Optional, Callable


class CompileReminderDialog:
    """编译提醒对话框"""
    
    def __init__(self, parent: tk.Tk, project_root: str):
        self.parent = parent
        self.project_root = project_root
        self.on_compile: Optional[Callable[[], None]] = None
        
        self.dialog: Optional[tk.Toplevel] = None
    
    def show(self):
        """显示对话框"""
        self.dialog = tk.Toplevel(self.parent)
        self.dialog.title("⚠️ 需要编译")
        self.dialog.geometry("500x320")
        self.dialog.transient(self.parent)
        self.dialog.grab_set()
        
        # 居中
        self.dialog.update_idletasks()
        x = self.parent.winfo_x() + (self.parent.winfo_width() - 500) // 2
        y = self.parent.winfo_y() + (self.parent.winfo_height() - 320) // 2
        self.dialog.geometry(f"+{x}+{y}")
        
        # 内容
        frame = ttk.Frame(self.dialog, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(
            frame, 
            text="⚠️ C++ 代码已生成，请编译项目！", 
            font=("", 14, "bold")
        ).pack(pady=(0, 15))
        
        info_text = """C++ 基类代码已生成到项目的 Source 目录。

在生成 Widget Blueprint 之前，需要先编译这些 C++ 代码：

方法1：点击下方 "🔧 立即编译" 按钮
  • 工具将自动调用 UnrealBuildTool 进行编译

方法2：在 UE 编辑器中
  • 点击 "Compile" 按钮或按 Ctrl+Alt+F11

方法3：在 IDE 中
  • Visual Studio: 按 Ctrl+Shift+B
  • Rider: 按 Ctrl+Shift+F9"""
        
        text = tk.Text(frame, height=13, font=("", 10), wrap=tk.WORD)
        text.pack(fill=tk.BOTH, expand=True, pady=10)
        text.insert("1.0", info_text)
        text.config(state=tk.DISABLED)
        
        # 按钮
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(fill=tk.X)
        
        ttk.Button(
            btn_frame, text="知道了", 
            command=self.dialog.destroy
        ).pack(side=tk.RIGHT, padx=5)
        
        ttk.Button(
            btn_frame, text="🔧 立即编译", 
            command=self._start_compile
        ).pack(side=tk.RIGHT, padx=5)
        
        ttk.Button(
            btn_frame, text="📂 打开项目", 
            command=lambda: os.startfile(self.project_root)
        ).pack(side=tk.RIGHT, padx=5)
    
    def _start_compile(self):
        self.dialog.destroy()
        if self.on_compile:
            self.on_compile()


class EngineSelectDialog:
    """引擎选择对话框"""
    
    @staticmethod
    def show(parent: tk.Tk) -> Optional[str]:
        """显示对话框并返回选择的引擎目录"""
        result = messagebox.askyesnocancel(
            "未找到 UE 引擎",
            "未能自动检测到 Unreal Engine 安装路径。\n\n"
            "是 = 手动选择引擎目录\n"
            "否 = 手动在 IDE 中编译\n"
            "取消 = 返回",
            parent=parent
        )
        
        if result is True:
            engine_dir = filedialog.askdirectory(
                title="选择 UE 引擎根目录",
                parent=parent
            )
            return engine_dir if engine_dir else None
        elif result is False:
            return "MANUAL"
        else:
            return None


class ManualCompileDialog:
    """手动编译确认对话框"""
    
    @staticmethod
    def show(parent: tk.Tk) -> bool:
        """显示对话框，返回用户是否确认编译完成"""
        return messagebox.askyesno(
            "手动编译模式",
            "请在 UE 编辑器或 IDE 中手动编译项目。\n\n"
            "编译方法:\n"
            "• UE 编辑器: 点击 Compile 按钮或 Ctrl+Alt+F11\n"
            "• Visual Studio: Ctrl+Shift+B\n"
            "• Rider: Ctrl+Shift+F9\n\n"
            "编译完成后点击 '是'。",
            parent=parent
        )


class NewSchemaDialog:
    """New schema dialog with template selection"""
    
    def __init__(self, parent: tk.Tk, templates: list):
        self.parent = parent
        self.templates = templates
        self.result: Optional[tuple] = None
    
    def show(self) -> Optional[tuple]:
        """Show dialog and return (template_name, widget_name) or None"""
        dialog = tk.Toplevel(self.parent)
        dialog.title("New Schema")
        dialog.geometry("450x280")
        dialog.transient(self.parent)
        dialog.grab_set()
        
        # Center
        dialog.update_idletasks()
        x = self.parent.winfo_x() + (self.parent.winfo_width() - 450) // 2
        y = self.parent.winfo_y() + (self.parent.winfo_height() - 280) // 2
        dialog.geometry(f"+{x}+{y}")
        
        frame = ttk.Frame(dialog, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        ttk.Label(frame, text="Create New Widget Schema", font=("", 12, "bold")).pack(pady=(0, 15))
        
        # Template selection
        ttk.Label(frame, text="Select Template:").pack(anchor=tk.W)
        
        template_var = tk.StringVar(value=self.templates[0] if self.templates else "")
        template_combo = ttk.Combobox(frame, textvariable=template_var, 
                                      values=self.templates, state='readonly', width=40)
        template_combo.pack(fill=tk.X, pady=(0, 15))
        
        # Template description
        desc_var = tk.StringVar(value="")
        desc_label = ttk.Label(frame, textvariable=desc_var, foreground="gray", wraplength=400)
        desc_label.pack(fill=tk.X, pady=(0, 15))
        
        # Widget name
        ttk.Label(frame, text="Widget Name (e.g. DJ01HealthBar):").pack(anchor=tk.W)
        name_var = tk.StringVar(value="DJ01MyWidget")
        name_entry = ttk.Entry(frame, textvariable=name_var)
        name_entry.pack(fill=tk.X, pady=(0, 15))
        name_entry.select_range(0, tk.END)
        name_entry.focus_set()
        
        # Update description on template change
        template_descriptions = {
            "Empty Widget": "Basic empty widget with a CanvasPanel root.",
            "HUD Element": "HUD element with background image and content box.",
            "Health Bar": "Health bar with progress bar and text, bound to ReSources BindingSet.",
            "Menu Screen": "Full screen menu with CommonActivatableWidget and input handling.",
            "Popup Dialog": "Modal popup dialog with title, message and buttons."
        }
        
        def update_desc(*args):
            template = template_var.get()
            desc_var.set(template_descriptions.get(template, ""))
        
        template_var.trace('w', update_desc)
        update_desc()  # Initial update
        
        # Buttons
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(fill=tk.X, pady=(10, 0))
        
        def create():
            name = name_var.get().strip()
            if not name:
                messagebox.showwarning("Invalid Name", "Please enter a widget name.", parent=dialog)
                return
            if not name[0].isupper():
                messagebox.showwarning("Invalid Name", "Widget name should start with uppercase letter.", parent=dialog)
                return
            
            self.result = (template_var.get(), name)
            dialog.destroy()
        
        def cancel():
            self.result = None
            dialog.destroy()
        
        ttk.Button(btn_frame, text="Cancel", command=cancel).pack(side=tk.RIGHT, padx=5)
        ttk.Button(btn_frame, text="Create", command=create).pack(side=tk.RIGHT)
        
        # Enter key to create
        dialog.bind('<Return>', lambda e: create())
        dialog.bind('<Escape>', lambda e: cancel())
        
        dialog.wait_window()
        return self.result


class SettingsDialog:
    """Settings dialog"""
    
    def __init__(self, parent: tk.Tk):
        self.parent = parent
        self.result: dict = {}
    
    def show(self, current_settings: dict) -> Optional[dict]:
        """显示设置对话框"""
        dialog = tk.Toplevel(self.parent)
        dialog.title("⚙️ 设置")
        dialog.geometry("450x300")
        dialog.transient(self.parent)
        dialog.grab_set()
        
        # 居中
        dialog.update_idletasks()
        x = self.parent.winfo_x() + (self.parent.winfo_width() - 450) // 2
        y = self.parent.winfo_y() + (self.parent.winfo_height() - 300) // 2
        dialog.geometry(f"+{x}+{y}")
        
        frame = ttk.Frame(dialog, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)
        
        # 引擎路径
        ttk.Label(frame, text="UE 引擎路径:").pack(anchor=tk.W)
        
        engine_frame = ttk.Frame(frame)
        engine_frame.pack(fill=tk.X, pady=(0, 15))
        
        engine_var = tk.StringVar(value=current_settings.get('engine_dir', ''))
        engine_entry = ttk.Entry(engine_frame, textvariable=engine_var)
        engine_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        def browse_engine():
            path = filedialog.askdirectory(title="选择引擎目录", parent=dialog)
            if path:
                engine_var.set(path)
        
        ttk.Button(engine_frame, text="浏览...", command=browse_engine).pack(side=tk.RIGHT, padx=(5, 0))
        
        # 默认输出路径
        ttk.Label(frame, text="默认 C++ 输出路径:").pack(anchor=tk.W)
        output_var = tk.StringVar(value=current_settings.get('output_path', 'Source/DJ01/UI/Generated'))
        ttk.Entry(frame, textvariable=output_var).pack(fill=tk.X, pady=(0, 15))
        
        # 默认蓝图路径
        ttk.Label(frame, text="默认蓝图路径:").pack(anchor=tk.W)
        bp_var = tk.StringVar(value=current_settings.get('blueprint_path', '/Game/UI/Generated'))
        ttk.Entry(frame, textvariable=bp_var).pack(fill=tk.X, pady=(0, 15))
        
        # 按钮
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(fill=tk.X, pady=(10, 0))
        
        def save():
            self.result = {
                'engine_dir': engine_var.get(),
                'output_path': output_var.get(),
                'blueprint_path': bp_var.get()
            }
            dialog.destroy()
        
        def cancel():
            self.result = {}
            dialog.destroy()
        
        ttk.Button(btn_frame, text="取消", command=cancel).pack(side=tk.RIGHT, padx=5)
        ttk.Button(btn_frame, text="保存", command=save).pack(side=tk.RIGHT)
        
        dialog.wait_window()
        return self.result if self.result else None