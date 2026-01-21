# UMVVMViewModelCollectionObject

**继承自**: `UObject`

## 方法

### AddViewModelInstance
```angelscript
bool AddViewModelInstance(FMVVMViewModelContext Context, UMVVMViewModelBase ViewModel)
```

### FindFirstViewModelInstanceOfType
```angelscript
UMVVMViewModelBase FindFirstViewModelInstanceOfType(TSubclassOf<UMVVMViewModelBase> ViewModelClass)
```
Finds a View Model of the given type.
If the collection contains multiple instances of the same type then this will return the first one found.

### FindViewModelInstance
```angelscript
UMVVMViewModelBase FindViewModelInstance(FMVVMViewModelContext Context)
```

### RemoveAllViewModelInstance
```angelscript
int RemoveAllViewModelInstance(UMVVMViewModelBase ViewModel)
```

### RemoveViewModel
```angelscript
bool RemoveViewModel(FMVVMViewModelContext Context)
```

