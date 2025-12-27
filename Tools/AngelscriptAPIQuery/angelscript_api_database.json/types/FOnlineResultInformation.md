# FOnlineResultInformation

Detailed information about the online error. Effectively a wrapper for FOnlineError.

## 属性

### bWasSuccessful
- **类型**: `bool`
- **描述**: Whether the operation was successful or not. If it was successful, the error fields of this struct will not contain extra information.

### ErrorId
- **类型**: `FString`
- **描述**: The unique error id. Can be used to compare against specific handled errors.

### ErrorText
- **类型**: `FText`
- **描述**: Error text to display to the user.

## 方法

### opAssign
```angelscript
FOnlineResultInformation& opAssign(FOnlineResultInformation Other)
```

