# UComboGraphProjectSettings

**继承自**: `UObject`

## 属性

### MontageNodeColor
- **类型**: `FLinearColor`
- **描述**: Default background color for Montage nodes

### SequenceNodeColor
- **类型**: `FLinearColor`
- **描述**: Default background color for Sequence nodes

### DebugActiveColor
- **类型**: `FLinearColor`
- **描述**: Default background color for combo nodes in active states (during debug)

### DebugFadeTime
- **类型**: `float32`
- **描述**: The duration used to interpolate the background color of nodes from Active to Default color when active states change (no longer active during debug).

If set to 0.0, will disable color interpolation.

### ContentMargin
- **类型**: `FMargin`
- **描述**: The padding around the main node box.

### ContentInternalPadding
- **类型**: `FMargin`
- **描述**: The padding within the main node box.

### PinSize
- **类型**: `float32`
- **描述**: The minimum desired sizes for pin connections.

### PinPadding
- **类型**: `float32`
- **描述**: The minimum amount of padding to draw around pin connections.

### ContextMapping
- **类型**: `TSoftObjectPtr<UInputMappingContext>`
- **描述**: Enhanced Input Context Mapping to use to draw edge (transition) icons in Graphs

### IconsDataTable
- **类型**: `TSoftObjectPtr<UDataTable>`
- **描述**: Path to the DataTable used to draw edge (transition) icons in Graph. Determine mappings between Keys and Icon textures.

This is set by default to an internal DataTables (that you can find in `/ComboGraph/Xelu_Icons/`) that setup texture icons for every keyboard and gamepad key.

Icons are coming from Xelu's Free Controllers & Keyboard Prompts: https://thoseawesomeguys.com/prompts/
Thanks to "Nicolae (Xelu) Berbece" and "Those Awesome Guys" to make it available in the public domain licence under Creative Commons 0 (CC0)

### IconPreference
- **类型**: `EComboGraphIconType`
- **描述**: Icon preference to draw edge (transition) icons in Graph. Can be either Keyboard or Gamepad based

### IconSize
- **类型**: `float32`
- **描述**: Size of Icons when drawing edges (transitions) in Combo Graphs

### DynamicMontageSlotName
- **类型**: `FName`
- **描述**: The Slot Name to use with dynamic montages, created from sequences

### NotifyStates
- **类型**: `TMap<TSoftClassPtr<UAnimNotifyState>,FComboGraphNotifyStateAutoSetup>`
- **描述**: Map of Auto Setup Animation Notify States. The key is the Anim Notify State class, the value is the time start / end definition in percent

### bSequencesNetworkedWarning
- **类型**: `bool`
- **描述**: Flag to enable / disable message warnings (logs and on screen) about Sequences being used in a networked environment

