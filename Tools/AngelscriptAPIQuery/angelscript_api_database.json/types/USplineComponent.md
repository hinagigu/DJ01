# USplineComponent

**继承自**: `UPrimitiveComponent`

A spline component is a spline shape which can be used for other purposes (e.g. animating objects). It contains debug rendering capabilities.
@see https://docs.unrealengine.com/latest/INT/Resources/ContentExamples/Blueprint_Splines

## 属性

### ReparamStepsPerSegment
- **类型**: `int`
- **描述**: Number of steps per spline segment to place in the reparameterization table

### Duration
- **类型**: `float32`

### bStationaryEndpoints
- **类型**: `bool`

### bSplineHasBeenEdited
- **类型**: `bool`
- **描述**: Whether the spline has been edited from its default by the spline component visualizer

### bInputSplinePointsToConstructionScript
- **类型**: `bool`

### bDrawDebug
- **类型**: `bool`

### bClosedLoop
- **类型**: `bool`
- **描述**: Whether the spline is to be considered as a closed loop.
Use SetClosedLoop() to set this property, and IsClosedLoop() to read it.

### bLoopPositionOverride
- **类型**: `bool`

### LoopPosition
- **类型**: `float32`

### EditorUnselectedSplineSegmentColor
- **类型**: `FLinearColor`
- **描述**: Color of unselected spline component parts in the editor

### EditorSelectedSplineSegmentColor
- **类型**: `FLinearColor`
- **描述**: Color of selected spline component parts in the editor

### EditorTangentColor
- **类型**: `FLinearColor`
- **描述**: Color of spline point tangents in the editor

### bAllowDiscontinuousSpline
- **类型**: `bool`
- **描述**: Whether the spline's leave and arrive tangents can be different

### bAdjustTangentsOnSnap
- **类型**: `bool`
- **描述**: Adjust tangents after snapping.

### bShouldVisualizeScale
- **类型**: `bool`
- **描述**: Whether scale visualization should be displayed

### ScaleVisualizationWidth
- **类型**: `float32`
- **描述**: Width of spline in editor for use with scale visualization

## 方法

### AddPoint
```angelscript
void AddPoint(FSplinePoint Point, bool bUpdateSpline)
```
Adds an FSplinePoint to the spline. This contains its input key, position, tangent, rotation and scale.

### AddPoints
```angelscript
void AddPoints(TArray<FSplinePoint> Points, bool bUpdateSpline)
```
Adds an array of FSplinePoints to the spline.

### AddSplinePoint
```angelscript
void AddSplinePoint(FVector Position, ESplineCoordinateSpace CoordinateSpace, bool bUpdateSpline)
```
Adds a point to the spline

### AddSplinePointAtIndex
```angelscript
void AddSplinePointAtIndex(FVector Position, int Index, ESplineCoordinateSpace CoordinateSpace, bool bUpdateSpline)
```
Adds a point to the spline at the specified index

### ClearSplinePoints
```angelscript
void ClearSplinePoints(bool bUpdateSpline)
```
Clears all the points in the spline

### ConvertSplineSegmentToPolyLine
```angelscript
bool ConvertSplineSegmentToPolyLine(int SplinePointStartIndex, ESplineCoordinateSpace CoordinateSpace, float32 MaxSquareDistanceFromSpline, TArray<FVector>& OutPoints)
```
Given a threshold, returns a list of vertices along the spline segment that, treated as a list of segments (polyline), matches the spline shape.

### ConvertSplineToPolyLine
```angelscript
bool ConvertSplineToPolyLine(ESplineCoordinateSpace CoordinateSpace, float32 MaxSquareDistanceFromSpline, TArray<FVector>& OutPoints)
```
Given a threshold, returns a list of vertices along the spline that, treated as a list of segments (polyline), matches the spline shape.

### ConvertSplineToPolyline_InDistanceRange
```angelscript
bool ConvertSplineToPolyline_InDistanceRange(ESplineCoordinateSpace CoordinateSpace, float32 MaxSquareDistanceFromSpline, float32 StartDistAlongSpline, float32 EndDistAlongSpline, TArray<FVector>& OutPoints, TArray<float>& OutDistancesAlongSpline, bool bAllowWrappingIfClosed)
```
Given a threshold and a start and end distance range, returns a list of vertices along the spline that, treated as a list of segments (polyline), matches the spline shape in that range. Also fills a list of corresponding distances along the spline for each point.

