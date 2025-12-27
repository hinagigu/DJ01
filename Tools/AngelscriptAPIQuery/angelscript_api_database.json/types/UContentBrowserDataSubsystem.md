# UContentBrowserDataSubsystem

**继承自**: `UEditorSubsystem`

Subsystem that provides access to Content Browser data.
This type deals with the composition of multiple data sources, which provide information about the folders and files available in the Content Browser.

## 方法

### ActivateAllDataSources
```angelscript
void ActivateAllDataSources()
```
Activate all available data sources.

### ActivateDataSource
```angelscript
bool ActivateDataSource(FName Name)
```
Attempt to activate the named data source.
@return True if the data source was available and not already active, false otherwise.

### DeactivateAllDataSources
```angelscript
void DeactivateAllDataSources()
```
Deactivate all active data sources.

### DeactivateDataSource
```angelscript
bool DeactivateDataSource(FName Name)
```
Attempt to deactivate the named data source.
@return True if the data source was available and active, false otherwise.

### GetActiveDataSources
```angelscript
TArray<FName> GetActiveDataSources()
```
Get the list of current active data sources.

### GetAvailableDataSources
```angelscript
TArray<FName> GetAvailableDataSources()
```
Get the list of current available data sources.

### GetItemAtPath
```angelscript
FContentBrowserItem GetItemAtPath(FName InPath, EContentBrowserItemTypeFilter InItemTypeFilter)
```
Get the first item (folder and/or file) that exists at the given virtual path.

### GetItemsAtPath
```angelscript
TArray<FContentBrowserItem> GetItemsAtPath(FName InPath, EContentBrowserItemTypeFilter InItemTypeFilter)
```
Get the items (folders and/or files) that exist at the given virtual path.
@note Multiple items may have the same virtual path if they are different types, or come from different data sources.

### GetItemsUnderPath
```angelscript
TArray<FContentBrowserItem> GetItemsUnderPath(FName InPath, FContentBrowserDataFilter InFilter)
```
Get the items (folders and/or files) that exist under the given virtual path.

