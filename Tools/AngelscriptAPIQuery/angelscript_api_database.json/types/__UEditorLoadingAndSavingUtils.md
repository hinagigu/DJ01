# __UEditorLoadingAndSavingUtils

## 方法

### ExportScene
```angelscript
void ExportScene(bool bExportSelectedActorsOnly)
```
Exports the current scene

### GetDirtyContentPackages
```angelscript
void GetDirtyContentPackages(TArray<UPackage>& OutDirtyPackages)
```
Appends array with all currently dirty content packages.

@param OutDirtyPackages Array to append dirty packages to.

### GetDirtyMapPackages
```angelscript
void GetDirtyMapPackages(TArray<UPackage>& OutDirtyPackages)
```
Appends array with all currently dirty map packages.

@param OutDirtyPackages Array to append dirty packages to.

### ImportScene
```angelscript
void ImportScene(FString Filename)
```
Imports a file such as (FBX or obj) and spawns actors f into the current level

### LoadMap
```angelscript
UWorld LoadMap(FString Filename)
```
Loads the specified map.  Does not prompt the user to save the current map.

@param       Filename                Level package filename, including path.
@return                                      true if the map was loaded successfully.

### LoadMapWithDialog
```angelscript
UWorld LoadMapWithDialog()
```
Prompts the user to save the current map if necessary, the presents a load dialog and
loads a new map if selected by the user.

### NewBlankMap
```angelscript
UWorld NewBlankMap(bool bSaveExistingMap)
```

### NewMapFromTemplate
```angelscript
UWorld NewMapFromTemplate(FString PathToTemplateLevel, bool bSaveExistingMap)
```

### ReloadPackages
```angelscript
void ReloadPackages(TArray<UPackage> PackagesToReload, bool& bOutAnyPackagesReloaded, FText& OutErrorMessage, EReloadPackagesInteractionMode InteractionMode)
```
Helper function that attempts to reload the specified top-level packages.

@param       PackagesToReload                The list of packages that should be reloaded
@param       bOutAnyPackagesReloaded True if the set of loaded packages was changed
@param       OutErrorMessage                 An error message specifying any problems with reloading packages
@param       InteractionMode                 Whether the function is allowed to ask the user questions (such as whether to reload dirty packages)

### SaveCurrentLevel
```angelscript
bool SaveCurrentLevel()
```
Saves the active level, prompting the use for checkout if necessary.

@return      true on success, False on fail

### SaveDirtyPackages
```angelscript
bool SaveDirtyPackages(bool bSaveMapPackages, bool bSaveContentPackages)
```
Looks at all currently loaded packages and saves them if their "bDirty" flag is set.
Assume all dirty packages should be saved and check out from source control (if enabled).

@param       bSaveMapPackages                        true if map packages should be saved
@param       bSaveContentPackages            true if we should save content packages.
@return                                                              true on success, false on fail.

### SaveDirtyPackagesWithDialog
```angelscript
bool SaveDirtyPackagesWithDialog(bool bSaveMapPackages, bool bSaveContentPackages)
```
Looks at all currently loaded packages and saves them if their "bDirty" flag is set.
Prompt the user to select which dirty packages to save and check them out from source control (if enabled).


@param       bSaveMapPackages                        true if map packages should be saved
@param       bSaveContentPackages            true if we should save content packages.
@return                                                              true on success, false on fail.

### SaveMap
```angelscript
bool SaveMap(UWorld World, FString AssetPath)
```
Saves the specified map, returning true on success.

@param       World                   The world to save.
@param       AssetPath               The valid content directory path and name for the asset.  E.g "/Game/MyMap"

@return                                      true if the map was saved successfully.

### SavePackages
```angelscript
bool SavePackages(TArray<UPackage> PackagesToSave, bool bOnlyDirty)
```
Save all packages.
Assume all dirty packages should be saved and check out from source control (if enabled).

@param               PackagesToSave                          The list of packages to save.  Both map and content packages are supported
@param               bCheckDirty                                     If true, only packages that are dirty in PackagesToSave will be saved
@return                                                                      true on success, false on fail.

### SavePackagesWithDialog
```angelscript
bool SavePackagesWithDialog(TArray<UPackage> PackagesToSave, bool bOnlyDirty)
```
Save all packages. Optionally prompting the user to select which packages to save.
Prompt the user to select which dirty packages to save and check them out from source control (if enabled).

@param                PackagesToSave                          The list of packages to save.  Both map and content packages are supported
@param                bCheckDirty                                     If true, only packages that are dirty in PackagesToSave will be saved
@return                                                                       true on success, false on fail.

### UnloadPackages
```angelscript
void UnloadPackages(TArray<UPackage> PackagesToUnload, bool& bOutAnyPackagesUnloaded, FText& OutErrorMessage)
```
Unloads a list of packages

@param PackagesToUnload Array of packages to unload.

### StaticClass
```angelscript
UClass StaticClass()
```

