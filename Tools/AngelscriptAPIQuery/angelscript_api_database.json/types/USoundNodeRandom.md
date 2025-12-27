# USoundNodeRandom

**继承自**: `USoundNode`

Selects sounds from a random set

## 属性

### Weights
- **类型**: `TArray<float32>`

### PreselectAtLevelLoad
- **类型**: `int`
- **描述**: If greater than 0, then upon each level load such a number of inputs will be randomly selected
and the rest will be removed. This can be used to cut down the memory usage of large randomizing
cues.

### bShouldExcludeFromBranchCulling
- **类型**: `bool`

### bRandomizeWithoutReplacement
- **类型**: `bool`

