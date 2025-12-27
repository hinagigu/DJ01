# UAnimationCompressionLibraryDatabase

**继承自**: `UObject`

An ACL database object references several UAnimSequence instances that it contains.

## 属性

### MediumImportanceProportion
- **类型**: `float32`
- **描述**: What percentage of the key frames should be moved to the database. Medium importance key frames are moved second.

### LowestImportanceProportion
- **类型**: `float32`
- **描述**: What percentage of the key frames should be moved to the database. Least important key frames are moved first.

### StripLowestImportanceTier
- **类型**: `FPerPlatformBool`
- **描述**: Whether or not to strip the lowest importance tier entirely from disk. Stripping the lowest tier means that the visual fidelity of Highest and Medium are equivalent.

### MaxStreamRequestSizeKB
- **类型**: `uint`
- **描述**: The maximum size in KiloBytes of streaming requests. Setting this to 0 will force tiers to load in a single request regardless of their size.

### PreviewVisualFidelity
- **类型**: `ACLVisualFidelity`
- **描述**: The level of quality to preview with the database when decompressing in the editor.

