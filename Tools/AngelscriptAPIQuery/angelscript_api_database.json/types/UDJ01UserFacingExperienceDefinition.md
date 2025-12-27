# UDJ01UserFacingExperienceDefinition

**继承自**: `UPrimaryDataAsset`

Description of settings used to display experiences in the UI and start a new session

## 属性

### MapID
- **类型**: `FPrimaryAssetId`

### ExperienceID
- **类型**: `FPrimaryAssetId`

### ExtraArgs
- **类型**: `TMap<FString,FString>`

### TileTitle
- **类型**: `FText`

### TileSubTitle
- **类型**: `FText`

### TileDescription
- **类型**: `FText`

### TileIcon
- **类型**: `UTexture2D`

### LoadingScreenWidget
- **类型**: `TSoftClassPtr<UUserWidget>`

### bIsDefaultExperience
- **类型**: `bool`

### bShowInFrontEnd
- **类型**: `bool`

### bRecordReplay
- **类型**: `bool`

### MaxPlayerCount
- **类型**: `int`

## 方法

### CreateHostingRequest
```angelscript
UCommonSession_HostSessionRequest CreateHostingRequest()
```
Create a request object that is used to actually start a session with these settings

