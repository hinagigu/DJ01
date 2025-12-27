# FIniStringValue

Helper struct for setting string console ini values.

## 属性

### Section
- **类型**: `FString`
- **描述**: From .ini. Ex: /Script/Engine.RendererSettings

### Key
- **类型**: `FString`
- **描述**: From .ini. Ex: r.GPUSkin.Support16BitBoneIndex

### Value
- **类型**: `FString`
- **描述**: From .ini. Ex: True

### Filename
- **类型**: `FString`
- **描述**: From .ini, relative to {PROJECT}. Ex: /Config/DefaultEngine.ini

## 方法

### opAssign
```angelscript
FIniStringValue& opAssign(FIniStringValue Other)
```

