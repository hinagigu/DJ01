---
status: todo
progress: 0
milestones: 5
completed: 0
priority: P0
phase: phase1
tags: [protocol, phase1]
---

# 01 - 服务地址编码规范

## 📋 里程碑追踪

| # | 里程碑 | 状态 | 验收标准 |
|---|--------|:----:|----------|
| M1 | 文档理解 | ⬜ | 能口述地址编码规则 |
| M2 | Go实现 | ⬜ | 编译通过 + 单元测试通过 |
| M3 | UE5实现 | ⬜ | 编译通过 + 单元测试通过 |
| M4 | 跨语言验证 | ⬜ | Go编码 ↔ UE5解码 一致 |
| M5 | 集成测试 | ⬜ | 在Switcher中正确路由 |

> **进度**: 0/5 = 0%

---

### M1: 文档理解

**目标**: 理解32位服务地址编码规范

**验收标准**:
- [ ] 理解 `[ServerId:8][Type:8][Index:16]` 结构
- [ ] 理解各ServiceType含义
- [ ] 理解编码/解码算法

**完成日期**: ____

---

### M2: Go实现

**目标**: `ServerGo/pkg/address/address.go`

**任务**:
- [ ] 创建 `ServerGo/` 项目结构
- [ ] 实现 `ServiceAddress` struct
- [ ] 实现 `Encode()` 方法
- [ ] 实现 `Decode()` 方法
- [ ] 实现 `String()` 方法

**验收标准**:
```bash
cd ServerGo && go test ./pkg/address/... -v
# 全部 PASS
```

**完成日期**: ____

---

### M3: UE5实现

**目标**: `Source/DJ01/Network/Distributed/DJ01ServiceAddress.h/cpp`

**任务**:
- [ ] 创建 `Network/Distributed/` 目录
- [ ] 实现 `FDJ01ServiceAddress` USTRUCT
- [ ] 实现 `Encode()` 静态方法
- [ ] 实现 `GetServerId/Type/Index()` 方法
- [ ] 添加到 `DJ01.Build.cs`

**验收标准**:
```
编译通过 + Automation Test 通过
```

**完成日期**: ____

---

### M4: 跨语言验证

**目标**: 确保Go和UE5编码一致

**测试用例**:
| 输入 | Go结果 | UE5结果 | 一致 |
|------|--------|---------|:----:|
| ServerId=1, Type=0x10, Index=1 | 0x01100001 | ? | ⬜ |
| ServerId=255, Type=0x03, Index=65535 | 0xFF03FFFF | ? | ⬜ |

**完成日期**: ____

---

### M5: 集成测试

**目标**: 在Switcher消息路由中验证

**前置条件**: 02_Switcher M3 完成

**测试用例**:
- [ ] DS发送消息到Master，地址正确解析
- [ ] Master返回消息到DS，地址正确路由

**完成日期**: ____

## 目标

定义一个32位的服务地址编码系统，用于在分布式系统中唯一标识每个服务实例。


---

## 编码格式

```
┌─────────────────────────────────────────────────────────┐
│  Bit 31-24   │  Bit 23-16    │  Bit 15-0              │
│  ServerId    │  ServiceType  │  ServiceIndex          │
│  (8 bit)     │  (8 bit)      │  (16 bit)              │
└─────────────────────────────────────────────────────────┘
```

| 字段 | 位宽 | 范围 | 说明 |
|------|------|------|------|
| ServerId | 8 | 0-255 | 区服ID（1区、2区...） |
| ServiceType | 8 | 0-255 | 服务类型枚举 |
| ServiceIndex | 16 | 0-65535 | 实例索引 |

---

## 服务类型枚举

| 值 | 名称 | 说明 |
|----|------|------|
| 0x00 | Invalid | 无效 |
| 0x01 | Master | 全局协调 |
| 0x02 | Switcher | 消息路由 |
| 0x03 | Gateway | 客户端网关 |
| 0x04 | Login | 登录服务 |
| 0x05 | DBProxy | 数据库代理 |
| 0x10 | GAS | 游戏服(UE5 DS) |
| 0x11 | Chat | 聊天服务 |
| 0x12 | Match | 匹配服务 |
| 0xFE | Broadcast | 广播地址 |
| 0xFF | All | 所有服务 |

---

## Index分配规则

| 范围 | 用途 |
|------|------|
| 0 | 保留(无效) |
| 1-999 | 大世界Zone DS |
| 1000-9999 | 副本DS |
| 10000+ | 临时/活动DS |

---

## 示例

| 地址 | 十六进制 | 含义 |
|------|----------|------|
| 1-Master-1 | 0x01010001 | 1区Master |
| 1-GAS-3 | 0x01100003 | 1区第3个DS |
| 2-Chat-1 | 0x02110001 | 2区聊天服 |

---

## 待实现

### Go侧
- [ ] `pkg/protocol/address.go` - ServiceAddress结构体
- [ ] 编码/解码函数
- [ ] 字符串转换

### UE5侧
- [ ] `FDJ01ServiceAddress` USTRUCT
- [ ] `EDJ01ServiceType` UENUM
- [ ] Blueprint工具函数

### Proto定义
- [ ] `common.proto` 中定义 ServiceAddress 消息

---

## 接口定义

```go
// Go接口 (待实现)
type ServiceAddress uint32

func NewServiceAddress(serverId uint8, svcType ServiceType, index uint16) ServiceAddress
func (a ServiceAddress) ServerId() uint8
func (a ServiceAddress) ServiceType() ServiceType
func (a ServiceAddress) ServiceIndex() uint16
func (a ServiceAddress) String() string
func ParseServiceAddress(s string) (ServiceAddress, error)
```

```cpp
// UE5接口 (待实现)
USTRUCT() struct FDJ01ServiceAddress {
    uint32 RawAddress;
    
    static FDJ01ServiceAddress Make(uint8 ServerId, EDJ01ServiceType Type, uint16 Index);
    uint8 GetServerId() const;
    EDJ01ServiceType GetServiceType() const;
    uint16 GetServiceIndex() const;
    FString ToString() const;
};
```