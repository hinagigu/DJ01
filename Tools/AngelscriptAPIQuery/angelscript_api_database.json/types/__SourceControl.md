# __SourceControl

## 方法

### AsyncQueryFileState
```angelscript
void AsyncQueryFileState(FQueryFileStateDelegate__SourceControlHelpers FileStateCallback, FString InFile, bool bSilent)
```
Query the source control state of the specified file, asynchronously.

@param        FileStateCallback Source control state - see USourceControlState. It will have bIsValid set to false if it could not have its values set.
@param        InFile                    The file to query - can be either fully qualified path, relative path, long package name, asset path or export text path (often stored on clipboard)
@param        bSilent                   if false (default) then write out any error info to the Log. Any error text can be retrieved by LastErrorMsg() regardless.

### CheckInFile
```angelscript
bool CheckInFile(FString InFile, FString InDescription, bool bSilent, bool bKeepCheckedOut)
```
Use currently set source control provider to check in a file.
@note        Blocks until action is complete.

@param       InFile                  The file to check in - can be either fully qualified path, relative path, long package name, asset path or export text path (often stored on clipboard)
@param       InDescription   Description for check in
@param       bSilent                 if false (default) then write out any error info to the Log. Any error text can be retrieved by LastErrorMsg() regardless.
@param       bKeepCheckedOut Keep files checked-out after checking in. This is helpful for maintaining "ownership" of files if further operations are needed.
@return      true if succeeded, false if failed and can call LastErrorMsg() for more info.

### CheckInFiles
```angelscript
bool CheckInFiles(TArray<FString> InFiles, FString InDescription, bool bSilent, bool bKeepCheckedOut)
```
Use currently set source control provider to check in specified files.
@note        Blocks until action is complete.

@param       InFiles                 Files to check out - can be either fully qualified path, relative path, long package name, asset path or export text path (often stored on clipboard)
@param       InDescription   Description for check in
@param       bSilent                 if false (default) then write out any error info to the Log. Any error text can be retrieved by LastErrorMsg() regardless.
@param       bKeepCheckedOut Keep files checked-out after checking in. This is helpful for maintaining "ownership" of files if further operations are needed.
@return      true if succeeded, false if failed and can call LastErrorMsg() for more info.

### CheckOutFile
```angelscript
bool CheckOutFile(FString InFile, bool bSilent)
```
Use currently set source control provider to check out a file.
@note        Blocks until action is complete.

@param       InFile          The file to check out - can be either fully qualified path, relative path, long package name, asset path or export text path (often stored on clipboard)
@param       bSilent         if false (default) then write out any error info to the Log. Any error text can be retrieved by LastErrorMsg() regardless.
@return      true if succeeded, false if failed and can call LastErrorMsg() for more info.

### CheckOutFiles
```angelscript
bool CheckOutFiles(TArray<FString> InFiles, bool bSilent)
```
Use currently set source control provider to check out specified files.
@note        Blocks until action is complete.

@param       InFiles         Files to check out - can be either fully qualified path, relative path, long package name, asset path or export text path (often stored on clipboard)
@param       bSilent         if false (default) then write out any error info to the Log. Any error text can be retrieved by LastErrorMsg() regardless.
@return      true if succeeded, false if failed and can call LastErrorMsg() for more info.

### CheckOutOrAddFile
```angelscript
bool CheckOutOrAddFile(FString InFile, bool bSilent)
```
Use currently set source control provider to check out file or mark it for add.
@note        Blocks until action is complete.

@param       InFile          The file to check out/add - can be either fully qualified path, relative path, long package name, asset path or export text path (often stored on clipboard)
@param       bSilent         if false (default) then write out any error info to the Log. Any error text can be retrieved by LastErrorMsg() regardless.
@return      true if succeeded, false if failed and can call LastErrorMsg() for more info.

### CheckOutOrAddFiles
```angelscript
bool CheckOutOrAddFiles(TArray<FString> InFiles, bool bSilent)
```
Use currently set source control provider to check out files or mark them for add.
@note        Blocks until action is complete.

