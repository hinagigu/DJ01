# UK2Node_MathExpression

**继承自**: `UK2Node_Composite`

This node type acts like a collapsed node, a single node that represents
a larger sub-network of nodes (contained within a sub-graph). This node will
take the math expression it was named with, and attempt to convert it into a
series of math nodes. If it is unsuccessful, then it generates a series of
actionable errors.

## 属性

### Expression
- **类型**: `FString`
- **描述**: The math expression to evaluate

