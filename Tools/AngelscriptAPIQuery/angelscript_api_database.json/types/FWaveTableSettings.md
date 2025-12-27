# FWaveTableSettings

## 属性

### FilePath
- **类型**: `FFilePath`
- **描述**: File to import

### ChannelIndex
- **类型**: `int`
- **描述**: Index of channel in file to build WaveTable from (wraps if channel is greater than number in file)

### SourceData
- **类型**: `FWaveTableData`
- **描述**: Source data last imported from the source file

### Phase
- **类型**: `float32`
- **描述**: Percent to phase shift of table

### Top
- **类型**: `float32`
- **描述**: Percent to remove from beginning of sampled WaveTable.

### Tail
- **类型**: `float32`
- **描述**: Percent to remove from end of sampled WaveTable.

### FadeIn
- **类型**: `float32`
- **描述**: Percent to fade in over.

### FadeOut
- **类型**: `float32`
- **描述**: Percent to fade out over.

### bNormalize
- **类型**: `bool`
- **描述**: Whether or not to normalize the WaveTable.

### bRemoveOffset
- **类型**: `bool`
- **描述**: Whether or not to remove offset from original file
(analogous to "DC offset" in circuit theory).

## 方法

### opAssign
```angelscript
FWaveTableSettings& opAssign(FWaveTableSettings Other)
```

