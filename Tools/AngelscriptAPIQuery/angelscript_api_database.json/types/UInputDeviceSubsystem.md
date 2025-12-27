# UInputDeviceSubsystem

**继承自**: `UEngineSubsystem`

The input device subsystem provides an interface to allow users to set Input Device Properties
on any Platform User.

## 属性

### OnInputHardwareDeviceChanged
- **类型**: `FHardwareInputDeviceChanged`

## 方法

### ActivateDevicePropertyOfClass
```angelscript
FInputDevicePropertyHandle ActivateDevicePropertyOfClass(TSubclassOf<UInputDeviceProperty> PropertyClass, FActivateDevicePropertyParams Params)
```
Spawn a new instance of the given device property class and activate it.

### GetActiveDeviceProperty
```angelscript
UInputDeviceProperty GetActiveDeviceProperty(FInputDevicePropertyHandle Handle)
```
Returns a pointer to the active input device property with the given handle. Returns null if the property doesn't exist

### GetInputDeviceHardwareIdentifier
```angelscript
FHardwareDeviceIdentifier GetInputDeviceHardwareIdentifier(FInputDeviceId InputDevice)
```

### GetMostRecentlyUsedHardwareDevice
```angelscript
FHardwareDeviceIdentifier GetMostRecentlyUsedHardwareDevice(FPlatformUserId InUserId)
```
Gets the most recently used hardware input device for the given platform user

### IsPropertyActive
```angelscript
bool IsPropertyActive(FInputDevicePropertyHandle Handle)
```
Returns true if the property associated with the given handle is currently active, and it is not pending removal

### RemoveAllDeviceProperties
```angelscript
void RemoveAllDeviceProperties()
```
Removes all the current Input Device Properties that are active, regardless of the Platform User

### RemoveDevicePropertyByHandle
```angelscript
void RemoveDevicePropertyByHandle(FInputDevicePropertyHandle HandleToRemove)
```
Remove a single device property based on it's handle

@param FInputDevicePropertyHandle             Device property handle to be removed

@return                                                               The number of removed device properties.

### RemoveDevicePropertyHandles
```angelscript
void RemoveDevicePropertyHandles(TSet<FInputDevicePropertyHandle> HandlesToRemove)
```
Remove a set of device properties based on their handles.

@param HandlesToRemove        The set of device property handles to remove

@return                                       The number of removed device properties

