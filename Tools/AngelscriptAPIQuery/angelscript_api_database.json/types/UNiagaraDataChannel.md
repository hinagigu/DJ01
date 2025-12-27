# UNiagaraDataChannel

**继承自**: `UObject`

## 属性

### ChannelVariables
- **类型**: `TArray<FNiagaraDataChannelVariable>`
- **描述**: The variables that define the data contained in this Data Channel.

### bKeepPreviousFrameData
- **类型**: `bool`
- **描述**: If true, we keep our previous frame's data. This comes at a memory and performance cost but allows users to avoid tick order dependency by reading last frame's data. Some users will prefer a frame of latency to tick order dependency.

### bEnforceTickGroupReadWriteOrder
- **类型**: `bool`
- **描述**: If true we ensure that all writes happen in or before the Tick Group specified in EndWriteTickGroup and that all reads happen in tick groups after this.

### FinalWriteTickGroup
- **类型**: `ETickingGroup`
- **描述**: The final tick group that this data channel can be written to.

