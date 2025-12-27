# UMovieSceneCameraCutSection

**继承自**: `UMovieSceneSection`

Movie CameraCuts are sections on the CameraCuts track, that show what the viewer "sees"

## 属性

### bLockPreviousCamera
- **类型**: `bool`
- **描述**: When blending, lock the previous camera (camera cut or gameplay camera).

## 方法

### GetCameraBindingID
```angelscript
FMovieSceneObjectBindingID GetCameraBindingID()
```
Gets the camera binding for this CameraCut section

### SetCameraBindingID
```angelscript
void SetCameraBindingID(FMovieSceneObjectBindingID InCameraBindingID)
```
Sets the camera binding for this CameraCut section

