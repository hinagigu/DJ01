# __Paths

## 方法

### AutomationDir
```angelscript
FString AutomationDir()
```
Returns the directory for automation save files

### AutomationLogDir
```angelscript
FString AutomationLogDir()
```
Returns the directory for automation log files

### AutomationTransientDir
```angelscript
FString AutomationTransientDir()
```
Returns the directory for automation save files that are meant to be deleted every run

### BugItDir
```angelscript
FString BugItDir()
```
Returns the directory the engine uses to output BugIt files.

@return screenshot directory

### ChangeExtension
```angelscript
FString ChangeExtension(FString InPath, FString InNewExtension)
```
Changes the extension of the given filename (does nothing if the file has no extension)

### CloudDir
```angelscript
FString CloudDir()
```
Returns the directory for local files used in cloud emulation or support

### CollapseRelativeDirectories
```angelscript
bool CollapseRelativeDirectories(FString InPath, FString& OutPath)
```
Takes a fully pathed string and eliminates relative pathing (eg: annihilates ".." with the adjacent directory).
Assumes all slashes have been converted to TEXT('/').
For example, takes the string:
      BaseDirectory/SomeDirectory/../SomeOtherDirectory/Filename.ext
and converts it to:
      BaseDirectory/SomeOtherDirectory/Filename.ext

### Combine
```angelscript
FString Combine(TArray<FString> InPaths)
```
Combine two or more Paths into one single Path

### ConvertFromSandboxPath
```angelscript
FString ConvertFromSandboxPath(FString InPath, FString InSandboxName)
```
Converts a sandbox (in Saved/Sandboxes) path to a normal path.

@param InSandboxName The name of the sandbox.

### ConvertRelativePathToFull
```angelscript
FString ConvertRelativePathToFull(FString InPath, FString InBasePath)
```
Converts a relative path name to a fully qualified name relative to the specified BasePath.
BasePath will be the process BaseDir() if not BasePath is given

### ConvertToSandboxPath
```angelscript
FString ConvertToSandboxPath(FString InPath, FString InSandboxName)
```
Converts a normal path to a sandbox path (in Saved/Sandboxes).

@param InSandboxName The name of the sandbox.

### CreateTempFilename
```angelscript
FString CreateTempFilename(FString Path, FString Prefix, FString Extension)
```
Creates a temporary filename with the specified prefix.

@param Path The file pathname.
@param Prefix The file prefix.
@param Extension File extension ('.' required).

### DiffDir
```angelscript
FString DiffDir()
```
Returns the directory for temp files used for diffing

### DirectoryExists
```angelscript
bool DirectoryExists(FString InPath)
```
Returns true if this directory was found, false otherwise

### EngineConfigDir
```angelscript
FString EngineConfigDir()
```
Returns the directory the root configuration files are located.

@return root config directory

### EngineContentDir
```angelscript
FString EngineContentDir()
```
Returns the content directory of the "core" engine that can be shared across
several games or across games & mods.

@return engine content directory

### EngineDir
```angelscript
FString EngineDir()
```
Returns the base directory of the "core" engine that can be shared across
several games or across games & mods. Shaders and base localization files
e.g. reside in the engine directory.

@return engine directory

### EngineIntermediateDir
```angelscript
FString EngineIntermediateDir()
```
Returns the intermediate directory of the engine

@return content directory

### EnginePluginsDir
```angelscript
FString EnginePluginsDir()
```
Returns the plugins directory of the engine

@return Plugins directory.

### EngineSavedDir
```angelscript
FString EngineSavedDir()
```
Returns the saved directory of the engine

@return Saved directory.

### EngineSourceDir
```angelscript
FString EngineSourceDir()
```
Returns the directory where engine source code files are kept

### EngineUserDir
```angelscript
FString EngineUserDir()
```
Returns the root directory for user-specific engine files. Always writable.

@return root user directory

### EngineVersionAgnosticUserDir
```angelscript
FString EngineVersionAgnosticUserDir()
```
Returns the root directory for user-specific engine files which can be shared between versions. Always writable.

@return root user directory

### EnterpriseDir
```angelscript
FString EnterpriseDir()
```
Returns the base directory enterprise directory.

@return enterprise directory

### EnterpriseFeaturePackDir
```angelscript
FString EnterpriseFeaturePackDir()
```
Returns the enterprise FeaturePack directory

@return FeaturePack directory.

### EnterprisePluginsDir
```angelscript
FString EnterprisePluginsDir()
```
Returns the enterprise plugins directory

@return Plugins directory.

### FeaturePackDir
```angelscript
FString FeaturePackDir()
```
Returns the directory where feature packs are kept

### FileExists
```angelscript
bool FileExists(FString InPath)
```
Returns true if this file was found, false otherwise

### GameAgnosticSavedDir
```angelscript
FString GameAgnosticSavedDir()
```
Returns the saved directory that is not game specific. This is usually the same as
EngineSavedDir().

@return saved directory

### GameDevelopersDir
```angelscript
FString GameDevelopersDir()
```
Returns the directory that contains subfolders for developer-specific content

