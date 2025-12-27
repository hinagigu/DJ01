# AChaosCacheManager

**继承自**: `AActor`

## 属性

### CacheMode
- **类型**: `ECacheMode`
- **描述**: How to use the cache - playback or record

### StartMode
- **类型**: `EStartMode`
- **描述**: How to trigger the cache record or playback, timed will start counting at BeginPlay, Triggered will begin
counting from when the owning cache manager is requested to trigger the cache action
@see AChaosCacheManager::TriggerObservedComponent

### StartTime
- **类型**: `float32`

### ObservedComponents
- **类型**: `TArray<FObservedComponent>`
- **描述**: List of observed objects and their caches

## 方法

### EnablePlayback
```angelscript
void EnablePlayback(int Index, bool bEnable)
```
Enable playback for a specific component using its index in the list of observed component

### EnablePlaybackByCache
```angelscript
void EnablePlaybackByCache(FName InCacheName, bool bEnable)
```
Enable playback for a specific component using its cache name

### ResetAllComponentTransforms
```angelscript
void ResetAllComponentTransforms()
```
Resets all components back to the world space transform they had when the cache for them was originally recorded
if one is available

### ResetSingleTransform
```angelscript
void ResetSingleTransform(int InIndex)
```
Resets the component at the specified index in the observed list back to the world space transform it had when the
cache for it was originally recorded if one is available
@param InIndex Index of the component to reset

### SetCacheCollection
```angelscript
void SetCacheCollection(UChaosCacheCollection InCacheCollection)
```
change the cache collection for this player
if the cache is playing or recording this will have no effect

### SetCurrentTime
```angelscript
void SetCurrentTime(float32 CurrentTime)
```

### TriggerAll
```angelscript
void TriggerAll()
```
Triggers the recording or playback of all observed components

### TriggerComponent
```angelscript
void TriggerComponent(UPrimitiveComponent InComponent)
```
Triggers a component to play or record.
If the cache manager has an observed component entry for InComponent and it is a triggered entry
this will begin the playback or record for that component, otherwise no action is taken.
@param InComponent Component to trigger

### TriggerComponentByCache
```angelscript
void TriggerComponentByCache(FName InCacheName)
```
Triggers a component to play or record.
Searches the observed component list for an entry matching InCacheName and triggers the
playback or recording of the linked observed component
@param InCacheName Cache name to trigger

