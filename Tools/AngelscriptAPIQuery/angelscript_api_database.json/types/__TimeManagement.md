# __TimeManagement

## 方法

### Add_FrameNumberFrameNumber
```angelscript
FFrameNumber Add_FrameNumberFrameNumber(FFrameNumber A, FFrameNumber B)
```
Addition (FrameNumber A + FrameNumber B)

### Add_FrameNumberInteger
```angelscript
FFrameNumber Add_FrameNumberInteger(FFrameNumber A, int B)
```
Addition (FrameNumber A + int B)

### FrameNumberToInteger
```angelscript
int FrameNumberToInteger(FFrameNumber InFrameNumber)
```
Converts a FrameNumber to an int32 for use in functions that take int32 frame counts for convenience.

### Conv_FrameRateToInterval
```angelscript
float32 Conv_FrameRateToInterval(FFrameRate InFrameRate)
```
Converts a FrameRate to an interval float representing the frame time in seconds ie: 1/30 returns 0.0333333

### Conv_QualifiedFrameTimeToSeconds
```angelscript
float32 Conv_QualifiedFrameTimeToSeconds(FQualifiedFrameTime InFrameTime)
```
Converts an QualifiedFrameTime to seconds.

### Conv_TimecodeToString
```angelscript
FString Conv_TimecodeToString(FTimecode InTimecode, bool bForceSignDisplay)
```
Converts an Timecode to a string (hh:mm:ss:ff). If bForceSignDisplay then the number sign will always be prepended instead of just when expressing a negative time.

### Divide_FrameNumberInteger
```angelscript
FFrameNumber Divide_FrameNumberInteger(FFrameNumber A, int B)
```
Divide (FrameNumber A / B)

### GetTimecode
```angelscript
FTimecode GetTimecode()
```
Get the current timecode of the engine.

### GetTimecodeFrameRate
```angelscript
FFrameRate GetTimecodeFrameRate()
```
Gets the current timecode frame rate.

### IsValid_Framerate
```angelscript
bool IsValid_Framerate(FFrameRate InFrameRate)
```
Verifies that this is a valid framerate with a non-zero denominator.

### IsValid_MultipleOf
```angelscript
bool IsValid_MultipleOf(FFrameRate InFrameRate, FFrameRate OtherFramerate)
```
Checks if this framerate is an even multiple of another framerate, ie: 60 is a multiple of 30, but 59.94 is not.

### Multiply_FrameNumberInteger
```angelscript
FFrameNumber Multiply_FrameNumberInteger(FFrameNumber A, int B)
```
Multiply (FrameNumber A * B)

### Multiply_SecondsFrameRate
```angelscript
FFrameTime Multiply_SecondsFrameRate(float32 TimeInSeconds, FFrameRate FrameRate)
```
Multiplies a value in seconds against a FrameRate to get a new FrameTime.

### SnapFrameTimeToRate
```angelscript
FFrameTime SnapFrameTimeToRate(FFrameTime SourceTime, FFrameRate SourceRate, FFrameRate SnapToRate)
```
Snaps the given SourceTime to the nearest frame in the specified Destination Framerate. Useful for determining the nearest frame for another resolution. Returns the frame time in the destination frame rate.

### Subtract_FrameNumberFrameNumber
```angelscript
FFrameNumber Subtract_FrameNumberFrameNumber(FFrameNumber A, FFrameNumber B)
```
Subtraction (FrameNumber A - FrameNumber B)

### Subtract_FrameNumberInteger
```angelscript
FFrameNumber Subtract_FrameNumberInteger(FFrameNumber A, int B)
```
Subtraction (FrameNumber A - int B)

### TransformTime
```angelscript
FFrameTime TransformTime(FFrameTime SourceTime, FFrameRate SourceRate, FFrameRate DestinationRate)
```
Converts the specified time from one framerate to another framerate. This is useful for converting between tick resolution and display rate.

