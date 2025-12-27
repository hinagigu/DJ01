# __GameplayTag

## 方法

### AddGameplayTag
```angelscript
void AddGameplayTag(FGameplayTagContainer& TagContainer, FGameplayTag Tag)
```
Adds a single tag to the passed in tag container

@param InOutTagContainer             The container that will be appended too.
@param Tag                                   The tag to add to the container

### AppendGameplayTagContainers
```angelscript
void AppendGameplayTagContainers(FGameplayTagContainer& InOutTagContainer, FGameplayTagContainer InTagContainer)
```
Appends all tags in the InTagContainer to InOutTagContainer

@param InOutTagContainer             The container that will be appended too.
@param InTagContainer                The container to append.

### BreakGameplayTagContainer
```angelscript
void BreakGameplayTagContainer(FGameplayTagContainer GameplayTagContainer, TArray<FGameplayTag>& GameplayTags)
```
Breaks tag container into explicit array of tags

### DoesContainerMatchTagQuery
```angelscript
bool DoesContainerMatchTagQuery(FGameplayTagContainer TagContainer, FGameplayTagQuery TagQuery)
```
Check if the specified tag container matches the given Tag Query

@param TagContainer                  Container to check if it matches all of the tags in the other container
@param TagQuery                              Query to match against

@return True if the container matches the query, false otherwise.

### EqualEqual_GameplayTag
```angelscript
bool EqualEqual_GameplayTag(FGameplayTag A, FGameplayTag B)
```
Returns true if the values are equal (A == B)

### EqualEqual_GameplayTagContainer
```angelscript
bool EqualEqual_GameplayTagContainer(FGameplayTagContainer A, FGameplayTagContainer B)
```
Returns true if the values are equal (A == B)

### GetAllActorsOfClassMatchingTagQuery
```angelscript
void GetAllActorsOfClassMatchingTagQuery(TSubclassOf<AActor> ActorClass, FGameplayTagQuery GameplayTagQuery, TArray<AActor>& OutActors)
```
Get an array of all actors of a specific class (or subclass of that class) which match the specified gameplay tag query.

@param ActorClass                    Class of actors to fetch
@param GameplayTagQuery              Query to match against

### GetDebugStringFromGameplayTag
```angelscript
FString GetDebugStringFromGameplayTag(FGameplayTag GameplayTag)
```
Returns an FString representation of a gameplay tag for debugging purposes.

@param GameplayTag   The tag to get the debug string from.

### GetDebugStringFromGameplayTagContainer
```angelscript
FString GetDebugStringFromGameplayTagContainer(FGameplayTagContainer TagContainer)
```
Returns an FString listing all of the gameplay tags in the tag container for debugging purposes.

@param TagContainer  The tag container to get the debug string from.

### GetNumGameplayTagsInContainer
```angelscript
int GetNumGameplayTagsInContainer(FGameplayTagContainer TagContainer)
```
Get the number of gameplay tags in the specified container

@param TagContainer  Tag container to get the number of tags from

@return The number of tags in the specified container

### GetTagName
```angelscript
FName GetTagName(FGameplayTag GameplayTag)
```
Returns FName of this tag

### HasAllTags
```angelscript
bool HasAllTags(FGameplayTagContainer TagContainer, FGameplayTagContainer OtherContainer, bool bExactMatch)
```
Check if the specified tag container has ALL of the tags in the other container

@param TagContainer                  Container to check if it matches all of the tags in the other container
@param OtherContainer                Container to check against. If this is empty, the check will succeed
@param bExactMatch                   If true, the tag has to be exactly present, if false then TagContainer will include it's parent tags while matching

@return True if the container has ALL of the tags in the other container

### HasAnyTags
```angelscript
bool HasAnyTags(FGameplayTagContainer TagContainer, FGameplayTagContainer OtherContainer, bool bExactMatch)
```
Check if the specified tag container has ANY of the tags in the other container

@param TagContainer                  Container to check if it matches any of the tags in the other container
@param OtherContainer                Container to check against.
@param bExactMatch                   If true, the tag has to be exactly present, if false then TagContainer will include it's parent tags while matching

@return True if the container has ANY of the tags in the other container

### HasTag
```angelscript
bool HasTag(FGameplayTagContainer TagContainer, FGameplayTag Tag, bool bExactMatch)
```
Check if the tag container has the specified tag

@param TagContainer                  Container to check for the tag
@param Tag                                   Tag to check for in the container
@param bExactMatch                   If true, the tag has to be exactly present, if false then TagContainer will include it's parent tags while matching

