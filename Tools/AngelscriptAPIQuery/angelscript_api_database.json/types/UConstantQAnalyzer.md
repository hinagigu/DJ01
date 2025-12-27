# UConstantQAnalyzer

**继承自**: `UAudioAnalyzer`

UConstantQAnalyzer

UConstantQAnalyzer calculates the temporal evolution of constant q transform for a given
audio bus in real-time. ConstantQ is available for individual channels or the overall audio bus.

## 属性

### Settings
- **类型**: `UConstantQSettings`

### OnConstantQResults
- **类型**: `FOnConstantQResults`

### OnLatestConstantQResults
- **类型**: `FOnLatestConstantQResults`

## 方法

### GetCenterFrequencies
```angelscript
void GetCenterFrequencies(TArray<float32>& OutCenterFrequencies)
```

### GetNumCenterFrequencies
```angelscript
int GetNumCenterFrequencies()
```

