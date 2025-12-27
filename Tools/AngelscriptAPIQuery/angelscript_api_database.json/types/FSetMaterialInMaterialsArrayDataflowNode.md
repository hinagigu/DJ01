# FSetMaterialInMaterialsArrayDataflowNode

Set a Material in a Materials array

## 属性

### Material
- **类型**: `UMaterial`
- **描述**: Material to add/insert to/in Materials array

### Operation
- **类型**: `ESetMaterialOperationTypeEnum`
- **描述**: Operation type for setting the material, add will add the new material to the end off Materials array, insert will insert the
      new material into Materials array at the index specified by MaterialIdx

### MaterialIdx
- **类型**: `int`
- **描述**: Index for inserting a nem material into the Materials array

### bActive
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FSetMaterialInMaterialsArrayDataflowNode& opAssign(FSetMaterialInMaterialsArrayDataflowNode Other)
```

