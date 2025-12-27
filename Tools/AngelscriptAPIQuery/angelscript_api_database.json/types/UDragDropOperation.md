# UDragDropOperation

**继承自**: `UObject`

This class is the base drag drop operation for UMG, extend it to add additional data and add new functionality.

## 属性

### Tag
- **类型**: `FString`

### Payload
- **类型**: `UObject`

### DefaultDragVisual
- **类型**: `UWidget`

### Pivot
- **类型**: `EDragPivot`

### Offset
- **类型**: `FVector2D`

### OnDrop
- **类型**: `FOnDragDropMulticast`

### OnDragCancelled
- **类型**: `FOnDragDropMulticast`

### OnDragged
- **类型**: `FOnDragDropMulticast`

## 方法

### DragCancelled
```angelscript
void DragCancelled(FPointerEvent PointerEvent)
```

### Dragged
```angelscript
void Dragged(FPointerEvent PointerEvent)
```

### Drop
```angelscript
void Drop(FPointerEvent PointerEvent)
```

