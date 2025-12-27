# __UMovieSceneFolderExtensions

## 方法

### AddChildFolder
```angelscript
bool AddChildFolder(UMovieSceneFolder TargetFolder, UMovieSceneFolder FolderToAdd)
```
Add a child folder to the target folder

@param TargetFolder  The folder to add a child folder to
@param FolderToAdd   The child folder to be added
@return True if the addition is successful

### AddChildObjectBinding
```angelscript
bool AddChildObjectBinding(UMovieSceneFolder Folder, FMovieSceneBindingProxy InObjectBinding)
```
Add a guid for an object binding to this folder

@param Folder                        The folder to add a child object to
@param InObjectBinding       The binding to add to the folder
@return True if the addition is successful

### AddChildTrack
```angelscript
bool AddChildTrack(UMovieSceneFolder Folder, UMovieSceneTrack InTrack)
```
Add a track to this folder

@param Folder                        The folder to add a child track to
@param InTrack                   The track to add to the folder
@return True if the addition is successful

### GetChildFolders
```angelscript
TArray<UMovieSceneFolder> GetChildFolders(UMovieSceneFolder Folder)
```
Get the child folders of a given folder

@param Folder        The folder to get the child folders of
@return The child folders associated with the given folder

### GetChildObjectBindings
```angelscript
TArray<FMovieSceneBindingProxy> GetChildObjectBindings(UMovieSceneFolder Folder)
```
Get the object bindings contained by this folder

@param Folder        The folder to get the bindings of
@return The object bindings under the given folder

### GetChildTracks
```angelscript
TArray<UMovieSceneTrack> GetChildTracks(UMovieSceneFolder Folder)
```
Get the tracks contained by this folder

@param Folder        The folder to get the tracks of
@return The tracks under the given folder

### GetFolderColor
```angelscript
FColor GetFolderColor(UMovieSceneFolder Folder)
```
Get the display color of the given folder

@param Folder        The folder to get the display color of
@return The display color of the given folder

### GetFolderName
```angelscript
FName GetFolderName(UMovieSceneFolder Folder)
```
Get the given folder's display name

@param Folder        The folder to use
@return The target folder's name

### RemoveChildFolder
```angelscript
bool RemoveChildFolder(UMovieSceneFolder TargetFolder, UMovieSceneFolder FolderToRemove)
```
Remove a child folder from the given folder

@param TargetFolder          The folder from which to remove a child folder
@param FolderToRemove        The child folder to be removed
@return True if the removal succeeds

### RemoveChildObjectBinding
```angelscript
bool RemoveChildObjectBinding(UMovieSceneFolder Folder, FMovieSceneBindingProxy InObjectBinding)
```
Remove an object binding from the given folder

@param Folder                        The folder from which to remove an object binding
@param InObjectBinding       The object binding to remove
@return True if the operation succeeds

### RemoveChildTrack
```angelscript
bool RemoveChildTrack(UMovieSceneFolder Folder, UMovieSceneTrack InTrack)
```
Remove a track from the given folder

@param Folder                        The folder from which to remove a track
@param InTrack                   The track to remove
@return True if the removal succeeds

### SetFolderColor
```angelscript
bool SetFolderColor(UMovieSceneFolder Folder, FColor InFolderColor)
```
Set the display color of the given folder

@param Folder                        The folder to set the display color of
@param InFolderColor         The new display color for the folder
@return True if the folder's display color is set successfully

### SetFolderName
```angelscript
bool SetFolderName(UMovieSceneFolder Folder, FName InFolderName)
```
Set the name of the given folder

@param Folder                The folder to set the name of
@param InFolderName  The new name for the folder
@return True if the setting of the folder name succeeds

### StaticClass
```angelscript
UClass StaticClass()
```

