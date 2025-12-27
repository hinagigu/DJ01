# FNiagaraMeshMaterialOverride

## 属性

### ExplicitMat
- **类型**: `UMaterialInterface`
- **描述**: Use this UMaterialInterface if set to a valid value. This will be subordinate to UserParamBinding if it is set to a valid user variable.

### UserParamBinding
- **类型**: `FNiagaraUserParameterBinding`
- **描述**: Use the UMaterialInterface bound to this user variable if it is set to a valid value. If this is bound to a valid value and ExplicitMat is also set, UserParamBinding wins.

## 方法

### opAssign
```angelscript
FNiagaraMeshMaterialOverride& opAssign(FNiagaraMeshMaterialOverride Other)
```

