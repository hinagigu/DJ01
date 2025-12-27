# UNodeMappingContainer

**继承自**: `UObject`

Node Mapping Container Class
* This saves source items, and target items, and mapping between
* Used by Retargeting, Control Rig mapping. Will need to improve interface better

## 属性

### SourceToTarget
- **类型**: `TMap<FName,FName>`

### SourceAsset
- **类型**: `TSoftObjectPtr<UObject>`
- **描述**: source asset that is used to create source
should be UNodeMappingProviderInterface

### TargetAsset
- **类型**: `TSoftObjectPtr<UObject>`
- **描述**: source asset that is used to create target
should be UNodeMappingProviderInterface

