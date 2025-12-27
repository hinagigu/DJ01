# UBTDecorator_ConeCheck

**继承自**: `UBTDecorator`

Cone check decorator node.
A decorator node that bases its condition on a cone check, using Blackboard entries to form the parameters of the check.

## 属性

### ConeHalfAngle
- **类型**: `float32`
- **描述**: Angle between cone direction and code cone edge, or a half of the total cone angle

### ConeOrigin
- **类型**: `FBlackboardKeySelector`
- **描述**: blackboard key selector

### ConeDirection
- **类型**: `FBlackboardKeySelector`
- **描述**: "None" means "use ConeOrigin's direction"

### Observed
- **类型**: `FBlackboardKeySelector`
- **描述**: blackboard key selector

