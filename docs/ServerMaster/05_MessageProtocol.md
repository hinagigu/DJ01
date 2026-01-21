---
status: todo
progress: 0
milestones: 5
completed: 0
priority: P0
phase: phase1
tags: [protocol, protobuf, phase1]
---

# 05 - 消息协议定义

## 📋 里程碑追踪

| # | 里程碑 | 状态 | 验收标准 |
|---|--------|:----:|----------|
| M1 | 文档理解 | ⬜ | 理解Protobuf消息结构 |
| M2 | Proto文件 | ⬜ | 创建.proto文件 |
| M3 | Go代码生成 | ⬜ | protoc生成Go代码 |
| M4 | C++代码生成 | ⬜ | protoc生成C++代码 |
| M5 | 跨语言验证 | ⬜ | Go序列化 ↔ C++反序列化 一致 |

> **进度**: 0/5 = 0%

---

### M1: 文档理解

- [ ] 理解消息分类
- [ ] 理解各消息字段含义
- [ ] 理解二进制Header设计

**完成日期**: ____

---

### M2: Proto文件

**目标**: `Proto/` 目录

- [ ] 创建 `common.proto` (ServiceAddress, ZoneId)
- [ ] 创建 `service.proto` (Register, Heartbeat)
- [ ] 创建 `game.proto` (Ghost, Transfer)

**验收**: protoc 编译无错误

**完成日期**: ____

---

### M3: Go代码生成

**目标**: `ServerGo/internal/pb/`

- [ ] 安装 protoc-gen-go
- [ ] 编写生成脚本
- [ ] 生成Go代码
- [ ] 编译测试

**验收**: `go build ./...` 成功

**完成日期**: ____

---

### M4: C++代码生成

**目标**: `Source/DJ01/Network/Proto/`

- [ ] 下载protobuf for UE5
- [ ] 生成C++代码
- [ ] 集成到Build.cs
- [ ] 编译测试

**验收**: UE5编译成功

**完成日期**: ____

---

### M5: 跨语言验证

**测试用例**:
- [ ] Go创建消息 → 序列化 → 发送
- [ ] C++接收 → 反序列化 → 字段正确
- [ ] 反向测试

**完成日期**: ____

## 概述

定义系统中所有消息的Protobuf格式，确保Go服务端与UE5客户端/DS的通信一致性。

---

## 目录结构

```
Proto/
├── common.proto         # 通用类型
├── service.proto        # 服务间消息
├── client.proto         # 客户端消息
├── game.proto           # 游戏消息
└── ghost.proto          # Ghost同步消息
```

---

## common.proto - 通用类型

```protobuf
syntax = "proto3";
package dj01;
option go_package = "github.com/xxx/dj01/proto";

// 服务地址 (32位编码)
message ServiceAddress {
    uint32 raw = 1;  // [ServerId:8][Type:8][Index:16]
}

// 服务类型
enum ServiceType {
    SERVICE_INVALID = 0;
    SERVICE_MASTER = 1;
    SERVICE_SWITCHER = 2;
    SERVICE_GATEWAY = 3;
    SERVICE_LOGIN = 4;
    SERVICE_DBPROXY = 5;
    SERVICE_GAS = 16;      // DS
    SERVICE_CHAT = 17;
    SERVICE_MATCH = 18;
}

// 服务状态
enum ServiceStatus {
    STATUS_OFFLINE = 0;
    STATUS_STARTING = 1;
    STATUS_RUNNING = 2;
    STATUS_BUSY = 3;
    STATUS_STOPPING = 4;
}

// 3D向量
message Vector3 {
    float x = 1;
    float y = 2;
    float z = 3;
}

// Zone ID
message ZoneId {
    int32 world_id = 1;   // 世界实例ID
    int32 x = 2;          // Zone X坐标
    int32 y = 3;          // Zone Y坐标
}

// 结果码
enum ResultCode {
    OK = 0;
    ERROR_UNKNOWN = 1;
    ERROR_INVALID_PARAM = 2;
    ERROR_NOT_FOUND = 3;
    ERROR_ALREADY_EXISTS = 4;
    ERROR_PERMISSION_DENIED = 5;
    ERROR_TIMEOUT = 6;
    ERROR_SERVER_BUSY = 7;
}

// 通用响应
message CommonResponse {
    ResultCode code = 1;
    string message = 2;
}
```

