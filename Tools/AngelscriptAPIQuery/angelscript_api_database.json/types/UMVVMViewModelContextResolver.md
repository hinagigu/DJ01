# UMVVMViewModelContextResolver

**继承自**: `UObject`

Shared data to find or create a ViewModel at runtime.

## 属性

### AllowedViewModelClasses
- **类型**: `TArray<FSoftClassPath>`
- **描述**: Viewmodel class that the resolver supports.

### DeniedViewModelClasses
- **类型**: `TArray<FSoftClassPath>`
- **描述**: Viewmodel class that the resolver explicitly does not support.

## 方法

### DestroyInstance
```angelscript
void DestroyInstance(const UObject ViewModel, const UMVVMView View)
```

