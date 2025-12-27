# __Input

## 方法

### CalibrateTilt
```angelscript
void CalibrateTilt()
```
Calibrate the tilt for the input device

### EqualEqual_InputChordInputChord
```angelscript
bool EqualEqual_InputChordInputChord(FInputChord A, FInputChord B)
```
Test if the input chords are equal (A == B)
@param A - The chord to compare against
@param B - The chord to compare
Returns true if the chords are equal, false otherwise

### EqualEqual_KeyKey
```angelscript
bool EqualEqual_KeyKey(FKey A, FKey B)
```
Test if the input key are equal (A == B)
@param A - The key to compare against
@param B - The key to compare
Returns true if the key are equal, false otherwise

### GetAnalogValue
```angelscript
float32 GetAnalogValue(FAnalogInputEvent Input)
```

### GetKey
```angelscript
FKey GetKey(FKeyEvent Input)
```
Returns the key for this event.

@return  Key name

### GetModifierKeysState
```angelscript
FSlateModifierKeysState GetModifierKeysState()
```
Returns a snapshot of the cached modifier-keys state for the application.

### GetUserIndex
```angelscript
int GetUserIndex(FKeyEvent Input)
```

### InputChord_GetDisplayName
```angelscript
FText InputChord_GetDisplayName(FInputChord Key)
```
@return The display name of the input chord

### InputEvent_IsAltDown
```angelscript
bool InputEvent_IsAltDown(FInputEvent Input)
```
Returns true if either alt key was down when this event occurred

### InputEvent_IsCommandDown
```angelscript
bool InputEvent_IsCommandDown(FInputEvent Input)
```
Returns true if either command key was down when this event occurred

### InputEvent_IsControlDown
```angelscript
bool InputEvent_IsControlDown(FInputEvent Input)
```
Returns true if either control key was down when this event occurred

### InputEvent_IsLeftAltDown
```angelscript
bool InputEvent_IsLeftAltDown(FInputEvent Input)
```
Returns true if left alt key was down when this event occurred

### InputEvent_IsLeftCommandDown
```angelscript
bool InputEvent_IsLeftCommandDown(FInputEvent Input)
```
Returns true if left command key was down when this event occurred

### InputEvent_IsLeftControlDown
```angelscript
bool InputEvent_IsLeftControlDown(FInputEvent Input)
```
Returns true if left control key was down when this event occurred

### InputEvent_IsLeftShiftDown
```angelscript
bool InputEvent_IsLeftShiftDown(FInputEvent Input)
```
Returns true if left shift key was down when this event occurred

### InputEvent_IsRepeat
```angelscript
bool InputEvent_IsRepeat(FInputEvent Input)
```
Returns whether or not this character is an auto-repeated keystroke

### InputEvent_IsRightAltDown
```angelscript
bool InputEvent_IsRightAltDown(FInputEvent Input)
```
Returns true if right alt key was down when this event occurred

### InputEvent_IsRightCommandDown
```angelscript
bool InputEvent_IsRightCommandDown(FInputEvent Input)
```
Returns true if right command key was down when this event occurred

### InputEvent_IsRightControlDown
```angelscript
bool InputEvent_IsRightControlDown(FInputEvent Input)
```
Returns true if left control key was down when this event occurred

### InputEvent_IsRightShiftDown
```angelscript
bool InputEvent_IsRightShiftDown(FInputEvent Input)
```
Returns true if right shift key was down when this event occurred

### InputEvent_IsShiftDown
```angelscript
bool InputEvent_IsShiftDown(FInputEvent Input)
```
Returns true if either shift key was down when this event occurred

### Key_GetDisplayName
```angelscript
FText Key_GetDisplayName(FKey Key, bool bLongDisplayName)
```
Returns the display name of the key.

### Key_GetNavigationActionFromKey
```angelscript
EUINavigationAction Key_GetNavigationActionFromKey(FKeyEvent InKeyEvent)
```
Returns the navigation action corresponding to this key, or Invalid if not found

### Key_GetNavigationDirectionFromAnalog
```angelscript
EUINavigation Key_GetNavigationDirectionFromAnalog(FAnalogInputEvent InAnalogEvent)
```
Returns the navigation action corresponding to this key, or Invalid if not found

### Key_GetNavigationDirectionFromKey
```angelscript
EUINavigation Key_GetNavigationDirectionFromKey(FKeyEvent InKeyEvent)
```
Returns the navigation action corresponding to this key, or Invalid if not found

### Key_IsAnalog
```angelscript
bool Key_IsAnalog(FKey Key)
```
Returns true if the key is an analog axis

