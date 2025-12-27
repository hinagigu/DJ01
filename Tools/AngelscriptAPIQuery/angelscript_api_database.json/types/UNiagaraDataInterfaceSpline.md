# UNiagaraDataInterfaceSpline

**继承自**: `UNiagaraDataInterface`

Data Interface allowing sampling of in-world spline components. Note that this data interface is very experimental.

## 属性

### SoftSourceActor
- **类型**: `TSoftObjectPtr<AActor>`
- **描述**: The source actor from which to sample.  Note that this can only be set when used as a user variable on a component in the world.

### SplineUserParameter
- **类型**: `FNiagaraUserParameterBinding`
- **描述**: Reference to a user parameter if we're reading one. This should  be an Object user parameter that is either a USplineComponent or an AActor containing a USplineComponent.

### bUseLUT
- **类型**: `bool`

### NumLUTSteps
- **类型**: `int`

