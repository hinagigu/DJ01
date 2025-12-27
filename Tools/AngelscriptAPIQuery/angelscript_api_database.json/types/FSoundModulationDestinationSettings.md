# FSoundModulationDestinationSettings

Parameter destination settings allowing modulation control override for parameter destinations opting in to the Modulation System.

## 属性

### Value
- **类型**: `float32`

### bEnableModulation
- **类型**: `bool`
- **描述**: Whether or not to enable modulation

### Modulators
- **类型**: `TSet<TObjectPtr<USoundModulatorBase>>`

## 方法

### opAssign
```angelscript
FSoundModulationDestinationSettings& opAssign(FSoundModulationDestinationSettings Other)
```

