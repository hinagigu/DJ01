# __FPaths

## 方法

### RootDir
```angelscript
FString RootDir()
```

### LaunchDir
```angelscript
FString LaunchDir()
```

### CombinePaths
```angelscript
FString CombinePaths(FString FirstPath, FString SecondPath)
```

### EngineDir
```angelscript
FString EngineDir()
```

### EngineContentDir
```angelscript
FString EngineContentDir()
```

### EngineConfigDir
```angelscript
FString EngineConfigDir()
```

### EngineEditorSettingsDir
```angelscript
FString EngineEditorSettingsDir()
```

### EngineIntermediateDir
```angelscript
FString EngineIntermediateDir()
```

### EngineSavedDir
```angelscript
FString EngineSavedDir()
```

### ProjectDir
```angelscript
FString ProjectDir()
```

### ProjectUserDir
```angelscript
FString ProjectUserDir()
```

### ProjectContentDir
```angelscript
FString ProjectContentDir()
```

### ProjectConfigDir
```angelscript
FString ProjectConfigDir()
```

### ProjectSavedDir
```angelscript
FString ProjectSavedDir()
```

### ProjectIntermediateDir
```angelscript
FString ProjectIntermediateDir()
```

### ScreenShotDir
```angelscript
FString ScreenShotDir()
```

### VideoCaptureDir
```angelscript
FString VideoCaptureDir()
```

### GetRelativePathToRoot
```angelscript
FString GetRelativePathToRoot()
```

### GetExtension
```angelscript
FString GetExtension(FString InPath, bool bIncludeDot)
```

### GetCleanFilename
```angelscript
FString GetCleanFilename(FString InPath)
```

### GetBaseFilename
```angelscript
FString GetBaseFilename(FString InPath, bool bRemovePath)
```

### GetPath
```angelscript
FString GetPath(FString InPath)
```

### GetPathLeaf
```angelscript
FString GetPathLeaf(FString InPath)
```

### ChangeExtension
```angelscript
FString ChangeExtension(FString InPath, FString InNewExtension)
```

### SetExtension
```angelscript
FString SetExtension(FString InPath, FString InNewExtension)
```

### Split
```angelscript
void Split(FString InPath, FString& PathPart, FString& FilenamePart, FString& ExtensionPart)
```

### FileExists
```angelscript
bool FileExists(FString InPath)
```

### DirectoryExists
```angelscript
bool DirectoryExists(FString InPath)
```

### IsDrive
```angelscript
bool IsDrive(FString InPath)
```

### IsRelative
```angelscript
bool IsRelative(FString InPath)
```

### IsRestrictedPath
```angelscript
bool IsRestrictedPath(FString InPath)
```

### IsSamePath
```angelscript
bool IsSamePath(FString PathA, FString PathB)
```

### IsUnderDirectory
```angelscript
bool IsUnderDirectory(FString InPath, FString InDirectory)
```

### NormalizeFilename
```angelscript
void NormalizeFilename(FString& InPath)
```

### NormalizeDirectoryName
```angelscript
void NormalizeDirectoryName(FString& InPath)
```

### CollapseRelativeDirectories
```angelscript
bool CollapseRelativeDirectories(FString& InPath)
```

### RemoveDuplicateSlashes
```angelscript
void RemoveDuplicateSlashes(FString& InPath)
```

### MakeStandardFilename
```angelscript
void MakeStandardFilename(FString& InPath)
```

### MakePlatformFilename
```angelscript
void MakePlatformFilename(FString& InPath)
```

### ConvertRelativePathToFull
```angelscript
FString ConvertRelativePathToFull(FString InPath)
```

### ConvertRelativePathToFull
```angelscript
FString ConvertRelativePathToFull(FString BasePath, FString InPath)
```

