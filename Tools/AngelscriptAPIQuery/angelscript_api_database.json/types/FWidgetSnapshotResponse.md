# FWidgetSnapshotResponse

Implements a message that is used to receive a widget snapshot from a remote target.

## 属性

### SnapshotRequestId
- **类型**: `FGuid`
- **描述**: The request ID of this snapshot (used to identify the correct response from the target)

### SnapshotData
- **类型**: `TArray<uint8>`
- **描述**: The snapshot data, to be used by FWidgetSnapshotData::LoadSnapshotFromBuffer

## 方法

### opAssign
```angelscript
FWidgetSnapshotResponse& opAssign(FWidgetSnapshotResponse Other)
```