### ConvertSplineToPolyline_InTimeRange
```angelscript
bool ConvertSplineToPolyline_InTimeRange(ESplineCoordinateSpace CoordinateSpace, float32 MaxSquareDistanceFromSpline, float32 StartTimeAlongSpline, float32 EndTimeAlongSpline, bool bUseConstantVelocity, TArray<FVector>& OutPoints, TArray<float>& OutDistancesAlongSpline, bool bAllowWrappingIfClosed)
```
Given a threshold and start and end time range, returns a list of vertices along the spline that, treated as a list of segments (polyline), matches the spline shape in that range. Also fills a list of corresponding distances along the spline for each point.

### ConvertSplineToPolyLineWithDistances
```angelscript
bool ConvertSplineToPolyLineWithDistances(ESplineCoordinateSpace CoordinateSpace, float32 MaxSquareDistanceFromSpline, TArray<FVector>& OutPoints, TArray<float>& OutDistancesAlongSpline)
```
Given a threshold, returns a list of vertices along the spline that, treated as a list of segments (polyline), matches the spline shape. Also fills a list of corresponding distances along the spline for each point.

### DivideSplineIntoPolylineRecursive
```angelscript
bool DivideSplineIntoPolylineRecursive(float32 StartDistanceAlongSpline, float32 EndDistanceAlongSpline, ESplineCoordinateSpace CoordinateSpace, float32 MaxSquareDistanceFromSpline, TArray<FVector>& OutPoints)
```
Given a threshold, recursively sub-divides the spline section until the list of segments (polyline) matches the spline shape. Note: Prefer ConvertSplineToPolyline_InDistanceRange

### DivideSplineIntoPolylineRecursiveWithDistances
```angelscript
bool DivideSplineIntoPolylineRecursiveWithDistances(float32 StartDistanceAlongSpline, float32 EndDistanceAlongSpline, ESplineCoordinateSpace CoordinateSpace, float32 MaxSquareDistanceFromSpline, TArray<FVector>& OutPoints, TArray<float>& OutDistancesAlongSpline)
```
Given a threshold, recursively sub-divides the spline section until the list of segments (polyline) matches the spline shape. Note: Prefer ConvertSplineToPolyline_InDistanceRange

### FindDirectionClosestToWorldLocation
```angelscript
FVector FindDirectionClosestToWorldLocation(FVector WorldLocation, ESplineCoordinateSpace CoordinateSpace)
```
Given a location, in world space, return a unit direction vector of the spline tangent closest to the location.

### FindInputKeyClosestToWorldLocation
```angelscript
float32 FindInputKeyClosestToWorldLocation(FVector WorldLocation)
```
Given a location, in world space, return the input key closest to that location.

### FindLocationClosestToWorldLocation
```angelscript
FVector FindLocationClosestToWorldLocation(FVector WorldLocation, ESplineCoordinateSpace CoordinateSpace)
```
Given a location, in world space, return the point on the curve that is closest to the location.

### FindRightVectorClosestToWorldLocation
```angelscript
FVector FindRightVectorClosestToWorldLocation(FVector WorldLocation, ESplineCoordinateSpace CoordinateSpace)
```
Given a location, in world space, return a unit direction vector corresponding to the spline's right vector closest to the location.

### FindRollClosestToWorldLocation
```angelscript
float32 FindRollClosestToWorldLocation(FVector WorldLocation, ESplineCoordinateSpace CoordinateSpace)
```
Given a location, in world space, return the spline's roll closest to the location, in degrees.

### FindRotationClosestToWorldLocation
```angelscript
FRotator FindRotationClosestToWorldLocation(FVector WorldLocation, ESplineCoordinateSpace CoordinateSpace)
```
Given a location, in world space, return rotation corresponding to the spline's rotation closest to the location.

### FindScaleClosestToWorldLocation
```angelscript
FVector FindScaleClosestToWorldLocation(FVector WorldLocation)
```
Given a location, in world space, return the spline's scale closest to the location.

