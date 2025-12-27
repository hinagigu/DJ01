# FPluginReferenceMetadata

We use this object to display plugin reference properties using details view.

## 属性

### Name
- **类型**: `FString`
- **描述**: Name of the dependency plugin

### bOptional
- **类型**: `bool`
- **描述**: Whether the dependency plugin is optional meaning it will be silently ignored if not present

### bEnabled
- **类型**: `bool`
- **描述**: Whether the dependency plugin should be enabled by default

## 方法

### opAssign
```angelscript
FPluginReferenceMetadata& opAssign(FPluginReferenceMetadata Other)
```