### GameSourceDir
```angelscript
FString GameSourceDir()
```
Returns the directory where game source code files are kept

### GameUserDeveloperDir
```angelscript
FString GameUserDeveloperDir()
```
Returns the directory that contains developer-specific content for the current user

### GeneratedConfigDir
```angelscript
FString GeneratedConfigDir()
```
Returns the directory the engine saves generated config files.

@return config directory

### GetBaseFilename
```angelscript
FString GetBaseFilename(FString InPath, bool bRemovePath)
```
Returns the same thing as GetCleanFilename, but without the extension

### GetCleanFilename
```angelscript
FString GetCleanFilename(FString InPath)
```
Returns the filename (with extension), minus any path information.

### GetEditorLocalizationPaths
```angelscript
TArray<FString> GetEditorLocalizationPaths()
```
Returns a list of editor-specific localization paths

### GetEngineLocalizationPaths
```angelscript
TArray<FString> GetEngineLocalizationPaths()
```
Returns a list of engine-specific localization paths

### GetExtension
```angelscript
FString GetExtension(FString InPath, bool bIncludeDot)
```
Gets the extension for this filename.

@param        bIncludeDot             if true, includes the leading dot in the result

@return       the extension of this filename, or an empty string if the filename doesn't have an extension.

### GetGameLocalizationPaths
```angelscript
TArray<FString> GetGameLocalizationPaths()
```
Returns a list of game-specific localization paths

### GetInvalidFileSystemChars
```angelscript
FString GetInvalidFileSystemChars()
```
Returns a string containing all invalid characters as dictated by the operating system

### GetPath
```angelscript
FString GetPath(FString InPath)
```
Returns the path in front of the filename

### GetProjectFilePath
```angelscript
FString GetProjectFilePath()
```
Gets the path to the project file.

@return Project file path.

### GetPropertyNameLocalizationPaths
```angelscript
TArray<FString> GetPropertyNameLocalizationPaths()
```
Returns a list of property name localization paths

### GetRelativePathToRoot
```angelscript
FString GetRelativePathToRoot()
```
Gets the relative path to get from BaseDir to RootDirectory

### GetRestrictedFolderNames
```angelscript
TArray<FString> GetRestrictedFolderNames()
```
Returns a list of restricted/internal folder names (without any slashes) which may be tested against full paths to determine if a path is restricted or not.

### GetToolTipLocalizationPaths
```angelscript
TArray<FString> GetToolTipLocalizationPaths()
```
Returns a list of tool tip localization paths

### HasProjectPersistentDownloadDir
```angelscript
bool HasProjectPersistentDownloadDir()
```
* Returns true if a writable directory for downloaded data that persists across play sessions is available

### IsDrive
```angelscript
bool IsDrive(FString InPath)
```
Returns true if this path represents a root drive or volume

### IsProjectFilePathSet
```angelscript
bool IsProjectFilePathSet()
```
Checks whether the path to the project file, if any, is set.

@return true if the path is set, false otherwise.

### IsRelative
```angelscript
bool IsRelative(FString InPath)
```
Returns true if this path is relative to another path

### IsRestrictedPath
```angelscript
bool IsRestrictedPath(FString InPath)
```
Determines if supplied path uses a restricted/internal subdirectory.  Note that slashes are normalized and character case is ignored for the comparison.

### IsSamePath
```angelscript
bool IsSamePath(FString PathA, FString PathB)
```
Checks if two paths are the same.

@param PathA First path to check.
@param PathB Second path to check.

@returns True if both paths are the same. False otherwise.

### LaunchDir
```angelscript
FString LaunchDir()
```
Returns the directory the application was launched from (useful for commandline utilities)

### MakePathRelativeTo
```angelscript
bool MakePathRelativeTo(FString InPath, FString InRelativeTo, FString& OutPath)
```
Assuming both paths (or filenames) are relative to the same base dir, converts InPath to be relative to InRelativeTo

@param InPath Path to change to be relative to InRelativeTo
@param InRelativeTo Path to use as the new relative base
@param InPath New path relative to InRelativeTo
@returns true if OutPath was changed to be relative

### MakePlatformFilename
```angelscript
void MakePlatformFilename(FString InPath, FString& OutPath)
```
Takes an "Unreal" pathname and converts it to a platform filename.

### MakeStandardFilename
```angelscript
void MakeStandardFilename(FString InPath, FString& OutPath)
```
Make fully standard "Unreal" pathname:
   - Normalizes path separators [NormalizeFilename]
   - Removes extraneous separators  [NormalizeDirectoryName, as well removing adjacent separators]
   - Collapses internal ..'s
   - Makes relative to Engine\Binaries\<Platform> (will ALWAYS start with ..\..\..)

### MakeValidFileName
```angelscript
FString MakeValidFileName(FString InString, FString InReplacementChar)
```
Returns a string that is safe to use as a filename because all items in
GetInvalidFileSystemChars() are removed

Optionally specify the character to replace invalid characters with

