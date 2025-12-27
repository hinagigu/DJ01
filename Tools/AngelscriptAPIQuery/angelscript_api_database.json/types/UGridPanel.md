# UGridPanel

**继承自**: `UPanelWidget`

A table-like panel that retains the width of every column throughout the table.

* Many Children

## 属性

### ColumnFill
- **类型**: `TArray<float32>`

### RowFill
- **类型**: `TArray<float32>`

## 方法

### AddChildToGrid
```angelscript
UGridSlot AddChildToGrid(UWidget Content, int InRow, int InColumn)
```

### SetColumnFill
```angelscript
void SetColumnFill(int ColumnIndex, float32 Coefficient)
```

### SetRowFill
```angelscript
void SetRowFill(int RowIndex, float32 Coefficient)
```

