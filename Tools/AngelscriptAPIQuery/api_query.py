"""
Unreal AngelScript API 批量查询工具

该工具利用 VSCode Unreal AngelScript 插件的 Language Server 来批量查询 API 信息。
需要确保 Unreal Engine 正在运行并且启用了 AngelScript 调试端口（默认 27099）。

使用方法:
1. 确保 Unreal Engine 编辑器正在运行
2. 确保安装了 hazelight.unreal-angelscript 扩展
3. 运行此脚本来查询 API

工作原理:
- 直接连接到 Unreal Engine 的调试端口获取类型数据库
- 解析二进制协议获取所有导出的 API 信息
"""

import socket
import struct
import json
import time
from enum import IntEnum
from typing import Optional, List, Dict, Any
from dataclasses import dataclass, field


class MessageType(IntEnum):
    """消息类型枚举，对应 unreal-buffers.ts 中的定义"""
    Diagnostics = 0
    RequestDebugDatabase = 1
    DebugDatabase = 2
    StartDebugging = 3
    StopDebugging = 4
    Pause = 5
    Continue = 6
    RequestCallStack = 7
    CallStack = 8
    ClearBreakpoints = 9
    SetBreakpoint = 10
    HasStopped = 11
    HasContinued = 12
    StepOver = 13
    StepIn = 14
    StepOut = 15
    EngineBreak = 16
    RequestVariables = 17
    Variables = 18
    RequestEvaluate = 19
    Evaluate = 20
    GoToDefinition = 21
    BreakOptions = 22
    RequestBreakFilters = 23
    BreakFilters = 24
    Disconnect = 25
    DebugDatabaseFinished = 26
    AssetDatabaseInit = 27
    AssetDatabase = 28
    AssetDatabaseFinished = 29
    FindAssets = 30
    DebugDatabaseSettings = 31
    PingAlive = 32
    DebugServerVersion = 33
    CreateBlueprint = 34
    ReplaceAssetDefinition = 35
    SetDataBreakpoints = 36
    ClearDataBreakpoints = 37


@dataclass
class Message:
    """二进制消息解析器"""
    msg_type: int
    buffer: bytes
    offset: int = 5  # 跳过消息头(4字节长度 + 1字节类型)
    size: int = 0
    
    def read_int(self) -> int:
        """读取4字节小端整数"""
        value = struct.unpack_from('<i', self.buffer, self.offset)[0]
        self.offset += 4
        return value
    
    def read_byte(self) -> int:
        """读取1字节"""
        value = struct.unpack_from('b', self.buffer, self.offset)[0]
        self.offset += 1
        return value
    
    def read_bool(self) -> bool:
        """读取布尔值"""
        return self.read_int() != 0
    
    def read_string(self) -> str:
        """读取字符串 (支持UTF-8和UTF-16)"""
        num = self.read_int()
        is_ucs2 = num < 0
        if is_ucs2:
            num = -num
        
        if is_ucs2:
            data = self.buffer[self.offset:self.offset + num * 2]
            self.offset += num * 2
            result = data.decode('utf-16-le')
        else:
            data = self.buffer[self.offset:self.offset + num]
            self.offset += num
            result = data.decode('utf-8')
        
        # 移除末尾的空字符
        if result and result[-1] == '\0':
            result = result[:-1]
        
        return result


@dataclass
class APIMethod:
    """API方法信息"""
    name: str
    return_type: str = ""
    args: List[Dict[str, str]] = field(default_factory=list)
    documentation: str = ""
    is_static: bool = False
    is_const: bool = False
    containing_type: str = ""
    namespace: str = ""


@dataclass
class APIProperty:
    """API属性信息"""
    name: str
    typename: str = ""
    documentation: str = ""
    containing_type: str = ""
    namespace: str = ""


@dataclass
class APIType:
    """API类型信息"""
    name: str
    supertype: str = ""
    documentation: str = ""
    methods: List[APIMethod] = field(default_factory=list)
    properties: List[APIProperty] = field(default_factory=list)
    is_enum: bool = False
    is_struct: bool = False
    namespace: str = ""


