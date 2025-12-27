# __EnhancedInput

## 方法

### BreakInputActionValue
```angelscript
void BreakInputActionValue(FInputActionValue InActionValue, float& X, float& Y, float& Z, EInputActionValueType& Type)
```
Breaks an ActionValue into X, Y, Z. Axes not supported by value type will be 0.

### Conv_InputActionValueToString
```angelscript
FString Conv_InputActionValueToString(FInputActionValue ActionValue)
```
Converts a FInputActionValue to a string

### GetMappingName
```angelscript
FName GetMappingName(FEnhancedActionKeyMapping ActionKeyMapping)
```
Returns the name of the mapping based on setting behavior used. If no name is found in the Mappable Key Settings it will return the name set in Player Mappable Options if bIsPlayerMappable is true.

### GetPlayerMappableKeySettings
```angelscript
UPlayerMappableKeySettings GetPlayerMappableKeySettings(FEnhancedActionKeyMapping ActionKeyMapping)
```
Returns the Player Mappable Key Settings owned by the Action Key Mapping or by the referenced Input Action, or nothing based of the Setting Behavior.

### IsActionKeyMappingPlayerMappable
```angelscript
bool IsActionKeyMappingPlayerMappable(FEnhancedActionKeyMapping ActionKeyMapping)
```
Returns true if this Action Key Mapping either holds a Player Mappable Key Settings or is set bIsPlayerMappable.

### MakeInputActionValueOfType
```angelscript
FInputActionValue MakeInputActionValueOfType(float X, float Y, float Z, EInputActionValueType ValueType)
```
Builds an ActionValue from X, Y, Z. Inherits type from an existing ActionValue. Ignores axis values unused by the provided value type.
@note Intended for use in Input Modifier Modify Raw overloads to modify an existing Input Action Value.

### RequestRebuildControlMappingsUsingContext
```angelscript
void RequestRebuildControlMappingsUsingContext(const UInputMappingContext Context, bool bForceImmediately)
```
Flag all enhanced input subsystems making use of the mapping context for reapplication of all control mappings at the end of this frame.
@param Context                               Mappings will be rebuilt for all subsystems utilizing this context.
@param bForceImmediately             The mapping changes will be applied synchronously, rather than at the end of the frame, making them available to the input system on the same frame.

