# UPersonaPreviewSceneDescription

**继承自**: `UObject`

## 属性

### PreviewController
- **类型**: `TSubclassOf<UPersonaPreviewSceneController>`

### PreviewMesh
- **类型**: `TSoftObjectPtr<USkeletalMesh>`
- **描述**: The preview mesh to use

### PreviewAnimationBlueprint
- **类型**: `TSoftObjectPtr<UAnimBlueprint>`
- **描述**: The preview anim blueprint to use

### ApplicationMethod
- **类型**: `EPreviewAnimationBlueprintApplicationMethod`
- **描述**: The method by which a preview animation blueprint is applied, either as an overlay layer, or as a linked instance

### LinkedAnimGraphTag
- **类型**: `FName`
- **描述**: The tag to use when applying a preview animation blueprint via LinkAnimGraphByTag

### AdditionalMeshes
- **类型**: `TSoftObjectPtr<UDataAsset>`