@param  InString
@param  InReplacementChar

### NormalizeDirectoryName
```angelscript
void NormalizeDirectoryName(FString InPath, FString& OutPath)
```
Normalize all / and \ to TEXT("/") and remove any trailing TEXT("/") if the character before that is not a TEXT("/") or a colon

### NormalizeFilename
```angelscript
void NormalizeFilename(FString InPath, FString& OutPath)
```
Convert all / and \ to TEXT("/")

### ProfilingDir
```angelscript
FString ProfilingDir()
```
Returns the directory the engine uses to output profiling files.

@return log directory

### ProjectConfigDir
```angelscript
FString ProjectConfigDir()
```
Returns the directory the root configuration files are located.

@return root config directory

### ProjectContentDir
```angelscript
FString ProjectContentDir()
```
Returns the content directory of the current game by looking at FApp::GetProjectName().

@return content directory

### ProjectDir
```angelscript
FString ProjectDir()
```
Returns the base directory of the current project by looking at FApp::GetProjectName().
This is usually a subdirectory of the installation
root directory and can be overridden on the command line to allow self
contained mod support.

@return base directory

### ProjectIntermediateDir
```angelscript
FString ProjectIntermediateDir()
```
Returns the intermediate directory of the current game by looking at FApp::GetProjectName().

@return intermediate directory

### ProjectLogDir
```angelscript
FString ProjectLogDir()
```
Returns the directory the engine uses to output logs. This currently can't
be an .ini setting as the game starts logging before it can read from .ini
files.

@return log directory

### ProjectModsDir
```angelscript
FString ProjectModsDir()
```
Returns the mods directory of the current project by looking at FApp::GetProjectName().

@return mods directory

### ProjectPersistentDownloadDir
```angelscript
FString ProjectPersistentDownloadDir()
```
* Returns the writable directory for downloaded data that persists across play sessions.

### ProjectPluginsDir
```angelscript
FString ProjectPluginsDir()
```
Returns the plugins directory of the current game by looking at FApp::GetProjectName().

@return plugins directory

### ProjectSavedDir
```angelscript
FString ProjectSavedDir()
```
Returns the saved directory of the current game by looking at FApp::GetProjectName().

@return saved directory

### ProjectUserDir
```angelscript
FString ProjectUserDir()
```
Returns the root directory for user-specific game files.

@return game user directory

### RemoveDuplicateSlashes
```angelscript
void RemoveDuplicateSlashes(FString InPath, FString& OutPath)
```
Removes duplicate slashes in paths.
Assumes all slashes have been converted to TEXT('/').
For example, takes the string:
      BaseDirectory/SomeDirectory//SomeOtherDirectory////Filename.ext
and converts it to:
      BaseDirectory/SomeDirectory/SomeOtherDirectory/Filename.ext

### RootDir
```angelscript
FString RootDir()
```
Returns the root directory of the engine directory tree

@return Root directory.

### SandboxesDir
```angelscript
FString SandboxesDir()
```
Returns the directory the engine stores sandbox output

@return sandbox directory

### ScreenShotDir
```angelscript
FString ScreenShotDir()
```
Returns the directory the engine uses to output screenshot files.

@return screenshot directory

### SetExtension
```angelscript
FString SetExtension(FString InPath, FString InNewExtension)
```
Sets the extension of the given filename (like ChangeExtension, but also applies the extension if the file doesn't have one)

### SetProjectFilePath
```angelscript
void SetProjectFilePath(FString NewGameProjectFilePath)
```
Sets the path to the project file.

@param NewGameProjectFilePath - The project file path to set.

### ShaderWorkingDir
```angelscript
FString ShaderWorkingDir()
```
Returns the Shader Working Directory

@return shader working directory

### ShouldSaveToUserDir
```angelscript
bool ShouldSaveToUserDir()
```
Should the "saved" directory structures be rooted in the user dir or relative to the "engine/game"

### SourceConfigDir
```angelscript
FString SourceConfigDir()
```
Returns the directory the engine uses to look for the source leaf ini files. This
can't be an .ini variable for obvious reasons.

@return source config directory

### Split
```angelscript
void Split(FString InPath, FString& PathPart, FString& FilenamePart, FString& ExtensionPart)
```
Parses a fully qualified or relative filename into its components (filename, path, extension).

@param        Path            [out] receives the value of the path portion of the input string
@param        Filename        [out] receives the value of the filename portion of the input string
@param        Extension       [out] receives the value of the extension portion of the input string

### ValidatePath
```angelscript
void ValidatePath(FString InPath, bool& bDidSucceed, FText& OutReason)
```
Validates that the parts that make up the path contain no invalid characters as dictated by the operating system
Note that this is a different set of restrictions to those imposed by FPackageName

@param InPath - path to validate
@param OutReason - If validation fails, this is filled with the failure reason
@param bDidSucceed - Whether the path could be validated

### VideoCaptureDir
```angelscript
FString VideoCaptureDir()
```
Returns the directory the engine uses to output user requested video capture files.

@return Video capture directory

