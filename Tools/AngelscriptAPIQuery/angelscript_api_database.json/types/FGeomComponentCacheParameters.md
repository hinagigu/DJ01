# FGeomComponentCacheParameters

## 属性

### CacheMode
- **类型**: `EGeometryCollectionCacheType`
- **描述**: Cache mode, whether disabled, playing or recording

### TargetCache
- **类型**: `UGeometryCollectionCache`
- **描述**: The cache to target when recording or playing

### ReverseCacheBeginTime
- **类型**: `float32`
- **描述**: Cache mode, whether disabled, playing or recording

### SaveCollisionData
- **类型**: `bool`
- **描述**: Whether to buffer collisions during recording

### DoGenerateCollisionData
- **类型**: `bool`
- **描述**: Whether to generate collisions during playback

### CollisionDataSizeMax
- **类型**: `int`
- **描述**: Maximum size of the collision buffer

### DoCollisionDataSpatialHash
- **类型**: `bool`
- **描述**: Spatial hash collision data

### CollisionDataSpatialHashRadius
- **类型**: `float32`
- **描述**: Spatial hash radius for collision data

### MaxCollisionPerCell
- **类型**: `int`
- **描述**: Maximum number of collisions per cell

### SaveBreakingData
- **类型**: `bool`
- **描述**: Whether to buffer breakings during recording

### DoGenerateBreakingData
- **类型**: `bool`
- **描述**: Whether to generate breakings during playback

### BreakingDataSizeMax
- **类型**: `int`
- **描述**: Maximum size of the breaking buffer

### DoBreakingDataSpatialHash
- **类型**: `bool`
- **描述**: Spatial hash breaking data

### BreakingDataSpatialHashRadius
- **类型**: `float32`
- **描述**: Spatial hash radius for breaking data

### MaxBreakingPerCell
- **类型**: `int`
- **描述**: Maximum number of breaking per cell

### SaveTrailingData
- **类型**: `bool`
- **描述**: Whether to buffer trailings during recording

### DoGenerateTrailingData
- **类型**: `bool`
- **描述**: Whether to generate trailings during playback

### TrailingDataSizeMax
- **类型**: `int`
- **描述**: Maximum size of the trailing buffer

### TrailingMinSpeedThreshold
- **类型**: `float32`
- **描述**: Minimum speed to record trailing

### TrailingMinVolumeThreshold
- **类型**: `float32`
- **描述**: Minimum volume to record trailing

## 方法

### opAssign
```angelscript
FGeomComponentCacheParameters& opAssign(FGeomComponentCacheParameters Other)
```