@param       InFiles         The files to check out/add - can be either fully qualified path, relative path, long package name, asset path or export text path (often stored on clipboard)
@param       bSilent         if false (default) then write out any error info to the Log. Any error text can be retrieved by LastErrorMsg() regardless.
@return      true if succeeded, false if failed and can call LastErrorMsg() for more info.

### CopyFile
```angelscript
bool CopyFile(FString InSourceFile, FString InDestFile, bool bSilent)
```
Use currently set source control provider to copy a file.
@note        Blocks until action is complete.

@param       InSourceFile    Source file string to copy from - can be either fully qualified path, relative path, long package name, asset path or export text path (often stored on clipboard)
@param       InDestFile              Source file string to copy to - can be either fully qualified path, relative path, long package name, asset path or export text path (often stored on clipboard). If package, then uses same extension as source file.
@param       bSilent                 if false (default) then write out any error info to the Log. Any error text can be retrieved by LastErrorMsg() regardless.
@return      true if succeeded, false if failed and can call LastErrorMsg() for more info.

### CurrentProvider
```angelscript
FString CurrentProvider()
```
Determine the name of the current source control provider.
@return      the name of the current source control provider. If one is not set then "None" is returned.

### IsAvailable
```angelscript
bool IsAvailable()
```
Quick check if currently set source control provider is enabled and available for use
(server-based providers can use this to return whether the server is available or not)

@return      true if source control is available, false if it is not

### IsEnabled
```angelscript
bool IsEnabled()
```
Determine if there is a source control system enabled
@return      true if enabled, false if not

### LastErrorMsg
```angelscript
FText LastErrorMsg()
```
Get status text set by SourceControl system if an error occurs regardless whether bSilent is set or not.
Only set if there was an error.

### MarkFileForAdd
```angelscript
bool MarkFileForAdd(FString InFile, bool bSilent)
```
Use currently set source control provider to mark a file for add. Does nothing (and returns true) if the file is already under SC
@note        Blocks until action is complete.

@param       InFile          The file to add - can be either fully qualified path, relative path, long package name, asset path or export text path (often stored on clipboard)
@param       bSilent         if false (default) then write out any error info to the Log. Any error text can be retrieved by LastErrorMsg() regardless.
@return      true if succeeded, false if failed and can call LastErrorMsg() for more info.

### MarkFileForDelete
```angelscript
bool MarkFileForDelete(FString InFile, bool bSilent)
```
Use currently set source control provider to remove file from source control and
delete the file.
@note        Blocks until action is complete.

@param       InFile          The file to delete - can be either fully qualified path, relative path, long package name, asset path or export text path (often stored on clipboard)
@param       bSilent         if false (default) then write out any error info to the Log. Any error text can be retrieved by LastErrorMsg() regardless.
@return      true if succeeded, false if failed and can call LastErrorMsg() for more info.

### MarkFilesForAdd
```angelscript
bool MarkFilesForAdd(TArray<FString> InFiles, bool bSilent)
```
Use currently set source control provider to mark files for add. Does nothing (and returns true) for any file that is already under SC
@note        Blocks until action is complete.

@param       InFiles         Files to check out - can be either fully qualified path, relative path, long package name, asset path or export text path (often stored on clipboard)
@param       bSilent         if false (default) then write out any error info to the Log. Any error text can be retrieved by LastErrorMsg() regardless.
@return      true if succeeded, false if failed and can call LastErrorMsg() for more info.

### MarkFilesForDelete
```angelscript
bool MarkFilesForDelete(TArray<FString> InFiles, bool bSilent)
```
Use currently set source control provider to remove files from source control and delete the files.
@note        Blocks until action is complete.

@param       InFile          The file to delete - can be either fully qualified path, relative path, long package name, asset path or export text path (often stored on clipboard)
@param       bSilent         if false (default) then write out any error info to the Log. Any error text can be retrieved by LastErrorMsg() regardless.
@return      true if succeeded, false if failed and can call LastErrorMsg() for more info.

### QueryFileState
```angelscript
FSourceControlState QueryFileState(FString InFile, bool bSilent)
```
Use currently set source control provider to query a file's source control state.
@note        Blocks until action is complete.

