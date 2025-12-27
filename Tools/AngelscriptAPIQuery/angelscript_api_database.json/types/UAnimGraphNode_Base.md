# UAnimGraphNode_Base

**继承自**: `UK2Node`

This is the base class for any animation graph nodes that generate or consume an animation pose in
the animation blend graph.

Any concrete implementations will be paired with a runtime graph node derived from FAnimNode_Base

## 属性

### ShowPinForProperties
- **类型**: `TArray<FOptionalPinFromProperty>`

### Binding
- **类型**: `UAnimGraphNodeBinding`
- **描述**: Bindings for pins that this node exposes

### Tag
- **类型**: `FName`
- **描述**: Optional reference tag name. If this is set then this node can be referenced from elsewhere in this animation blueprint using an anim node reference

