# FGeometry

Represents the position, size, and absolute position of a Widget in Slate.
The absolute location of a geometry is usually screen space or
window space depending on where the geometry originated.
Geometries are usually paired with a SWidget pointer in order
to provide information about a specific widget (see FArrangedWidget).
A Geometry's parent is generally thought to be the Geometry of the
the corresponding parent widget.

## 方法

### GetLocalSize
```angelscript
FVector2D GetLocalSize()
```

### GetAbsoluteSize
```angelscript
FVector2D GetAbsoluteSize()
```

### AbsoluteToLocal
```angelscript
FVector2D AbsoluteToLocal(FVector2D Position)
```

### LocalToAbsolute
```angelscript
FVector2D LocalToAbsolute(FVector2D Position)
```

### MakeChild
```angelscript
FGeometry MakeChild(FVector2D Position, FVector2D Size)
```

### opAssign
```angelscript
FGeometry& opAssign(FGeometry Other)
```

