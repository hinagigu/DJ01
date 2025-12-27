# UQuartzClockHandle

**继承自**: `UObject`

This class is a BP / Game thread wrapper around FQuartzClockProxy
   (to talk to the underlying clock)

...and inherits from FQuartzTickableObject
   (to listen to the underlying clock)

It can subscribe to Quantized Event & Metronome delegates to synchronize
gameplay & VFX to Quartz events fired from the Audio Engine

## 方法

### GetBeatProgressPercent
```angelscript
float32 GetBeatProgressPercent(EQuartzCommandQuantization QuantizationBoundary, float32 PhaseOffset, float32 MsOffset)
```
Returns the current progress until the next occurrence of the provided musical duration as a float value from 0 (previous beat) to 1 (next beat).
This is useful for indexing into curves to animate parameters to musical time.
Ms and Phase offsets are combined internally.

### GetBeatsPerMinute
```angelscript
float32 GetBeatsPerMinute()
```

### GetCurrentTimestamp
```angelscript
FQuartzTransportTimeStamp GetCurrentTimestamp()
```
Retrieves a timestamp for the clock

### GetDurationOfQuantizationTypeInSeconds
```angelscript
float32 GetDurationOfQuantizationTypeInSeconds(EQuartzCommandQuantization QuantizationType, float32 Multiplier)
```
Returns the duration in seconds of the given Quantization Type

@param The Quantization type to measure
@param The quantity of the Quantization Type to calculate the time of
@return The duration, in seconds, of a multiplier amount of the Quantization Type, or -1 in the case the clock is invalid

### GetEstimatedRunTime
```angelscript
float32 GetEstimatedRunTime()
```
Returns the amount of time, in seconds, the clock has been running. Caution: due to latency, this will not be perfectly accurate

### GetMillisecondsPerTick
```angelscript
float32 GetMillisecondsPerTick()
```
Metronome getters

### GetSecondsPerTick
```angelscript
float32 GetSecondsPerTick()
```

### GetThirtySecondNotesPerMinute
```angelscript
float32 GetThirtySecondNotesPerMinute()
```

### GetTicksPerSecond
```angelscript
float32 GetTicksPerSecond()
```

### IsClockRunning
```angelscript
bool IsClockRunning()
```

### NotifyOnQuantizationBoundary
```angelscript
void NotifyOnQuantizationBoundary(FQuartzQuantizationBoundary InQuantizationBoundary, FOnQuartzCommandEventBP InDelegate, float32 InMsOffset)
```

### PauseClock
```angelscript
void PauseClock(UQuartzClockHandle& ClockHandle)
```

### ResetTransport
```angelscript
void ResetTransport(FOnQuartzCommandEventBP InDelegate)
```

### ResetTransportQuantized
```angelscript
void ResetTransportQuantized(FQuartzQuantizationBoundary InQuantizationBoundary, FOnQuartzCommandEventBP InDelegate, UQuartzClockHandle& ClockHandle)
```

### ResumeClock
```angelscript
void ResumeClock(UQuartzClockHandle& ClockHandle)
```

### SetBeatsPerMinute
```angelscript
void SetBeatsPerMinute(FQuartzQuantizationBoundary QuantizationBoundary, FOnQuartzCommandEventBP Delegate, UQuartzClockHandle& ClockHandle, float32 BeatsPerMinute)
```

### SetMillisecondsPerTick
```angelscript
void SetMillisecondsPerTick(FQuartzQuantizationBoundary QuantizationBoundary, FOnQuartzCommandEventBP Delegate, UQuartzClockHandle& ClockHandle, float32 MillisecondsPerTick)
```
Metronome Alteration (setters)

### SetSecondsPerTick
```angelscript
void SetSecondsPerTick(FQuartzQuantizationBoundary QuantizationBoundary, FOnQuartzCommandEventBP Delegate, UQuartzClockHandle& ClockHandle, float32 SecondsPerTick)
```

### SetThirtySecondNotesPerMinute
```angelscript
void SetThirtySecondNotesPerMinute(FQuartzQuantizationBoundary QuantizationBoundary, FOnQuartzCommandEventBP Delegate, UQuartzClockHandle& ClockHandle, float32 ThirtySecondsNotesPerMinute)
```

### SetTicksPerSecond
```angelscript
void SetTicksPerSecond(FQuartzQuantizationBoundary QuantizationBoundary, FOnQuartzCommandEventBP Delegate, UQuartzClockHandle& ClockHandle, float32 TicksPerSecond)
```

### StartClock
```angelscript
void StartClock(UQuartzClockHandle& ClockHandle)
```
Clock manipulation

### StartOtherClock
```angelscript
void StartOtherClock(FName OtherClockName, FQuartzQuantizationBoundary InQuantizationBoundary, FOnQuartzCommandEventBP InDelegate)
```
"other" clock manipulation

### StopClock
```angelscript
void StopClock(bool CancelPendingEvents, UQuartzClockHandle& ClockHandle)
```

### SubscribeToAllQuantizationEvents
```angelscript
void SubscribeToAllQuantizationEvents(FOnQuartzMetronomeEventBP OnQuantizationEvent, UQuartzClockHandle& ClockHandle)
```

### SubscribeToQuantizationEvent
```angelscript
void SubscribeToQuantizationEvent(EQuartzCommandQuantization InQuantizationBoundary, FOnQuartzMetronomeEventBP OnQuantizationEvent, UQuartzClockHandle& ClockHandle)
```
Metronome subscription

### UnsubscribeFromAllTimeDivisions
```angelscript
void UnsubscribeFromAllTimeDivisions(UQuartzClockHandle& ClockHandle)
```

### UnsubscribeFromTimeDivision
```angelscript
void UnsubscribeFromTimeDivision(EQuartzCommandQuantization InQuantizationBoundary, UQuartzClockHandle& ClockHandle)
```

