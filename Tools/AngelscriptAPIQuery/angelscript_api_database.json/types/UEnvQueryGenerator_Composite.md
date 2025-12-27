# UEnvQueryGenerator_Composite

**继承自**: `UEnvQueryGenerator`

Composite generator allows using multiple generators in single query option
All child generators must produce exactly the same item type!

## 属性

### Generators
- **类型**: `TArray<TObjectPtr<UEnvQueryGenerator>>`

### ForcedItemType
- **类型**: `TSubclassOf<UEnvQueryItemType>`

### bAllowDifferentItemTypes
- **类型**: `bool`

