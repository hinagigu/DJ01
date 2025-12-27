# UGridSlot

**继承自**: `UPanelSlot`

A slot for UGridPanel, these slots all share the same size as the largest slot
in the grid.

## 属性

### Padding
- **类型**: `FMargin`

### HorizontalAlignment
- **类型**: `EHorizontalAlignment`

### VerticalAlignment
- **类型**: `EVerticalAlignment`

### Row
- **类型**: `int`

### RowSpan
- **类型**: `int`

### Column
- **类型**: `int`

### ColumnSpan
- **类型**: `int`

### Layer
- **类型**: `int`

### Nudge
- **类型**: `FVector2D`

## 方法

### SetColumn
```angelscript
void SetColumn(int InColumn)
```
Sets the column index of the slot, this determines what cell the slot is in the panel

### SetColumnSpan
```angelscript
void SetColumnSpan(int InColumnSpan)
```
How many columns this slot spans over

### SetHorizontalAlignment
```angelscript
void SetHorizontalAlignment(EHorizontalAlignment InHorizontalAlignment)
```

### SetLayer
```angelscript
void SetLayer(int InLayer)
```
Sets positive values offset this cell to be hit-tested and drawn on top of others.

### SetNudge
```angelscript
void SetNudge(FVector2D InNudge)
```
Sets the offset for this slot's content by some amount; positive values offset to lower right

### SetPadding
```angelscript
void SetPadding(FMargin InPadding)
```

### SetRow
```angelscript
void SetRow(int InRow)
```
Sets the row index of the slot, this determines what cell the slot is in the panel

### SetRowSpan
```angelscript
void SetRowSpan(int InRowSpan)
```
How many rows this this slot spans over

### SetVerticalAlignment
```angelscript
void SetVerticalAlignment(EVerticalAlignment InVerticalAlignment)
```