### FindTangentClosestToWorldLocation
```angelscript
FVector FindTangentClosestToWorldLocation(FVector WorldLocation, ESplineCoordinateSpace CoordinateSpace)
```
Given a location, in world space, return the tangent vector of the spline closest to the location.

### FindTransformClosestToWorldLocation
```angelscript
FTransform FindTransformClosestToWorldLocation(FVector WorldLocation, ESplineCoordinateSpace CoordinateSpace, bool bUseScale)
```
Given a location, in world space, return an FTransform closest to that location.

### FindUpVectorClosestToWorldLocation
```angelscript
FVector FindUpVectorClosestToWorldLocation(FVector WorldLocation, ESplineCoordinateSpace CoordinateSpace)
```
Given a location, in world space, return a unit direction vector corresponding to the spline's up vector closest to the location.

### GetArriveTangentAtSplinePoint
```angelscript
FVector GetArriveTangentAtSplinePoint(int PointIndex, ESplineCoordinateSpace CoordinateSpace)
```
Get the arrive tangent at spline point

### GetDefaultUpVector
```angelscript
FVector GetDefaultUpVector(ESplineCoordinateSpace CoordinateSpace)
```
Gets the default up vector used by this spline

### GetDirectionAtDistanceAlongSpline
```angelscript
FVector GetDirectionAtDistanceAlongSpline(float32 Distance, ESplineCoordinateSpace CoordinateSpace)
```
Given a distance along the length of this spline, return a unit direction vector of the spline tangent there.

### GetDirectionAtSplineInputKey
```angelscript
FVector GetDirectionAtSplineInputKey(float32 InKey, ESplineCoordinateSpace CoordinateSpace)
```
Get unit direction along spline at the provided input key value

### GetDirectionAtSplinePoint
```angelscript
FVector GetDirectionAtSplinePoint(int PointIndex, ESplineCoordinateSpace CoordinateSpace)
```
Get the direction at spline point

### GetDirectionAtTime
```angelscript
FVector GetDirectionAtTime(float32 Time, ESplineCoordinateSpace CoordinateSpace, bool bUseConstantVelocity)
```
Given a time from 0 to the spline duration, return a unit direction vector of the spline tangent there.

### GetDistanceAlongSplineAtLocation
```angelscript
float32 GetDistanceAlongSplineAtLocation(FVector InLocation, ESplineCoordinateSpace CoordinateSpace)
```
Get distance along the spline at closest point of the provided input location

### GetDistanceAlongSplineAtSplineInputKey
```angelscript
float32 GetDistanceAlongSplineAtSplineInputKey(float32 InKey)
```
Get distance along the spline at the provided input key value

### GetDistanceAlongSplineAtSplinePoint
```angelscript
float32 GetDistanceAlongSplineAtSplinePoint(int PointIndex)
```
Get the distance along the spline at the spline point

### GetFloatPropertyAtSplineInputKey
```angelscript
float32 GetFloatPropertyAtSplineInputKey(float32 InKey, FName PropertyName)
```
Get a metadata property float value along the spline at spline input key

### GetFloatPropertyAtSplinePoint
```angelscript
float32 GetFloatPropertyAtSplinePoint(int Index, FName PropertyName)
```
Get a metadata property float value along the spline at spline point

### GetInputKeyValueAtDistanceAlongSpline
```angelscript
float32 GetInputKeyValueAtDistanceAlongSpline(float32 Distance)
```
Given a distance along the length of this spline, return the corresponding input key at that point
with a fractional component between the current input key and the next as a percentage.

### GetInputKeyValueAtSplinePoint
```angelscript
float32 GetInputKeyValueAtSplinePoint(int PointIndex)
```
Get the input key (e.g. the time) of the control point of the spline at the specified index.

### GetLeaveTangentAtSplinePoint
```angelscript
FVector GetLeaveTangentAtSplinePoint(int PointIndex, ESplineCoordinateSpace CoordinateSpace)
```
Get the leave tangent at spline point

### GetLocationAndTangentAtSplinePoint
```angelscript
void GetLocationAndTangentAtSplinePoint(int PointIndex, FVector& Location, FVector& Tangent, ESplineCoordinateSpace CoordinateSpace)
```
Get location and tangent at a spline point

