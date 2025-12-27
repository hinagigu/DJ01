# UPropertyEditorTestObject

**继承自**: `UObject`

## 属性

### Int8Property
- **类型**: `int8`

### Int16Property
- **类型**: `int16`

### Int32Property
- **类型**: `int`

### Int64Property
- **类型**: `int64`

### ByteProperty
- **类型**: `uint8`

### UnsignedInt16Property
- **类型**: `uint16`

### UnsignedInt32Property
- **类型**: `uint`

### UnsignedInt64Property
- **类型**: `uint64`

### FloatProperty
- **类型**: `float32`

### DoubleProperty
- **类型**: `float`

### NameProperty
- **类型**: `FName`

### BoolProperty
- **类型**: `bool`

### StringProperty
- **类型**: `FString`

### TextProperty
- **类型**: `FText`

### IntPointProperty
- **类型**: `FIntPoint`

### Vector3Property
- **类型**: `FVector`

### Vector2Property
- **类型**: `FVector2D`

### Vector4Property
- **类型**: `FVector4`

### RotatorProperty
- **类型**: `FRotator`

### ObjectProperty
- **类型**: `UObject`

### LinearColorProperty
- **类型**: `FLinearColor`

### ColorProperty
- **类型**: `FColor`

### EnumByteProperty
- **类型**: `EPropertyEditorTestEnum`

### EnumProperty
- **类型**: `EPropertyEditorTestEditColor`

### EnumUnderscores
- **类型**: `EPropertyEditorTestUnderscores`

### MatrixProperty
- **类型**: `FMatrix`

### TransformProperty
- **类型**: `FTransform`

### GigabyteProperty
- **类型**: `float`

### ClassProperty
- **类型**: `UClass`

### ClassPropertyWithAllowed
- **类型**: `UClass`

### ClassPropertyWithDisallowed
- **类型**: `UClass`

### SubclassOfTexture
- **类型**: `TSubclassOf<UTexture>`

### SubclassOfWithAllowed
- **类型**: `TSubclassOf<UTexture>`

### SubclassOfWithDisallowed
- **类型**: `TSubclassOf<UTexture>`

### AssetPointerWithAllowedAndWhitespace
- **类型**: `TSoftObjectPtr<UObject>`

### IntProperty32Array
- **类型**: `TArray<int>`
- **描述**: Integer

### BytePropertyArray
- **类型**: `TArray<uint8>`
- **描述**: Byte

### FloatPropertyArray
- **类型**: `TArray<float32>`

### NamePropertyArray
- **类型**: `TArray<FName>`

### BoolPropertyArray
- **类型**: `TArray<bool>`

### StringPropertyArray
- **类型**: `TArray<FString>`

### TextPropertyArray
- **类型**: `TArray<FText>`

### Vector3PropertyArray
- **类型**: `TArray<FVector>`

### Vector2PropertyArray
- **类型**: `TArray<FVector2D>`

### Vector4PropertyArray
- **类型**: `TArray<FVector4>`

### RotatorPropertyArray
- **类型**: `TArray<FRotator>`

### ObjectPropertyArray
- **类型**: `TArray<TObjectPtr<UObject>>`

### ActorPropertyArray
- **类型**: `TArray<TObjectPtr<AActor>>`

### LinearColorPropertyArray
- **类型**: `TArray<FLinearColor>`

### ColorPropertyArray
- **类型**: `TArray<FColor>`

### TimecodePropertyArray
- **类型**: `TArray<FTimecode>`

### EnumPropertyArray
- **类型**: `TArray<EPropertyEditorTestEnum>`

### StructPropertyArray
- **类型**: `TArray<FPropertyEditorTestBasicStruct>`

### StructPropertyArrayWithTitle
- **类型**: `TArray<FPropertyEditorTestBasicStruct>`

### StructPropertyArrayWithFormattedTitle
- **类型**: `TArray<FPropertyEditorTestBasicStruct>`

### StructPropertyArrayWithTitleError
- **类型**: `TArray<FPropertyEditorTestBasicStruct>`

### StructPropertyArrayWithFormattedTitleError
- **类型**: `TArray<FPropertyEditorTestBasicStruct>`

### InstancedStructArray
- **类型**: `TArray<FPropertyEditorTestInstancedStruct>`

### ObjectPropertyArrayWithTitle
- **类型**: `TArray<TObjectPtr<UPropertyEditorTestInstancedObject>>`

### InstancedUObjectArray
- **类型**: `TArray<TObjectPtr<UPropertyEditorTestInstancedObject>>`

### FixedArrayOfInts
- **类型**: `TArray<int>`

### StaticArrayOfInts
- **类型**: `int`

