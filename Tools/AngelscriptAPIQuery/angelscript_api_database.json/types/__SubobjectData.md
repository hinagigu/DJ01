# __SubobjectData

## 方法

### CanCopy
```angelscript
bool CanCopy(FSubobjectData Data)
```
@return Whether or not this object represents a subobject that can be copied

### CanDelete
```angelscript
bool CanDelete(FSubobjectData Data)
```
@return Whether or not this object represents a subobject that can be deleted

### CanDuplicate
```angelscript
bool CanDuplicate(FSubobjectData Data)
```
@return Whether or not this object represents a subobject that can be duplicated

### CanEdit
```angelscript
bool CanEdit(FSubobjectData Data)
```
@return Whether or not we can edit properties for this subobject

### CanRename
```angelscript
bool CanRename(FSubobjectData Data)
```

### CanReparent
```angelscript
bool CanReparent(FSubobjectData Data)
```
@return Whether or not this object represents a subobject that can
be reparented to other subobjects based on its context.

### GetData
```angelscript
void GetData(FSubobjectDataHandle DataHandle, FSubobjectData& OutData)
```

### GetHandle
```angelscript
void GetHandle(FSubobjectData Data, FSubobjectDataHandle& OutHandle)
```
@return Get the handle for this subobject data

### GetObject
```angelscript
const UObject GetObject(FSubobjectData Data, bool bEvenIfPendingKill)
```

### GetObjectForBlueprint
```angelscript
const UObject GetObjectForBlueprint(FSubobjectData Data, UBlueprint Blueprint)
```

### GetVariableName
```angelscript
FName GetVariableName(FSubobjectData Data)
```

### IsActor
```angelscript
bool IsActor(FSubobjectData Data)
```

### IsAttachedTo
```angelscript
bool IsAttachedTo(FSubobjectData Data, FSubobjectDataHandle InHandle)
```

### IsChildActor
```angelscript
bool IsChildActor(FSubobjectData Data)
```

### IsComponent
```angelscript
bool IsComponent(FSubobjectData Data)
```
Returns true if this subobject is a component.

### IsDefaultSceneRoot
```angelscript
bool IsDefaultSceneRoot(FSubobjectData Data)
```

### IsHandleValid
```angelscript
bool IsHandleValid(FSubobjectDataHandle DataHandle)
```

### IsInheritedComponent
```angelscript
bool IsInheritedComponent(FSubobjectData Data)
```

### IsInstancedActor
```angelscript
bool IsInstancedActor(FSubobjectData Data)
```

### IsInstancedComponent
```angelscript
bool IsInstancedComponent(FSubobjectData Data)
```

### IsNativeComponent
```angelscript
bool IsNativeComponent(FSubobjectData Data)
```

### IsRootActor
```angelscript
bool IsRootActor(FSubobjectData Data)
```

### IsRootComponent
```angelscript
bool IsRootComponent(FSubobjectData Data)
```

### IsSceneComponent
```angelscript
bool IsSceneComponent(FSubobjectData Data)
```

### IsValid
```angelscript
bool IsValid(FSubobjectData Data)
```

