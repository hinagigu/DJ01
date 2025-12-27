# UBTDecorator_DoesPathExist

**继承自**: `UBTDecorator`

Does Path Exist decorator node.
A decorator node that bases its condition on whether a path exists between two points from the Blackboard.

## 属性

### BlackboardKeyA
- **类型**: `FBlackboardKeySelector`
- **描述**: blackboard key selector

### BlackboardKeyB
- **类型**: `FBlackboardKeySelector`
- **描述**: blackboard key selector

### PathQueryType
- **类型**: `EPathExistanceQueryType`

### FilterClass
- **类型**: `TSubclassOf<UNavigationQueryFilter>`
- **描述**: "None" will result in default filter being used

