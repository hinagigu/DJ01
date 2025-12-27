# UInputDeviceProperty

**继承自**: `UObject`

Base class that represents a single Input Device Property. An Input Device Property
represents a feature that can be set on an input device. Things like what color a
light is, advanced rumble patterns, or trigger haptics.

This top level object can then be evaluated at a specific time to create a lower level
FInputDeviceProperty, which the IInputInterface implementation can interpret however it desires.

The behavior of device properties can vary depending on the current platform. Some platforms may not
support certain device properties. An older gamepad may not have any advanced trigger haptics for
example.

## 属性

### PropertyDuration
- **类型**: `float32`
- **描述**: The duration that this device property should last. Override this if your property has any dynamic curves
to be the max time range.

A duration of 0 means that the device property will be treated as a "One Shot" effect, being applied once
before being removed by the Input Device Subsystem.

## 方法

### EvaluateDeviceProperty
```angelscript
void EvaluateDeviceProperty(FPlatformUserId PlatformUser, FInputDeviceId DeviceId, float DeltaTime, float Duration)
```
Evaluate this device property for a given duration.
If overriding in Blueprints, make sure to call the parent function!

@param PlatformUser           The platform user that should receive this device property change
@param DeltaTime                      Delta time
@param Duration                       The number of seconds that this property has been active. Use this to get things like curve data over time.
@return                                       A pointer to the evaluated input device property.

### ResetDeviceProperty
```angelscript
void ResetDeviceProperty(FPlatformUserId PlatformUser, FInputDeviceId DeviceId, bool bForceReset)
```
Reset the current device property. Provides an opportunity to reset device state after evaluation is complete.
If overriding in Blueprints, make sure to call the parent function!

@param PlatformUser           The platform user that should receive this device property change

