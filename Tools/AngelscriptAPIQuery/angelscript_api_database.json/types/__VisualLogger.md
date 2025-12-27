# __VisualLogger

## 方法

### EnableRecording
```angelscript
void EnableRecording(bool bEnabled)
```

### LogArrow
```angelscript
void LogArrow(UObject WorldContextObject, FVector SegmentStart, FVector SegmentEnd, FString Text, FLinearColor ObjectColor, FName CategoryName, bool bAddToMessageLog)
```
Logs arrow - recording for Visual Logs has to be enabled to record this data

### LogBox
```angelscript
void LogBox(UObject WorldContextObject, FBox BoxShape, FString Text, FLinearColor ObjectColor, FName LogCategory, bool bAddToMessageLog, bool bWireframe)
```
Logs box shape - recording for Visual Logs has to be enabled to record this data

### LogCapsule
```angelscript
void LogCapsule(UObject WorldContextObject, FVector Base, float32 HalfHeight, float32 Radius, FQuat Rotation, FString Text, FLinearColor ObjectColor, FName LogCategory, bool bAddToMessageLog, bool bWireframe)
```
Logs capsule shape - recording for Visual Logs has to be enabled to record this data

### LogCircle
```angelscript
void LogCircle(UObject WorldContextObject, FVector Center, FVector UpAxis, float32 Radius, FString Text, FLinearColor ObjectColor, float32 Thickness, FName CategoryName, bool bAddToMessageLog)
```
Logs circle - recording for Visual Logs has to be enabled to record this data

### LogCone
```angelscript
void LogCone(UObject WorldContextObject, FVector Origin, FVector Direction, float32 Length, float32 Angle, FString Text, FLinearColor ObjectColor, FName LogCategory, bool bAddToMessageLog, bool bWireframe)
```
Logs cone shape - recording for Visual Logs has to be enabled to record this data

### LogCylinder
```angelscript
void LogCylinder(UObject WorldContextObject, FVector Start, FVector End, float32 Radius, FString Text, FLinearColor ObjectColor, FName LogCategory, bool bAddToMessageLog, bool bWireframe)
```
Logs cylinder shape - recording for Visual Logs has to be enabled to record this data

### LogLocation
```angelscript
void LogLocation(UObject WorldContextObject, FVector Location, FString Text, FLinearColor ObjectColor, float32 Radius, FName LogCategory, bool bAddToMessageLog)
```
Logs location as sphere with given radius - recording for Visual Logs has to be enabled to record this data

### LogOrientedBox
```angelscript
void LogOrientedBox(UObject WorldContextObject, FBox BoxShape, FTransform Transform, FString Text, FLinearColor ObjectColor, FName LogCategory, bool bAddToMessageLog, bool bWireframe)
```
Logs oriented box shape - recording for Visual Logs has to be enabled to record this data

### LogSegment
```angelscript
void LogSegment(UObject WorldContextObject, FVector SegmentStart, FVector SegmentEnd, FString Text, FLinearColor ObjectColor, float32 Thickness, FName CategoryName, bool bAddToMessageLog)
```
Logs segment - recording for Visual Logs has to be enabled to record this data

### LogSphere
```angelscript
void LogSphere(UObject WorldContextObject, FVector Center, float32 Radius, FString Text, FLinearColor ObjectColor, FName LogCategory, bool bAddToMessageLog, bool bWireframe)
```
Logs sphere shape - recording for Visual Logs has to be enabled to record this data

### LogText
```angelscript
void LogText(UObject WorldContextObject, FString Text, FName LogCategory, bool bAddToMessageLog)
```
Logs simple text string with Visual Logger - recording for Visual Logs has to be enabled to record this data

### RedirectVislog
```angelscript
void RedirectVislog(UObject SourceOwner, UObject DestinationOwner)
```
Makes SourceOwner log to DestinationOwner's vislog

