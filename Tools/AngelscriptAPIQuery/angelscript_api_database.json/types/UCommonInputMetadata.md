# UCommonInputMetadata

**继承自**: `UObject`

Metadata CommonUI will try to acquire from Enhanced Input Mapping Contexts (IMC)

You can Inherit from this class if you have any info that may need to be parsed per platform
by CommonUI. IMC's can be specified per platform, so each platform may have different
Common Input Metadata

Note: We intentionally do not define any context-independant metadata. Even though some
metadata should be context-independant (Like NavBarPriority below). Locking it that info
to a seperate metadata type prevents any chance of future overriding. Instead, we prefer
info for all metadata to be set across all instances.

## 属性

### NavBarPriority
- **类型**: `int`

### bIsGenericInputAction
- **类型**: `bool`