class UnrealAngelScriptClient:
    """Unreal AngelScript 调试客户端"""
    
    def __init__(self, host: str = "127.0.0.1", port: int = 27099):
        self.host = host
        self.port = port
        self.socket: Optional[socket.socket] = None
        self.pending_buffer = b''
        self.types_database: Dict[str, Any] = {}
        self.database_finished = False
        
    def connect(self) -> bool:
        """连接到 Unreal Engine"""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.settimeout(30)
            self.socket.connect((self.host, self.port))
            print(f"已连接到 Unreal Engine ({self.host}:{self.port})")
            return True
        except Exception as e:
            print(f"连接失败: {e}")
            return False
    
    def disconnect(self):
        """断开连接"""
        if self.socket:
            try:
                # 发送断开消息
                msg = self._build_simple_message(MessageType.Disconnect)
                self.socket.send(msg)
            except:
                pass
            finally:
                self.socket.close()
                self.socket = None
    
    def _build_simple_message(self, msg_type: MessageType) -> bytes:
        """构建简单消息(无payload)"""
        header = struct.pack('<IB', 1, msg_type)  # 4字节长度(1) + 1字节类型
        return header
    
    def request_debug_database(self) -> bool:
        """请求调试数据库"""
        if not self.socket:
            return False
        
        try:
            msg = self._build_simple_message(MessageType.RequestDebugDatabase)
            self.socket.send(msg)
            return True
        except Exception as e:
            print(f"请求调试数据库失败: {e}")
            return False
    
    def _read_messages(self, data: bytes) -> List[Message]:
        """解析接收到的消息"""
        messages = []
        self.pending_buffer += data
        
        while len(self.pending_buffer) >= 5:
            msg_len = struct.unpack_from('<I', self.pending_buffer, 0)[0]
            msg_type = struct.unpack_from('b', self.pending_buffer, 4)[0]
            
            total_size = 5 + msg_len
            if len(self.pending_buffer) >= total_size:
                msg = Message(
                    msg_type=msg_type,
                    buffer=self.pending_buffer[:total_size],
                    size=msg_len
                )
                messages.append(msg)
                self.pending_buffer = self.pending_buffer[total_size:]
            else:
                break
        
        return messages
    
    def receive_database(self, timeout: float = 30.0) -> Dict[str, Any]:
        """接收完整的类型数据库"""
        if not self.socket:
            return {}
        
        start_time = time.time()
        all_types = {}
        
        while not self.database_finished:
            if time.time() - start_time > timeout:
                print("接收数据库超时")
                break
            
            try:
                data = self.socket.recv(65536)
                if not data:
                    break
                
                messages = self._read_messages(data)
                for msg in messages:
                    if msg.msg_type == MessageType.DebugDatabase:
                        db_str = msg.read_string()
                        try:
                            db_obj = json.loads(db_str)
                            # 合并类型信息
                            for key, value in db_obj.items():
                                if key not in all_types:
                                    all_types[key] = value
                                elif isinstance(value, list) and isinstance(all_types[key], list):
                                    all_types[key].extend(value)
                        except json.JSONDecodeError as e:
                            print(f"JSON解析错误: {e}")
                    
                    elif msg.msg_type == MessageType.DebugDatabaseFinished:
                        print("数据库接收完成")
                        self.database_finished = True
                        break
                        
            except socket.timeout:
                continue
            except Exception as e:
                print(f"接收数据错误: {e}")
                break
        
        self.types_database = all_types
        return all_types
    
    def get_all_types(self) -> List[str]:
        """获取所有类型名称"""
        # 数据库的键就是类型名
        return sorted([k for k in self.types_database.keys() if isinstance(self.types_database[k], dict)])
    
    def search_api(self, query: str) -> List[Dict[str, Any]]:
        """搜索 API"""
        results = []
        query_lower = query.lower()
        
        for type_name, type_info in self.types_database.items():
            if not isinstance(type_info, dict):
                continue
                
            # 搜索类型名
            if query_lower in type_name.lower():
                results.append({
                    'type': 'class',
                    'name': type_name,
                    'supertype': type_info.get('inherits', ''),
                    'documentation': type_info.get('doc', '')
                })
            
            # 搜索方法
            for method in type_info.get('methods', []):
                if not isinstance(method, dict):
                    continue
                method_name = method.get('name', '')
                if query_lower in method_name.lower():
                    results.append({
                        'type': 'method',
                        'name': f"{type_name}.{method_name}",
                        'return_type': method.get('return', method.get('returnType', '')),
                        'args': method.get('args', []),
                        'documentation': method.get('doc', '')
                    })
            
            # 搜索属性 - properties 是一个字典，键是属性名，值是 [类型, 标志, 文档]
            properties = type_info.get('properties', {})
            if isinstance(properties, dict):
                for prop_name, prop_data in properties.items():
                    if query_lower in prop_name.lower():
                        # prop_data 格式: [类型名, 标志, 文档说明]
                        prop_type = prop_data[0] if isinstance(prop_data, list) and len(prop_data) > 0 else ''
                        prop_doc = prop_data[2] if isinstance(prop_data, list) and len(prop_data) > 2 else ''
                        results.append({
                            'type': 'property',
                            'name': f"{type_name}.{prop_name}",
                            'typename': prop_type,
                            'documentation': prop_doc
                        })
        
        return results
    
    def get_type_info(self, type_name: str) -> Optional[Dict[str, Any]]:
        """获取指定类型的详细信息"""
        type_info = self.types_database.get(type_name)
        if isinstance(type_info, dict):
            return {'name': type_name, **type_info}
        return None
    
    def export_to_json(self, filepath: str):
        """导出数据库到 JSON 文件"""
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.types_database, f, indent=2, ensure_ascii=False)
        print(f"数据库已导出到: {filepath}")
    
    def generate_api_markdown(self, type_name: str) -> str:
        """生成指定类型的 Markdown 文档"""
        type_info = self.get_type_info(type_name)
        if not type_info:
            return f"类型 '{type_name}' 未找到"
        
        md = f"# {type_name}\n\n"
        
        if type_info.get('inherits'):
            md += f"**继承自**: `{type_info['inherits']}`\n\n"
        
        if type_info.get('doc'):
            md += f"{type_info['doc']}\n\n"
        
        # 属性 - properties 是一个字典，键是属性名，值是 [类型, 标志, 文档]
        properties = type_info.get('properties', {})
        if properties and isinstance(properties, dict):
            md += "## 属性\n\n"
            for prop_name, prop_data in properties.items():
                prop_type = prop_data[0] if isinstance(prop_data, list) and len(prop_data) > 0 else ''
                prop_doc = prop_data[2] if isinstance(prop_data, list) and len(prop_data) > 2 else ''
                md += f"### {prop_name}\n"
                md += f"- **类型**: `{prop_type}`\n"
                if prop_doc:
                    md += f"- **描述**: {prop_doc}\n"
                md += "\n"
        
        # 方法
        methods = type_info.get('methods', [])
        if methods:
            md += "## 方法\n\n"
            for method in methods:
                if not isinstance(method, dict):
                    continue
                name = method.get('name', '')
                return_type = method.get('return', method.get('returnType', 'void'))
                args = method.get('args', [])
                
                args_str = ", ".join([
                    f"{arg.get('type', arg.get('typename', ''))} {arg.get('name', '')}"
                    for arg in args if isinstance(arg, dict)
                ])
                
                md += f"### {name}\n"
                md += f"```angelscript\n{return_type} {name}({args_str})\n```\n"
                if method.get('doc'):
                    md += f"{method.get('doc')}\n"
                md += "\n"
        
        return md


