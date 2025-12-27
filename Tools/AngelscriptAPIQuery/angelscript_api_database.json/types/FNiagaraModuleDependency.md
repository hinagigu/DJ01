# FNiagaraModuleDependency

## 属性

### Id
- **类型**: `FName`
- **描述**: Specifies the provided id of the required dependent module (e.g. 'ProvidesNormalizedAge')

### Type
- **类型**: `ENiagaraModuleDependencyType`
- **描述**: Whether the dependency belongs before or after this module

### ScriptConstraint
- **类型**: `ENiagaraModuleDependencyScriptConstraint`
- **描述**: Specifies constraints related to the source script a modules provides as dependency.

### RequiredVersion
- **类型**: `FString`
- **描述**: Specifies the version constraint that module providing the dependency must fulfill.
Example usages:
'1.2' requires the exact version 1.2 of the source script
'1.2+' requires at least version 1.2, but any higher version is also ok
'1.2-2.0' requires any version between 1.2 and 2.0

### OnlyEvaluateInScriptUsage
- **类型**: `int`
- **描述**: This property can limit where the dependency is evaluated. By default, the dependency is enforced in all script usages

### Description
- **类型**: `FText`
- **描述**: Detailed description of the dependency

## 方法

### opAssign
```angelscript
FNiagaraModuleDependency& opAssign(FNiagaraModuleDependency Other)
```

