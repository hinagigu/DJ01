# __Niagara

## 方法

### AcquireNiagaraGPURayTracedCollisionGroup
```angelscript
int AcquireNiagaraGPURayTracedCollisionGroup()
```
Returns a free collision group for use in HWRT collision group filtering. Returns -1 on failure.

### GetNiagaraParameterCollection
```angelscript
UNiagaraParameterCollectionInstance GetNiagaraParameterCollection(UNiagaraParameterCollection Collection)
```
This is gonna be totally reworked
       UFUNCTION(BlueprintCallable, Category = Niagara, meta = (Keywords = "niagara System", UnsafeDuringActorConstruction = "true"))
       static void SetUpdateScriptConstant(UNiagaraComponent* Component, FName EmitterName, FName ConstantName, FVector Value);

### OverrideSystemUserVariableSkeletalMeshComponent
```angelscript
void OverrideSystemUserVariableSkeletalMeshComponent(UNiagaraComponent NiagaraSystem, FString OverrideName, USkeletalMeshComponent SkeletalMeshComponent)
```
Sets a Niagara StaticMesh parameter by name, overriding locally if necessary.

### OverrideSystemUserVariableStaticMesh
```angelscript
void OverrideSystemUserVariableStaticMesh(UNiagaraComponent NiagaraSystem, FString OverrideName, UStaticMesh StaticMesh)
```

### OverrideSystemUserVariableStaticMeshComponent
```angelscript
void OverrideSystemUserVariableStaticMeshComponent(UNiagaraComponent NiagaraSystem, FString OverrideName, UStaticMeshComponent StaticMeshComponent)
```
Sets a Niagara StaticMesh parameter by name, overriding locally if necessary.

### ReleaseNiagaraGPURayTracedCollisionGroup
```angelscript
void ReleaseNiagaraGPURayTracedCollisionGroup(int CollisionGroup)
```
Releases a collision group back to the system for use by ohers.

### SetActorNiagaraGPURayTracedCollisionGroup
```angelscript
void SetActorNiagaraGPURayTracedCollisionGroup(AActor Actor, int CollisionGroup)
```
Sets the Niagara GPU ray traced collision group for all primitive components on the given actor.

### SetComponentNiagaraGPURayTracedCollisionGroup
```angelscript
void SetComponentNiagaraGPURayTracedCollisionGroup(UPrimitiveComponent Primitive, int CollisionGroup)
```
Sets the Niagara GPU ray traced collision group for the give primitive component.

### SetSkeletalMeshDataInterfaceFilteredBones
```angelscript
void SetSkeletalMeshDataInterfaceFilteredBones(UNiagaraComponent NiagaraSystem, FString OverrideName, TArray<FName> FilteredBones)
```
Sets the Filtered Bones to use on the skeletal mesh data interface, this is destructive as it modifies the data interface.

### SetSkeletalMeshDataInterfaceFilteredSockets
```angelscript
void SetSkeletalMeshDataInterfaceFilteredSockets(UNiagaraComponent NiagaraSystem, FString OverrideName, TArray<FName> FilteredSockets)
```
Sets the Filtered Sockets to use on the skeletal mesh data interface, this is destructive as it modifies the data interface.

### SetSkeletalMeshDataInterfaceSamplingRegions
```angelscript
void SetSkeletalMeshDataInterfaceSamplingRegions(UNiagaraComponent NiagaraSystem, FString OverrideName, TArray<FName> SamplingRegions)
```
Sets the SamplingRegion to use on the skeletal mesh data interface, this is destructive as it modifies the data interface.

### SetTexture2DArrayObject
```angelscript
void SetTexture2DArrayObject(UNiagaraComponent NiagaraSystem, FString OverrideName, UTexture2DArray Texture)
```
Overrides the 2D Array Texture for a Niagara 2D Array Texture Data Interface User Parameter.

### SetTextureObject
```angelscript
void SetTextureObject(UNiagaraComponent NiagaraSystem, FString OverrideName, UTexture Texture)
```
Overrides the Texture Object for a Niagara Texture Data Interface User Parameter.

### SetVolumeTextureObject
```angelscript
void SetVolumeTextureObject(UNiagaraComponent NiagaraSystem, FString OverrideName, UVolumeTexture Texture)
```
Overrides the Volume Texture for a Niagara Volume Texture Data Interface User Parameter.

### SpawnSystemAtLocation
```angelscript
UNiagaraComponent SpawnSystemAtLocation(UNiagaraSystem SystemTemplate, FVector Location, FRotator Rotation, FVector Scale, bool bAutoDestroy, bool bAutoActivate, ENCPoolMethod PoolingMethod, bool bPreCullCheck)
```
Spawns a Niagara System at the specified world location/rotation
@return                       The spawned UNiagaraComponent

### SpawnSystemAtLocationWithParams
```angelscript
UNiagaraComponent SpawnSystemAtLocationWithParams(FFXSystemSpawnParameters SpawnParams)
```

### SpawnSystemAttached
```angelscript
UNiagaraComponent SpawnSystemAttached(UNiagaraSystem SystemTemplate, USceneComponent AttachToComponent, FName AttachPointName, FVector Location, FRotator Rotation, EAttachLocation LocationType, bool bAutoDestroy, bool bAutoActivate, ENCPoolMethod PoolingMethod, bool bPreCullCheck)
```

### SpawnSystemAttachedWithParams
```angelscript
UNiagaraComponent SpawnSystemAttachedWithParams(FFXSystemSpawnParameters SpawnParams)
```

