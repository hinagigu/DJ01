# ULevelSequence

**继承自**: `UMovieSceneSequence`

Movie scene animation for Actors.

## 属性

### AssetUserData
- **类型**: `TArray<TObjectPtr<UAssetUserData>>`
- **描述**: Array of user data stored with the asset

## 方法

### CopyMetaData
```angelscript
UObject CopyMetaData(UObject InMetaData)
```
Copy the specified meta data into this level sequence, overwriting any existing meta-data of the same type
Meta-data may implement the ILevelSequenceMetaData interface in order to hook into default ULevelSequence functionality.
@param InMetaData - Existing Metadata Object that you wish to copy into this Level Sequence.
@return The newly copied instance of the Metadata that now exists on this sequence.

### FindMetaDataByClass
```angelscript
UObject FindMetaDataByClass(TSubclassOf<UObject> InClass)
```
Find meta-data of a particular type for this level sequence instance.
@param InClass - Class that you wish to find the metadata object for.
@return An instance of this class if it already exists as metadata on this Level Sequence, otherwise null.

### FindOrAddMetaDataByClass
```angelscript
UObject FindOrAddMetaDataByClass(TSubclassOf<UObject> InClass)
```
Find meta-data of a particular type for this level sequence instance, adding it if it doesn't already exist.
@param InClass - Class that you wish to find or create the metadata object for.
@return An instance of this class as metadata on this Level Sequence.

### RemoveMetaDataByClass
```angelscript
void RemoveMetaDataByClass(TSubclassOf<UObject> InClass)
```
Remove meta-data of a particular type for this level sequence instance, if it exists
@param InClass - The class type that you wish to remove the metadata for

