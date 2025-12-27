# UNiagaraSimCache

**继承自**: `UObject`

## 方法

### GetAttributeCaptureMode
```angelscript
ENiagaraSimCacheAttributeCaptureMode GetAttributeCaptureMode()
```
How were the attributes captured for this sim cache.

### GetEmitterName
```angelscript
FName GetEmitterName(int EmitterIndex)
```
Get the emitter name at the provided index.

### GetEmitterNames
```angelscript
TArray<FName> GetEmitterNames()
```
Returns a list of emitters we have captured in the SimCache.

### GetNumEmitters
```angelscript
int GetNumEmitters()
```
Get number of emitters stored inside the cache.

### GetNumFrames
```angelscript
int GetNumFrames()
```
Get number of frames stored in the cache.

### GetStartSeconds
```angelscript
float32 GetStartSeconds()
```
Get the time the simulation was at when recorded.

### IsCacheValid
```angelscript
bool IsCacheValid()
```
A valid cache is one that contains at least 1 frames worth of data.

### IsEmpty
```angelscript
bool IsEmpty()
```
An empty cache contains no frame data and can not be used

### ReadColorAttribute
```angelscript
void ReadColorAttribute(TArray<FLinearColor>& OutValues, FName AttributeName, FName EmitterName, int FrameIndex)
```
Reads Niagara Color attributes by name from the cache frame and appends them into the OutValues array.
EmitterName - If left blank will return the system simulation attributes.

### ReadFloatAttribute
```angelscript
void ReadFloatAttribute(TArray<float32>& OutValues, FName AttributeName, FName EmitterName, int FrameIndex)
```
Reads Niagara float attributes by name from the cache frame and appends them into the OutValues array.
EmitterName - If left blank will return the system simulation attributes.

### ReadIDAttribute
```angelscript
void ReadIDAttribute(TArray<FNiagaraID>& OutValues, FName AttributeName, FName EmitterName, int FrameIndex)
```
Reads Niagara ID attributes by name from the cache frame and appends them into the OutValues array.
EmitterName - If left blank will return the system simulation attributes.

### ReadIntAttribute
```angelscript
void ReadIntAttribute(TArray<int>& OutValues, FName AttributeName, FName EmitterName, int FrameIndex)
```
Reads Niagara int attributes by name from the cache frame and appends them into the OutValues array.
EmitterName - If left blank will return the system simulation attributes.

### ReadPositionAttribute
```angelscript
void ReadPositionAttribute(TArray<FVector>& OutValues, FName AttributeName, FName EmitterName, bool bLocalSpaceToWorld, int FrameIndex)
```
Reads Niagara Position attributes by name from the cache frame and appends them into the OutValues array.
Local space emitters provide data at local locations unless bLocalSpaceToWorld is true.
EmitterName - If left blank will return the system simulation attributes.
LocalSpaceToWorld - Caches are always stored in the emitters space, i.e. local or world space.  You can set this to false if you want the local position rather than the world position.

### ReadPositionAttributeWithRebase
```angelscript
void ReadPositionAttributeWithRebase(TArray<FVector>& OutValues, FTransform Transform, FName AttributeName, FName EmitterName, int FrameIndex)
```
Reads Niagara Position attributes by name from the cache frame and appends them into the OutValues array.
All attributes read with this method will be re-based from the captured space into the provided transform space,
this will occur even if the cache was not captured with re-basing enabled.
EmitterName - If left blank will return the system simulation attributes.

### ReadQuatAttribute
```angelscript
void ReadQuatAttribute(TArray<FQuat>& OutValues, FName AttributeName, FName EmitterName, bool bLocalSpaceToWorld, int FrameIndex)
```
Reads Niagara Quaternion attributes by name from the cache frame and appends them into the OutValues array.
Local space emitters provide data at local rotation unless bLocalSpaceToWorld is true.
EmitterName - If left blank will return the system simulation attributes.
LocalSpaceToWorld - Caches are always stored in the emitters space, i.e. local or world space.  You can set this to false if you want the local Quat rather than the world Quat.

### ReadQuatAttributeWithRebase
```angelscript
void ReadQuatAttributeWithRebase(TArray<FQuat>& OutValues, FQuat Quat, FName AttributeName, FName EmitterName, int FrameIndex)
```
Reads Niagara Quaternion attributes by name from the cache frame and appends them into the OutValues array.
Only attributes that in the rebase list will be transform into the provided Quat space.  Therefore the cache
must be captured with rebasing enabled to have any impact.
EmitterName - If left blank will return the system simulation attributes.

### ReadVector2Attribute
```angelscript
void ReadVector2Attribute(TArray<FVector2D>& OutValues, FName AttributeName, FName EmitterName, int FrameIndex)
```
Reads Niagara Vec2 attributes by name from the cache frame and appends them into the OutValues array.
EmitterName - If left blank will return the system simulation attributes.

### ReadVector4Attribute
```angelscript
void ReadVector4Attribute(TArray<FVector4>& OutValues, FName AttributeName, FName EmitterName, int FrameIndex)
```
Reads Niagara Vec4 attributes by name from the cache frame and appends them into the OutValues array.
EmitterName - If left blank will return the system simulation attributes.

### ReadVectorAttribute
```angelscript
void ReadVectorAttribute(TArray<FVector>& OutValues, FName AttributeName, FName EmitterName, int FrameIndex)
```
Reads Niagara Vec3 attributes by name from the cache frame and appends them into the OutValues array.
EmitterName - If left blank will return the system simulation attributes.

