# TOptional

## 方法

### opAssign
```angelscript
TOptional<T>& opAssign(TOptional<T> Other)
```

### opAssign
```angelscript
TOptional<T>& opAssign(T Value)
```

### opEquals
```angelscript
bool opEquals(TOptional<T> Other)
```

### IsSet
```angelscript
bool IsSet()
```
Returns if the optional has a valid value. This must be true in order for Get() or GetValue() to be called.


### Set
```angelscript
void Set(T Value)
```

### GetValue
```angelscript
T GetValue()
```
Gets a const reference to the optional's set value. IsSet() must return true for this function to be called.


### GetValue
```angelscript
T& GetValue()
```
Gets a non-const reference to the optional's set value. IsSet() must return true for this function to be called.


### Get
```angelscript
T Get(T DefaultValue)
```
If set returns the optional's set value, otherwise returns DefaultValue

### Reset
```angelscript
void Reset()
```
Destruct the value inside the optional and unset it.


