# FLevelSequenceAnimSequenceLinkItem

Link To Anim Sequence that we are linked too.

## 属性

### SkelTrackGuid
- **类型**: `FGuid`

### PathToAnimSequence
- **类型**: `FSoftObjectPath`

### bExportTransforms
- **类型**: `bool`
- **描述**: From Editor Only UAnimSeqExportOption we cache this since we can re-import dynamically

### bExportMorphTargets
- **类型**: `bool`

### bExportAttributeCurves
- **类型**: `bool`

### bExportMaterialCurves
- **类型**: `bool`

### Interpolation
- **类型**: `EAnimInterpolationType`

### CurveInterpolation
- **类型**: `ERichCurveInterpMode`

### bRecordInWorldSpace
- **类型**: `bool`

### bEvaluateAllSkeletalMeshComponents
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FLevelSequenceAnimSequenceLinkItem& opAssign(FLevelSequenceAnimSequenceLinkItem Other)
```

