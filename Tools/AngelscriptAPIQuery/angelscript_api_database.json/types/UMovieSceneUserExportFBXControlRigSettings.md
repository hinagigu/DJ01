# UMovieSceneUserExportFBXControlRigSettings

**继承自**: `UObject`

## 属性

### ExportFileName
- **类型**: `FString`
- **描述**: Imported File Name

### FbxExportCompatibility
- **类型**: `EFbxExportCompatibility`

### bForceFrontXAxis
- **类型**: `bool`
- **描述**: Convert the scene from FBX coordinate system to UE coordinate system with front X axis instead of -Y

### bExportOnlySelectedControls
- **类型**: `bool`
- **描述**: Whether or not import onto selected controls or all controls

### ControlChannelMappings
- **类型**: `TArray<FControlToTransformMappings>`
- **描述**: Mappings for how Control Rig Control Attributes Map to the incoming Transforms

### bASCII
- **类型**: `bool`

### bExportLocalTime
- **类型**: `bool`

## 方法

### LoadControlMappingsFromPreset
```angelscript
void LoadControlMappingsFromPreset(bool bMetaHumanPreset)
```
Load the default or metahuman preset into the current mappings

