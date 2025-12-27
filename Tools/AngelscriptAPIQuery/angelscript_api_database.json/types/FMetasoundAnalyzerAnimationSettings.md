# FMetasoundAnalyzerAnimationSettings

## 属性

### bAnimateConnections
- **类型**: `bool`
- **描述**: Whether or not animated connections are enabled.

### EnvelopeWireThickness
- **类型**: `float32`
- **描述**: Thickness of default envelope analyzer wire thickness when connection analyzer is active.

### EnvelopeSpeed
- **类型**: `float32`
- **描述**: Speed of default envelope analyzer drawing over wire when connection analyzer is active, where 0 is full visual history (slowest progress) and 1 is no visual history (fastest progress).

### EnvelopeDirection
- **类型**: `EMetasoundActiveAnalyzerEnvelopeDirection`
- **描述**: Whether analyzer envelopes draw from a source output (default) or from the destination input. From the destination input may not
give the expected illusion of audio processing flowing left-to-right, but results in a waveform with earlier events on the left
and later on the right (like a traditional timeline with a moving play head).

### NumericWireThickness
- **类型**: `float32`
- **描述**: Thickness of default numeric analyzer wire thickness when connection analyzer is active.

### WireScalarMin
- **类型**: `float32`
- **描述**: Minimum height scalar of wire signal analyzers (ex. audio, triggers).

### WireScalarMax
- **类型**: `float32`
- **描述**: Maximum height scalar of wire signal analyzers (ex. audio, triggers).

## 方法

### opAssign
```angelscript
FMetasoundAnalyzerAnimationSettings& opAssign(FMetasoundAnalyzerAnimationSettings Other)
```

