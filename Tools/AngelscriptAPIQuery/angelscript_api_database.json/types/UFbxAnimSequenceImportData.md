# UFbxAnimSequenceImportData

**继承自**: `UFbxAssetImportData`

Import data and options used when importing any mesh from FBX

## 属性

### bImportMeshesInBoneHierarchy
- **类型**: `bool`
- **描述**: If checked, meshes nested in bone hierarchies will be imported instead of being converted to bones.

### AnimationLength
- **类型**: `EFBXAnimationLengthImportType`
- **描述**: Which animation range to import. The one defined at Exported, at Animated time or define a range manually

### FrameImportRange
- **类型**: `FInt32Interval`
- **描述**: Frame range used when Set Range is used in Animation Length

### bUseDefaultSampleRate
- **类型**: `bool`
- **描述**: If enabled, samples all animation curves to 30 FPS

### CustomSampleRate
- **类型**: `int`
- **描述**: Sample fbx animation data at the specified sample rate, 0 find automaticaly the best sample rate

### bSnapToClosestFrameBoundary
- **类型**: `bool`
- **描述**: If enabled, snaps the animation to the closest frame boundary using the import sampling rate

### bImportCustomAttribute
- **类型**: `bool`
- **描述**: If true, import node attributes as either Animation Curves or Animation Attributes

### bDeleteExistingCustomAttributeCurves
- **类型**: `bool`
- **描述**: If true, all previous node attributes imported as Animation Curves will be deleted when doing a re-import.

### bDeleteExistingNonCurveCustomAttributes
- **类型**: `bool`
- **描述**: If true, all previous node attributes imported as Animation Attributes will be deleted when doing a re-import.

### bImportBoneTracks
- **类型**: `bool`
- **描述**: Import bone transform tracks. If false, this will discard any bone transform tracks. (useful for curves only animations)

### bSetMaterialDriveParameterOnCustomAttribute
- **类型**: `bool`
- **描述**: Set Material Curve Type for all custom attributes that exists

### bAddCurveMetadataToSkeleton
- **类型**: `bool`
- **描述**: Whether to automatically add curve metadata to an animation's skeleton. If this is disabled, curve metadata will be added to skeletal meshes for morph targets, but no metadata entry will be created for general curves.

### MaterialCurveSuffixes
- **类型**: `TArray<FString>`
- **描述**: Set Material Curve Type for the custom attribute with the following suffixes. This doesn't matter if Set Material Curve Type is true

### bRemoveRedundantKeys
- **类型**: `bool`
- **描述**: When importing custom attribute as curve, remove redundant keys

### bDeleteExistingMorphTargetCurves
- **类型**: `bool`
- **描述**: If enabled, this will delete this type of asset from the FBX

### bDoNotImportCurveWithZero
- **类型**: `bool`
- **描述**: When importing custom attribute or morphtarget as curve, do not import if it doesn't have any value other than zero. This is to avoid adding extra curves to evaluate

### bPreserveLocalTransform
- **类型**: `bool`
- **描述**: If enabled, this will import a curve within the animation

