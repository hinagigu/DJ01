# UEditorValidatorBase

**继承自**: `UObject`

* The EditorValidatorBase is a class which verifies that an asset meets a specific ruleset.
* It should be used when checking engine-level classes, as UObject::IsDataValid requires
* overriding the base class. You can create project-specific version of the validator base,
* with custom logging and enabled logic.
*
* C++ and Blueprint validators will be gathered on editor start, while python validators need
* to register themselves

## 属性

### bIsEnabled
- **类型**: `bool`

### bOnlyPrintCustomMessage
- **类型**: `bool`
- **描述**: Whether we should also print out the source validator when printing validation errors.

## 方法

### AssetFails
```angelscript
void AssetFails(const UObject InAsset, FText InMessage)
```
Marks the validation as failed and adds an error message.

### AssetPasses
```angelscript
void AssetPasses(const UObject InAsset)
```
Marks the validation as successful. Failure to call this will report the validator as not having checked the asset.

### AssetWarning
```angelscript
void AssetWarning(const UObject InAsset, FText InMessage)
```
Adds a message to this validation but doesn't mark it as failed.

### GetValidationResult
```angelscript
EDataValidationResult GetValidationResult()
```

### CanValidate
```angelscript
bool CanValidate(EDataValidationUsecase InUsecase)
```
Override this to determine whether or not you can use this validator given this usecase

### CanValidateAsset
```angelscript
bool CanValidateAsset(UObject InAsset)
```
Override this to determine whether or not you can validate a given asset with this validator

### ValidateLoadedAsset
```angelscript
EDataValidationResult ValidateLoadedAsset(UObject InAsset)
```
Override this in blueprint to validate assets

