# UEditorValidatorSubsystem

**继承自**: `UEditorSubsystem`

UEditorValidatorSubsystem manages all the asset validation in the engine.

The first validation handled is UObject::IsDataValid and its overridden functions.
Those validations require custom classes and are most suited to project-specific
classes.

The next validation set is of all registered UEditorValidationBases. These validators
have a function to determine if they can validate a given asset, and if they are
currently enabled. They are good candidates for validating engine classes or
very specific project logic.

Finally, this subsystem may be subclassed to change the overally behavior of
validation in your project. If a subclass exist in your project module, it will
supercede the engine validation subsystem.

## 方法

### AddValidator
```angelscript
void AddValidator(UEditorValidatorBase InValidator)
```
* Adds a validator to the list, making sure it is a unique instance

### IsAssetValid
```angelscript
EDataValidationResult IsAssetValid(FAssetData AssetData, TArray<FText>& ValidationErrors, TArray<FText>& ValidationWarnings, EDataValidationUsecase InValidationUsecase)
```
Loads the object referred to by the provided AssetData and runs registered validators on it.
Does not add anything to any FMessageLog tabs.
@return Returns Valid if the object pointed to by AssetData contains valid data; returns Invalid if the object contains invalid data or does not exist; returns NotValidated if no validations was performed on the object

### IsObjectValid
```angelscript
EDataValidationResult IsObjectValid(UObject InObject, TArray<FText>& ValidationErrors, TArray<FText>& ValidationWarnings, EDataValidationUsecase InValidationUsecase)
```
Runs registered validators on the provided object.
Does not add anything to any FMessageLog tabs.
@return Returns Valid if the object contains valid data; returns Invalid if the object contains invalid data; returns NotValidated if no validations was performed on the object

### RemoveValidator
```angelscript
void RemoveValidator(UEditorValidatorBase InValidator)
```
* Removes a validator
* Should be called during module shutdown if a validator was added.

### ValidateAssetsWithSettings
```angelscript
int ValidateAssetsWithSettings(TArray<FAssetData> AssetDataList, FValidateAssetsSettings& InSettings, FValidateAssetsResults& OutResults)
```
Called to validate assets from either the UI or a commandlet.
Loads the specified assets and runs all registered validators on them.
Populates the message log with errors and warnings with clickable links.
@param InSettings Structure passing context and settings for ValidateAssetsWithSettings
@param OutResults More detailed information about the results of the validate assets command
@returns Number of assets with validation failures or warnings

### ValidateChangelist
```angelscript
EDataValidationResult ValidateChangelist(UDataValidationChangelist InChangelist, FValidateAssetsSettings InSettings, FValidateAssetsResults& OutResults)
```
Called to validate assets from either the UI or a commandlet.
Loads the specified assets and runs all registered validators on them.
Populates the message log with errors and warnings with clickable links.
@param InSettings Structure passing context and settings for ValidateAssetsWithSettings
@param OutResults More detailed information about the results of the validate assets command
@returns Validation results for the changelist object itself

### ValidateChangelists
```angelscript
EDataValidationResult ValidateChangelists(TArray<UDataValidationChangelist> InChangelists, FValidateAssetsSettings InSettings, FValidateAssetsResults& OutResults)
```

