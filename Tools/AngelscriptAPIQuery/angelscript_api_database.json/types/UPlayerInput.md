# UPlayerInput

**继承自**: `UObject`

Object within PlayerController that processes player input.
Only exists on the client in network games.

@see https://docs.unrealengine.com/latest/INT/Gameplay/Input/index.html

## 方法

### GetOuterAPlayerController
```angelscript
APlayerController GetOuterAPlayerController()
```
Return's this object casted to a player controller. This can be null if there is no player controller.

### AddActionMapping
```angelscript
void AddActionMapping(FInputActionKeyMapping KeyMapping)
```

### AddAxisMapping
```angelscript
void AddAxisMapping(FInputAxisKeyMapping KeyMapping)
```

### ForceRebuildingKeyMaps
```angelscript
void ForceRebuildingKeyMaps(bool bRestoreDefaults)
```

### GetEngineDefinedActionMappings
```angelscript
TArray<FInputActionKeyMapping> GetEngineDefinedActionMappings(FName ActionName)
```

### GetEngineDefinedAxisMappings
```angelscript
TArray<FInputAxisKeyMapping> GetEngineDefinedAxisMappings(FName AxisName)
```

### GetKeysForAction
```angelscript
TArray<FInputActionKeyMapping> GetKeysForAction(FName ActionName)
```

### GetKeysForAxis
```angelscript
TArray<FInputAxisKeyMapping> GetKeysForAxis(FName AxisName)
```

### GetMouseSensitivityX
```angelscript
float32 GetMouseSensitivityX()
```

### GetMouseSensitivityY
```angelscript
float32 GetMouseSensitivityY()
```

### InvertAxis
```angelscript
void InvertAxis(FName AxisName)
```

### RemoveActionMapping
```angelscript
void RemoveActionMapping(FInputActionKeyMapping KeyMapping)
```

### RemoveAxisMapping
```angelscript
void RemoveAxisMapping(FInputAxisKeyMapping KeyMapping)
```

### SetMouseSensitivity
```angelscript
void SetMouseSensitivity(float32 Sensitivity)
```

