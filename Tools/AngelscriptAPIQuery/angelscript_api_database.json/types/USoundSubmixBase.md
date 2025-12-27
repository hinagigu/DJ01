# USoundSubmixBase

**继承自**: `UObject`

## 属性

### bAutoDisable
- **类型**: `bool`

### AutoDisableTime
- **类型**: `float32`

### ChildSubmixes
- **类型**: `TArray<TObjectPtr<USoundSubmixBase>>`
- **描述**: Child submixes to this sound mix

## 方法

### DynamicConnect
```angelscript
bool DynamicConnect(USoundSubmixBase InParent)
```
Dynamically Connects to a parent submix.
@param        WorldContextObject      UObject that's used to GetWorld
@param        InParent        Parent Submix to connect to

### DynamicDisconnect
```angelscript
bool DynamicDisconnect()
```
Dynamically Disconnect from a parent.
@param        WorldContextObject      UObject that's used to GetWorld

### FindDynamicAncestor
```angelscript
USoundSubmixBase FindDynamicAncestor()
```
Searching upwards from this Submix to the root looking for the first Submix marked Dynamic
If this Submix is Dynamic this will be returned.

