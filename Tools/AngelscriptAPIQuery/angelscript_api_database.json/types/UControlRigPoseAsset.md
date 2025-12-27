# UControlRigPoseAsset

**继承自**: `UObject`

An individual Pose made of Control Rig Controls

## 属性

### Pose
- **类型**: `FControlRigControlPose`

## 方法

### DoesMirrorMatch
```angelscript
bool DoesMirrorMatch(UControlRig ControlRig, FName ControlName)
```

### GetControlNames
```angelscript
TArray<FName> GetControlNames()
```

### GetCurrentPose
```angelscript
void GetCurrentPose(UControlRig InControlRig, FControlRigControlPose& OutPose)
```

### PastePose
```angelscript
void PastePose(UControlRig InControlRig, bool bDoKey, bool bDoMirror)
```

### ReplaceControlName
```angelscript
void ReplaceControlName(FName CurrentName, FName NewName)
```

### SavePose
```angelscript
void SavePose(UControlRig InControlRig, bool bUseAll)
```

### SelectControls
```angelscript
void SelectControls(UControlRig InControlRig, bool bDoMirror)
```

