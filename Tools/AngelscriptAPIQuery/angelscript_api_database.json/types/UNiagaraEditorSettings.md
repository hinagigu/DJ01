# UNiagaraEditorSettings

**继承自**: `UDeveloperSettings`

## 属性

### DefaultScript
- **类型**: `FSoftObjectPath`
- **描述**: Niagara script to duplicate as the base of all new script assets created.

### DefaultDynamicInputScript
- **类型**: `FSoftObjectPath`
- **描述**: Niagara script to duplicate as the base of all new script assets created.

### DefaultFunctionScript
- **类型**: `FSoftObjectPath`
- **描述**: Niagara script to duplicate as the base of all new script assets created.

### DefaultModuleScript
- **类型**: `FSoftObjectPath`
- **描述**: Niagara script to duplicate as the base of all new script assets created.

### RequiredSystemUpdateScript
- **类型**: `FSoftObjectPath`
- **描述**: Niagara script which is required in the system update script to control system state.

### DefaultValidationRuleSets
- **类型**: `TArray<TSoftObjectPtr<UNiagaraValidationRuleSet>>`
- **描述**: Validation rules applied to all Niagara systems.

### GraphCreationShortcuts
- **类型**: `TArray<FNiagaraSpawnShortcut>`
- **描述**: Shortcut key bindings that if held down while doing a mouse click, will spawn the specified type of Niagara node.

### bSimplifyStackNodesAtLowResolution
- **类型**: `bool`
- **描述**: If true then emitter and system nodes will show a simplified representation on low zoom levels. This improves performance and readablity when zoomed out of the system overview graph.

### LowResolutionNodeMaxNameChars
- **类型**: `int`
- **描述**: The max number of chars before names on the low resolution nodes are truncated.

### bAlwaysZoomToFitSystemGraph
- **类型**: `bool`
- **描述**: If true then the system editor will zoom to fit all emitters when opening an asset.

### RendererCategoryExpandState
- **类型**: `ENiagaraCategoryExpandState`

### DefaultsSequencerSubtracks
- **类型**: `ENiagaraAddDefaultsTrackMode`

### bAutoCompile
- **类型**: `bool`
- **描述**: Whether or not auto-compile is enabled in the editors.

### bAutoPlay
- **类型**: `bool`
- **描述**: Whether or not simulations should start playing automatically when the emitter or system editor is opened, or when the data is changed in the editor.

### bResetSimulationOnChange
- **类型**: `bool`
- **描述**: Whether or not the simulation should reset when a value on the emitter or system is changed.

### bResimulateOnChangeWhilePaused
- **类型**: `bool`
- **描述**: Whether or not to rerun the simulation to the current time when making modifications while paused.

### bResetDependentSystemsWhenEditingEmitters
- **类型**: `bool`
- **描述**: Whether or not to reset all components that include the system currently being reset.

### bDisplayAdvancedParameterPanelCategories
- **类型**: `bool`
- **描述**: Whether or not to display advanced categories for the parameter panel.

### bDisplayAffectedAssetStats
- **类型**: `bool`
- **描述**: If true, then the emitter and script editors will show an info message how many downstream asset are affected by a change. Gathering this information for large asset graphs can delay the opening of the asset editors a bit.

### AffectedAssetSearchLimit
- **类型**: `int`
- **描述**: The maximum amount of asset references that are searched before stopping. Setting this too high can lead to long load times when opening default assets (basically the same as disabling the breadth limit in the reference viewer).

### bUpdateStackValuesOnCommitOnly
- **类型**: `bool`
- **描述**: This affects numeric inputs for modules. When set to false, the inputs update the simulation while typing. When set to true, the simulation is only updated after submitting the change by pressing Enter.

### PlaybackSpeeds
- **类型**: `TArray<float32>`
- **描述**: Speeds used for slowing down and speeding up the playback speeds

### ActionColors
- **类型**: `FNiagaraActionColors`

### CurveTemplates
- **类型**: `TArray<FNiagaraCurveTemplate>`

