# UAutomationPerformaceHelper

**继承自**: `UObject`

Class for use with functional tests which provides various performance measuring features.
Recording of basic, unintrusive performance stats.
Automatic captures using external CPU and GPU profilers.
Triggering and ending of writing full stats to a file.

## 方法

### BeginRecording
```angelscript
void BeginRecording(FString RecordName, float32 InGPUBudget, float32 InRenderThreadBudget, float32 InGameThreadBudget)
```
Begins recording a new named performance stats record. We start by recording the baseline.

### BeginRecordingBaseline
```angelscript
void BeginRecordingBaseline(FString RecordName)
```
Begins recording a new named performance stats record. We start by recording the baseline

### BeginStatsFile
```angelscript
void BeginStatsFile(FString RecordName)
```
Begins recording stats to a file.

### EndRecording
```angelscript
void EndRecording()
```
Stops recording performance stats.

### EndRecordingBaseline
```angelscript
void EndRecordingBaseline()
```
Stops recording the baseline and moves to the main record.

### EndStatsFile
```angelscript
void EndStatsFile()
```
Ends recording stats to a file.

### IsCurrentRecordWithinGameThreadBudget
```angelscript
bool IsCurrentRecordWithinGameThreadBudget()
```

### IsCurrentRecordWithinGPUBudget
```angelscript
bool IsCurrentRecordWithinGPUBudget()
```

### IsCurrentRecordWithinRenderThreadBudget
```angelscript
bool IsCurrentRecordWithinRenderThreadBudget()
```

### IsRecording
```angelscript
bool IsRecording()
```
Returns true if this stats tracker is currently recording performance stats.

### OnAllTestsComplete
```angelscript
void OnAllTestsComplete()
```
Does any final work needed as all tests are complete.

### OnBeginTests
```angelscript
void OnBeginTests()
```
Does any init work across all tests..

### Sample
```angelscript
void Sample(float32 DeltaSeconds)
```
Adds a sample to the stats counters for the current performance stats record.

### StartCPUProfiling
```angelscript
void StartCPUProfiling()
```
Communicates with external profiler to being a CPU capture.

### StopCPUProfiling
```angelscript
void StopCPUProfiling()
```
Communicates with external profiler to end a CPU capture.

### Tick
```angelscript
void Tick(float32 DeltaSeconds)
```
Begin basic stat recording

### TriggerGPUTraceIfRecordFallsBelowBudget
```angelscript
void TriggerGPUTraceIfRecordFallsBelowBudget()
```
Will trigger a GPU trace next time the current test falls below GPU budget.

### WriteLogFile
```angelscript
void WriteLogFile(FString CaptureDir, FString CaptureExtension)
```
Writes the current set of performance stats records to a csv file in the profiling directory. An additional directory and an extension override can also be used.

