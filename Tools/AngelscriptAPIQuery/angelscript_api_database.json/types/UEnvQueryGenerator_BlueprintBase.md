# UEnvQueryGenerator_BlueprintBase

**继承自**: `UEnvQueryGenerator`

## 属性

### GeneratorsActionDescription
- **类型**: `FText`
- **描述**: A short description of what test does, like "Generate pawn named Joe"

### Context
- **类型**: `TSubclassOf<UEnvQueryContext>`
- **描述**: context

### GeneratedItemType
- **类型**: `TSubclassOf<UEnvQueryItemType>`
- **描述**: @todo this should show up only in the generator's BP, but
    due to the way EQS editor is generating widgets it's there as well
    It's a bug and we'll fix it

## 方法

### AddGeneratedActor
```angelscript
void AddGeneratedActor(AActor GeneratedActor)
```

### AddGeneratedVector
```angelscript
void AddGeneratedVector(FVector GeneratedVector)
```

### DoItemGeneration
```angelscript
void DoItemGeneration(TArray<FVector> ContextLocations)
```

### DoItemGenerationFromActors
```angelscript
void DoItemGenerationFromActors(TArray<AActor> ContextActors)
```

### GetQuerier
```angelscript
UObject GetQuerier()
```

