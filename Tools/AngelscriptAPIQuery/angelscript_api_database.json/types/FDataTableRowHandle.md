# FDataTableRowHandle

Handle to a particular row in a table

## 属性

### DataTable
- **类型**: `const UDataTable`

### RowName
- **类型**: `FName`

## 方法

### IsNull
```angelscript
bool IsNull()
```

### opEquals
```angelscript
bool opEquals(FDataTableRowHandle Other)
```

### ToDebugString
```angelscript
FString ToDebugString(bool bUseFullPath)
```

### GetRow
```angelscript
bool GetRow(? OutRow)
```

### opAssign
```angelscript
FDataTableRowHandle& opAssign(FDataTableRowHandle Other)
```

