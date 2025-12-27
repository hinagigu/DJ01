# UMaterialExpressionMaterialXOverlay

**继承自**: `UMaterialExpression`

Blend nodes take two 1-4 channel inputs and apply the same operator to all channels.
Blend nodes support an optional float input mix , which can be used
to mix the original B value with the result of the blend operation.
Operation: 2*A*B          if A < 0.5;
           1-(1-A)(1-B) if A >= 0.5
Result: Lerp(B, Op, Alpha)

## 属性

### ConstAlpha
- **类型**: `float32`
- **描述**: only used if Alpha is not hooked up

