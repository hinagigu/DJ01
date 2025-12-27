# UDJ01ExperienceDefinition

**继承自**: `UPrimaryDataAsset`

Definition of an experience

## 属性

### GameFeaturesToEnable
- **类型**: `TArray<FString>`
- **描述**: List of Game Feature Plugins this experience wants to have active

### DefaultPawnData
- **类型**: `const UDJ01PawnData`
- **描述**: The default pawn class to spawn for players //@TODO: Make soft?

### Actions
- **类型**: `TArray<TObjectPtr<UGameFeatureAction>>`
- **描述**: List of actions to perform as this experience is loaded/activated/deactivated/unloaded

### ActionSets
- **类型**: `TArray<TObjectPtr<UDJ01ExperienceActionSet>>`
- **描述**: List of additional action sets to compose into this experience

