# __GooglePAD

## 方法

### CancelDownload
```angelscript
EGooglePADErrorCode CancelDownload(TArray<FString> AssetPacks)
```
Cancel download of a set of asset packs

### GetAssetPackLocation
```angelscript
EGooglePADErrorCode GetAssetPackLocation(FString Name, int& Location)
```
Get location handle of requested asset pack (release when done)

### GetAssetsPath
```angelscript
FString GetAssetsPath(int Location)
```
Get asset path from from location

### GetBytesDownloaded
```angelscript
int GetBytesDownloaded(int State)
```
Get the number of bytes downloaded from a download state

### GetDownloadState
```angelscript
EGooglePADErrorCode GetDownloadState(FString Name, int& State)
```
Get download state handle of an asset pack (release when done)

### GetDownloadStatus
```angelscript
EGooglePADDownloadStatus GetDownloadStatus(int State)
```
Get download status from a download state

### GetShowCellularDataConfirmationStatus
```angelscript
EGooglePADErrorCode GetShowCellularDataConfirmationStatus(EGooglePADCellularDataConfirmStatus& Status)
```
Get status of cellular confirmation dialog

### GetStorageMethod
```angelscript
EGooglePADStorageMethod GetStorageMethod(int Location)
```
Get storage method from location

### GetTotalBytesToDownload
```angelscript
int GetTotalBytesToDownload(int State)
```
Get the total number of bytes to download from a download state

### ReleaseAssetPackLocation
```angelscript
void ReleaseAssetPackLocation(int Location)
```
Release location resources

### ReleaseDownloadState
```angelscript
void ReleaseDownloadState(int State)
```
Release download state resources

### RequestDownload
```angelscript
EGooglePADErrorCode RequestDownload(TArray<FString> AssetPacks)
```
Request download of a set of asset packs

### RequestInfo
```angelscript
EGooglePADErrorCode RequestInfo(TArray<FString> AssetPacks)
```
Request information about a set of asset packs

### RequestRemoval
```angelscript
EGooglePADErrorCode RequestRemoval(FString Name)
```
Request removal of an asset pack

### ShowCellularDataConfirmation
```angelscript
EGooglePADErrorCode ShowCellularDataConfirmation()
```
Show confirmation dialog requesting data download over cellular network

