# FRigVMRuntimeSettings

## 属性

### MaximumArraySize
- **类型**: `int`
- **描述**: The largest allowed size for arrays within the RigVM.
Accessing or creating larger arrays will cause runtime errors in the rig.

### bEnableProfiling
- **类型**: `bool`
- **描述**: When enabled records the timing of each instruction / node
on each node and within the execution stack window.
Keep in mind when looking at nodes in a function the duration
represents the accumulated duration of all invocations
of the function currently running.

Note: This can only be used when in Debug Mode. Click the "Release" button
in the top toolbar to switch to Debug mode.

## 方法

### opAssign
```angelscript
FRigVMRuntimeSettings& opAssign(FRigVMRuntimeSettings Other)
```

