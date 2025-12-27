# UPersonaOptions

**继承自**: `UObject`

## 属性

### ShowMeshStats
- **类型**: `int`
- **描述**: Currently Stats can have None, Basic and Detailed. Please refer to EDisplayInfoMode.

### DefaultLocalAxesSelection
- **类型**: `uint`
- **描述**: Index used to determine which ViewMode should be used by default for the Animation Editor(s)

### DefaultBoneDrawSelection
- **类型**: `uint`
- **描述**: Index used to determine which Bone Draw Mode should be used by default for the Animation Editor(s)

### DefaultBoneColor
- **类型**: `FLinearColor`

### SelectedBoneColor
- **类型**: `FLinearColor`

### AffectedBoneColor
- **类型**: `FLinearColor`

### DisabledBoneColor
- **类型**: `FLinearColor`

### ParentOfSelectedBoneColor
- **类型**: `FLinearColor`

### VirtualBoneColor
- **类型**: `FLinearColor`

### SectionTimingNodeColor
- **类型**: `FLinearColor`

### NotifyTimingNodeColor
- **类型**: `FLinearColor`

### BranchingPointTimingNodeColor
- **类型**: `FLinearColor`

### bPauseAnimationOnCameraMove
- **类型**: `bool`
- **描述**: Pause the preview animation if playing when moving the camera and resume when finished

### bUseInlineSocketEditor
- **类型**: `bool`
- **描述**: Whether to use a socket editor that is created in-line inside the skeleton tree, or whether to use the separate details panel

### bFlattenSkeletonHierarchyWhenFiltering
- **类型**: `bool`
- **描述**: Whether to keep the hierarchy or flatten it when searching for bones, sockets etc.

### bHideParentsWhenFiltering
- **类型**: `bool`
- **描述**: Whether to hide parent items when filtering or to display them grayed out

### bExpandTreeOnSelection
- **类型**: `bool`
- **描述**: Whether to focus and expand an item's tree recursively based on selection

### bAllowPreviewMeshCollectionsToSelectFromDifferentSkeletons
- **类型**: `bool`

### bAllowPreviewMeshCollectionsToUseCustomAnimBP
- **类型**: `bool`

### bAllowMeshSectionSelection
- **类型**: `bool`
- **描述**: Whether or not Skeletal Mesh Section selection should be enabled by default for the Animation Editor(s)

### NumFolderFiltersInAssetBrowser
- **类型**: `uint`
- **描述**: The number of folder filters to allow at any one time in the animation tool's asset browser

### bAllowIncompatibleSkeletonSelection
- **类型**: `bool`
- **描述**: Whether to allow animation assets that are incompatible with the current skeleton/skeletal mesh to be selected.

### bUseTreeViewForAnimationCurves
- **类型**: `bool`
- **描述**: Whether to use tree view for animation curves

### AnimationCurveGroupingDelimiters
- **类型**: `FString`
- **描述**: Delimiters to split animation curve names for grouping

### bAutoAlignFloorToMesh
- **类型**: `bool`

### bAlwaysOpenAnimationAssetsInNewTab
- **类型**: `bool`

### bShowGrid
- **类型**: `bool`

### bHighlightOrigin
- **类型**: `bool`

### bMuteAudio
- **类型**: `bool`