### Key_IsAxis1D
```angelscript
bool Key_IsAxis1D(FKey Key)
```
Returns true if the key is a 1D (float) axis

### Key_IsAxis2D
```angelscript
bool Key_IsAxis2D(FKey Key)
```
Returns true if the key is a 2D (vector) axis

### Key_IsAxis3D
```angelscript
bool Key_IsAxis3D(FKey Key)
```
Returns true if the key is a 3D (vector) axis

### Key_IsButtonAxis
```angelscript
bool Key_IsButtonAxis(FKey Key)
```
Returns true if the key is a 1D axis emulating a digital button press.

### Key_IsDigital
```angelscript
bool Key_IsDigital(FKey Key)
```
Returns true if the key is a digital button press

### Key_IsGamepadKey
```angelscript
bool Key_IsGamepadKey(FKey Key)
```
Returns true if the key is a gamepad button

### Key_IsKeyboardKey
```angelscript
bool Key_IsKeyboardKey(FKey Key)
```
Returns true if the key is a keyboard button

### Key_IsModifierKey
```angelscript
bool Key_IsModifierKey(FKey Key)
```
Returns true if the key is a modifier key: Ctrl, Command, Alt, Shift

### Key_IsMouseButton
```angelscript
bool Key_IsMouseButton(FKey Key)
```
Returns true if the key is a mouse button

### Key_IsValid
```angelscript
bool Key_IsValid(FKey Key)
```
Returns true if this is a valid key.

### ModifierKeysState_IsAltDown
```angelscript
bool ModifierKeysState_IsAltDown(FSlateModifierKeysState KeysState)
```
Returns true if either alt key was down when the key state was captured

### ModifierKeysState_IsCommandDown
```angelscript
bool ModifierKeysState_IsCommandDown(FSlateModifierKeysState KeysState)
```
Returns true if either command key was down when the key state was captured

### ModifierKeysState_IsControlDown
```angelscript
bool ModifierKeysState_IsControlDown(FSlateModifierKeysState KeysState)
```
Returns true if either control key was down when the key state was captured

### ModifierKeysState_IsShiftDown
```angelscript
bool ModifierKeysState_IsShiftDown(FSlateModifierKeysState KeysState)
```
Returns true if either shift key was down when the key state was captured

### PointerEvent_GetCursorDelta
```angelscript
FVector2D PointerEvent_GetCursorDelta(FPointerEvent Input)
```
Returns the distance the mouse traveled since the last event was handled.

### PointerEvent_GetEffectingButton
```angelscript
FKey PointerEvent_GetEffectingButton(FPointerEvent Input)
```
Mouse button that caused this event to be raised (possibly FKey::Invalid)

### PointerEvent_GetGestureDelta
```angelscript
FVector2D PointerEvent_GetGestureDelta(FPointerEvent Input)
```
Returns the change in gesture value since the last gesture event of the same type.

### PointerEvent_GetGestureType
```angelscript
ESlateGesture PointerEvent_GetGestureType(FPointerEvent Input)
```
Returns the type of touch gesture

### PointerEvent_GetLastScreenSpacePosition
```angelscript
FVector2D PointerEvent_GetLastScreenSpacePosition(FPointerEvent Input)
```
Returns the position of the cursor in screen space last time we handled an input event

### PointerEvent_GetPointerIndex
```angelscript
int PointerEvent_GetPointerIndex(FPointerEvent Input)
```
Returns the unique identifier of the pointer (e.g., finger index)

### PointerEvent_GetScreenSpacePosition
```angelscript
FVector2D PointerEvent_GetScreenSpacePosition(FPointerEvent Input)
```
Returns The position of the cursor in screen space

### PointerEvent_GetTouchpadIndex
```angelscript
int PointerEvent_GetTouchpadIndex(FPointerEvent Input)
```
Returns the index of the touch pad that generated this event (for platforms with multiple touch pads per user)

### PointerEvent_GetUserIndex
```angelscript
int PointerEvent_GetUserIndex(FPointerEvent Input)
```
Returns the index of the user that caused the event

### PointerEvent_GetWheelDelta
```angelscript
float32 PointerEvent_GetWheelDelta(FPointerEvent Input)
```
How much did the mouse wheel turn since the last mouse event

### PointerEvent_IsMouseButtonDown
```angelscript
bool PointerEvent_IsMouseButtonDown(FPointerEvent Input, FKey MouseButton)
```
Mouse buttons that are currently pressed

### PointerEvent_IsTouchEvent
```angelscript
bool PointerEvent_IsTouchEvent(FPointerEvent Input)
```
Returns true if this event a result from a touch (as opposed to a mouse)

