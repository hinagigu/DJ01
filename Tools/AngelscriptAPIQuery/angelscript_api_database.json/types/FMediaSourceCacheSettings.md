# FMediaSourceCacheSettings

Cache settings to pass to the player.

## 属性

### bOverride
- **类型**: `bool`
- **描述**: Override the default cache settings.
Currently only the ImgMedia player supports these settings.

### TimeToLookAhead
- **类型**: `float32`
- **描述**: The cache will fill up with frames that are up to this time from the current time.
E.g. if this is 0.2, and we are at time index 5 seconds,
then we will fill the cache with frames between 5 seconds and 5.2 seconds.

## 方法

### opAssign
```angelscript
FMediaSourceCacheSettings& opAssign(FMediaSourceCacheSettings Other)
```

