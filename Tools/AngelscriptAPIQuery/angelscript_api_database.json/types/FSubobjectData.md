# FSubobjectData

A struct that represents a single subobject. This can be anything, but are
most commonly components attached to an actor instance or blueprint. Keeps track
of the handles to its parent object and any child that it has.

If you wish to modify a subobject, use the SubobjectDataSubsystem.

## 方法

### opAssign
```angelscript
FSubobjectData& opAssign(FSubobjectData Other)
```

