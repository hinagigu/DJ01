# __ULevelStreamingDynamic

## 方法

### LoadLevelInstance
```angelscript
ULevelStreamingDynamic LoadLevelInstance(FString LevelName, FVector Location, FRotator Rotation, bool& bOutSuccess, FString OptionalLevelNameOverride, TSubclassOf<ULevelStreamingDynamic> OptionalLevelStreamingClass, bool bLoadAsTempPackage)
```
Stream in a level with a specific location and rotation. You can create multiple instances of the same level!

The level to be loaded does not have to be in the persistent map's Levels list, however to ensure that the .umap does get
packaged, please be sure to include the .umap in your Packaging Settings:

  Project Settings -> Packaging -> List of Maps to Include in a Packaged Build (you may have to show advanced or type in filter)

@param LevelName - Level package name to load, ex: /Game/Maps/MyMapName, specifying short name like MyMapName will force very slow search on disk
@param Location - World space location where the level should be spawned
@param Rotation - World space rotation for rotating the entire level
@param bOutSuccess - Whether operation was successful (map was found and added to the sub-levels list)
@param OptionalLevelNameOverride - If set, the loaded level package have this name, which is used by other functions like UnloadStreamLevel. Note this is necessary for server and client networking because the level must have the same name on both.
@param OptionalLevelStreamingClass - If set, the level streaming class will be used instead of ULevelStreamingDynamic
@param bLoadAsTempPackage - If set, package path is prefixed by /Temp
@return Streaming level object for a level instance

### LoadLevelInstanceBySoftObjectPtr
```angelscript
ULevelStreamingDynamic LoadLevelInstanceBySoftObjectPtr(TSoftObjectPtr<UWorld> Level, FVector Location, FRotator Rotation, bool& bOutSuccess, FString OptionalLevelNameOverride, TSubclassOf<ULevelStreamingDynamic> OptionalLevelStreamingClass, bool bLoadAsTempPackage)
```

### StaticClass
```angelscript
UClass StaticClass()
```