---

## service.proto - 服务间消息

```protobuf
syntax = "proto3";
package dj01;
import "common.proto";

// ========== 消息头 ==========
// 注：消息头使用二进制格式，不用Protobuf
// 这里只定义Payload部分

// ========== 服务注册 (0x0010-0x001F) ==========

// DS → Master: 注册请求
message ServiceRegisterReq {
    string host = 1;           // DS IP
    int32 port = 2;            // DS 游戏端口
    ZoneId zone_id = 3;        // 负责的Zone
    int32 max_players = 4;     // 最大玩家数
}

// Master → DS: 注册响应
message ServiceRegisterAck {
    ResultCode code = 1;
    repeated ServiceAddress neighbors = 2;  // 相邻DS列表
}

// DS → Master: 心跳 (含负载信息)
message ServiceHeartbeat {
    float cpu_usage = 1;       // 0-1
    float memory_usage = 2;    // 0-1
    int32 player_count = 3;    // 当前玩家数
    ServiceStatus status = 4;  // 当前状态
}

// ========== 服务发现 (0x0020-0x002F) ==========

// Any → Master: 查询服务
message ServiceQueryReq {
    ServiceType type = 1;      // 查询的服务类型
    ZoneId zone_id = 2;        // 可选：指定Zone
}

// Master → Any: 查询结果
message ServiceQueryResult {
    repeated ServiceInfo services = 1;
}

message ServiceInfo {
    ServiceAddress address = 1;
    string host = 2;
    int32 port = 3;
    ServiceStatus status = 4;
    int32 player_count = 5;
    int32 max_players = 6;
    ZoneId zone_id = 7;
}

// ========== 玩家路由 (0x0030-0x003F) ==========

// Gateway → Master: 选择DS
message ChooseDSReq {
    uint64 player_id = 1;
    int32 scene_id = 2;        // 场景ID
    Vector3 position = 3;      // 目标位置
}

// Master → Gateway: DS信息
message ChooseDSResult {
    ResultCode code = 1;
    string ds_host = 2;
    int32 ds_port = 3;
    string session_token = 4;  // 用于DS验证
    ZoneId zone_id = 5;
}

// ========== 权威转移 (0x0040-0x004F) ==========

// DS-A → Master: 请求转移
message AuthorityTransferReq {
    uint64 player_id = 1;
    ServiceAddress source_ds = 2;
    ZoneId target_zone = 3;
    Vector3 target_position = 4;
}

// Master → DS-A: 转移批准
message AuthorityTransferApproved {
    string transfer_token = 1;
    ServiceAddress target_ds = 2;
    string target_host = 3;
    int32 target_port = 4;
}

// DS-A → DS-B: 传送玩家数据
message PlayerTransferData {
    string transfer_token = 1;
    uint64 player_id = 2;
    bytes player_state = 3;    // 序列化的玩家状态
    Vector3 position = 4;
    Vector3 velocity = 5;
}

// DS → Master: 转移完成
message AuthorityTransferComplete {
    uint64 player_id = 1;
    ServiceAddress new_ds = 2;
    bool success = 3;
}
```

---

## client.proto - 客户端消息

```protobuf
syntax = "proto3";
package dj01;
import "common.proto";

// ========== 登录相关 (0x1001-0x100F) ==========

// Client → Gateway: 登录
message C2G_Login {
    string account = 1;
    string token = 2;          // 从登录服获取的Token
    string device_id = 3;
    string version = 4;        // 客户端版本
}

// Gateway → Client: 登录结果
message G2C_LoginResult {
    ResultCode code = 1;
    uint64 player_id = 2;
    string session_token = 3;
    repeated ServerInfo servers = 4;  // 可选：服务器列表
}

message ServerInfo {
    int32 server_id = 1;
    string name = 2;
    int32 status = 3;          // 0=维护 1=流畅 2=繁忙 3=爆满
    int32 player_count = 4;
}

// ========== 进入场景 (0x1010-0x101F) ==========

// Client → Gateway: 进入场景
message C2G_EnterScene {
    int32 scene_id = 1;
    Vector3 position = 2;      // 可选：指定位置
}

// Gateway → Client: 进入场景结果
message G2C_EnterSceneResult {
    ResultCode code = 1;
    string ds_host = 2;
    int32 ds_port = 3;
    string session_token = 4;
}

// Client → DS: 进入游戏
message C2S_EnterGame {
    string session_token = 1;
}

// DS → Client: 进入游戏结果
message S2C_EnterGameResult {
    ResultCode code = 1;
    uint64 player_id = 2;
    Vector3 position = 3;
    // ... 其他初始化数据
}
```

