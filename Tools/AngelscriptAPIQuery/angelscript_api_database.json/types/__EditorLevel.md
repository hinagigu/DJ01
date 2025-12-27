# __EditorLevel

## 方法

### EditorEndPlay
```angelscript
void EditorEndPlay()
```

### GetPIEWorlds
```angelscript
TArray<UWorld> GetPIEWorlds(bool bIncludeDedicatedServer)
```

### ReplaceSelectedActors
```angelscript
void ReplaceSelectedActors(FString InAssetPath)
```
Replaces the selected Actors with the same number of a different kind of Actor using the specified factory to spawn the new Actors
note that only Location, Rotation, Drawscale, Drawscale3D, Tag, and Group are copied from the old Actors

### SpawnActorFromClass
```angelscript
AActor SpawnActorFromClass(TSubclassOf<AActor> ActorClass, FVector Location, FRotator Rotation, bool bTransient)
```

### SpawnActorFromObject
```angelscript
AActor SpawnActorFromObject(UObject ObjectToUse, FVector Location, FRotator Rotation, bool bTransient)
```

