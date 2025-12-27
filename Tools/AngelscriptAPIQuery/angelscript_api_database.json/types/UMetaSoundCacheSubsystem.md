# UMetaSoundCacheSubsystem

**继承自**: `UAudioEngineSubsystem`

UMetaSoundCacheSubsystem

## 方法

### PrecacheMetaSound
```angelscript
void PrecacheMetaSound(UMetaSoundSource InMetaSound, int InNumInstances)
```
Builds the requested number of MetaSound operators (asynchronously) and puts them in the pool for playback.
      (If these operators are not yet available when the MetaSound attempts to play, one will be created Independent of this request.)

### RemoveCachedOperatorsForMetaSound
```angelscript
void RemoveCachedOperatorsForMetaSound(UMetaSoundSource InMetaSound)
```
Clear the operator pool of any operators associated with the given MetaSound

### TouchOrPrecacheMetaSound
```angelscript
void TouchOrPrecacheMetaSound(UMetaSoundSource InMetaSound, int InNumInstances)
```
same as PrecacheMetaSound except cached operator that already exists in the cache will be moved to the top instead of building,
      any operators that we couldn't move to the top, will be built.
      (i.e. if 2 operators are already cached and Num Instances is 4, it will construct 2 and move the existing 2 to the top of the cache)

