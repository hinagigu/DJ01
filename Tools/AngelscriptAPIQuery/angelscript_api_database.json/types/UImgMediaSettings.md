# UImgMediaSettings

**继承自**: `UObject`

Settings for the ImgMedia module.

## 属性

### DefaultFrameRate
- **类型**: `FFrameRate`
- **描述**: Default frame rate to use if none was specified in image sequence or media source (default = 1/24).

### BandwidthThrottlingEnabled
- **类型**: `bool`
- **描述**: If there is not enough bandwidth to play the media, then lower it (for example by skipping frames) to try and get playback.

### CacheBehindPercentage
- **类型**: `float32`
- **描述**: Percentage of cache to use for frames behind the play head (default = 25%).

### CacheSizeGB
- **类型**: `float32`
- **描述**: Maximum size of the look-ahead cache (in GB; default = 1 GB).

### CacheThreads
- **类型**: `int`
- **描述**: Maximum number of image caching threads to use (0 = number of cores, default = 2).

### CacheThreadStackSizeKB
- **类型**: `int`
- **描述**: Size of the stack for each caching thread (in kB; default = 128).

### GlobalCacheSizeGB
- **类型**: `float32`
- **描述**: Maximum size of the global look-ahead cache (in GB; default = 1 GB). Must be greater or equal to CacheSizeGB.

### UseGlobalCache
- **类型**: `bool`
- **描述**: Whether to use the global cache or not.

### ExrDecoderThreads
- **类型**: `uint`
- **描述**: Number of worker threads to use when decoding EXR images (0 = auto).

### DefaultProxy
- **类型**: `FString`
- **描述**: Name of default media source proxy URLs (default = 'proxy').

Image sequence media sources may contain more than one media source URL. Additional
URLs are called media source proxies, and they are generally used for switching to
lower resolution media content for improved performance during development and testing.

Each proxy URL has a name associated with it, such as 'proxy', 'lowres', or any
other user defined tag. It is up to the media source to interpret this value and
map it to a media source URL. For example, a media source consisting of a sequence
of uncompressed images may use a proxy name as the name of the sub-directory that
contains proxy content, such as a low-res version of the image sequence.

When default proxies are enabled via the UseDefaultProxy setting, media players
will first try to locate the proxy content identified by the DefaultProxy tag.
If no such proxy content is available, they will fall back to the media source's
default URL.

@see UseDefaultProxy

### UseDefaultProxy
- **类型**: `bool`
- **描述**: Whether to enable image sequence proxies (default = false).

Image sequence media sources may contain more than one media source URL. Additional
URLs are called media source proxies, and they are generally used for switching to
lower resolution media content for improved performance during development and testing.

Each proxy URL has a name associated with it, such as 'proxy', 'lowres', or any
other user defined tag. It is up to the media source to interpret this value and
map it to a media source URL. For example, a media source consisting of a sequence
of uncompressed images may use a proxy name as the name of the sub-directory that
contains proxy content, such as a low-res version of the image sequence.

When default proxies are enabled via the UseDefaultProxy setting, media players
will first try to locate the proxy content identified by the DefaultProxy tag.
If no such proxy content is available, they will fall back to the media source's
default URL.

@see DefaultProxy

