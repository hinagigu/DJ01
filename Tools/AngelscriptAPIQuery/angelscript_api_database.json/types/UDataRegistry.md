# UDataRegistry

**继承自**: `UObject`

Defines a place to efficiently store and retrieve structure data, can be used as a wrapper around Data/Curve Tables or extended with other sources

## 属性

### RegistryType
- **类型**: `FName`
- **描述**: Globally unique name used to identify this registry

### IdFormat
- **类型**: `FDataRegistryIdFormat`
- **描述**: Rules for specifying valid item Ids, if default than any name can be used

### ItemStruct
- **类型**: `const UScriptStruct`
- **描述**: Structure type of all for items in this registry

### DataSources
- **类型**: `TArray<TObjectPtr<UDataRegistrySource>>`
- **描述**: List of data sources to search for items

### TimerUpdateFrequency
- **类型**: `float32`
- **描述**: How often to check for cache updates

### DefaultCachePolicy
- **类型**: `FDataRegistryCachePolicy`
- **描述**: Editor-set cache policy