### StaticArrayOfIntsWithEnumLabels
- **类型**: `int`

### FloatPropertyWithClampedRange
- **类型**: `float32`
- **描述**: This is a custom tooltip that should be shown

### IntPropertyWithClampedRange
- **类型**: `int`

### ObjectThatCannotBeChanged
- **类型**: `UPrimitiveComponent`

### EnumBitflags
- **类型**: `int`

### StringPasswordProperty
- **类型**: `FString`

### TextPasswordProperty
- **类型**: `FText`

### ThisIsBrokenIfItsVisibleInADetailsView
- **类型**: `FPropertyEditorTestBasicStruct`

### StructWithMultipleInstances1
- **类型**: `FPropertyEditorTestBasicStruct`

### bEditConditionStructWithMultipleInstances2
- **类型**: `bool`

### StructWithMultipleInstances2
- **类型**: `FPropertyEditorTestBasicStruct`

### RichCurve
- **类型**: `FRichCurve`

### SoftObjectPath
- **类型**: `FSoftObjectPath`

### PrimaryAssetId
- **类型**: `FPrimaryAssetId`

### PrimaryAssetIdWithoutThumbnail
- **类型**: `FPrimaryAssetId`

### AssetReferenceCustomStructWithThumbnail
- **类型**: `FSoftObjectPath`

### ExactlyPointLightActorReference
- **类型**: `FSoftObjectPath`

### LightActorReference
- **类型**: `FSoftObjectPath`

### ExactPointOrSpotLightActorReference
- **类型**: `FSoftObjectPath`

### LightOrStaticMeshActorReference
- **类型**: `FSoftObjectPath`
- **描述**: NOTE: intentionally misplaced space in AllowedClasses

### NotLightActorReference
- **类型**: `FSoftObjectPath`

### MaterialOrTextureAssetReference
- **类型**: `FSoftObjectPath`

### ActorWithMetaClass
- **类型**: `FSoftObjectPath`

### DisabledByCanEditChange
- **类型**: `FSoftObjectPath`

### ComponentReference
- **类型**: `FComponentReference`

### bEditCondition
- **类型**: `bool`

### SimplePropertyWithEditCondition
- **类型**: `int`

### bEditConditionAssetReferenceCustomStructWithEditCondition
- **类型**: `bool`

### AssetReferenceCustomStructWithEditCondition
- **类型**: `FSoftObjectPath`

### ArrayOfStructs
- **类型**: `TArray<FPropertyEditorTestBasicStruct>`

### Struct
- **类型**: `FPropertyEditTestTextStruct`

### EditInlineNewStaticMeshComponent
- **类型**: `UStaticMeshComponent`

### ArrayOfEditInlineNewSMCs
- **类型**: `TArray<TObjectPtr<UStaticMeshComponent>>`

### TextureProp
- **类型**: `UTexture`

### StaticMeshProp
- **类型**: `UStaticMesh`

### AnyMaterialInterface
- **类型**: `UMaterialInterface`

### MaterialNoThumbnail
- **类型**: `UMaterialInterface`

### OnlyActorsAllowed
- **类型**: `AActor`

### Int32Set
- **类型**: `TSet<int>`

### FloatSet
- **类型**: `TSet<float32>`

### StringSet
- **类型**: `TSet<FString>`

### ObjectSet
- **类型**: `TSet<TObjectPtr<UObject>>`

### ActorSet
- **类型**: `TSet<TObjectPtr<AActor>>`

### EditColorSet
- **类型**: `TSet<EPropertyEditorTestEditColor>`

### NameSet
- **类型**: `TSet<FName>`

### Int32ToStringMap
- **类型**: `TMap<int,FString>`

### StringToMultilineTextMap
- **类型**: `TMap<FString,FText>`

### StringToColorMap
- **类型**: `TMap<FString,FLinearColor>`

### Int32ToStructMap
- **类型**: `TMap<int,FPropertyEditorTestBasicStruct>`

### StringToFloatMap
- **类型**: `TMap<FString,float32>`

### StringToObjectMap
- **类型**: `TMap<FString,TObjectPtr<UObject>>`

### StringToActorMap
- **类型**: `TMap<FString,TObjectPtr<AActor>>`

### ObjectToInt32Map
- **类型**: `TMap<TObjectPtr<UObject>,int>`

### ObjectToColorMap
- **类型**: `TMap<TObjectPtr<UObject>,FLinearColor>`

### IntToEnumMap
- **类型**: `TMap<int,EPropertyEditorTestEnum>`

### NameToNameMap
- **类型**: `TMap<FName,FName>`

### NameToObjectMap
- **类型**: `TMap<FName,TObjectPtr<UObject>>`

