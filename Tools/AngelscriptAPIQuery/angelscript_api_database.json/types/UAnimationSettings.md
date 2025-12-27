# UAnimationSettings

**继承自**: `UDeveloperSettings`

Default animation settings.

## 属性

### KeyEndEffectorsMatchNameArray
- **类型**: `TArray<FString>`
- **描述**: List of bone names to treat with higher precision, in addition to any bones with sockets

### ForceRecompression
- **类型**: `bool`
- **描述**: If true, this will forcibly recompress every animation, this should not be checked in enabled

### bForceBelowThreshold
- **类型**: `bool`
- **描述**: If true and the existing compression error is greater than Alternative Compression Threshold, then any compression technique (even one that increases the size) with a lower error will be used until it falls below the threshold

### bFirstRecompressUsingCurrentOrDefault
- **类型**: `bool`
- **描述**: If true, then the animation will be first recompressed with it's current compressor if non-NULL, or with the global default compressor (specified in the engine ini)
Also known as "Run Current Default Compressor"

### bEnablePerformanceLog
- **类型**: `bool`
- **描述**: If true, recompression will log performance information

### bStripAnimationDataOnDedicatedServer
- **类型**: `bool`
- **描述**: If true, animation track data will be stripped from dedicated server cooked data

### bTickAnimationOnSkeletalMeshInit
- **类型**: `bool`
- **描述**: If true, pre-4.19 behavior of zero-ticking animations during skeletal mesh init

### BoneTimecodeCustomAttributeNameSettings
- **类型**: `FTimecodeCustomAttributeNameSettings`
- **描述**: Names that identify bone animation attributes representing the individual components of a timecode and a subframe along with a take name.
          These will be included in the list of bone custom attribute names to import.

### BoneCustomAttributesNames
- **类型**: `TArray<FCustomAttributeSetting>`
- **描述**: List of animation attribute names to import directly on their corresponding bone names. The meaning field allows to contextualize the attribute name and customize tooling for it.

### BoneNamesWithCustomAttributes
- **类型**: `TArray<FString>`
- **描述**: List of bone names for which all animation attributes are directly imported on the bone.

### AttributeBlendModes
- **类型**: `TMap<FName,ECustomAttributeBlendType>`
- **描述**: Animation Attribute specific blend types (by name)

### DefaultAttributeBlendMode
- **类型**: `ECustomAttributeBlendType`
- **描述**: Default Animation Attribute blend type

### TransformAttributeNames
- **类型**: `TArray<FString>`
- **描述**: Names to match against when importing FBX node transform curves as attributes (can use ? and * wildcards)

### UserDefinedStructAttributes
- **类型**: `TArray<TSoftObjectPtr<UUserDefinedStruct>>`
- **描述**: Register user defined structs as animation attributes

### MirrorFindReplaceExpressions
- **类型**: `TArray<FMirrorFindReplaceExpression>`
- **描述**: Find and Replace Expressions used for mirroring

### DefaultFrameRate
- **类型**: `FFrameRate`
- **描述**: Project specific default frame-rate used when (re)initializing any animation based data

### bEnforceSupportedFrameRates
- **类型**: `bool`
- **描述**: Whether to enforce the project to only use entries from SupportedFrameRates for the animation assets, if disable will warn instead

## 方法

### GetBoneCustomAttributeNamesToImport
```angelscript
TArray<FString> GetBoneCustomAttributeNamesToImport()
```
Gets the complete list of bone animation attribute names to consider for import.
          This includes the designated timecode animation attributes as well as other bone animation attributes identified in the settings.

