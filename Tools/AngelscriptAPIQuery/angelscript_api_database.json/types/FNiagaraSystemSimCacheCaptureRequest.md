# FNiagaraSystemSimCacheCaptureRequest

Message sent from the debugger to a client to request a sim cache capture for a particular component.

## 属性

### ComponentName
- **类型**: `FName`
- **描述**: Name of the component we're going to capture.

### CaptureDelayFrames
- **类型**: `uint`
- **描述**: How many frames to delay capture.

### CaptureFrames
- **类型**: `uint`
- **描述**: How many frames to capture.

## 方法

### opAssign
```angelscript
FNiagaraSystemSimCacheCaptureRequest& opAssign(FNiagaraSystemSimCacheCaptureRequest Other)
```

