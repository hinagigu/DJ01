# UFractureProximitySettings

**继承自**: `UFractureToolSettings`

Settings controlling how proximity is detected for geometry collections

## 属性

### Method
- **类型**: `EProximityMethod`
- **描述**: Which method to use to decide whether a given piece of geometry is in proximity with another

### DistanceThreshold
- **类型**: `float`
- **描述**: If hull-based proximity detection is enabled, amount to expand hulls when searching for overlapping neighbors

### ContactMethod
- **类型**: `EProximityContactMethod`
- **描述**: Method to use to determine the contact between two pieces, if the Contact Threshold is greater than 0

### ContactThreshold
- **类型**: `float`
- **描述**: If greater than zero, proximity will be additionally filtered by a 'contact' threshold, in cm, to exclude grazing / corner proximity

### bUseAsConnectionGraph
- **类型**: `bool`
- **描述**: Whether to automatically transform the proximity graph into a connection graph to be used for simulation

### ContactAreaMethod
- **类型**: `EConnectionContactMethod`
- **描述**: Method to use for determining contact areas that define the strength of connections for destruction simulation

### bShowProximity
- **类型**: `bool`
- **描述**: Whether to display the proximity graph edges

### bOnlyShowForSelected
- **类型**: `bool`
- **描述**: Whether to only show the proximity graph connections for selected bones

### LineThickness
- **类型**: `float32`
- **描述**: Line thickness for connections

### LineColor
- **类型**: `FColor`
- **描述**: Line color for connections

### CenterSize
- **类型**: `float32`
- **描述**: Point size for centers

### CenterColor
- **类型**: `FColor`
- **描述**: Point color for centers

