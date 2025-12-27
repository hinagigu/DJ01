# UMetaSoundSourceBuilder

**继承自**: `UMetaSoundBuilderBase`

Builder in charge of building a MetaSound Source

## 方法

### Audition
```angelscript
void Audition(UAudioComponent AudioComponent, FOnCreateAuditionGeneratorHandleDelegate OnCreateGenerator, bool bLiveUpdatesEnabled)
```

### GetLiveUpdatesEnabled
```angelscript
bool GetLiveUpdatesEnabled()
```
Returns whether or not live updates are both globally enabled (via cvar) and are enabled on this builder's last built sound, which may or may not still be playing.

### SetBlockRateOverride
```angelscript
void SetBlockRateOverride(float32 BlockRate)
```
Sets the MetaSound's BlockRate override

### SetFormat
```angelscript
void SetFormat(EMetaSoundOutputAudioFormat OutputFormat, EMetaSoundBuilderResult& OutResult)
```
Sets the output audio format of the source

### SetQuality
```angelscript
void SetQuality(FName Quality)
```
Sets the MetaSound's Quality level

### SetSampleRateOverride
```angelscript
void SetSampleRateOverride(int SampleRate)
```
Sets the MetaSound's SampleRate override

