# FImageWriteOptions

Options specific to writing image files to disk

## 属性

### Format
- **类型**: `EDesiredImageFormat`

### OnComplete
- **类型**: `FOnImageWriteComplete`
- **描述**: A callback to invoke when the image has been written, or there was an error

### CompressionQuality
- **类型**: `int`

### bOverwriteFile
- **类型**: `bool`

### bAsync
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FImageWriteOptions& opAssign(FImageWriteOptions Other)
```

