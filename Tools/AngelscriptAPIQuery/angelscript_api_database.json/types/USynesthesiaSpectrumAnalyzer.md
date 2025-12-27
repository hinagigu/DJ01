# USynesthesiaSpectrumAnalyzer

**继承自**: `UAudioAnalyzer`

USynesthesiaSpectrumAnalysisAnalyzer

USynesthesiaSpectrumAnalysisAnalyzer calculates the current amplitude of an
audio bus in real-time.

## 属性

### Settings
- **类型**: `USynesthesiaSpectrumAnalysisSettings`

### OnSpectrumResults
- **类型**: `FOnSpectrumResults`

### OnLatestSpectrumResults
- **类型**: `FOnLatestSpectrumResults`

## 方法

### GetCenterFrequencies
```angelscript
void GetCenterFrequencies(float32 InSampleRate, TArray<float32>& OutCenterFrequencies)
```

### GetNumCenterFrequencies
```angelscript
int GetNumCenterFrequencies()
```

