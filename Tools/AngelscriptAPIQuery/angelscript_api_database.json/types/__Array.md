# __Array

## 方法

### FilterArray
```angelscript
void FilterArray(TArray<AActor> TargetArray, TSubclassOf<AActor> FilterClass, TArray<AActor>& FilteredArray)
```
*Filter an array based on a Class derived from Actor.
*
*@param        TargetArray             The array to filter from
*@param        FilterClass             The Actor sub-class type that acts as the filter, only objects derived from it will be returned.
*@return       An array containing only those objects which are derived from the class specified.

### SortByteArray
```angelscript
void SortByteArray(TArray<uint8>& TargetArray, bool bStableSort, EArraySortOrder SortOrder)
```
Sorts an array of bytes.

@param       TargetArray             The array to sort.
@param       bStableSort             If a stable sort should be used. This preserves the order of identical elements, but is slower.
@param       SortOrder               If the array should be sorted in ascending or descending order.

### SortFloatArray
```angelscript
void SortFloatArray(TArray<float>& TargetArray, bool bStableSort, EArraySortOrder SortOrder)
```
Sorts an array of doubles.

@param       TargetArray             The array to sort.
@param       bStableSort             If a stable sort should be used. This preserves the order of identical elements, but is slower.
@param       SortOrder               If the array should be sorted in ascending or descending order.

### SortInt64Array
```angelscript
void SortInt64Array(TArray<int64>& TargetArray, bool bStableSort, EArraySortOrder SortOrder)
```
Sorts an array of 64-bit integers.

@param       TargetArray             The array to sort.
@param       bStableSort             If a stable sort should be used. This preserves the order of identical elements, but is slower.
@param       SortOrder               If the array should be sorted in ascending or descending order.

### SortIntArray
```angelscript
void SortIntArray(TArray<int>& TargetArray, bool bStableSort, EArraySortOrder SortOrder)
```
Sorts an array of integers.

@param       TargetArray             The array to sort.
@param       bStableSort             If a stable sort should be used. This preserves the order of identical elements, but is slower.
@param       SortOrder               If the array should be sorted in ascending or descending order.

### SortNameArray
```angelscript
void SortNameArray(TArray<FName>& TargetArray, bool bStableSort, bool bLexicalSort, EArraySortOrder SortOrder)
```
Sorts an array of FNames.

@param       TargetArray             The array to sort.
@param       bStableSort             If a stable sort should be used. This preserves the order of identical elements, but is slower.
@param       bLexicalSort    If the names should be sorted based on the string value of the name rather than the comparison index. This is slower when enabled.
@param       SortOrder               If the array should be sorted in ascending or descending order.

### SortStringArray
```angelscript
void SortStringArray(TArray<FString>& TargetArray, bool bStableSort, EArraySortOrder SortOrder)
```
Sorts an array of strings alphabetically.

@param       TargetArray             The array to sort.
@param       bStableSort             If a stable sort should be used. This preserves the order of identical elements, but is slower.
@param       SortOrder               If the array should be sorted in ascending or descending order.

