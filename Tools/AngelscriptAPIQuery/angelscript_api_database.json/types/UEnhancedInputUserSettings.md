# UEnhancedInputUserSettings

**继承自**: `USaveGame`

The Enhanced Input User Settings class is a place where you can put all of your Input Related settings
that you want your user to be able to change. Things like their key mappings, aim sensitivity, accessibility
settings, etc. This also provides a Registration point for Input Mappings Contexts (IMC) from possibly unloaded
plugins (i.e. Game Feature Plugins). You can register your IMC from a Game Feature Action plugin here, and then
have access to all the key mappings available. This is very useful for building settings screens because you can
now access all the mappings in your game, even if the entire plugin isn't loaded yet.

The user settings are stored on each UEnhancedPlayerInput object, so each instance of the settings can represent
a single User or Local Player.

To customize this for your game, you can create a subclass of it and change the "UserSettingsClass" in the
Enhanced Input Project Settings.

## 属性

### OnSettingsChanged
- **类型**: `FEnhancedInputUserSettingsChanged__EnhancedInputUserSettings`

### OnSettingsApplied
- **类型**: `FEnhancedInputUserSettingsApplied__EnhancedInputUserSettings`

## 方法

### ApplySettings
```angelscript
void ApplySettings()
```
Apply any custom input settings to your user. By default, this will just broadcast the OnSettingsApplied delegate
which is a useful hook to maybe rebuild some UI or do other user facing updates.

### AsyncSaveSettings
```angelscript
void AsyncSaveSettings()
```
Asynchronously save the settings to a hardcoded save game slot. This will work for simple games,
but if you need to integrate it into an advanced save system you should Serialize this object out with the rest of your save data.

OnAsyncSaveComplete will be called upon save completion.

### CreateNewKeyProfile
```angelscript
UEnhancedPlayerMappableKeyProfile CreateNewKeyProfile(FPlayerMappableKeyProfileCreationArgs InArgs)
```
Creates a new profile with this name and type.

### FindMappingsInRow
```angelscript
TSet<FPlayerKeyMapping> FindMappingsInRow(FName MappingName)
```
Returns a set of all player key mappings for the given mapping name.

### GetCurrentKeyProfile
```angelscript
UEnhancedPlayerMappableKeyProfile GetCurrentKeyProfile()
```
Get the current key profile that the user has set

### GetCurrentKeyProfileIdentifier
```angelscript
FGameplayTag GetCurrentKeyProfileIdentifier()
```
Gets the currently selected key profile

### GetKeyProfileWithIdentifier
```angelscript
UEnhancedPlayerMappableKeyProfile GetKeyProfileWithIdentifier(FGameplayTag ProfileId)
```
Returns the key profile with the given name if one exists. Null if one doesn't exist

### IsMappingContextRegistered
```angelscript
bool IsMappingContextRegistered(const UInputMappingContext IMC)
```
Returns true if this mapping context is currently registered with the settings

### MapPlayerKey
```angelscript
void MapPlayerKey(FMapPlayerKeyArgs InArgs, FGameplayTagContainer& FailureReason)
```
Sets the player mapped key on the current key profile.

### RegisterInputMappingContext
```angelscript
bool RegisterInputMappingContext(const UInputMappingContext IMC)
```
Registers this mapping context with the user settings. This will iterate all the key mappings
in the context and create an initial Player Mappable Key for every mapping that is marked as mappable.

### RegisterInputMappingContexts
```angelscript
bool RegisterInputMappingContexts(TSet<UInputMappingContext> MappingContexts)
```
Registers multiple mapping contexts with the settings

### ResetAllPlayerKeysInRow
```angelscript
void ResetAllPlayerKeysInRow(FMapPlayerKeyArgs InArgs, FGameplayTagContainer& FailureReason)
```
Resets each player mapped key to it's default value from the Input Mapping Context that it was registered from.
If a key did not come from an IMC (i.e. it was added additionally by the player) then it will be reset to EKeys::Invalid.

@param InArgs                         Arguments that contain the mapping name and profile ID to find the mapping to reset.
@param FailureReason          Populated with failure reasons if the operation fails.

### ResetKeyProfileToDefault
```angelscript
void ResetKeyProfileToDefault(FGameplayTag ProfileId, FGameplayTagContainer& FailureReason)
```
Resets the given key profile to default key mappings

@param ProfileId             The ID of the key profile to reset
@param FailureReason Populated with failure reasons if the operation fails.

### SaveSettings
```angelscript
void SaveSettings()
```
Synchronously save the settings to a hardcoded save game slot. This will work for simple games,
but if you need to integrate it into an advanced save system you should Serialize this object out with the rest of your save data.

### SetKeyProfile
```angelscript
bool SetKeyProfile(FGameplayTag InProfileId)
```
Changes the currently active key profile to the one with the given name. Returns true if the operation was successful.

### UnMapPlayerKey
```angelscript
void UnMapPlayerKey(FMapPlayerKeyArgs InArgs, FGameplayTagContainer& FailureReason)
```
Unmaps a single player mapping that matches the given Mapping name, slot, and hardware device.

### UnregisterInputMappingContext
```angelscript
bool UnregisterInputMappingContext(const UInputMappingContext IMC)
```
Removes this mapping context from the registered mapping contexts

### UnregisterInputMappingContexts
```angelscript
bool UnregisterInputMappingContexts(TSet<UInputMappingContext> MappingContexts)
```
Removes multiple mapping contexts from the registered mapping contexts

