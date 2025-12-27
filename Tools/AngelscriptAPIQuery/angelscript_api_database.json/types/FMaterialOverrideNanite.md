# FMaterialOverrideNanite

Storage for nanite material override.
An override material can be selected, and the override material can be used according to the current settings.
We handle removing the override material and its dependencies from the cook on platforms where we can determine
that the override material can never be used.

## 属性

### OverrideMaterialEditor
- **类型**: `UMaterialInterface`
- **描述**: EditorOnly version of the OverrideMaterial reference.
This is a hard reference, but is editoronly. We rely on -skiponlyeditoronly to avoid pulling this editoronly hard reference into the cook.

## 方法

### opAssign
```angelscript
FMaterialOverrideNanite& opAssign(FMaterialOverrideNanite Other)
```

