# FReAssignMaterialInCollectionDataflowNode

Reassign existing material(s) to Outside/Inside faces

## 属性

### Materials
- **类型**: `TArray<TObjectPtr<UMaterial>>`
- **描述**: Materials array storing the materials

### OutsideMaterialIdx
- **类型**: `int`
- **描述**: Index of the material in the Materials array to assign to the outside faces from the face selection

### InsideMaterialIdx
- **类型**: `int`
- **描述**: Index of the material in the Materials array to assign to the inside faces from the face selection

### bAssignOutsideMaterial
- **类型**: `bool`
- **描述**: If true, the selected material from the Materials array will be assigned to the outside faces from the face selection

### bAssignInsideMaterial
- **类型**: `bool`
- **描述**: If true, the selected material from the Materials array will be assigned to the inside faces from the face selection

### bActive
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FReAssignMaterialInCollectionDataflowNode& opAssign(FReAssignMaterialInCollectionDataflowNode Other)
```

