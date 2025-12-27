# __VariantManager

## 方法

### AddActorBinding
```angelscript
void AddActorBinding(UVariant Variant, AActor Actor)
```
Binds the Actor to the Variant, internally creating a VariantObjectBinding

### AddDependency
```angelscript
int AddDependency(UVariant Variant, FVariantDependency& Dependency)
```

### AddVariant
```angelscript
void AddVariant(UVariantSet VariantSet, UVariant Variant)
```
Adds Variant to the VariantSet's list of Variants

### AddVariantSet
```angelscript
void AddVariantSet(ULevelVariantSets LevelVariantSets, UVariantSet VariantSet)
```
Adds VariantSet to the LevelVariantSets' list of VariantSets

### Apply
```angelscript
void Apply(UPropertyValue PropVal)
```
Applies the recorded data from PropVal to the actor from which it was captured

### CaptureProperty
```angelscript
UPropertyValue CaptureProperty(UVariant Variant, AActor Actor, FString PropertyPath)
```
Finds the actor binding to Actor within Variant and tries capturing a property with PropertyPath
Returns the captured UPropertyValue if succeeded or nullptr if it failed.

### CreateLevelVariantSetsActor
```angelscript
ALevelVariantSetsActor CreateLevelVariantSetsActor(ULevelVariantSets LevelVariantSetsAsset)
```
Creates a new ALevelVariantSetsActor in the current scene and assigns LevelVariantSetsAsset to it

### CreateLevelVariantSetsAsset
```angelscript
ULevelVariantSets CreateLevelVariantSetsAsset(FString AssetName, FString AssetPath)
```
Creates a new LevelVariantSetsAsset named AssetName (e.g. 'MyLevelVariantSets') in the content path AssetPath (e.g. '/Game')

### DeleteDependency
```angelscript
void DeleteDependency(UVariant Variant, int Index)
```

### GetCapturableProperties
```angelscript
TArray<FString> GetCapturableProperties(UObject ActorOrClass)
```
Returns a property path for all the properties we can capture for an actor. Will also
handle receiving the actor's class instead.

### GetCapturedProperties
```angelscript
TArray<UPropertyValue> GetCapturedProperties(UVariant Variant, AActor Actor)
```
Returns which properties have been captured for this actor in Variant

### GetPropertyTypeString
```angelscript
FString GetPropertyTypeString(UPropertyValue PropVal)
```
This allows the scripting language to get the type of the C++ property its dealing with

### GetValueBool
```angelscript
bool GetValueBool(UPropertyValue Property)
```

### GetValueColor
```angelscript
FColor GetValueColor(UPropertyValue Property)
```

### GetValueFloat
```angelscript
float32 GetValueFloat(UPropertyValue Property)
```

### GetValueInt
```angelscript
int GetValueInt(UPropertyValue Property)
```

### GetValueIntPoint
```angelscript
FIntPoint GetValueIntPoint(UPropertyValue Property)
```

### GetValueLinearColor
```angelscript
FLinearColor GetValueLinearColor(UPropertyValue Property)
```

### GetValueObject
```angelscript
UObject GetValueObject(UPropertyValue Property)
```

### GetValueQuat
```angelscript
FQuat GetValueQuat(UPropertyValue Property)
```

### GetValueRotator
```angelscript
FRotator GetValueRotator(UPropertyValue Property)
```

### GetValueString
```angelscript
FString GetValueString(UPropertyValue Property)
```

### GetValueVector
```angelscript
FVector GetValueVector(UPropertyValue Property)
```

### GetValueVector2D
```angelscript
FVector2D GetValueVector2D(UPropertyValue Property)
```

### GetValueVector4
```angelscript
FVector4 GetValueVector4(UPropertyValue Property)
```

### Record
```angelscript
void Record(UPropertyValue PropVal)
```
Records new data for PropVal from the actor from which it was captured

### RemoveActorBinding
```angelscript
void RemoveActorBinding(UVariant Variant, AActor Actor)
```
Removes an actor binding to Actor from Variant, if it exists

### RemoveActorBindingByName
```angelscript
void RemoveActorBindingByName(UVariant Variant, FString ActorName)
```
Looks for an actor binding to an actor with ActorLabel within Variant and removes it, if it exists

### RemoveCapturedProperty
```angelscript
void RemoveCapturedProperty(UVariant Variant, AActor Actor, UPropertyValue Property)
```
Removes a property capture from an actor binding within Variant, if it exists

### RemoveCapturedPropertyByName
```angelscript
void RemoveCapturedPropertyByName(UVariant Variant, AActor Actor, FString PropertyPath)
```
Removes property capture with PropertyPath from Actor's binding within Variant, if it exists

### RemoveVariant
```angelscript
void RemoveVariant(UVariantSet VariantSet, UVariant Variant)
```
Removes Variant from VariantSet, if that is its parent

### RemoveVariantByName
```angelscript
void RemoveVariantByName(UVariantSet VariantSet, FString VariantName)
```
Looks for a variant with VariantName within VariantSet and removes it, if it exists

### RemoveVariantSet
```angelscript
void RemoveVariantSet(ULevelVariantSets LevelVariantSets, UVariantSet VariantSet)
```
Removes VariantSet from LevelVariantSets, if that is its parent

### RemoveVariantSetByName
```angelscript
void RemoveVariantSetByName(ULevelVariantSets LevelVariantSets, FString VariantSetName)
```
Looks for a variant set with VariantSetName within LevelVariantSets and removes it, if it exists

### SetDependency
```angelscript
void SetDependency(UVariant Variant, int Index, FVariantDependency& Dependency)
```

### SetValueBool
```angelscript
void SetValueBool(UPropertyValue Property, bool InValue)
```

### SetValueColor
```angelscript
void SetValueColor(UPropertyValue Property, FColor InValue)
```

### SetValueFloat
```angelscript
void SetValueFloat(UPropertyValue Property, float32 InValue)
```

### SetValueInt
```angelscript
void SetValueInt(UPropertyValue Property, int InValue)
```

### SetValueIntPoint
```angelscript
void SetValueIntPoint(UPropertyValue Property, FIntPoint InValue)
```

### SetValueLinearColor
```angelscript
void SetValueLinearColor(UPropertyValue Property, FLinearColor InValue)
```

### SetValueObject
```angelscript
void SetValueObject(UPropertyValue Property, UObject InValue)
```

### SetValueQuat
```angelscript
void SetValueQuat(UPropertyValue Property, FQuat InValue)
```

### SetValueRotator
```angelscript
void SetValueRotator(UPropertyValue Property, FRotator InValue)
```

### SetValueString
```angelscript
void SetValueString(UPropertyValue Property, FString InValue)
```

### SetValueVector
```angelscript
void SetValueVector(UPropertyValue Property, FVector InValue)
```

### SetValueVector2D
```angelscript
void SetValueVector2D(UPropertyValue Property, FVector2D InValue)
```

### SetValueVector4
```angelscript
void SetValueVector4(UPropertyValue Property, FVector4 InValue)
```

