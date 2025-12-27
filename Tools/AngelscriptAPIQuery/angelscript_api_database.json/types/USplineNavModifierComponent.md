# USplineNavModifierComponent

**继承自**: `UNavModifierComponent`

Assign a chosen NavArea in the vicinity of a spline
This component must only be attached to an actor with a USplineComponent

## 属性

### SplineExtent
- **类型**: `float`
- **描述**: Radius of the tube surrounding the spline which will be used to generate the Nav Modifiers

### NumSplineSamples
- **类型**: `int`
- **描述**: How many sections the spline will be divided into for generating overlap volumes. More samples result in finer detail

