# __USubobjectDataSubsystem

## 方法

### CreateNewBPComponent
```angelscript
UClass CreateNewBPComponent(TSubclassOf<UActorComponent> ComponentClass, FString NewClassPath, FString NewClassName)
```
Creates a new Blueprint component from the specified class type
The user will be prompted to pick a new subclass name and a blueprint asset will be created

@return The new class that was created

### CreateNewCPPComponent
```angelscript
UClass CreateNewCPPComponent(TSubclassOf<UActorComponent> ComponentClass, FString NewClassPath, FString NewClassName)
```
Creates a new C++ component from the specified class type
The user will be prompted to pick a new subclass name and code will be recompiled

@return The new class that was created

### RenameSubobjectMemberVariable
```angelscript
void RenameSubobjectMemberVariable(UBlueprint BPContext, FSubobjectDataHandle InHandle, FName NewName)
```

### StaticClass
```angelscript
UClass StaticClass()
```

### Get
```angelscript
USubobjectDataSubsystem Get()
```

