"""
批量查询脚本 - 用于导出和查询 AngelScript API

用法示例:
    python batch_query.py --export                    # 导出完整API数据库
    python batch_query.py --search "GetComponent"    # 搜索API
    python batch_query.py --type "AActor"            # 获取类型详情
    python batch_query.py --list-types               # 列出所有类型
"""

import argparse
import json
import os
from api_query import UnrealAngelScriptClient


def export_database(client: UnrealAngelScriptClient, output_dir: str):
    """导出完整的API数据库"""
    os.makedirs(output_dir, exist_ok=True)
    
    # 导出完整 JSON
    json_path = os.path.join(output_dir, "full_database.json")
    client.export_to_json(json_path)
    
    # 按类型分组导出
    types_dir = os.path.join(output_dir, "types")
    os.makedirs(types_dir, exist_ok=True)
    
    for type_name in client.get_all_types():
        type_info = client.get_type_info(type_name)
        if type_info:
            # 导出 JSON
            safe_name = type_name.replace("::", "_").replace("<", "_").replace(">", "_")
            json_path = os.path.join(types_dir, f"{safe_name}.json")
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(type_info, f, indent=2, ensure_ascii=False)
            
            # 导出 Markdown
            md_path = os.path.join(types_dir, f"{safe_name}.md")
            md_content = client.generate_api_markdown(type_name)
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(md_content)
    
    print(f"已导出 {len(client.get_all_types())} 个类型到 {output_dir}")


def search_and_display(client: UnrealAngelScriptClient, query: str, format_type: str = "table"):
    """搜索并显示结果"""
    results = client.search_api(query)
    
    if format_type == "json":
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        print(f"找到 {len(results)} 个结果:\n")
        for result in results:
            result_type = result['type']
            name = result['name']
            
            if result_type == 'class':
                supertype = result.get('supertype', '')
                print(f"[类] {name}" + (f" : {supertype}" if supertype else ""))
            elif result_type == 'method':
                return_type = result.get('return_type', 'void')
                print(f"[方法] {return_type} {name}()")
            elif result_type == 'property':
                typename = result.get('typename', '')
                print(f"[属性] {typename} {name}")
            
            doc = result.get('documentation', '')
            if doc:
                print(f"        {doc[:80]}..." if len(doc) > 80 else f"        {doc}")


def display_type_info(client: UnrealAngelScriptClient, type_name: str, format_type: str = "markdown"):
    """显示类型详情"""
    type_info = client.get_type_info(type_name)
    
    if not type_info:
        print(f"类型 '{type_name}' 未找到")
        return
    
    if format_type == "json":
        print(json.dumps(type_info, indent=2, ensure_ascii=False))
    else:
        print(client.generate_api_markdown(type_name))


def list_all_types(client: UnrealAngelScriptClient, filter_str: str = None):
    """列出所有类型"""
    types = client.get_all_types()
    
    if filter_str:
        filter_lower = filter_str.lower()
        types = [t for t in types if filter_lower in t.lower()]
    
    print(f"共 {len(types)} 个类型:\n")
    for t in types:
        print(f"  {t}")


def main():
    parser = argparse.ArgumentParser(description="批量查询 Unreal AngelScript API")
    parser.add_argument("--host", default="127.0.0.1", help="Unreal Engine 主机地址")
    parser.add_argument("--port", type=int, default=27099, help="调试端口")
    parser.add_argument("--export", action="store_true", help="导出完整API数据库")
    parser.add_argument("--output", default="./api_export", help="导出输出目录")
    parser.add_argument("--search", type=str, help="搜索API")
    parser.add_argument("--type", type=str, help="获取指定类型详情")
    parser.add_argument("--list-types", action="store_true", help="列出所有类型")
    parser.add_argument("--filter", type=str, help="类型过滤器 (与 --list-types 一起使用)")
    parser.add_argument("--format", choices=["table", "json", "markdown"], default="table", help="输出格式")
    
    args = parser.parse_args()
    
    client = UnrealAngelScriptClient(host=args.host, port=args.port)
    
    if not client.connect():
        print("连接失败")
        return 1
    
    try:
        print("正在获取类型数据库...")
        client.request_debug_database()
        client.receive_database()
        
        if args.export:
            export_database(client, args.output)
        elif args.search:
            search_and_display(client, args.search, args.format)
        elif args.type:
            display_type_info(client, args.type, args.format)
        elif args.list_types:
            list_all_types(client, args.filter)
        else:
            parser.print_help()
            
    finally:
        client.disconnect()
    
    return 0


if __name__ == "__main__":
    exit(main())