# __DJ01Team

## 方法

### AreActorsFriendly
```angelscript
bool AreActorsFriendly(AActor ActorA, AActor ActorB)
```

### AreConfigsFriendly
```angelscript
bool AreConfigsFriendly(FDJ01TeamConfig ConfigA, FDJ01TeamConfig ConfigB)
```

### AreConfigsHostile
```angelscript
bool AreConfigsHostile(FDJ01TeamConfig ConfigA, FDJ01TeamConfig ConfigB)
```

### CanActorAttackActor
```angelscript
bool CanActorAttackActor(AActor Attacker, AActor Target)
```

### CanConfigAttackTeam
```angelscript
bool CanConfigAttackTeam(FDJ01TeamConfig AttackerConfig, EDJ01Team TargetTeam)
```
团队关系判断

### GetActorTeamConfig
```angelscript
bool GetActorTeamConfig(AActor Actor, FDJ01TeamConfig& OutConfig)
```
Actor级别的团队操作

### MakeFriendlyNPCConfig
```angelscript
FDJ01TeamConfig MakeFriendlyNPCConfig()
```

### MakeMonsterTeamConfig
```angelscript
FDJ01TeamConfig MakeMonsterTeamConfig()
```

### MakeNeutralConfig
```angelscript
FDJ01TeamConfig MakeNeutralConfig()
```

### MakePlayerTeamConfig
```angelscript
FDJ01TeamConfig MakePlayerTeamConfig()
```
创建预设团队配置

### SetActorTeamConfig
```angelscript
void SetActorTeamConfig(AActor Actor, FDJ01TeamConfig NewConfig)
```

### TeamConfigToString
```angelscript
FString TeamConfigToString(FDJ01TeamConfig Config)
```
工具函数

### TeamEnumToString
```angelscript
FString TeamEnumToString(EDJ01Team Team)
```

