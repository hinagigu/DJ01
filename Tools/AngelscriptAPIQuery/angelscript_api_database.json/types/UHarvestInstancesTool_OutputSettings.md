# UHarvestInstancesTool_OutputSettings

**继承自**: `UInteractiveToolPropertySet`

Output Settings for the Pattern Tool

## 属性

### ComponentType
- **类型**: `EHarvestInstancesToolOutputType`
- **描述**: Which type of Instanced Static Mesh Component to Create

### bSingleActor
- **类型**: `bool`
- **描述**: Group all output Instanced Components under a single Actor. By default, multiple Actors will be created.

### ActorName
- **类型**: `FString`
- **描述**: Base Name to use for the emitted single Actor

### bIncludeSingleInstances
- **类型**: `bool`

### bDeleteInputs
- **类型**: `bool`
- **描述**: Delete Actors that have had their Components harvested

