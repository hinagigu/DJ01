# UBTDecorator_KeepInCone

**继承自**: `UBTDecorator`

Keep In Cone decorator node.
A decorator node that bases its condition on whether the observed position is still inside a cone. The cone's direction is calculated when the node first becomes relevant.

## 属性

### ConeHalfAngle
- **类型**: `float32`
- **描述**: max allowed time for execution of underlying node

### ConeOrigin
- **类型**: `FBlackboardKeySelector`
- **描述**: blackboard key selector

### Observed
- **类型**: `FBlackboardKeySelector`
- **描述**: blackboard key selector

