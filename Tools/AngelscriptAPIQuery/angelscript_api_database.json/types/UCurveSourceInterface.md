# UCurveSourceInterface

**继承自**: `UInterface`

## 方法

### GetBindingName
```angelscript
FName GetBindingName()
```
Get the name that this curve source can be bound to by.
Clients of this curve source will use this name to identify this source.

### GetCurves
```angelscript
void GetCurves(TArray<FNamedCurveValue>& OutValues)
```
Evaluate all curves that this source provides

### GetCurveValue
```angelscript
float32 GetCurveValue(FName CurveName)
```
Get the value for a specified curve

