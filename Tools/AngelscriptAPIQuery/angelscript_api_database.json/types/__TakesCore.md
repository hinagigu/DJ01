# __TakesCore

## 方法

### ComputeNextTakeNumber
```angelscript
int ComputeNextTakeNumber(FString Slate)
```
Compute the next unused sequential take number for the specified slate

### FindTakes
```angelscript
TArray<FAssetData> FindTakes(FString Slate, int TakeNumber)
```
Find all the existing takes that were recorded with the specified slate

@param Slate        The slate to filter by
@param TakeNumber   The take number to filter by. <=0 denotes all takes

### SetOnTakeRecorderSlateChanged
```angelscript
void SetOnTakeRecorderSlateChanged(FOnTakeRecorderSlateChanged__TakesCoreBlueprintLibrary OnTakeRecorderSlateChanged)
```
Called when the slate is changed.

### SetOnTakeRecorderTakeNumberChanged
```angelscript
void SetOnTakeRecorderTakeNumberChanged(FOnTakeRecorderTakeNumberChanged__TakesCoreBlueprintLibrary OnTakeRecorderTakeNumberChanged)
```
Called when the take number is changed.

