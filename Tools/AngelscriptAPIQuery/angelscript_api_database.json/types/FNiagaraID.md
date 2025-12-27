# FNiagaraID

## 属性

### Index
- **类型**: `int`
- **描述**: Index in the indirection table for this particle. Allows fast access to this particles data.
Is always unique among currently living particles but will be reused after the particle dies.

### AcquireTag
- **类型**: `int`
- **描述**: A unique tag for when this ID was acquired.
Allows us to differentiate between particles when one dies and another reuses it's Index.

## 方法

### opAssign
```angelscript
FNiagaraID& opAssign(FNiagaraID Other)
```

