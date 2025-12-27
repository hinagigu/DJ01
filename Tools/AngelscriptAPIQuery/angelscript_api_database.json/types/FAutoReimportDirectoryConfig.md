# FAutoReimportDirectoryConfig

Auto reimport settings for a specific directory

## 属性

### SourceDirectory
- **类型**: `FString`
- **描述**: Path to a virtual package path (eg /Game/ or /MyPlugin/), or absolute paths on disk where your source content files reside.

### MountPoint
- **类型**: `FString`
- **描述**: (Optional) Specify a virtual mout point (e.g. /Game/) to map this directory to on disk. Doing so allows auto-creation of assets when a source content file is created in this folder (see below).

### Wildcards
- **类型**: `TArray<FAutoReimportWildcard>`
- **描述**: (Optional) Specify a set of wildcards to include or exclude files from this auto-reimporter.

## 方法

### opAssign
```angelscript
FAutoReimportDirectoryConfig& opAssign(FAutoReimportDirectoryConfig Other)
```

