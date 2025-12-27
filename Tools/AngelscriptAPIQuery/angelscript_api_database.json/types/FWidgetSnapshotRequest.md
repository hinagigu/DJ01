# FWidgetSnapshotRequest

Implements a message that is used to request a widget snapshot from a remote target.

## 属性

### TargetInstanceId
- **类型**: `FGuid`
- **描述**: The instance ID of the remote target we want to receive a snapshot from

### SnapshotRequestId
- **类型**: `FGuid`
- **描述**: The request ID of this snapshot (used to identify the correct response from the target)

## 方法

### opAssign
```angelscript
FWidgetSnapshotRequest& opAssign(FWidgetSnapshotRequest Other)
```

