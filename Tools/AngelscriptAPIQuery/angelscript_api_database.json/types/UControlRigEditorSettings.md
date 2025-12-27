# UControlRigEditorSettings

**继承自**: `URigVMEditorSettings`

Customize Control Rig Editor.

## 属性

### bResetControlsOnCompile
- **类型**: `bool`
- **描述**: When this is checked all controls will return to their initial
value as the user hits the Compile button.

### bResetControlsOnPinValueInteraction
- **类型**: `bool`
- **描述**: When this is checked all controls will return to their initial
value as the user interacts with a pin value

### bResetPoseWhenTogglingEventQueue
- **类型**: `bool`
- **描述**: When this is checked all elements will be reset to their initial value
if the user changes the event queue (for example between forward / backward solve)

### bEnableUndoForPoseInteraction
- **类型**: `bool`
- **描述**: When this is checked any hierarchy interaction within the Control Rig
Editor will be stored on the undo stack

### bResetControlTransformsOnCompile
- **类型**: `bool`
- **描述**: When checked controls will be reset during a manual compilation
(when pressing the Compile button)

### RigUnitPinExpansion
- **类型**: `TMap<FString,FControlRigSettingsPerPinBool>`
- **描述**: A map which remembers the expansion setting for each rig unit pin.

### ConstructionEventBorderColor
- **类型**: `FLinearColor`
- **描述**: The border color of the viewport when entering "Construction Event" mode

### BackwardsSolveBorderColor
- **类型**: `FLinearColor`
- **描述**: The border color of the viewport when entering "Backwards Solve" mode

### BackwardsAndForwardsBorderColor
- **类型**: `FLinearColor`
- **描述**: The border color of the viewport when entering "Backwards And Forwards" mode

### bShowStackedHierarchy
- **类型**: `bool`
- **描述**: Option to toggle displaying the stacked hierarchy items.
Note that changing this option potentially requires to re-open the editors in question.

### MaxStackSize
- **类型**: `int`
- **描述**: The maximum number of stacked items in the view
Note that changing this option potentially requires to re-open the editors in question.

### bLeftMouseDragDoesMarquee
- **类型**: `bool`
- **描述**: If turned on we'll offer box / marquee selection in the control rig editor viewport.