### GetLocationAtDistanceAlongSpline
```angelscript
FVector GetLocationAtDistanceAlongSpline(float32 Distance, ESplineCoordinateSpace CoordinateSpace)
```
Given a distance along the length of this spline, return the point in space where this puts you

### GetLocationAtSplineInputKey
```angelscript
FVector GetLocationAtSplineInputKey(float32 InKey, ESplineCoordinateSpace CoordinateSpace)
```
Get location along spline at the provided input key value

### GetLocationAtSplinePoint
```angelscript
FVector GetLocationAtSplinePoint(int PointIndex, ESplineCoordinateSpace CoordinateSpace)
```
Get the location at spline point

### GetLocationAtTime
```angelscript
FVector GetLocationAtTime(float32 Time, ESplineCoordinateSpace CoordinateSpace, bool bUseConstantVelocity)
```
Given a time from 0 to the spline duration, return the point in space where this puts you

### GetNumberOfSplinePoints
```angelscript
int GetNumberOfSplinePoints()
```
Get the number of points that make up this spline

### GetNumberOfSplineSegments
```angelscript
int GetNumberOfSplineSegments()
```
Get the number of segments that make up this spline

### GetRightVectorAtDistanceAlongSpline
```angelscript
FVector GetRightVectorAtDistanceAlongSpline(float32 Distance, ESplineCoordinateSpace CoordinateSpace)
```
Given a distance along the length of this spline, return a unit direction vector corresponding to the spline's right vector there.

### GetRightVectorAtSplineInputKey
```angelscript
FVector GetRightVectorAtSplineInputKey(float32 InKey, ESplineCoordinateSpace CoordinateSpace)
```
Get right vector at the provided input key value

### GetRightVectorAtSplinePoint
```angelscript
FVector GetRightVectorAtSplinePoint(int PointIndex, ESplineCoordinateSpace CoordinateSpace)
```
Get the right vector at spline point

### GetRightVectorAtTime
```angelscript
FVector GetRightVectorAtTime(float32 Time, ESplineCoordinateSpace CoordinateSpace, bool bUseConstantVelocity)
```
Given a time from 0 to the spline duration, return the spline's right vector there.

### GetRollAtDistanceAlongSpline
```angelscript
float32 GetRollAtDistanceAlongSpline(float32 Distance, ESplineCoordinateSpace CoordinateSpace)
```
Given a distance along the length of this spline, return the spline's roll there, in degrees.

### GetRollAtSplineInputKey
```angelscript
float32 GetRollAtSplineInputKey(float32 InKey, ESplineCoordinateSpace CoordinateSpace)
```
Get roll in degrees at the provided input key value

### GetRollAtSplinePoint
```angelscript
float32 GetRollAtSplinePoint(int PointIndex, ESplineCoordinateSpace CoordinateSpace)
```
Get the amount of roll at spline point, in degrees

### GetRollAtTime
```angelscript
float32 GetRollAtTime(float32 Time, ESplineCoordinateSpace CoordinateSpace, bool bUseConstantVelocity)
```
Given a time from 0 to the spline duration, return the spline's roll there, in degrees.

### GetRotationAtDistanceAlongSpline
```angelscript
FRotator GetRotationAtDistanceAlongSpline(float32 Distance, ESplineCoordinateSpace CoordinateSpace)
```
Given a distance along the length of this spline, return a rotation corresponding to the spline's rotation there.

### GetRotationAtSplineInputKey
```angelscript
FRotator GetRotationAtSplineInputKey(float32 InKey, ESplineCoordinateSpace CoordinateSpace)
```
Get rotator corresponding to rotation along spline at the provided input key value

### GetRotationAtSplinePoint
```angelscript
FRotator GetRotationAtSplinePoint(int PointIndex, ESplineCoordinateSpace CoordinateSpace)
```
Get the rotation at spline point as a rotator

### GetRotationAtTime
```angelscript
FRotator GetRotationAtTime(float32 Time, ESplineCoordinateSpace CoordinateSpace, bool bUseConstantVelocity)
```
Given a time from 0 to the spline duration, return a rotation corresponding to the spline's position and direction there.