### NameToCustomMap
- **类型**: `TMap<FName,FPropertyEditorTestBasicStruct>`

### NameToColorMap
- **类型**: `TMap<FName,FLinearColor>`

### IntToCustomMap
- **类型**: `TMap<int,FPropertyEditorTestBasicStruct>`

### IntToSubStructMap
- **类型**: `TMap<int,FPropertyEditorTestSubStruct>`

### LinearColorSet
- **类型**: `TSet<FLinearColor>`

### VectorSet
- **类型**: `TSet<FVector>`

### LinearColorToStringMap
- **类型**: `TMap<FLinearColor,FString>`

### VectorToFloatMap
- **类型**: `TMap<FVector,float32>`

### LinearColorToVectorMap
- **类型**: `TMap<FLinearColor,FVector>`

### TextureOrBlendableInterface
- **类型**: `UObject`
- **描述**: Allows either an object that's derived from UTexture or IBlendableInterface, to ensure that Object Property handles know how to
filter for AllowedClasses correctly.

### bSubcategory
- **类型**: `bool`

### bSubcategoryAdvanced
- **类型**: `bool`

### bSubcategoryFooSimple
- **类型**: `bool`

### bSubcategoryFooAdvanced
- **类型**: `bool`

### bSubcategoryBarSimple
- **类型**: `bool`

### bSubcategoryBarAdvanced
- **类型**: `bool`

### bSubcategoryLast
- **类型**: `bool`

### bEnablesNext
- **类型**: `bool`

### bEnabledByPrevious
- **类型**: `bool`

### EnumEditCondition
- **类型**: `EPropertyEditorTestEditColor`

### bEnabledWhenBlue
- **类型**: `bool`

### bEnabledWhenPink
- **类型**: `bool`

### EnumAsByteEditCondition
- **类型**: `EPropertyEditorTestEnum`

### bEnabledWhenEnumIs2
- **类型**: `bool`

### bEnabledWhenEnumIs4
- **类型**: `bool`

### IntegerEditCondition
- **类型**: `int`

### bEnabledWhenIntGreaterOrEqual5
- **类型**: `bool`

### bEnabledWhenIntLessOrEqual10
- **类型**: `bool`

### FloatEditCondition
- **类型**: `float32`

### bEnabledWhenFloatGreaterThan5
- **类型**: `bool`

### bEnabledWhenFloatLessThan10
- **类型**: `bool`

### bEditConditionForArrays
- **类型**: `bool`

### ArrayWithEditCondition
- **类型**: `TArray<TObjectPtr<UTexture2D>>`

### ArrayOfStructsWithEditCondition
- **类型**: `TArray<FPropertyEditorTestBasicStruct>`

### bEditConditionForFixedArray
- **类型**: `bool`

### FixedArrayWithEditCondition
- **类型**: `FString`

### bEditConditionForDirectoryPath
- **类型**: `bool`

### DirectoryPath
- **类型**: `FDirectoryPath`

### EditConditionFlags
- **类型**: `int64`

### bEnabledWhenFlagsHasTwoOrFour
- **类型**: `bool`

### bDisabledWhenFlagsIsOdd
- **类型**: `bool`

### AlwaysDisabled
- **类型**: `int`

### bCategoryInlineEditCondition
- **类型**: `bool`

### EnabledWhenCategoryChecked
- **类型**: `float32`

### InlineProperty
- **类型**: `EComponentMobility`

### PropertyThatHides
- **类型**: `EComponentMobility`

### bVisibleWhenStatic
- **类型**: `bool`

### VisibleWhenStationary
- **类型**: `int`

### DateTime
- **类型**: `FDateTime`

### Timespan
- **类型**: `FTimespan`

### Guid
- **类型**: `FGuid`

### PerPlatformFloat
- **类型**: `FPerPlatformFloat`

### PerPlatformInt
- **类型**: `FPerPlatformInt`

### InlineEditConditionWithoutMeta
- **类型**: `float32`

### bInlineEditConditionWithMetaToggle
- **类型**: `bool`

### InlineEditConditionWithMeta
- **类型**: `float32`

### HasNonEditableInlineCondition
- **类型**: `float32`

### bSharedEditCondition
- **类型**: `bool`

### UsesSharedEditCondition1
- **类型**: `float32`

### UsesSharedEditCondition2
- **类型**: `float32`

### StructWithInlineCondition
- **类型**: `FPropertyEditorTestEditCondition`

### ArrayOfStructsWithInlineCondition
- **类型**: `TArray<FPropertyEditorTestEditCondition>`

### NestedArrayOfInts
- **类型**: `int`

