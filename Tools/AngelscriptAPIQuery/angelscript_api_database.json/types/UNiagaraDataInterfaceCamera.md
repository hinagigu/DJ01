# UNiagaraDataInterfaceCamera

**继承自**: `UNiagaraDataInterface`

## 属性

### PlayerControllerIndex
- **类型**: `int`
- **描述**: This is used to determine which camera position to query for cpu emitters. If no valid index is supplied, the first controller is used as camera reference.

### bRequireCurrentFrameData
- **类型**: `bool`
- **描述**: When this option is disabled, we use the previous frame's data for the camera and issue the simulation early. This greatly
      reduces overhead and allows the game thread to run faster, but comes at a tradeoff if the dependencies might leave gaps or other visual artifacts.

