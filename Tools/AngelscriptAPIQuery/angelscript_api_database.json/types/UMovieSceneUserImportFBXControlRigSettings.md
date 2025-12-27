# UMovieSceneUserImportFBXControlRigSettings

**继承自**: `UObject`

## 属性

### FindAndReplaceStrings
- **类型**: `TArray<FControlFindReplaceString>`
- **描述**: Strings In Imported Node To Find And Replace

### bStripNamespace
- **类型**: `bool`
- **描述**: Will strip any namespace from the FBX node names

### bForceFrontXAxis
- **类型**: `bool`
- **描述**: Convert the scene from FBX coordinate system to UE coordinate system with front X axis instead of -Y

### bConvertSceneUnit
- **类型**: `bool`
- **描述**: Convert the scene from FBX unit to UE unit(centimeter)

### ImportUniformScale
- **类型**: `float32`
- **描述**: Import Uniform Scale

### bImportOntoSelectedControls
- **类型**: `bool`
- **描述**: Whether or not import onto selected controls or all controls

### TimeToInsertOrReplaceAnimation
- **类型**: `FFrameNumber`
- **描述**: Time that we insert or replace the imported animation

### bInsertAnimation
- **类型**: `bool`
- **描述**: Whether or not we insert or replace, by default we insert

### bSpecifyTimeRange
- **类型**: `bool`
- **描述**: Whether to import over specific Time Range

### StartTimeRange
- **类型**: `FFrameNumber`
- **描述**: Start Time Range To Import

### EndTimeRange
- **类型**: `FFrameNumber`
- **描述**: End Time Range To Import

### ControlChannelMappings
- **类型**: `TArray<FControlToTransformMappings>`
- **描述**: Mappings for how Control Rig Control Attributes Map to the incoming Transforms

## 方法

### LoadControlMappingsFromPreset
```angelscript
void LoadControlMappingsFromPreset(bool bMetaHumanPreset)
```
Load the default or metahuman preset into the current mappings

