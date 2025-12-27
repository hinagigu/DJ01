# __AndroidPermission

## 方法

### AcquirePermissions
```angelscript
UAndroidPermissionCallbackProxy AcquirePermissions(TArray<FString> permissions)
```
try to acquire permissions and return a singleton callback proxy object containing OnPermissionsGranted delegate

### CheckPermission
```angelscript
bool CheckPermission(FString permission)
```
check if the permission is already granted

