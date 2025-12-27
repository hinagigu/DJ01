# UEditorSettings

**继承自**: `UObject`

## 属性

### GlobalLocalDDCPath
- **类型**: `FDirectoryPath`
- **描述**: Adjusts the Local Cache location. This affects every project on your computer that uses the UE-LocalDataCachePath environment environment variable override.
This is usually the first location to query for previously built data.

### GlobalSharedDDCPath
- **类型**: `FDirectoryPath`
- **描述**: Adjusts the Shared cache location. This affects every project on your computer that uses the UE-SharedDataCachePath environment variable override.
The Shared Cache location is usually queried if we do't find previously built data in the Local cache. Colleauges should point to the same shared location so that work can be distributed.

### LocalDerivedDataCache
- **类型**: `FDirectoryPath`
- **描述**: Project specific overide for the Local Cache location. The editor must be restarted for changes to take effect.
This will override the 'Global Local DDC Path'.

### SharedDerivedDataCache
- **类型**: `FDirectoryPath`
- **描述**: Project specific overide for the Shared Cache location. The editor must be restarted for changes to take effect.
This will override the 'Global Shared DDC Path'.

### bEnableDDCNotifications
- **类型**: `bool`
- **描述**: Whether to enable any DDC Notifications

### bNotifyUseUnrealCloudDDC
- **类型**: `bool`
- **描述**: Whether to enable the Unreal Cloud DDC notification

### bNotifySetupDDCPath
- **类型**: `bool`
- **描述**: Whether to enable the DDC path notification

### bNotifyEnableS3DD
- **类型**: `bool`
- **描述**: Whether to enable the DDC path notification

### bEnableS3DDC
- **类型**: `bool`
- **描述**: Whether to enable the S3 derived data cache backend

### GlobalS3DDCPath
- **类型**: `FDirectoryPath`
- **描述**: Adjusts the Local Cache location for AWS/S3 downloaded package bundles.
This affects every project on your computer that uses the UE-S3DataCachePath environment variable override.

