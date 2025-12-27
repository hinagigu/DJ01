# __Plugin

## 方法

### GetAdditionalPluginSearchPaths
```angelscript
TArray<FString> GetAdditionalPluginSearchPaths()
```
Get the list of extra directories that are recursively searched for
plugins (aside from the engine and project plugin directories).

@return The additional filesystem plugin search paths.

### GetAdditionalProjectPluginSearchPaths
```angelscript
TArray<FString> GetAdditionalProjectPluginSearchPaths()
```
Get the list of extra directories added by the project that are
recursively searched for plugins.

@return The additional project filesystem plugin search paths.

### GetEnabledPluginNames
```angelscript
TArray<FString> GetEnabledPluginNames()
```
Get the names of all enabled plugins.

@return The names of all enabled plugins.

### GetPluginBaseDir
```angelscript
bool GetPluginBaseDir(FString PluginName, FString& OutBaseDir)
```
Get the filesystem path to a plugin's base directory.

@param PluginName - Name of the plugin
@param OutBaseDir - Filesystem path to the plugin's base directory, if found

@return true if the named plugin was found and the plugin base directory
        filesystem path was stored in OutBaseDir, or false otherwise

### GetPluginContentDir
```angelscript
bool GetPluginContentDir(FString PluginName, FString& OutContentDir)
```
Get the filesystem path to a plugin's content directory.

@param PluginName - Name of the plugin
@param OutContentDir - Filesystem path to the plugin's content directory, if found

@return true if the named plugin was found and the plugin content
        directory filesystem path was stored in OutContentDir, or false otherwise

### GetPluginDescription
```angelscript
bool GetPluginDescription(FString PluginName, FString& OutDescription)
```
Get the description of a plugin.

@param PluginName - Name of the plugin
@param OutDescription - Description of the plugin, if found

@return true if the named plugin was found and the plugin's description
        was stored in OutDescription, or false otherwise

### GetPluginDescriptorFilePath
```angelscript
bool GetPluginDescriptorFilePath(FString PluginName, FString& OutFilePath)
```
Get the filesystem path to a plugin's descriptor.

@param PluginName - Name of the plugin
@param OutFilePath - Filesystem path to the plugin's descriptor, if found

@return true if the named plugin was found and the plugin descriptor
        filesystem path was stored in OutFilePath, or false otherwise

### GetPluginEditorCustomVirtualPath
```angelscript
bool GetPluginEditorCustomVirtualPath(FString PluginName, FString& OutVirtualPath)
```
Get the editor custom virtual path of a plugin.

@param PluginName - Name of the plugin
@param OutVirtualPath - Editor custom virtual path of the plugin, if found

@return true if the named plugin was found and the plugin's editor
        custom virtual path was stored in OutVirtualPath, or false otherwise

### GetPluginMountedAssetPath
```angelscript
bool GetPluginMountedAssetPath(FString PluginName, FString& OutAssetPath)
```
Get the virtual root path for assets in a plugin.

@param PluginName - Name of the plugin
@param OutAssetPath - Virtual root path for the plugin's assets, if found

@return true if the named plugin was found and the plugin's virtual
        root path was stored in OutAssetPath, or false otherwise

### GetPluginNameForObjectPath
```angelscript
bool GetPluginNameForObjectPath(FSoftObjectPath ObjectPath, FString& OutPluginName)
```
Get the name of the plugin containing an object.

@param ObjectPath - Path to the object
@param OutPluginName - Name of the plugin containing the object, if found

@return true if the object is contained within a plugin and the plugin
        name was stored in OutPluginName, or false otherwise

### GetPluginVersion
```angelscript
bool GetPluginVersion(FString PluginName, int& OutVersion)
```
Get the version number of a plugin.

@param PluginName - Name of the plugin
@param OutVersion - Version number of the plugin, if found

@return true if the named plugin was found and the plugin's version
        number was stored in OutVersion, or false otherwise

### GetPluginVersionName
```angelscript
bool GetPluginVersionName(FString PluginName, FString& OutVersionName)
```
Get the version name of a plugin.

@param PluginName - Name of the plugin
@param OutVersionName - Version name of the plugin, if found

@return true if the named plugin was found and the plugin's version
        name was stored in OutVersionName, or false otherwise

### IsPluginMounted
```angelscript
bool IsPluginMounted(FString PluginName)
```
Determine whether a plugin is mounted.

@param PluginName - Name of the plugin

@return true if the named plugin is mounted, or false otherwise

