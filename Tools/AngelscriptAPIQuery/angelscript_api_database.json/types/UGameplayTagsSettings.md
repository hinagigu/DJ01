# UGameplayTagsSettings

**继承自**: `UGameplayTagsList`

Class for importing GameplayTags directly from a config file.
FGameplayTagsEditorModule::StartupModule adds this class to the Project Settings menu to be edited.
Editing this in Project Settings will output changes to Config/DefaultGameplayTags.ini.

Primary advantages of this approach are:
-Adding new tags doesn't require checking out external and editing file (CSV or xls) then reimporting.
-New tags are mergeable since .ini are text and non exclusive checkout.

To do:
-Better support could be added for adding new tags. We could match existing tags and autocomplete subtags as
the user types (e.g, autocomplete 'Damage.Physical' as the user is adding a 'Damage.Physical.Slash' tag).

## 属性

### ImportTagsFromConfig
- **类型**: `bool`
- **描述**: If true, will import tags from ini files in the config/tags folder

### WarnOnInvalidTags
- **类型**: `bool`
- **描述**: If true, will give load warnings when reading in saved tag references that are not in the dictionary

### ClearInvalidTags
- **类型**: `bool`
- **描述**: If true, will clear any invalid tags when reading in saved tag references that are not in the dictionary

### AllowEditorTagUnloading
- **类型**: `bool`
- **描述**: If true, will allow unloading of tags in the editor when plugins are removed

### AllowGameTagUnloading
- **类型**: `bool`
- **描述**: If true, will allow unloading of tags in a non-editor gebuild when plugins are removed, this is potentially unsafe and affects requests to unload during play in editor

### FastReplication
- **类型**: `bool`
- **描述**: If true, will replicate gameplay tags by index instead of name. For this to work, tags must be identical on client and server

### InvalidTagCharacters
- **类型**: `FString`
- **描述**: These characters cannot be used in gameplay tags, in addition to special ones like newline

### CategoryRemapping
- **类型**: `TArray<FGameplayTagCategoryRemap>`
- **描述**: Category remapping. This allows base engine tag category meta data to remap to multiple project-specific categories.

### GameplayTagTableList
- **类型**: `TArray<FSoftObjectPath>`
- **描述**: List of data tables to load tags from

### GameplayTagRedirects
- **类型**: `TArray<FGameplayTagRedirect>`
- **描述**: List of active tag redirects

### CommonlyReplicatedTags
- **类型**: `TArray<FName>`
- **描述**: List of most frequently replicated tags

### NumBitsForContainerSize
- **类型**: `int`
- **描述**: Numbers of bits to use for replicating container size, set this based on how large your containers tend to be

### NetIndexFirstBitSegment
- **类型**: `int`
- **描述**: The length in bits of the first segment when net serializing tags. We will serialize NetIndexFirstBitSegment + 1 bit to indicate "more", which is slower to replicate

### RestrictedConfigFiles
- **类型**: `TArray<FRestrictedConfigInfo>`
- **描述**: A list of .ini files used to store restricted gameplay tags.

### RestrictedTagList
- **类型**: `FString`
- **描述**: Restricted Gameplay Tags.

Restricted tags are intended to be top level tags that are important for your data hierarchy and modified by very few people.

### NewTagSource
- **类型**: `FString`
- **描述**: Add a new gameplay tag config file for saving plugin or game-specific tags.

