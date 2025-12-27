# USkinnedAsset

**继承自**: `UStreamableRenderAsset`

## 方法

### FindSocket
```angelscript
USkeletalMeshSocket FindSocket(FName InSocketName)
```
Find a socket object in this SkeletalMesh by name.
Entering NAME_None will return NULL. If there are multiple sockets with the same name, will return the first one.

### FindSocketInfo
```angelscript
USkeletalMeshSocket FindSocketInfo(FName InSocketName, FTransform& OutTransform, int& OutBoneIndex, int& OutIndex)
```
Find a socket object and associated info in this SkeletalMesh by name.
Entering NAME_None will return NULL. If there are multiple sockets with the same name, will return the first one.
Also returns the index for the socket allowing for future fast access via GetSocketByIndex()
Also returns the socket transform and the bone index (if any)

