# FMetaSoundQualitySettings

## 属性

### Name
- **类型**: `FName`
- **描述**: Name of this quality setting. This will appear in the quality dropdown list.
              The names should be unique and adequately describe the Entry. "High", "Low" etc. *

### SampleRate
- **类型**: `FPerPlatformInt`
- **描述**: Sample Rate (in Hz). NOTE: A Zero value will have no effect and use the Device Rate. *

### BlockRate
- **类型**: `FPerPlatformFloat`
- **描述**: Block Rate (in Hz). NOTE: A Zero value will have no effect and use the Default (100)  *

## 方法

### opAssign
```angelscript
FMetaSoundQualitySettings& opAssign(FMetaSoundQualitySettings Other)
```

