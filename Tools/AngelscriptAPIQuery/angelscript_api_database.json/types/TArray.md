# TArray

## 方法

### opIndex
```angelscript
T& opIndex(int Index)
```

### opIndex
```angelscript
T opIndex(int Index)
```

### opAssign
```angelscript
TArray<T>& opAssign(TArray<T> Other)
```

### opEquals
```angelscript
bool opEquals(TArray<T> Other)
```

### Add
```angelscript
void Add(T Value)
```

### Append
```angelscript
void Append(TArray<T> Other)
```

### Shuffle
```angelscript
void Shuffle()
```

### Swap
```angelscript
void Swap(int FirstIndexToSwap, int SecondIndexToSwap)
```
Swap the element at index FirstIndexToSwap with the element at index SecondIndexToSwap.


### MoveAssignFrom
```angelscript
void MoveAssignFrom(TArray<T>& OtherArray)
```
Perform a move-assign from the passed in array into this array.
The passed in array will be emptied in the process as its memory is moved over.

### IsValidIndex
```angelscript
bool IsValidIndex(int Index)
```

### Last
```angelscript
T Last(int IndexFromEnd)
```

### Last
```angelscript
T& Last(int IndexFromEnd)
```

### Insert
```angelscript
void Insert(T Value, int Index)
```

### AddUnique
```angelscript
bool AddUnique(T Value)
```
Will first do a check if the object already is in the array.
Returns 'True' if the object is added.


### Empty
```angelscript
void Empty(int ReservedSize)
```

### Reset
```angelscript
void Reset(int ReservedSize)
```

### Reserve
```angelscript
void Reserve(int ReservedSize)
```

### SetNum
```angelscript
void SetNum(int NewNum)
```

### Copy
```angelscript
void Copy(TArray<T> SourceArray, int SourceIndex, int Count, int TargetIndex)
```

### SetNumZeroed
```angelscript
void SetNumZeroed(int NewNum)
```

### FindIndex
```angelscript
int FindIndex(T Value)
```
Find the first index that contains an element with the given value.
If no element matches the value, it will return -1.

### Contains
```angelscript
bool Contains(T Value)
```

### RemoveSingle
```angelscript
int RemoveSingle(T Value)
```

### Remove
```angelscript
int Remove(T Value)
```

### RemoveSingleSwap
```angelscript
int RemoveSingleSwap(T Value)
```

### RemoveSwap
```angelscript
int RemoveSwap(T Value)
```

### RemoveAt
```angelscript
void RemoveAt(int Index)
```

### RemoveAtSwap
```angelscript
void RemoveAtSwap(int Index)
```

### Sort
```angelscript
void Sort(bool bDescendingOrder)
```

### Num
```angelscript
int Num()
```

### Max
```angelscript
int Max()
```

### GetAllocatedSize
```angelscript
int64 GetAllocatedSize()
```

### IsEmpty
```angelscript
bool IsEmpty()
```

### GetSlack
```angelscript
int GetSlack()
```

### Shrink
```angelscript
void Shrink()
```

### Iterator
```angelscript
TArrayIterator<T> Iterator()
```

### Iterator
```angelscript
TArrayConstIterator<T> Iterator()
```

