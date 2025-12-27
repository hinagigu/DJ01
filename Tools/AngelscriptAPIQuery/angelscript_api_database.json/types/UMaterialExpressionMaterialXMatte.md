# UMaterialExpressionMaterialXMatte

**继承自**: `UMaterialExpression`

Merge nodes take two 4-channel (color4) inputs and use the built-in alpha channel(s) to control the
compositing of the A and B inputs. "A" and "B" refer to the non-alpha channels of the A and B inputs respectively,
and "a" and "b" refer to the alpha channels of the A and B inputs.
Merge nodes are only defined for float4 inputs
Merge nodes support an optional float input Alpha , which can be used to mix the
original B value with the result of the blend operation.

Operation: A*a + B*(1-a)
Result: Lerp(B, A*a + B*(1-a), Alpha)

## 属性

### ConstAlpha
- **类型**: `float32`
- **描述**: only used if Alpha is not hooked up