### GetScaleAtDistanceAlongSpline
```angelscript
FVector GetScaleAtDistanceAlongSpline(float32 Distance)
```
Given a distance along the length of this spline, return the spline's scale there.

### GetScaleAtSplineInputKey
```angelscript
FVector GetScaleAtSplineInputKey(float32 InKey)
```
Get scale at the provided input key value

### GetScaleAtSplinePoint
```angelscript
FVector GetScaleAtSplinePoint(int PointIndex)
```
Get the scale at spline point

### GetScaleAtTime
```angelscript
FVector GetScaleAtTime(float32 Time, bool bUseConstantVelocity)
```
Given a time from 0 to the spline duration, return the spline's scale there.

### GetSplineLength
```angelscript
float32 GetSplineLength()
```
Returns total length along this spline

### GetSplinePointAt
```angelscript
FSplinePoint GetSplinePointAt(int PointIndex, ESplineCoordinateSpace CoordinateSpace)
```
Gets the spline point of the spline at the specified index

### GetSplinePointType
```angelscript
ESplinePointType GetSplinePointType(int PointIndex)
```
Get the type of a spline point

### GetTangentAtDistanceAlongSpline
```angelscript
FVector GetTangentAtDistanceAlongSpline(float32 Distance, ESplineCoordinateSpace CoordinateSpace)
```
Given a distance along the length of this spline, return the tangent vector of the spline there.

### GetTangentAtSplineInputKey
```angelscript
FVector GetTangentAtSplineInputKey(float32 InKey, ESplineCoordinateSpace CoordinateSpace)
```
Get tangent along spline at the provided input key value

### GetTangentAtSplinePoint
```angelscript
FVector GetTangentAtSplinePoint(int PointIndex, ESplineCoordinateSpace CoordinateSpace)
```
Get the tangent at spline point. This fetches the Leave tangent of the point.

### GetTangentAtTime
```angelscript
FVector GetTangentAtTime(float32 Time, ESplineCoordinateSpace CoordinateSpace, bool bUseConstantVelocity)
```
Given a time from 0 to the spline duration, return the spline's tangent there.

### GetTimeAtDistanceAlongSpline
```angelscript
float32 GetTimeAtDistanceAlongSpline(float32 Distance)
```
Given a distance along the length of this spline, return the corresponding time at that point

### GetTransformAtDistanceAlongSpline
```angelscript
FTransform GetTransformAtDistanceAlongSpline(float32 Distance, ESplineCoordinateSpace CoordinateSpace, bool bUseScale)
```
Given a distance along the length of this spline, return an FTransform corresponding to that point on the spline.

### GetTransformAtSplineInputKey
```angelscript
FTransform GetTransformAtSplineInputKey(float32 InKey, ESplineCoordinateSpace CoordinateSpace, bool bUseScale)
```
Get transform at the provided input key value

### GetTransformAtSplinePoint
```angelscript
FTransform GetTransformAtSplinePoint(int PointIndex, ESplineCoordinateSpace CoordinateSpace, bool bUseScale)
```
Get the transform at spline point

### GetTransformAtTime
```angelscript
FTransform GetTransformAtTime(float32 Time, ESplineCoordinateSpace CoordinateSpace, bool bUseConstantVelocity, bool bUseScale)
```
Given a time from 0 to the spline duration, return the spline's transform at the corresponding position.

### GetUpVectorAtDistanceAlongSpline
```angelscript
FVector GetUpVectorAtDistanceAlongSpline(float32 Distance, ESplineCoordinateSpace CoordinateSpace)
```
Given a distance along the length of this spline, return a unit direction vector corresponding to the spline's up vector there.

### GetUpVectorAtSplineInputKey
```angelscript
FVector GetUpVectorAtSplineInputKey(float32 InKey, ESplineCoordinateSpace CoordinateSpace)
```
Get up vector at the provided input key value

### GetUpVectorAtSplinePoint
```angelscript
FVector GetUpVectorAtSplinePoint(int PointIndex, ESplineCoordinateSpace CoordinateSpace)
```
Get the up vector at spline point

