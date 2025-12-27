# FNiagaraOutlinerCaptureSettings

## 属性

### bTriggerCapture
- **类型**: `bool`
- **描述**: Press to trigger a single capture of Niagara data from the connected debugger client.

### CaptureDelayFrames
- **类型**: `uint`
- **描述**: How many frames to delay capture. If gathering performance data, this is how many frames will be collected.

### bGatherPerfData
- **类型**: `bool`

### SimCacheCaptureFrames
- **类型**: `uint`
- **描述**: How many frames capture when capturing a sim cache.

## 方法

### opAssign
```angelscript
FNiagaraOutlinerCaptureSettings& opAssign(FNiagaraOutlinerCaptureSettings Other)
```

