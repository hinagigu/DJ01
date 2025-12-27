# FTemplateSequenceBindingOverrideData

Template sequence binding override data

This is similar to FMovieSceneBindingOverrideData, but works only for a template sequence's root object,
so we don't need it to store the object binding ID.

## 属性

### Object
- **类型**: `TWeakObjectPtr<UObject>`
- **描述**: Specifies the object binding to override.

### bOverridesDefault
- **类型**: `bool`
- **描述**: Specifies whether the default assignment should remain bound (false) or if this should completely override the default binding (true).

## 方法

### opAssign
```angelscript
FTemplateSequenceBindingOverrideData& opAssign(FTemplateSequenceBindingOverrideData Other)
```

