# __Platform

## 方法

### CancelLocalNotification
```angelscript
void CancelLocalNotification(FString ActivationEvent)
```
Cancel a local notification given the ActivationEvent
@param ActivationEvent The string passed into the Schedule call for the notification to be cancelled

### CancelLocalNotificationById
```angelscript
void CancelLocalNotificationById(int NotificationId)
```
Cancel a local notification given the ActivationEvent
@param NotificationId The Id returned from one of the ScheduleLocalNotification* functions

### ClearAllLocalNotifications
```angelscript
void ClearAllLocalNotifications()
```
Clear all pending local notifications. Typically this will be done before scheduling new notifications when going into the background

### GetAllowedDeviceOrientation
```angelscript
EScreenOrientation GetAllowedDeviceOrientation()
```
Returns the allowed orientation of the device. This is NOT the same as GetDeviceOrientation, which only returns Portrait, LandscapeLeft,
PortraitUpsideDown or LandscapeRight. The allowed orientation limits what orientation your device can have. So if you set the allowed orientation
to LandscapeLeft, GetDeviceOrientation will only ever return LandscapeLeft. But if you set the allowed orientation to LandscapeSensor, you are actually
restricting the allowed orientations to LandscapeLeft OR LandscapeRight (depending on the sensor), so GetDeviceOrientation might return LandscapeLeft OR LandscapeRight.

@return An EDeviceScreenOrientation value.

### GetDeviceOrientation
```angelscript
EScreenOrientation GetDeviceOrientation()
```
Returns the current orientation of the device: will be either Portrait, LandscapeLeft, PortraitUpsideDown or LandscapeRight.

@return An EDeviceScreenOrientation value.

### GetLaunchNotification
```angelscript
void GetLaunchNotification(bool& NotificationLaunchedApp, FString& ActivationEvent, int& FireDate)
```
Get the local notification that was used to launch the app
@param NotificationLaunchedApp Return true if a notification was used to launch the app
@param ActivationEvent Returns the name of the ActivationEvent if a notification was used to launch the app
@param FireDate Returns the time the notification was activated

### ScheduleLocalNotificationAtTime
```angelscript
int ScheduleLocalNotificationAtTime(FDateTime FireDateTime, bool LocalTime, FText Title, FText Body, FText Action, FString ActivationEvent)
```
Schedule a local notification at a specific time, inLocalTime specifies the current local time or if UTC time should be used
@param FireDateTime The time at which to fire the local notification
@param LocalTime If true the provided time is in the local timezone, if false it is in UTC
@param Title The title of the notification
@param Body The more detailed description of the notification
@param Action The text to be displayed on the slider controller
@param ActivationEvent A string that is passed in the delegate callback when the app is brought into the foreground from the user activating the notification

### ScheduleLocalNotificationBadgeAtTime
```angelscript
int ScheduleLocalNotificationBadgeAtTime(FDateTime FireDateTime, bool LocalTime, FString ActivationEvent)
```
Schedule a local notification badge at a specific time, inLocalTime specifies the current local time or if UTC time should be used
@param FireDateTime The time at which to fire the local notification
@param LocalTime If true the provided time is in the local timezone, if false it is in UTC
@param ActivationEvent A string that is passed in the delegate callback when the app is brought into the foreground from the user activating the notification

### ScheduleLocalNotificationBadgeFromNow
```angelscript
void ScheduleLocalNotificationBadgeFromNow(int inSecondsFromNow, FString ActivationEvent)
```
Schedule a local notification badge to fire inSecondsFromNow from now
@param inSecondsFromNow The seconds until the notification should fire
@param ActivationEvent A string that is passed in the delegate callback when the app is brought into the foreground from the user activating the notification

### ScheduleLocalNotificationFromNow
```angelscript
int ScheduleLocalNotificationFromNow(int inSecondsFromNow, FText Title, FText Body, FText Action, FString ActivationEvent)
```
Schedule a local notification to fire inSecondsFromNow from now
@param inSecondsFromNow The seconds until the notification should fire
@param LocalTime If true the provided time is in the local timezone, if false it is in UTC
@param Title The title of the notification
@param Body The more detailed description of the notification
@param Action The text to be displayed on the slider controller
@param ActivationEvent A string that is passed in the delegate callback when the app is brought into the foreground from the user activating the notification

### SetAllowedDeviceOrientation
```angelscript
void SetAllowedDeviceOrientation(EScreenOrientation NewAllowedDeviceOrientation)
```
Set the allowed orientation of the device.