---

## ghost.proto - Ghost同步消息

```protobuf
syntax = "proto3";
package dj01;
import "common.proto";

// ========== Ghost管理 (0x0300-0x030F) ==========

// DS-A → DS-B: 创建Ghost
message GhostCreateReq {
    uint64 entity_id = 1;      // 实体ID
    int32 entity_type = 2;     // 实体类型 (Player/NPC/...)
    bytes initial_state = 3;   // 初始状态
    Vector3 position = 4;
}

// DS-B → DS-A: 创建响应
message GhostCreateAck {
    uint64 entity_id = 1;
    uint64 ghost_id = 2;       // Ghost在目标DS的ID
    bool success = 3;
}

// DS-A → DS-B: 销毁Ghost
message GhostDestroy {
    uint64 entity_id = 1;
}

// ========== Ghost状态同步 (0x0310-0x031F) ==========

// DS-A → DS-B: 位置更新 (高频)
message GhostPositionUpdate {
    uint64 entity_id = 1;
    Vector3 position = 2;
    Vector3 velocity = 3;
    float yaw = 4;             // 朝向
    uint32 timestamp = 5;      // 服务器时间戳
}

// DS-A → DS-B: 状态更新 (低频)
message GhostStateUpdate {
    uint64 entity_id = 1;
    bytes state_data = 2;      // 序列化的状态数据
    uint32 state_flags = 3;    // 变化的状态标志
}

// DS-A → DS-B: 动画同步
message GhostAnimationUpdate {
    uint64 entity_id = 1;
    int32 montage_id = 2;      // Montage资源ID
    float play_rate = 3;
    float position = 4;        // 播放位置
}

// ========== 权威转移 (0x0320-0x032F) ==========

// DS-A → DS-B: 权威转移请求
message GhostAuthorityTransfer {
    uint64 entity_id = 1;
    bytes full_state = 2;      // 完整状态快照
    Vector3 position = 3;
    Vector3 velocity = 4;
}

// DS-B → DS-A: 权威转移完成
message GhostAuthorityTransferAck {
    uint64 entity_id = 1;
    bool success = 2;
}
```

---

## 消息ID分配总表

| 范围 | 类别 | 说明 |
|------|------|------|
| 0x0001-0x000F | 系统-连接 | 心跳、握手 |
| 0x0010-0x001F | 系统-注册 | 服务注册/注销 |
| 0x0020-0x002F | 系统-发现 | 服务查询 |
| 0x0030-0x003F | 系统-路由 | DS选择 |
| 0x0040-0x004F | 系统-转移 | 权威转移 |
| 0x0300-0x030F | Ghost-管理 | 创建/销毁 |
| 0x0310-0x031F | Ghost-同步 | 状态更新 |
| 0x0320-0x032F | Ghost-转移 | 权威转移 |
| 0x1001-0x100F | 客户端-登录 | 登录/登出 |
| 0x1010-0x101F | 客户端-场景 | 进入/离开 |
| 0x2001-0x200F | 服务端-登录 | 登录响应 |
| 0x2010-0x201F | 服务端-场景 | 场景响应 |

---

## 序列化规范

| 场景 | 格式 | 原因 |
|------|------|------|
| 消息头 | 二进制(固定32字节) | 高效解析 |
| 消息体 | Protobuf | 强类型、跨语言 |
| 复杂状态 | Protobuf嵌套bytes | 灵活扩展 |

---

## 下一步

- `06_SceneSegmentation.md` - 场景分割策略
- `07_GhostEntity.md` - Ghost实体系统