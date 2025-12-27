# FGameplayTagBlueprintPropertyMap

Struct used to manage gameplay tag blueprint property mappings.
It registers the properties with delegates on an ability system component.
This struct can not be used in containers (such as TArray) since it uses a raw pointer
to bind the delegate and it's address could change causing an invalid binding.

## 属性

### PropertyMappings
- **类型**: `TArray<FGameplayTagBlueprintPropertyMapping>`

## 方法

### opAssign
```angelscript
FGameplayTagBlueprintPropertyMap& opAssign(FGameplayTagBlueprintPropertyMap Other)
```

