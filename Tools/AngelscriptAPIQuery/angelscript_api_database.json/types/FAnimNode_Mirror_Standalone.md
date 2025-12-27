# FAnimNode_Mirror_Standalone

## 属性

### bMirror
- **类型**: `bool`

### MirrorDataTable
- **类型**: `UMirrorDataTable`

### BlendTime
- **类型**: `float32`
- **描述**: Inertialization blend time to use when transitioning between mirrored and unmirrored states

### bResetChild
- **类型**: `bool`
- **描述**: Whether to reset (reinitialize) the child (source) pose when the mirror state changes

### bBoneMirroring
- **类型**: `bool`

### bCurveMirroring
- **类型**: `bool`

### bAttributeMirroring
- **类型**: `bool`

### Source
- **类型**: `FPoseLink`

## 方法

### opAssign
```angelscript
FAnimNode_Mirror_Standalone& opAssign(FAnimNode_Mirror_Standalone Other)
```

