# UQuartzSubsystem

**继承自**: `UTickableWorldSubsystem`

## 方法

### CreateNewClock
```angelscript
UQuartzClockHandle CreateNewClock(FName ClockName, FQuartzClockSettings InSettings, bool bOverrideSettingsIfClockExists, bool bUseAudioEngineClockManager)
```
Clock Creation
create a new clock (or return handle if clock already exists)

### DeleteClockByHandle
```angelscript
void DeleteClockByHandle(UQuartzClockHandle& InClockHandle)
```
delete an existing clock given its clock handle

### DeleteClockByName
```angelscript
void DeleteClockByName(FName ClockName)
```
delete an existing clock given its name

### DoesClockExist
```angelscript
bool DoesClockExist(FName ClockName)
```
returns true if the clock exists

### GetAudioRenderThreadToGameThreadAverageLatency
```angelscript
float32 GetAudioRenderThreadToGameThreadAverageLatency()
```
latency data (Audio Render Thread -> Game thread)

### GetAudioRenderThreadToGameThreadMaxLatency
```angelscript
float32 GetAudioRenderThreadToGameThreadMaxLatency()
```

### GetAudioRenderThreadToGameThreadMinLatency
```angelscript
float32 GetAudioRenderThreadToGameThreadMinLatency()
```

### GetCurrentClockTimestamp
```angelscript
FQuartzTransportTimeStamp GetCurrentClockTimestamp(FName InClockName)
```
Retrieves a timestamp for the clock

### GetDurationOfQuantizationTypeInSeconds
```angelscript
float32 GetDurationOfQuantizationTypeInSeconds(FName ClockName, EQuartzCommandQuantization QuantizationType, float32 Multiplier)
```
Returns the duration in seconds of the given Quantization Type

### GetEstimatedClockRunTime
```angelscript
float32 GetEstimatedClockRunTime(FName InClockName)
```
Returns the amount of time, in seconds, the clock has been running. Caution: due to latency, this will not be perfectly accurate

### GetGameThreadToAudioRenderThreadAverageLatency
```angelscript
float32 GetGameThreadToAudioRenderThreadAverageLatency()
```
latency data (Game thread -> Audio Render Thread)

### GetGameThreadToAudioRenderThreadMaxLatency
```angelscript
float32 GetGameThreadToAudioRenderThreadMaxLatency()
```

### GetGameThreadToAudioRenderThreadMinLatency
```angelscript
float32 GetGameThreadToAudioRenderThreadMinLatency()
```

### GetHandleForClock
```angelscript
UQuartzClockHandle GetHandleForClock(FName ClockName)
```
get handle for existing clock

### GetRoundTripAverageLatency
```angelscript
float32 GetRoundTripAverageLatency()
```
latency data (Round trip)

### GetRoundTripMaxLatency
```angelscript
float32 GetRoundTripMaxLatency()
```

### GetRoundTripMinLatency
```angelscript
float32 GetRoundTripMinLatency()
```

### IsClockRunning
```angelscript
bool IsClockRunning(FName ClockName)
```
returns true if the clock is running

### IsQuartzEnabled
```angelscript
bool IsQuartzEnabled()
```

### SetQuartzSubsystemTickableWhenPaused
```angelscript
void SetQuartzSubsystemTickableWhenPaused(bool bInTickableWhenPaused)
```

