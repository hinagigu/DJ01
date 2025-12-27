# __TraceUtil

## 方法

### GetAllChannels
```angelscript
TArray<FString> GetAllChannels()
```

### GetEnabledChannels
```angelscript
TArray<FString> GetEnabledChannels()
```

### IsChannelEnabled
```angelscript
bool IsChannelEnabled(FString ChannelName)
```

### IsTracing
```angelscript
bool IsTracing()
```

### PauseTracing
```angelscript
bool PauseTracing()
```

### ResumeTracing
```angelscript
bool ResumeTracing()
```

### StartTraceSendTo
```angelscript
bool StartTraceSendTo(FString Target, TArray<FString> Channels)
```

### StartTraceToFile
```angelscript
bool StartTraceToFile(FString FileName, TArray<FString> Channels)
```

### StopTracing
```angelscript
bool StopTracing()
```

### ToggleChannel
```angelscript
bool ToggleChannel(FString ChannelName, bool enabled)
```

### TraceBookmark
```angelscript
void TraceBookmark(FString Name)
```
Traces a bookmark with specified name.

### TraceMarkRegionEnd
```angelscript
void TraceMarkRegionEnd(FString Name)
```
Traces an end event for a region with specified name.

### TraceMarkRegionStart
```angelscript
void TraceMarkRegionStart(FString Name)
```
Traces a begin event for a region with specified name.

