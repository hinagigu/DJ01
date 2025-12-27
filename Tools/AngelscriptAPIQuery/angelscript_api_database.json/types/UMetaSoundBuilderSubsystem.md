# UMetaSoundBuilderSubsystem

**继承自**: `UEngineSubsystem`

The subsystem in charge of tracking MetaSound builders

## 方法

### CreateBoolArrayMetaSoundLiteral
```angelscript
FMetasoundFrontendLiteral CreateBoolArrayMetaSoundLiteral(TArray<bool> Value, FName& DataType)
```

### CreateBoolMetaSoundLiteral
```angelscript
FMetasoundFrontendLiteral CreateBoolMetaSoundLiteral(bool Value, FName& DataType)
```

### CreateFloatArrayMetaSoundLiteral
```angelscript
FMetasoundFrontendLiteral CreateFloatArrayMetaSoundLiteral(TArray<float32> Value, FName& DataType)
```

### CreateFloatMetaSoundLiteral
```angelscript
FMetasoundFrontendLiteral CreateFloatMetaSoundLiteral(float32 Value, FName& DataType)
```

### CreateIntArrayMetaSoundLiteral
```angelscript
FMetasoundFrontendLiteral CreateIntArrayMetaSoundLiteral(TArray<int> Value, FName& DataType)
```

### CreateIntMetaSoundLiteral
```angelscript
FMetasoundFrontendLiteral CreateIntMetaSoundLiteral(int Value, FName& DataType)
```

### CreateMetaSoundLiteralFromParam
```angelscript
FMetasoundFrontendLiteral CreateMetaSoundLiteralFromParam(FAudioParameter Param)
```

### CreateObjectArrayMetaSoundLiteral
```angelscript
FMetasoundFrontendLiteral CreateObjectArrayMetaSoundLiteral(TArray<UObject> Value)
```

### CreateObjectMetaSoundLiteral
```angelscript
FMetasoundFrontendLiteral CreateObjectMetaSoundLiteral(UObject Value)
```

### CreatePatchBuilder
```angelscript
UMetaSoundPatchBuilder CreatePatchBuilder(FName BuilderName, EMetaSoundBuilderResult& OutResult)
```

### CreateSourceBuilder
```angelscript
UMetaSoundSourceBuilder CreateSourceBuilder(FName BuilderName, FMetaSoundBuilderNodeOutputHandle& OnPlayNodeOutput, FMetaSoundBuilderNodeInputHandle& OnFinishedNodeInput, TArray<FMetaSoundBuilderNodeInputHandle>& AudioOutNodeInputs, EMetaSoundBuilderResult& OutResult, EMetaSoundOutputAudioFormat OutputFormat, bool bIsOneShot)
```

### CreateStringArrayMetaSoundLiteral
```angelscript
FMetasoundFrontendLiteral CreateStringArrayMetaSoundLiteral(TArray<FString> Value, FName& DataType)
```

### CreateStringMetaSoundLiteral
```angelscript
FMetasoundFrontendLiteral CreateStringMetaSoundLiteral(FString Value, FName& DataType)
```

### FindBuilder
```angelscript
UMetaSoundBuilderBase FindBuilder(FName BuilderName)
```
Returns the builder manually registered with the MetaSound Builder Subsystem with the provided custom name (if previously registered)

### FindPatchBuilder
```angelscript
UMetaSoundPatchBuilder FindPatchBuilder(FName BuilderName)
```
Returns the patch builder manually registered with the MetaSound Builder Subsystem with the provided custom name (if previously registered)

### FindSourceBuilder
```angelscript
UMetaSoundSourceBuilder FindSourceBuilder(FName BuilderName)
```
Returns the source builder manually registered with the MetaSound Builder Subsystem with the provided custom name (if previously registered)

### IsInterfaceRegistered
```angelscript
bool IsInterfaceRegistered(FName InInterfaceName)
```

### RegisterBuilder
```angelscript
void RegisterBuilder(FName BuilderName, UMetaSoundBuilderBase Builder)
```
Adds builder to subsystem's registry to make it persistent and easily accessible by multiple systems or Blueprints

### RegisterPatchBuilder
```angelscript
void RegisterPatchBuilder(FName BuilderName, UMetaSoundPatchBuilder Builder)
```
Adds builder to subsystem's registry to make it persistent and easily accessible by multiple systems or Blueprints

### RegisterSourceBuilder
```angelscript
void RegisterSourceBuilder(FName BuilderName, UMetaSoundSourceBuilder Builder)
```
Adds builder to subsystem's registry to make it persistent and easily accessible by multiple systems or Blueprints

### UnregisterBuilder
```angelscript
bool UnregisterBuilder(FName BuilderName)
```

### UnregisterPatchBuilder
```angelscript
bool UnregisterPatchBuilder(FName BuilderName)
```

### UnregisterSourceBuilder
```angelscript
bool UnregisterSourceBuilder(FName BuilderName)
```

