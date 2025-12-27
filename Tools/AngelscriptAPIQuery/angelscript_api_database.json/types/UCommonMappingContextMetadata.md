# UCommonMappingContextMetadata

**继承自**: `UDataAsset`

Base CommonUI metadata implementation for specification in IMC's.

Utilizes a map of input actions to metadata to prevent users from having to create
multiple metadata assets / instances. Using this map is not mandatory.

## 属性

### EnhancedInputMetadata
- **类型**: `UCommonInputMetadata`

### PerActionEnhancedInputMetadata
- **类型**: `TMap<TObjectPtr<UInputAction>,TObjectPtr<UCommonInputMetadata>>`

