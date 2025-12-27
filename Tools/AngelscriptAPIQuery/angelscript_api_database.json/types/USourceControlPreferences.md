# USourceControlPreferences

**继承自**: `UDeveloperSettings`

Settings for the Source Control Integration

## 属性

### bEnableValidationTag
- **类型**: `bool`
- **描述**: Adds validation tag to changelist description on submit.

### bShouldDeleteNewFilesOnRevert
- **类型**: `bool`
- **描述**: Deletes new files when reverted.

### bEnableUncontrolledChangelists
- **类型**: `bool`
- **描述**: Enables Uncontrolled Changelists features. The editor must be restarted for the change to be fully taken into account.

### CollectionChangelistTags
- **类型**: `TArray<FString>`
- **描述**: List of lines to add to any collection on checkin

### SpecificCollectionChangelistTags
- **类型**: `TMap<FName,FString>`
- **描述**: Map of collection names and additional text to apply to changelist descriptions when checking them in

