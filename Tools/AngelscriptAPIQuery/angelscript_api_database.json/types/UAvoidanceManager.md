# UAvoidanceManager

**继承自**: `UObject`

## 属性

### DefaultTimeToLive
- **类型**: `float32`
- **描述**: How long an avoidance UID must not be updated before the system will put it back in the pool. Actual delay is up to 150% of this value.

### LockTimeAfterAvoid
- **类型**: `float32`
- **描述**: How long to stay on course (barring collision) after making an avoidance move

### LockTimeAfterClean
- **类型**: `float32`
- **描述**: How long to stay on course (barring collision) after making an unobstructed move (should be > 0.0, but can be less than a full frame)

### DeltaTimeToPredict
- **类型**: `float32`
- **描述**: This is how far forward in time (seconds) we extend our velocity cones and thus our prediction

### ArtificialRadiusExpansion
- **类型**: `float32`
- **描述**: Multiply the radius of all STORED avoidance objects by this value to allow a little extra room for avoidance maneuvers.

### HeightCheckMargin
- **类型**: `float32`
- **描述**: Allowable height margin between obstacles and agents. This is over and above the difference in agent heights.

## 方法

### GetAvoidanceVelocityForComponent
```angelscript
FVector GetAvoidanceVelocityForComponent(UMovementComponent MovementComp)
```
Calculate avoidance velocity for component (avoids collisions with the supplied component)

### GetNewAvoidanceUID
```angelscript
int GetNewAvoidanceUID()
```
Get appropriate UID for use when reporting to this function or requesting RVO assistance.

### GetObjectCount
```angelscript
int GetObjectCount()
```
Get the number of avoidance objects currently in the manager.

### RegisterMovementComponent
```angelscript
bool RegisterMovementComponent(UMovementComponent MovementComp, float32 AvoidanceWeight)
```
Register with the given avoidance manager.
@param AvoidanceWeight      When avoiding each other, actors divert course in proportion to their relative weights. Range is 0.0 to 1.0. Special: at 1.0, actor will not divert course at all.

