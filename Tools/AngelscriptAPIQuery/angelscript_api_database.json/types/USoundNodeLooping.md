# USoundNodeLooping

**继承自**: `USoundNode`

Defines how a sound loops; either indefinitely, or for a set number of times.
Note: The Looping node should only be used for logical or procedural looping such as introducing a delay.
These sounds will not be played seamlessly. If you want a sound to loop seamlessly and indefinitely,
use the Looping flag on the Wave Player node for that sound.

## 属性

### LoopCount
- **类型**: `int`
- **描述**: The amount of times to loop

### bLoopIndefinitely
- **类型**: `bool`

