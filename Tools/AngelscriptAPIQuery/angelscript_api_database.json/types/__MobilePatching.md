# __MobilePatching

## 方法

### GetActiveDeviceProfileName
```angelscript
FString GetActiveDeviceProfileName()
```
Get the name of currently selected device profile name

### GetInstalledContent
```angelscript
UMobileInstalledContent GetInstalledContent(FString InstallDirectory)
```
Get the installed content. Will return non-null object if there is an installed content at specified directory
User can choose to mount installed content into the game

### GetSupportedPlatformNames
```angelscript
TArray<FString> GetSupportedPlatformNames()
```
Get the list of supported platform names on this device. Example: Android_ETC2, Android_ASTC

### HasActiveWiFiConnection
```angelscript
bool HasActiveWiFiConnection()
```
Whether WiFi connection is currently available

### RequestContent
```angelscript
void RequestContent(FString RemoteManifestURL, FString CloudURL, FString InstallDirectory, FOnRequestContentSucceeded OnSucceeded, FOnRequestContentFailed OnFailed)
```
Attempt to download manifest file using specified manifest URL.
On success it will return an object that represents remote content. This object can be queried for additional information, like total content size, download size, etc.
User can choose to download and install remote content.
@param       RemoteManifestURL : URL from where manifest file can be downloaded. (http://my-server.com/awesomecontent.manifest)
@param       CloudURL :  URL from where content chunk data can be downloaded. (http://my-server.com/awesomecontent/clouddir)
@param       InstallDirectory: Relative directory to where downloaded content should be installed (MyContent/AwesomeContent)
@param       OnSucceeded: Callback on manifest download success. Will return object that represents remote content
@param       OnFailed: Callback on manifest download fail. Will return error message text and error integer code