### GetUpVectorAtTime
```angelscript
FVector GetUpVectorAtTime(float32 Time, ESplineCoordinateSpace CoordinateSpace, bool bUseConstantVelocity)
```
Given a time from 0 to the spline duration, return the spline's up vector there.

### GetVectorPropertyAtSplineInputKey
```angelscript
FVector GetVectorPropertyAtSplineInputKey(float32 InKey, FName PropertyName)
```
Get a metadata property vector value along the spline at spline input key

### GetVectorPropertyAtSplinePoint
```angelscript
FVector GetVectorPropertyAtSplinePoint(int Index, FName PropertyName)
```
Get a metadata property vector value along the spline at spline point

### IsClosedLoop
```angelscript
bool IsClosedLoop()
```
Check whether the spline is a closed loop or not

### RemoveSplinePoint
```angelscript
void RemoveSplinePoint(int Index, bool bUpdateSpline)
```
Removes point at specified index from the spline

### SetClosedLoop
```angelscript
void SetClosedLoop(bool bInClosedLoop, bool bUpdateSpline)
```
Specify whether the spline is a closed loop or not. The loop position will be at 1.0 after the last point's input key

### SetClosedLoopAtPosition
```angelscript
void SetClosedLoopAtPosition(bool bInClosedLoop, float32 Key, bool bUpdateSpline)
```
Specify whether the spline is a closed loop or not, and if so, the input key corresponding to the loop point

### SetDefaultUpVector
```angelscript
void SetDefaultUpVector(FVector UpVector, ESplineCoordinateSpace CoordinateSpace)
```
Sets the default up vector used by this spline

### SetDrawDebug
```angelscript
void SetDrawDebug(bool bShow)
```
Specify whether this spline should be rendered when the Editor/Game spline show flag is set

### SetLocationAtSplinePoint
```angelscript
void SetLocationAtSplinePoint(int PointIndex, FVector InLocation, ESplineCoordinateSpace CoordinateSpace, bool bUpdateSpline)
```
Move an existing point to a new location

### SetRotationAtSplinePoint
```angelscript
void SetRotationAtSplinePoint(int PointIndex, FRotator InRotation, ESplineCoordinateSpace CoordinateSpace, bool bUpdateSpline)
```
Set the rotation of an existing spline point

### SetScaleAtSplinePoint
```angelscript
void SetScaleAtSplinePoint(int PointIndex, FVector InScaleVector, bool bUpdateSpline)
```
Set the scale at a given spline point

### SetSelectedSplineSegmentColor
```angelscript
void SetSelectedSplineSegmentColor(FLinearColor SegmentColor)
```
Specify selected spline component segment color in the editor

### SetSplinePoints
```angelscript
void SetSplinePoints(TArray<FVector> Points, ESplineCoordinateSpace CoordinateSpace, bool bUpdateSpline)
```
Sets the spline to an array of points

### SetSplinePointType
```angelscript
void SetSplinePointType(int PointIndex, ESplinePointType Type, bool bUpdateSpline)
```
Specify the type of a spline point

### SetTangentAtSplinePoint
```angelscript
void SetTangentAtSplinePoint(int PointIndex, FVector InTangent, ESplineCoordinateSpace CoordinateSpace, bool bUpdateSpline)
```
Specify the tangent at a given spline point

### SetTangentColor
```angelscript
void SetTangentColor(FLinearColor TangentColor)
```
Specify selected spline component segment color in the editor

### SetTangentsAtSplinePoint
```angelscript
void SetTangentsAtSplinePoint(int PointIndex, FVector InArriveTangent, FVector InLeaveTangent, ESplineCoordinateSpace CoordinateSpace, bool bUpdateSpline)
```
Specify the tangents at a given spline point

### SetUnselectedSplineSegmentColor
```angelscript
void SetUnselectedSplineSegmentColor(FLinearColor SegmentColor)
```
Specify unselected spline component segment color in the editor

### SetUpVectorAtSplinePoint
```angelscript
void SetUpVectorAtSplinePoint(int PointIndex, FVector InUpVector, ESplineCoordinateSpace CoordinateSpace, bool bUpdateSpline)
```
Specify the up vector at a given spline point

### UpdateSpline
```angelscript
void UpdateSpline()
```
Update the spline tangents and SplineReparamTable

