# FMVVMBlueprintViewModelContext

## 属性

### NotifyFieldValueClass
- **类型**: `UClass`

### ViewModelName
- **类型**: `FName`
- **描述**: Property name that will be generated.

### CreationType
- **类型**: `EMVVMBlueprintViewModelContextCreationType`
- **描述**: When the view is spawn, create an instance of the viewmodel.

### GlobalViewModelIdentifier
- **类型**: `FName`
- **描述**: Identifier of an already registered viewmodel.

### ViewModelPropertyPath
- **类型**: `FString`
- **描述**: The Path to get the viewmodel instance.

### Resolver
- **类型**: `UMVVMViewModelContextResolver`

### InstancedViewModel
- **类型**: `UMVVMBlueprintInstancedViewModelBase`

### bCreateSetterFunction
- **类型**: `bool`
- **描述**: Generate a public setter for this viewmodel.
@note Always true when the Creation Type is Manual.

### bCreateGetterFunction
- **类型**: `bool`
- **描述**: Generate a public getter for this viewmodel.
@note Always false when using a Instanced viewmodel.

### bOptional
- **类型**: `bool`
- **描述**: Optional. Will not warn if the instance is not set or found.
@note Always true when the Creation Type is Manual.

### bExposeInstanceInEditor
- **类型**: `bool`
- **描述**: Expose the viewmodel instance on every instance of the user widget for modification in editor.

## 方法

### opAssign
```angelscript
FMVVMBlueprintViewModelContext& opAssign(FMVVMBlueprintViewModelContext Other)
```

