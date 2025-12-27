# USkeletalMeshLODSettings

**继承自**: `UDataAsset`

## 属性

### MinQualityLevelLod
- **类型**: `FPerQualityLevelInt`
- **描述**: Minimum Quality Level LOD to render. Can be overridden per mesh as well as set here for all mesh instances

### MinLod
- **类型**: `FPerPlatformInt`
- **描述**: Minimum LOD to render. Can be overridden per mesh as well as set here for all mesh instances

### DisableBelowMinLodStripping
- **类型**: `FPerPlatformBool`
- **描述**: When true LODs below MinLod will not be stripped during cook.

### bOverrideLODStreamingSettings
- **类型**: `bool`
- **描述**: Whether meshes in this group override default LOD streaming settings.

### bSupportLODStreaming
- **类型**: `FPerPlatformBool`
- **描述**: Whether meshes in this group stream LODs by default

### MaxNumStreamedLODs
- **类型**: `FPerPlatformInt`
- **描述**: Default maximum number of streamed LODs for meshes in this group

### MaxNumOptionalLODs
- **类型**: `FPerPlatformInt`
- **描述**: Default maximum number of optional LODs for meshes in this group (currently, need to be either 0 or > num of LODs below MinLod)

### LODGroups
- **类型**: `TArray<FSkeletalMeshLODGroupSettings>`

