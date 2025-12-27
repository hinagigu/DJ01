# UPhysicsSpringComponent

**继承自**: `USceneComponent`

Note: this component is still work in progress. Uses raycast springs for simple vehicle forces
   Used with objects that have physics to create a spring down the X direction
   ie. point X in the direction you want generate spring.

## 属性

### SpringStiffness
- **类型**: `float32`

### SpringDamping
- **类型**: `float32`

### SpringLengthAtRest
- **类型**: `float32`

### SpringRadius
- **类型**: `float32`

### SpringChannel
- **类型**: `ECollisionChannel`
- **描述**: Strength of thrust force applied to the base object.

### bIgnoreSelf
- **类型**: `bool`

### SpringCompression
- **类型**: `float32`
- **描述**: The current compression of the spring. A spring at rest will have SpringCompression 0.

## 方法

### GetNormalizedCompressionScalar
```angelscript
float32 GetNormalizedCompressionScalar()
```
Returns the spring compression as a normalized scalar along spring direction.
0 implies spring is at rest
1 implies fully compressed

### GetSpringCurrentEndPoint
```angelscript
FVector GetSpringCurrentEndPoint()
```
Returns the spring current end point in world space.

### GetSpringDirection
```angelscript
FVector GetSpringDirection()
```
Returns the spring direction from start to resting point

### GetSpringRestingPoint
```angelscript
FVector GetSpringRestingPoint()
```
Returns the spring resting point in world space.

