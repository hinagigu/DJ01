# FCacheRecorderProjectParameters

## 属性

### DefaultSlate
- **类型**: `FString`
- **描述**: The default name to use for the Slate information

### bCacheTrackRecorderControlsClockTime
- **类型**: `bool`
- **描述**: If true then take recorder will control the sequencer timing when recording with a fixed editor time step. The delta time is derived by the sequence's target frame rate.
This is useful when recording cache data where frame accuracy is important (e.g. Niagara systems), but should be set to false when dealing with data from external sources (e.g. LiveLink).

### RecordingClockSource
- **类型**: `EUpdateClockSource`
- **描述**: The clock source to use when recording

### bStartAtCurrentTimecode
- **类型**: `bool`
- **描述**: If enabled, track sections will start at the current timecode. Otherwise, 0.

### bRecordTimecode
- **类型**: `bool`
- **描述**: If enabled, timecode will be recorded into each actor track

### bShowNotifications
- **类型**: `bool`
- **描述**: Whether to show notification windows or not when recording

## 方法

### opAssign
```angelscript
FCacheRecorderProjectParameters& opAssign(FCacheRecorderProjectParameters Other)
```

