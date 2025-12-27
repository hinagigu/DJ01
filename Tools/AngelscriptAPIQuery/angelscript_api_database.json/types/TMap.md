# TMap

## 方法

### opIndex
```angelscript
V& opIndex(K Key)
```

### opIndex
```angelscript
V opIndex(K Key)
```

### Add
```angelscript
void Add(K Key, V Value)
```

### Contains
```angelscript
bool Contains(K Key)
```

### RemoveAndCopyValue
```angelscript
bool RemoveAndCopyValue(K Key, V&out OutValue)
```

### Remove
```angelscript
bool Remove(K Key)
```

### Num
```angelscript
int Num()
```

### IsEmpty
```angelscript
bool IsEmpty()
```

### FindOrAdd
```angelscript
V& FindOrAdd(K Key)
```
Find the value associated with the key. If none exists, add and return a new value using the default constructor.

### FindOrAdd
```angelscript
V& FindOrAdd(K Key, V DefaultValue)
```
Find the value associated with the key. If none exists, add and return new value set to DefaultValue.

### Find
```angelscript
bool Find(K Key, V&out OutValue)
```
Find the value associated with the key. If none exists, return false. Copies the found value to OutValue.

### opAssign
```angelscript
TMap<K,V>& opAssign(TMap<K,V> Other)
```

### Empty
```angelscript
void Empty(int Slack)
```

### Reset
```angelscript
void Reset()
```

### GetKeys
```angelscript
void GetKeys(TArray<K>& OutKeys)
```
Generates a list of the keys present in the map and stores them in the given array.

### GetValues
```angelscript
void GetValues(TArray<K>& OutValues)
```
Generates a list of the values present in the map and stores them in the given array.

### Iterator
```angelscript
TMapIterator<K,V> Iterator()
```

### Iterator
```angelscript
TMapConstIterator<K,V> Iterator()
```

