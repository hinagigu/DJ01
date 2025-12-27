# UAnimNotifyState_TimedNiagaraEffectAdvanced

**继承自**: `UAnimNotifyState_TimedNiagaraEffect`

Same as Timed Niagara Effect but also provides some more advanced abilities at an additional cost.

## 属性

### bEnableNormalizedNotifyProgress
- **类型**: `bool`
- **描述**: This send a 0-1 value of the normalized progress to the FX Component to the float User Parameter.

### bApplyRateScaleToProgress
- **类型**: `bool`

### NotifyProgressUserParameter
- **类型**: `FName`
- **描述**: The name of your niagara user variable you would like to send the normalized notify progress to.

### AnimCurves
- **类型**: `TArray<FCurveParameterPair>`
- **描述**: Array of fnames to map Anim Curve names to Niagara Parameters.

## 方法

### GetNotifyProgress
```angelscript
float32 GetNotifyProgress(UMeshComponent MeshComp)
```
Returns a 0 to 1 value for the progress of this component along the notify.

