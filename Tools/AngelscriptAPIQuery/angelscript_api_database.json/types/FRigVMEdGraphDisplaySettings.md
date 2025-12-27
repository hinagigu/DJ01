# FRigVMEdGraphDisplaySettings

## 属性

### bShowNodeInstructionIndex
- **类型**: `bool`
- **描述**: When enabled shows the first node instruction index
matching the execution stack window.

### bShowNodeRunCounts
- **类型**: `bool`
- **描述**: When enabled shows the node counts both in the graph view as
we as in the execution stack window.
The number on each node represents how often the node has been run.
Keep in mind when looking at nodes in a function the count
represents the sum of all counts for each node based on all
references of the function currently running.

### NodeRunLowerBound
- **类型**: `int`
- **描述**: A lower limit for counts for nodes used for debugging.
Any node lower than this count won't show the run count.

### NodeRunLimit
- **类型**: `int`
- **描述**: A upper limit for counts for nodes used for debugging.
If a node reaches this count a warning will be issued for the
node and displayed both in the execution stack as well as in the
graph. Setting this to <= 1 disables the warning.
Note: The count limit doesn't apply to functions / collapse nodes.

### MinMicroSeconds
- **类型**: `float`
- **描述**: The duration in microseconds of the fastest instruction / node

### MaxMicroSeconds
- **类型**: `float`
- **描述**: The duration in microseconds of the slowest instruction / node

### AverageFrames
- **类型**: `int`
- **描述**: If you set this to more than 1 the results will be averaged across multiple frames

### bAutoDetermineRange
- **类型**: `bool`

### MinDurationColor
- **类型**: `FLinearColor`
- **描述**: The color of the fastest instruction / node

### MaxDurationColor
- **类型**: `FLinearColor`
- **描述**: The color of the slowest instruction / node

## 方法

### opAssign
```angelscript
FRigVMEdGraphDisplaySettings& opAssign(FRigVMEdGraphDisplaySettings Other)
```

