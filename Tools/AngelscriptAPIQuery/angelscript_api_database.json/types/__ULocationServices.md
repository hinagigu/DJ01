# __ULocationServices

## 方法

### AreLocationServicesEnabled
```angelscript
bool AreLocationServicesEnabled()
```
Checks if the Location Services on the mobile device are enabled for this application
@return - true if the mobile device has enabled the appropriate service for the app

### GetLastKnownLocation
```angelscript
FLocationServicesData GetLastKnownLocation()
```
Returns the last location information returned by the location service. If no location update has been made, will return
a default-value-filled struct.
@return - the last known location from updates

### GetLocationServicesImpl
```angelscript
ULocationServicesImpl GetLocationServicesImpl()
```
* Returns the Location Services implementation object. Intended to be used to set up the FLocationServicesData_OnLocationChanged
* delegate in Blueprints.
* @return - the Android or IOS impl object

### InitLocationServices
```angelscript
bool InitLocationServices(ELocationAccuracy Accuracy, float32 UpdateFrequency, float32 MinDistanceFilter)
```
Called to set up the Location Service before use

@param Accuracy - as seen in the enum above
@param UpdateFrequency - in milliseconds. (Android only)
@param MinDistance - minDistance before a location update, in meters. 0 here means "update asap"
@return - true if Initialization was succesful

### IsLocationAccuracyAvailable
```angelscript
bool IsLocationAccuracyAvailable(ELocationAccuracy Accuracy)
```
Checks if the supplied Accuracy is available on the current device.
@param Accuracy - the accuracy to check
@return - true if the mobile device can support the Accuracy, false if it will use a different accuracy

### StartLocationServices
```angelscript
bool StartLocationServices()
```
Starts requesting location updates from the appropriate Location Service
@return - true if startup successful

### StopLocationServices
```angelscript
bool StopLocationServices()
```
Stops the updates of location from the Location Service that was started with StartLocationService
@return - true if stop is successful

### StaticClass
```angelscript
UClass StaticClass()
```

