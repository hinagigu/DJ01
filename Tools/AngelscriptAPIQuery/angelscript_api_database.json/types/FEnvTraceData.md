# FEnvTraceData

## 属性

### NavigationFilter
- **类型**: `TSubclassOf<UNavigationQueryFilter>`
- **描述**: navigation filter for tracing

### ProjectDown
- **类型**: `float32`
- **描述**: search height: below point

### ProjectUp
- **类型**: `float32`
- **描述**: search height: above point

### ExtentX
- **类型**: `float32`
- **描述**: shape parameter for trace

### ExtentY
- **类型**: `float32`
- **描述**: shape parameter for trace

### ExtentZ
- **类型**: `float32`
- **描述**: shape parameter for trace

### PostProjectionVerticalOffset
- **类型**: `float32`
- **描述**: this value will be added to resulting location's Z axis. Can be useful when
    projecting points to navigation since navmesh is just an approximation of level
    geometry and items may end up being under collide-able geometry which would
    for example falsify visibility tests.

### TraceChannel
- **类型**: `ETraceTypeQuery`
- **描述**: geometry trace channel

### SerializedChannel
- **类型**: `ECollisionChannel`
- **描述**: geometry trace channel for serialization purposes

### TraceProfileName
- **类型**: `FName`
- **描述**: geometry trace profile

### TraceShape
- **类型**: `EEnvTraceShape`
- **描述**: shape used for geometry tracing

### TraceMode
- **类型**: `EEnvQueryTrace`
- **描述**: shape used for geometry tracing

### bTraceComplex
- **类型**: `bool`

### bOnlyBlockingHits
- **类型**: `bool`

### bCanTraceOnNavMesh
- **类型**: `bool`

### bCanTraceOnGeometry
- **类型**: `bool`

### bCanDisableTrace
- **类型**: `bool`

### bCanProjectDown
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FEnvTraceData& opAssign(FEnvTraceData Other)
```

