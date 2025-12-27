# FDataTableCategoryHandle

Handle to a particular set of rows in a table

## 属性

### DataTable
- **类型**: `const UDataTable`

### ColumnName
- **类型**: `FName`

### RowContents
- **类型**: `FName`

## 方法

### IsNull
```angelscript
bool IsNull()
```

### opEquals
```angelscript
bool opEquals(FDataTableCategoryHandle Other)
```

### GetRowNames
```angelscript
TArray<FName> GetRowNames()
```

### GetRow
```angelscript
bool GetRow(FName RowName, ? OutRow)
```

### GetRows
```angelscript
void GetRows(? OutArray)
```

### opAssign
```angelscript
FDataTableCategoryHandle& opAssign(FDataTableCategoryHandle Other)
```

