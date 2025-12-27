# UWmfMediaSettings

**继承自**: `UObject`

Settings for the WmfMedia plug-in.

## 属性

### AllowNonStandardCodecs
- **类型**: `bool`
- **描述**: Whether to allow the loading of media that uses non-standard codecs (default = off).

By default, the player will attempt to detect audio and video codecs that
are not supported by the operating system out of the box, but may require
the user to install additional codec packs. Enable this option to skip
this check and allow the usage of non-standard codecs.

### LowLatency
- **类型**: `bool`
- **描述**: Enable low latency processing in the Windows media pipeline (default = off).

When this setting is enabled, the media data is generated with the lowest
possible delay. This might be desirable for certain real-time applications,
but it can negatively affect audio and video quality.

@note This setting is only supported on Windows 8 or newer

### NativeAudioOut
- **类型**: `bool`
- **描述**: Play audio tracks via the operating system's native sound mixer (default = off).

### HardwareAcceleratedVideoDecoding
- **类型**: `bool`
- **描述**: Use hardware accelerated video acceleration (GPU) when possible otherwise fallback to software implementation (CPU), Windows and DX11 only.

