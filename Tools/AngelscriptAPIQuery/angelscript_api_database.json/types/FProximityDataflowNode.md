# FProximityDataflowNode

Update the proximity (contact) graph for the bones in a Collection

## 属性

### ProximityMethod
- **类型**: `EProximityMethodEnum`
- **描述**: Which method to use to decide whether a given piece of geometry is in proximity with another

### DistanceThreshold
- **类型**: `float32`
- **描述**: If hull-based proximity detection is enabled, amount to expand hulls when searching for overlapping neighbors

### ContactThreshold
- **类型**: `float32`
- **描述**: If greater than zero, proximity will be additionally filtered by a 'contact' threshold, in cm, to exclude grazing / corner proximity

### FilterContactMethod
- **类型**: `EProximityContactFilteringMethodEnum`
- **描述**: How to use the Contact Threshold (if > 0) to filter out unwanted small or corner contacts from the proximity graph. If contact threshold is zero, no filtering is applied.

### bUseAsConnectionGraph
- **类型**: `bool`
- **描述**: Whether to automatically transform the proximity graph into a connection graph to be used for simulation

### ContactAreaMethod
- **类型**: `EConnectionContactAreaMethodEnum`
- **描述**: The method used to compute contact areas for simulation purposes (only when 'Use As Connection Graph' is enabled)

### bRecomputeConvexHulls
- **类型**: `bool`
- **描述**: Whether to compute new convex hulls for proximity, or use the pre-existing hulls on the Collection, when using convex hulls to determine proximity

### bActive
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FProximityDataflowNode& opAssign(FProximityDataflowNode Other)
```

