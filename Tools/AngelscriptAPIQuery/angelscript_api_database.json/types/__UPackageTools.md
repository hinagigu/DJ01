# __UPackageTools

## 方法

### FilenameToPackageName
```angelscript
FString FilenameToPackageName(FString Filename)
```
Tries to convert a given relative or absolute filename to a long package name or path starting with a root like /Game
This works on both package names and directories, and it does not validate that it actually exists on disk.
@param Filename Filename to convert.
@return Resulting long package name if the supplied filename properly maps to a long package root, empty string otherwise.

### PackageNameToFilename
```angelscript
FString PackageNameToFilename(FString PackageName, FString Extension)
```
Converts a long package name to a file name.
This can be called on package paths as well, provide no extension in that case.
Will return an empty string if it fails.
@param PackageName Long Package Name
@param Extension Package extension.
@return Package filename, or empty if it failed.

### SanitizePackageName
```angelscript
FString SanitizePackageName(FString InPackageName)
```
Replaces all invalid package name characters with _

### StaticClass
```angelscript
UClass StaticClass()
```

