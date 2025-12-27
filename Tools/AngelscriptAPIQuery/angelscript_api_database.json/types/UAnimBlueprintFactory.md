# UAnimBlueprintFactory

**继承自**: `UFactory`

## 属性

### BlueprintType
- **类型**: `EBlueprintType`
- **描述**: The type of blueprint that will be created

### ParentClass
- **类型**: `TSubclassOf<UAnimInstance>`
- **描述**: The parent class of the created blueprint

### TargetSkeleton
- **类型**: `USkeleton`
- **描述**: The kind of skeleton that animation graphs compiled from the blueprint will animate

### PreviewSkeletalMesh
- **类型**: `USkeletalMesh`
- **描述**: The preview mesh to use with this animation blueprint

### bTemplate
- **类型**: `bool`
- **描述**: Whether the created blueprint should be a template with no target skeleton

