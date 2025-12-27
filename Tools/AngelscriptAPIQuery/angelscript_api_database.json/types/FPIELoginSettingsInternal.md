# FPIELoginSettingsInternal

Stores PIE login credentials

## 属性

### Id
- **类型**: `FString`
- **描述**: Id of the user logging in (email, display name, facebook id, etc)

### Token
- **类型**: `FString`
- **描述**: Credentials of the user logging in (password or auth token)

### Type
- **类型**: `FString`
- **描述**: Type of account. Needed to identity the auth method to use (epic, internal, facebook, etc)

## 方法

### opAssign
```angelscript
FPIELoginSettingsInternal& opAssign(FPIELoginSettingsInternal Other)
```

