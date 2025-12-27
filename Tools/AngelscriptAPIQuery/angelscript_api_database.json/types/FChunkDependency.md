# FChunkDependency

A single dependency, read from ini file

## 属性

### ChunkID
- **类型**: `int`
- **描述**: The child chunk

### ParentChunkID
- **类型**: `int`
- **描述**: Parent chunk, anything in both Parent and Child is only placed into Parent

## 方法

### opAssign
```angelscript
FChunkDependency& opAssign(FChunkDependency Other)
```

