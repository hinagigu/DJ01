# __Guid

## 方法

### Conv_GuidToString
```angelscript
FString Conv_GuidToString(FGuid InGuid)
```
Converts a GUID value to a string, in the form 'A-B-C-D'

### EqualEqual_GuidGuid
```angelscript
bool EqualEqual_GuidGuid(FGuid A, FGuid B)
```
Returns true if the values are equal (A == B)

### Invalidate_Guid
```angelscript
void Invalidate_Guid(FGuid& InGuid)
```
Invalidates the given GUID

### IsValid_Guid
```angelscript
bool IsValid_Guid(FGuid InGuid)
```
Checks whether the given GUID is valid

### NewGuid
```angelscript
FGuid NewGuid()
```
Returns a new unique GUID

### NotEqual_GuidGuid
```angelscript
bool NotEqual_GuidGuid(FGuid A, FGuid B)
```
Returns true if the values are not equal (A != B)

### Parse_StringToGuid
```angelscript
void Parse_StringToGuid(FString GuidString, FGuid& OutGuid, bool& Success)
```
Converts a String of format EGuidFormats to a Guid. Returns Guid OutGuid, Returns bool Success

