# ACameraRig_Rail

**继承自**: `AActor`

## 属性

### CurrentPositionOnRail
- **类型**: `float32`

### bLockOrientationToRail
- **类型**: `bool`

### bShowRailVisualization
- **类型**: `bool`
- **描述**: Determines whether or not to show the rail mesh preview.

### PreviewMeshScale
- **类型**: `float32`
- **描述**: Determines the scale of the rail mesh preview

### TransformComponent
- **类型**: `USceneComponent`
- **描述**: Root component to give the whole actor a transform.

### RailCameraMount
- **类型**: `USceneComponent`
- **描述**: Component to define the attach point for cameras. Moves along the rail.

### RailSplineComponent
- **类型**: `USplineComponent`

## 方法

### GetRailSplineComponent
```angelscript
USplineComponent GetRailSplineComponent()
```
Returns the spline component that defines the rail path

