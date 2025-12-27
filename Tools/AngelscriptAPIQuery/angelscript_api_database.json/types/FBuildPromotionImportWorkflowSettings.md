# FBuildPromotionImportWorkflowSettings

Holds settings for the import workflow stage of the build promotion test

## 属性

### Diffuse
- **类型**: `FEditorImportWorkflowDefinition`
- **描述**: Import settings for the Diffuse texture

### Normal
- **类型**: `FEditorImportWorkflowDefinition`
- **描述**: Import settings for the Normalmap texture

### StaticMesh
- **类型**: `FEditorImportWorkflowDefinition`
- **描述**: Import settings for the static mesh

### ReimportStaticMesh
- **类型**: `FEditorImportWorkflowDefinition`
- **描述**: Import settings for the static mesh to re-import

### BlendShapeMesh
- **类型**: `FEditorImportWorkflowDefinition`
- **描述**: Import settings for the blend shape

### MorphMesh
- **类型**: `FEditorImportWorkflowDefinition`
- **描述**: Import settings for the morph mesh

### SkeletalMesh
- **类型**: `FEditorImportWorkflowDefinition`
- **描述**: Import settings for the skeletal mesh

### Animation
- **类型**: `FEditorImportWorkflowDefinition`
- **描述**: Import settings for the animation asset.  (Will automatically use the skeleton of the skeletal mesh above)

### Sound
- **类型**: `FEditorImportWorkflowDefinition`
- **描述**: Import settings for the sound

### SurroundSound
- **类型**: `FEditorImportWorkflowDefinition`
- **描述**: Import settings for the surround sound (Select any of the channels.  It will auto import the rest)

### OtherAssetsToImport
- **类型**: `TArray<FEditorImportWorkflowDefinition>`
- **描述**: Import settings for any other assets you may want to import

## 方法

### opAssign
```angelscript
FBuildPromotionImportWorkflowSettings& opAssign(FBuildPromotionImportWorkflowSettings Other)
```

