# __NiagaraDataChannel

## 方法

### GetDataChannelElementCount
```angelscript
int GetDataChannelElementCount(const UNiagaraDataChannelAsset Channel, FNiagaraDataChannelSearchParameters SearchParams, bool bReadPreviousFrame)
```
Returns the number of readable elements in the given data channel

@param WorldContextObject    World to execute in
@param Channel                               The channel to read from
@param SearchParams                  Parameters used when retrieving a specific set of Data Channel Data to read or write like the islands data channel type.
@param bReadPreviousFrame    True if this reader will read the previous frame's data. If false, we read the current frame.
                                                             Reading the current frame allows for zero latency reads, but any data elements that are generated after this reader is used are missed.
                                                             Reading the previous frame's data introduces a frame of latency but ensures we never miss any data as we have access to the whole frame.

### ReadFromNiagaraDataChannel
```angelscript
UNiagaraDataChannelReader ReadFromNiagaraDataChannel(const UNiagaraDataChannelAsset Channel, FNiagaraDataChannelSearchParameters SearchParams, bool bReadPreviousFrame)
```
Initializes and returns the Niagara Data Channel reader for the given data channel.

@param WorldContextObject    World to execute in
@param Channel                               The channel to read from
@param SearchParams                  Parameters used when retrieving a specific set of Data Channel Data to read or write like the islands data channel type.
@param bReadPreviousFrame    True if this reader will read the previous frame's data. If false, we read the current frame.
                                                             Reading the current frame allows for zero latency reads, but any data elements that are generated after this reader is used are missed.
                                                             Reading the previous frame's data introduces a frame of latency but ensures we never miss any data as we have access to the whole frame.

### WriteToNiagaraDataChannel
```angelscript
UNiagaraDataChannelWriter WriteToNiagaraDataChannel(const UNiagaraDataChannelAsset Channel, FNiagaraDataChannelSearchParameters SearchParams, int Count, bool bVisibleToGame, bool bVisibleToCPU, bool bVisibleToGPU, FString DebugSource)
```
Initializes and returns the Niagara Data Channel writer to write N elements to the given data channel.

@param WorldContextObject    World to execute in
@param Channel                               The channel to write to
@param SearchParams                  Parameters used when retrieving a specific set of Data Channel Data to read or write like the islands data channel type.
@param Count                                 The number of elements to write
@param bVisibleToGame        If true, the data written to this data channel is visible to Blueprint and C++ logic reading from it
@param bVisibleToCPU If true, the data written to this data channel is visible to Niagara CPU emitters
@param bVisibleToGPU If true, the data written to this data channel is visible to Niagara GPU emitters
@param DebugSource   Instigator for this write, used in the debug hud to track writes to the data channel from different sources

