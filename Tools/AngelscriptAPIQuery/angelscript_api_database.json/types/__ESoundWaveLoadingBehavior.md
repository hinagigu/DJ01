# __ESoundWaveLoadingBehavior

Only used when stream caching is enabled. Determines how we are going to load or retain a given audio asset.
A USoundWave's loading behavior can be overridden in the USoundWave itself, the sound wave's USoundClass, or by cvars.
The order of priority is defined as:
1) The loading behavior set on the USoundWave
2) The loading behavior set on the USoundWave's USoundClass.
3) The loading behavior set on the nearest parent of a USoundWave's USoundClass.
4) The loading behavior set via the au.streamcache cvars.

## 属性

### Inherited
- **类型**: `ESoundWaveLoadingBehavior`

### RetainOnLoad
- **类型**: `ESoundWaveLoadingBehavior`

### PrimeOnLoad
- **类型**: `ESoundWaveLoadingBehavior`

### LoadOnDemand
- **类型**: `ESoundWaveLoadingBehavior`

### ForceInline
- **类型**: `ESoundWaveLoadingBehavior`

### Uninitialized
- **类型**: `ESoundWaveLoadingBehavior`

### ESoundWaveLoadingBehavior_MAX
- **类型**: `ESoundWaveLoadingBehavior`

