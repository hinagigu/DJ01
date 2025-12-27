# FCrowdAvoidanceConfig

Crowd manager is responsible for handling crowds using Detour (Recast library)

Agents will respect navmesh for all steering and avoidance updates,
but it's slower than AvoidanceManager solution (RVO, cares only about agents)

All agents will operate on the same navmesh data, which will be picked from
navigation system defaults (UNavigationSystemV1::SupportedAgents[0])

To use it, you have to add CrowdFollowingComponent to your agent
(usually: replace class of PathFollowingComponent in AIController by adding
 those lines in controller's constructor

 ACrowdAIController::ACrowdAIController(const FObjectInitializer& ObjectInitializer)
     : Super(ObjectInitializer.SetDefaultSubobjectClass<UCrowdFollowingComponent>(TEXT("PathFollowingComponent")))

 or simply add both components and switch move requests between them)

Actors that should be avoided, but are not being simulated by crowd (like players)
should implement CrowdAgentInterface AND register/unregister themselves with crowd manager:

 UCrowdManager* CrowdManager = UCrowdManager::GetCurrent(this);
 if (CrowdManager)
 {
    CrowdManager->RegisterAgent(this);
 }

 Check flags in CrowdDebugDrawing namespace (CrowdManager.cpp) for debugging options.

## 属性

### VelocityBias
- **类型**: `float32`

### DesiredVelocityWeight
- **类型**: `float32`

### CurrentVelocityWeight
- **类型**: `float32`

### SideBiasWeight
- **类型**: `float32`

### ImpactTimeWeight
- **类型**: `float32`

### ImpactTimeRange
- **类型**: `float32`

### CustomPatternIdx
- **类型**: `uint8`
- **描述**: index in SamplingPatterns array or 0xff for adaptive sampling

### AdaptiveDivisions
- **类型**: `uint8`
- **描述**: adaptive sampling: number of divisions per ring

### AdaptiveRings
- **类型**: `uint8`
- **描述**: adaptive sampling: number of rings

### AdaptiveDepth
- **类型**: `uint8`
- **描述**: adaptive sampling: number of iterations at best velocity

## 方法

### opAssign
```angelscript
FCrowdAvoidanceConfig& opAssign(FCrowdAvoidanceConfig Other)
```

