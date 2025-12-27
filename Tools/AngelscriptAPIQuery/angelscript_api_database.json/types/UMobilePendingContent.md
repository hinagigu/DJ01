# UMobilePendingContent

**继承自**: `UMobileInstalledContent`

## 方法

### GetDownloadSize
```angelscript
float32 GetDownloadSize()
```
Get the total download size for this content installation

### GetDownloadSpeed
```angelscript
float32 GetDownloadSpeed()
```
Get the current download speed in megabytes per second. Valid during installation

### GetDownloadStatusText
```angelscript
FText GetDownloadStatusText()
```

### GetInstallProgress
```angelscript
float32 GetInstallProgress()
```
Get the current installation progress. Between 0 and 1 for known progress, or less than 0 for unknown progress

### GetRequiredDiskSpace
```angelscript
float32 GetRequiredDiskSpace()
```
Get the required disk space in megabytes for this content installation

### GetTotalDownloadedSize
```angelscript
float32 GetTotalDownloadedSize()
```
Get the total downloaded size in megabytes. Valid during installation

### StartInstall
```angelscript
void StartInstall(FOnContentInstallSucceeded OnSucceeded, FOnContentInstallFailed OnFailed)
```
Attempt to download and install remote content.
User can choose to mount installed content into the game.
@param       OnSucceeded: Callback on installation success.
@param       OnFailed: Callback on installation fail. Will return error message text and error integer code

