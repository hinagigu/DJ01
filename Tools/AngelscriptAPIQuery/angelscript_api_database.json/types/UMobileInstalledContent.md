# UMobileInstalledContent

**继承自**: `UObject`

## 方法

### GetDiskFreeSpace
```angelscript
float32 GetDiskFreeSpace()
```
Get the disk free space in megabytes where content is installed

### GetInstalledContentSize
```angelscript
float32 GetInstalledContentSize()
```
Get the installed content size in megabytes

### Mount
```angelscript
bool Mount(int PakOrder, FString MountPoint)
```
Mount installed content
@param       PakOrder : Content pak priority
@param       MountPoint : Path to mount the pak at