@return True if the container has the specified tag, false if it does not

### IsGameplayTagValid
```angelscript
bool IsGameplayTagValid(FGameplayTag GameplayTag)
```
Returns true if the passed in gameplay tag is non-null

### IsTagQueryEmpty
```angelscript
bool IsTagQueryEmpty(FGameplayTagQuery TagQuery)
```
Check if the specified tag query is empty

@param TagQuery                              Query to check

@return True if the query is empty, false otherwise.

### MakeGameplayTagContainerFromArray
```angelscript
FGameplayTagContainer MakeGameplayTagContainerFromArray(TArray<FGameplayTag> GameplayTags)
```
Creates a FGameplayTagContainer from the array of passed in tags

### MakeGameplayTagContainerFromTag
```angelscript
FGameplayTagContainer MakeGameplayTagContainerFromTag(FGameplayTag SingleTag)
```
Creates a FGameplayTagContainer containing a single tag

### MakeGameplayTagQuery
```angelscript
FGameplayTagQuery MakeGameplayTagQuery(FGameplayTagQuery TagQuery)
```
Creates a literal FGameplayTagQuery

@param       TagQuery        value to set the FGameplayTagQuery to

@return      The literal FGameplayTagQuery

### MakeGameplayTagQuery_MatchAllTags
```angelscript
FGameplayTagQuery MakeGameplayTagQuery_MatchAllTags(FGameplayTagContainer InTags)
```
Creates a literal FGameplayTagQuery with a prepopulated AllTagsMatch expression

@param        InTags  value to set the FGameplayTagQuery expression

@return      The literal FGameplayTagQuery

### MakeGameplayTagQuery_MatchAnyTags
```angelscript
FGameplayTagQuery MakeGameplayTagQuery_MatchAnyTags(FGameplayTagContainer InTags)
```
Creates a literal FGameplayTagQuery with a prepopulated AnyTagsMatch expression

@param       InTags  value to set the FGameplayTagQuery expression

@return      The literal FGameplayTagQuery

### MakeGameplayTagQuery_MatchNoTags
```angelscript
FGameplayTagQuery MakeGameplayTagQuery_MatchNoTags(FGameplayTagContainer InTags)
```
Creates a literal FGameplayTagQuery with a prepopulated NoTagsMatch expression

@param        InTags  value to set the FGameplayTagQuery expression

@return      The literal FGameplayTagQuery

### MakeLiteralGameplayTag
```angelscript
FGameplayTag MakeLiteralGameplayTag(FGameplayTag Value)
```
Creates a literal FGameplayTag

### MakeLiteralGameplayTagContainer
```angelscript
FGameplayTagContainer MakeLiteralGameplayTagContainer(FGameplayTagContainer Value)
```
Creates a literal FGameplayTagContainer

### MatchesAnyTags
```angelscript
bool MatchesAnyTags(FGameplayTag TagOne, FGameplayTagContainer OtherContainer, bool bExactMatch)
```
Determine if TagOne matches against any tag in OtherContainer

@param TagOne                        Tag to check for match
@param OtherContainer        Container to check against.
@param bExactMatch           If true, the tag has to be exactly present, if false then TagOne will include it's parent tags while matching

@return True if TagOne matches any tags explicitly present in OtherContainer

### MatchesTag
```angelscript
bool MatchesTag(FGameplayTag TagOne, FGameplayTag TagTwo, bool bExactMatch)
```
Determine if TagOne matches against TagTwo

@param TagOne                        Tag to check for match
@param TagTwo                        Tag to check match against
@param bExactMatch           If true, the tag has to be exactly present, if false then TagOne will include it's parent tags while matching

@return True if TagOne matches TagTwo

### NotEqual_GameplayTag
```angelscript
bool NotEqual_GameplayTag(FGameplayTag A, FGameplayTag B)
```
Returns true if the values are not equal (A != B)

### NotEqual_GameplayTagContainer
```angelscript
bool NotEqual_GameplayTagContainer(FGameplayTagContainer A, FGameplayTagContainer B)
```
Returns true if the values are not equal (A != B)

### RemoveGameplayTag
```angelscript
bool RemoveGameplayTag(FGameplayTagContainer& TagContainer, FGameplayTag Tag)
```
Remove a single tag from the passed in tag container, returns true if found

@param InOutTagContainer             The container that will be appended too.
@param Tag                                   The tag to add to the container

