# __EAssetRegistryWritebackMethod

The list of possible registry writebacks. During staging, iostore can
optionally write back data that is only available during the staging process
so that asset registry tools can associate this data with their respective
assets.

Note that this is used in UnrealPak and thus can't use StaticEnum<>, so if you
add any types here, be sure to add the parsing of the strings to IoStoreUtilities.cpp.

## 属性

### Disabled
- **类型**: `EAssetRegistryWritebackMethod`

### OriginalFile
- **类型**: `EAssetRegistryWritebackMethod`

### AdjacentFile
- **类型**: `EAssetRegistryWritebackMethod`

### EAssetRegistryWritebackMethod_MAX
- **类型**: `EAssetRegistryWritebackMethod`

