# UFractureModeSettings

**继承自**: `UDeveloperSettings`

Settings for the Fracture Editor Mode.

## 属性

### NewAssetLocation
- **类型**: `EFractureModeNewAssetLocation`
- **描述**: The default asset folder presented when using the "New" tool to create a Geometry Collection in Fracture Mode

### ConvexCanExceedFraction
- **类型**: `float32`
- **描述**: Default fraction of geometry volume by which a cluster's convex hull volume can exceed the actual geometry volume before instead using the hulls of the children.  0 means the convex volume cannot exceed the geometry volume; 1 means the convex volume is allowed to be 100% larger (2x) the geometry volume.

### ConvexSimplificationDistanceThreshold
- **类型**: `float32`
- **描述**: Default simplification threshold for convex hulls of new geometry collections

### ConvexRemoveOverlaps
- **类型**: `EConvexOverlapRemoval`
- **描述**: Default overlap removal setting for convex hulls of new geometry collections

### ConvexOverlapRemovalShrinkPercent
- **类型**: `float32`
- **描述**: Default overlap removal shrink percent (in range 0-100) for convex hulls of new geometry collections. Overlap removal will be computed assuming convex shapes will be scaled down by this percentage.

### ConvexFractionAllowRemove
- **类型**: `float`
- **描述**: Default fraction of convex hulls for a transform that we can remove before using the hulls of the children

### ProximityMethod
- **类型**: `EProximityMethod`
- **描述**: Default method used to detect proximity of geometry in a new geometry collection

### ProximityDistanceThreshold
- **类型**: `float32`
- **描述**: When Proximity Detection Method is Convex Hull, how close two hulls need to be to be considered as 'in proximity'

### bProximityUseAsConnectionGraph
- **类型**: `bool`
- **描述**: Whether to automatically transform the proximity graph into a connection graph to be used for simulation

### ProximityConnectionContactAreaMethod
- **类型**: `EConnectionContactMethod`
- **描述**: Method to use to determine the area of the contact for transforms that are connected in the connection graph used for simulation. Only used if "Use As Connection Graph" is enabled.

### ProximityContactMethod
- **类型**: `EProximityContactMethod`
- **描述**: Method to use to determine the contact between two pieces, if the Contact Threshold is greater than 0, for the purpose of filtering out too-small contacts

### ProximityContactThreshold
- **类型**: `float32`
- **描述**: If greater than zero, proximity will be additionally filtered by a 'contact' threshold, in cm, to exclude grazing / corner proximity

