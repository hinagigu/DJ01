# FSwarmTaskRequestSpecificationMessage

## 属性

### TaskGuid
- **类型**: `FGuid`
- **描述**: The GUID used for identifying the Task being referred to

### Parameters
- **类型**: `FString`
- **描述**: The Task's parameter string specified with AddTask

### Flags
- **类型**: `uint8`
- **描述**: Flags used to control the behavior of the Task, subject to overrides from the containing Job

### Cost
- **类型**: `uint`
- **描述**: The Task's cost, relative to all other Tasks in the same Job, used for even distribution and scheduling

### Dependencies
- **类型**: `TArray<FString>`
- **描述**: Any additional Task dependencies

## 方法

### opAssign
```angelscript
FSwarmTaskRequestSpecificationMessage& opAssign(FSwarmTaskRequestSpecificationMessage Other)
```

