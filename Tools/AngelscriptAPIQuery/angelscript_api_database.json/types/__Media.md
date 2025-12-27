# __Media

## 方法

### EnumerateAudioCaptureDevices
```angelscript
void EnumerateAudioCaptureDevices(TArray<FMediaCaptureDevice>& OutDevices, int Filter)
```
Enumerate available audio capture devices.

To filter for a specific subset of devices, use the MakeBitmask node
with EMediaAudioCaptureDeviceFilter as the Bitmask Enum.

@param OutDevices Will contain the available capture devices.
@param Filter The types of capture devices to return (-1 = all).

### EnumerateVideoCaptureDevices
```angelscript
void EnumerateVideoCaptureDevices(TArray<FMediaCaptureDevice>& OutDevices, int Filter)
```
Enumerate available audio capture devices.

To filter for a specific subset of devices, use the MakeBitmask node
with EMediaVideoCaptureDeviceFilter as the Bitmask Enum.

@param OutDevices Will contain the available capture devices.
@param Filter The types of capture devices to return (-1 = all).

### EnumerateWebcamCaptureDevices
```angelscript
void EnumerateWebcamCaptureDevices(TArray<FMediaCaptureDevice>& OutDevices, int Filter)
```
Enumerate available audio capture devices.

To filter for a specific subset of devices, use the MakeBitmask node
with EMediaWebcamCaptureDeviceFilter as the Bitmask Enum.

@param OutDevices Will contain the available capture devices.
@param Filter The types of capture devices to return (-1 = all).