@param       InFile                  The file to query - can be either fully qualified path, relative path, long package name, asset path or export text path (often stored on clipboard)
@param       bSilent                 if false (default) then write out any error info to the Log. Any error text can be retrieved by LastErrorMsg() regardless.
@return      Source control state - see USourceControlState. It will have bIsValid set to false if
                     it could not have its values set.

### RevertAndReloadPackages
```angelscript
bool RevertAndReloadPackages(TArray<FString> InPackagesToRevert, bool bRevertAll, bool bReloadWorld)
```
Reverts the provided files then reloads packages.
@param       InPackagesToRevert                                      The packages to revert
@param       bRevertAll                                                      Whether to revert all files
@param       bReloadWorld                                            Reload the world
@return true if succeeded.

### RevertFile
```angelscript
bool RevertFile(FString InFile, bool bSilent)
```
Use currently set source control provider to revert a file regardless whether any changes will be lost or not.
@note        Blocks until action is complete.

@param       InFile  The file to revert - can be either fully qualified path, relative path, long package name, asset path or export text path (often stored on clipboard)
@param       bSilent if false (default) then write out any error info to the Log. Any error text can be retrieved by LastErrorMsg() regardless.
@return      true if succeeded, false if failed and can call LastErrorMsg() for more info.

### RevertFiles
```angelscript
bool RevertFiles(TArray<FString> InFiles, bool bSilent)
```
Use currently set source control provider to revert files regardless whether any changes will be lost or not.
@note        Blocks until action is complete.

@param       InFiles Files to revert - can be either fully qualified path, relative path, long package name, asset path or export text path (often stored on clipboard)
@param       bSilent if false (default) then write out any error info to the Log. Any error text can be retrieved by LastErrorMsg() regardless.
@return      true if succeeded, false if failed and can call LastErrorMsg() for more info.

### RevertUnchangedFile
```angelscript
bool RevertUnchangedFile(FString InFile, bool bSilent)
```
Use currently set source control provider to revert a file provided no changes have been made.
@note        Blocks until action is complete.

@param       InFile  File to check out - can be either fully qualified path, relative path, long package name, asset path or export text path (often stored on clipboard)
@param       bSilent if false (default) then write out any error info to the Log. Any error text can be retrieved by LastErrorMsg() regardless.
@return      true if succeeded, false if failed and can call LastErrorMsg() for more info.

### RevertUnchangedFiles
```angelscript
bool RevertUnchangedFiles(TArray<FString> InFiles, bool bSilent)
```
Use currently set source control provider to revert files provided no changes have been made.
@note        Blocks until action is complete.

@param       InFiles Files to check out - can be either fully qualified path, relative path, long package name, asset path or export text path (often stored on clipboard)
@param       bSilent if false (default) then write out any error info to the Log. Any error text can be retrieved by LastErrorMsg() regardless.
@return      true if succeeded, false if failed and can call LastErrorMsg() for more info.

### SyncFile
```angelscript
bool SyncFile(FString InFile, bool bSilent)
```
Use currently set source control provider to sync a file or directory to the head revision.
@note        Blocks until action is complete.

@param       InFile  The file or directory to sync - can be either fully qualified path, relative path, long package name, asset path or export text path (often stored on clipboard)
@param       bSilent if false (default) then write out any error info to the Log. Any error text can be retrieved by LastErrorMsg() regardless.
@return      true if succeeded, false if failed and can call LastErrorMsg() for more info.

### SyncFiles
```angelscript
bool SyncFiles(TArray<FString> InFiles, bool bSilent)
```
Use currently set source control provider to sync files or directories to the head revision.
@note        Blocks until action is complete.

@param       InFiles Files or directories to sync - can be either fully qualified path, relative path, long package name, asset path or export text path (often stored on clipboard)
@param       bSilent if false (default) then write out any error info to the Log. Any error text can be retrieved by LastErrorMsg() regardless.
@return      true if succeeded, false if failed and can call LastErrorMsg() for more info.

