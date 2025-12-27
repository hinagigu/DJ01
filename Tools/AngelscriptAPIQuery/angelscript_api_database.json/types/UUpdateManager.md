# UUpdateManager

**继承自**: `UObject`

Update manager

Checks the system and/or backend for the possibility of a patch and hotfix
Will not apply a hotfix if a pending patch is available
Notifies the game of the result of the check
- possibly requires UI to prevent user from playing if a patch is available
- possibly requires UI to prevent user from player if a hotfix requires a reload of existing data

## 属性

### LastUpdateCheck
- **类型**: `FDateTime`
- **描述**: Timestamp of last update check (0:normal, 1:availability only)

### LastCompletionResult
- **类型**: `EUpdateCompletionStatus`
- **描述**: Last update check result (0:normal, 1:availability only)

