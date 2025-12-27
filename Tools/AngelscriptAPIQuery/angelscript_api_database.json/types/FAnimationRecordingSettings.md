# FAnimationRecordingSettings

Settings describing how to record an animation

## 属性

### bRecordInWorldSpace
- **类型**: `bool`
- **描述**: Whether to record animation in world space, defaults to true

### bRemoveRootAnimation
- **类型**: `bool`
- **描述**: Whether to remove the root bone transform from the animation

### bAutoSaveAsset
- **类型**: `bool`
- **描述**: Whether to auto-save asset when recording is completed. Defaults to false

### SampleFrameRate
- **类型**: `FFrameRate`
- **描述**: Sample rate of the recorded animation

### Length
- **类型**: `float32`
- **描述**: Maximum length of the animation recorded (in seconds). If zero the animation will keep on recording until stopped.

### Interpolation
- **类型**: `EAnimInterpolationType`
- **描述**: This defines how values between keys are calculated for transforms.*

### InterpMode
- **类型**: `ERichCurveInterpMode`
- **描述**: Interpolation mode for the recorded keys.

### TangentMode
- **类型**: `ERichCurveTangentMode`
- **描述**: Tangent mode for the recorded keys.

### bRecordTransforms
- **类型**: `bool`
- **描述**: Whether or not to record transforms

### bRecordMorphTargets
- **类型**: `bool`
- **描述**: Whether or not to record morph targets

### bRecordAttributeCurves
- **类型**: `bool`
- **描述**: Whether or not to record parameter curves

### bRecordMaterialCurves
- **类型**: `bool`
- **描述**: Whether or not to record material curves

### bTransactRecording
- **类型**: `bool`
- **描述**: Whether or not to transact recording changes

### IncludeAnimationNames
- **类型**: `TArray<FString>`
- **描述**: Include only the animation bones/curves that match this list

### ExcludeAnimationNames
- **类型**: `TArray<FString>`
- **描述**: Exclude all animation bones/curves that match this list

## 方法

### opAssign
```angelscript
FAnimationRecordingSettings& opAssign(FAnimationRecordingSettings Other)
```