def main():
    """主函数 - 演示批量查询功能"""
    client = UnrealAngelScriptClient()
    
    if not client.connect():
        print("无法连接到 Unreal Engine，请确保:")
        print("1. Unreal Engine 编辑器正在运行")
        print("2. AngelScript 调试端口已启用 (默认 27099)")
        return
    
    try:
        # 请求数据库
        print("正在请求类型数据库...")
        client.request_debug_database()
        
        # 接收数据库
        print("正在接收数据...")
        database = client.receive_database()
        
        if database:
            # 获取所有类型
            types = client.get_all_types()
            print(f"\n找到 {len(types)} 个类型")
            
            # 示例：搜索 API
            print("\n=== 搜索 'Actor' 相关的 API ===")
            results = client.search_api("Actor")
            for result in results[:10]:  # 只显示前10个
                print(f"  [{result['type']}] {result['name']}")
            
            # 导出完整数据库
            export_path = "angelscript_api_database.json"
            client.export_to_json(export_path)
            
            # 生成特定类型的文档
            if types:
                sample_type = types[0]
                md = client.generate_api_markdown(sample_type)
                print(f"\n=== {sample_type} 文档 ===")
                print(md[:500] + "..." if len(md) > 500 else md)
        else:
            print("未收到数据库内容")
            
    finally:
        client.disconnect()
        print("\n已断开连接")


if __name__ == "__main__":
    main()