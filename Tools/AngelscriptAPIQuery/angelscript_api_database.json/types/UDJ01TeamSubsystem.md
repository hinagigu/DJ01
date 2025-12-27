# UDJ01TeamSubsystem

**继承自**: `UWorldSubsystem`

DJ01团队子系统 - 提供全局团队查询和管理功能
保持简洁，主要提供便捷的静态查询方法

## 方法

### AreObjectsFriendly
```angelscript
bool AreObjectsFriendly(const UObject ObjectA, const UObject ObjectB)
```
判断两个对象是否是友军

### CanObjectAttackObject
```angelscript
bool CanObjectAttackObject(const UObject Attacker, const UObject Target)
```
判断A是否可以攻击B

### CompareTeamRelation
```angelscript
EDJ01TeamRelation CompareTeamRelation(const UObject ObjectA, const UObject ObjectB)
```
比较两个对象的团队关系

### GetObjectTeamConfig
```angelscript
bool GetObjectTeamConfig(const UObject Object, FDJ01TeamConfig& OutTeamConfig)
```
获取对象的团队配置

