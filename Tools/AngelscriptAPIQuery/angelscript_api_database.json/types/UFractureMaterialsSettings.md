# UFractureMaterialsSettings

**继承自**: `UFractureToolSettings`

Settings related to setting materials on a Geometry Collection *

## 属性

### Materials
- **类型**: `TArray<TObjectPtr<UMaterialInterface>>`
- **描述**: Materials on the selected Geometry Collection's underlying asset (the Rest Collection).

### bOnlySelectedComponents
- **类型**: `bool`
- **描述**: Whether 'Use Asset Materials On Components' should only update the selected components, or update all components using this asset

### AssignMaterial
- **类型**: `FString`
- **描述**: Material to assign to selected faces

### ToFaces
- **类型**: `EMaterialAssignmentTargets`
- **描述**: Which subset of faces to update materials assignments on, for the selected geometry

### bOnlySelectedBones
- **类型**: `bool`
- **描述**: Whether to only assign materials for faces in the selected bones, or the whole geometry collection

