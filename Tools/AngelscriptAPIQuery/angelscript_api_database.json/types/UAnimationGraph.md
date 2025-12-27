# UAnimationGraph

**继承自**: `UEdGraph`

## 属性

### BlendOptions
- **类型**: `FAnimGraphBlendOptions`
- **描述**: Blending options for animation graphs in Linked Animation Blueprints.

## 方法

### GetGraphNodesOfClass
```angelscript
void GetGraphNodesOfClass(TSubclassOf<UAnimGraphNode_Base> NodeClass, TArray<UAnimGraphNode_Base>& GraphNodes, bool bIncludeChildClasses)
```
Returns contained graph nodes of the specified (or child) class

