# UEditorExperimentalSettings

**继承自**: `UObject`

Implements Editor settings for experimental features.

## 属性

### bEnableAsyncTextureCompilation
- **类型**: `bool`
- **描述**: Enable async texture compilation to improve PIE and map load time performance when compilation is required

### bEnableAsyncStaticMeshCompilation
- **类型**: `bool`
- **描述**: Enable async static mesh compilation to improve import and map load time performance when compilation is required

### bEnableAsyncSkinnedAssetCompilation
- **类型**: `bool`
- **描述**: Enable async skinned asset compilation to improve import and map load time performance when compilation is required

### bEnableAsyncSoundWaveCompilation
- **类型**: `bool`
- **描述**: Enable async sound compilation to improve import and map load time performance when compilation is required

### bHDREditor
- **类型**: `bool`
- **描述**: Allows the editor to run on HDR monitors on Windows 10

### HDREditorNITLevel
- **类型**: `float32`
- **描述**: The brightness of the slate UI on HDR monitors

### bProceduralFoliage
- **类型**: `bool`
- **描述**: Allows usage of the procedural foliage system

### bEnableTranslationPicker
- **类型**: `bool`
- **描述**: Allows usage of the Translation Picker

### ConsoleForGamepadLabels
- **类型**: `EConsoleForGamepadLabels`
- **描述**: Specify which console-specific nomenclature to use for gamepad label text

### bBreakOnExceptions
- **类型**: `bool`
- **描述**: Break on Exceptions allows you to trap Access Nones and other exceptional events in Blueprints.

### bContextMenuChunkAssignments
- **类型**: `bool`
- **描述**: Allows ChunkIDs to be assigned to assets to via the content browser context menu.

### bDisableCookInEditor
- **类型**: `bool`
- **描述**: Disable cook in the editor

### bSharedCookedBuilds
- **类型**: `bool`

### bAllowLateJoinInPIE
- **类型**: `bool`
- **描述**: Enable late joining in PIE

### bAllowVulkanPreview
- **类型**: `bool`
- **描述**: Allow Vulkan Preview

### bEnableMultithreadedLightmapEncoding
- **类型**: `bool`
- **描述**: Enable multithreaded lightmap encoding (decreases time taken to encode lightmaps)

### bEnableMultithreadedShadowmapEncoding
- **类型**: `bool`
- **描述**: Enable multithreaded shadow map encoding (decreases time taken to encode shadow maps)

### bUseOpenCLForConvexHullDecomp
- **类型**: `bool`
- **描述**: Whether to use OpenCL to accelerate convex hull decomposition (uses GPU to decrease time taken to decompose meshes, currently only available on Mac OS X)

### bAllowPotentiallyUnsafePropertyEditing
- **类型**: `bool`
- **描述**: Allows editing of potentially unsafe properties during PIE. Advanced use only - use with caution.

### bFacialAnimationImporter
- **类型**: `bool`
- **描述**: Enable experimental bulk facial animation importer (found in Developer Tools menu, requires editor restart)

### bMobilePIEPreviewDeviceLaunch
- **类型**: `bool`
- **描述**: Enable experimental PIE preview device launch

### bTextAssetFormatSupport
- **类型**: `bool`
- **描述**: Enables in-editor support for text asset formats

### bVirtualizedAssetRehydration
- **类型**: `bool`
- **描述**: Enables in-editor support for rehydrating virtualized assets

### bExampleLayersAndBlends
- **类型**: `bool`
- **描述**: When creating new Material Layers and Material Layer Blends, set up example graphs.

### bEnableLongPathsSupport
- **类型**: `bool`
- **描述**: Allows creation of assets with paths longer than 260 characters. Note that this also requires the Windows 10 Anniversary Update (1607), and support for long paths to be enabled through the group policy editor.

### bPackedLevelActor
- **类型**: `bool`
- **描述**: Allows creating APackedLevelActor blueprint actors

### bLevelInstance
- **类型**: `bool`
- **描述**: Allows creating ALevelInstance actors

### bEnableWorldPartitionActorFilters
- **类型**: `bool`

### bEnableWorldPartitionExternalDataLayers
- **类型**: `bool`

