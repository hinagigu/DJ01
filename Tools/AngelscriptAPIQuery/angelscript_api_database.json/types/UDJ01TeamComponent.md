# UDJ01TeamComponent

**继承自**: `UActorComponent`

DJ01团队组件 - 为Actor提供团队功能的组件
可以挂载到任何需要团队功能的Actor上

## 属性

### OnTeamConfigChanged
- **类型**: `FDJ01TeamConfigChangedDelegate`

### TeamConfig
- **类型**: `FDJ01TeamConfig`

## 方法

### CanAttackActor
```angelscript
bool CanAttackActor(AActor TargetActor)
```

### GetTeamConfiguration
```angelscript
FDJ01TeamConfig GetTeamConfiguration()
```
蓝图访问

### IsFriendlyToActor
```angelscript
bool IsFriendlyToActor(AActor TargetActor)
```

### SetTeamConfiguration
```angelscript
void SetTeamConfiguration(FDJ01TeamConfig NewConfig)
```

