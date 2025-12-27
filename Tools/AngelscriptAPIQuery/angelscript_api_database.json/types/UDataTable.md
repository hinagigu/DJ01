# UDataTable

**继承自**: `UObject`

Imported spreadsheet table.

## 属性

### ImportKeyField
- **类型**: `FString`
- **描述**: Explicit field in import data to use as key. If this is empty it uses Name for JSON and the first field found for CSV

### AssetImportData
- **类型**: `UAssetImportData`
- **描述**: The file this data table was imported from, may be empty

### bStripFromClientBuilds
- **类型**: `bool`

### bIgnoreExtraFields
- **类型**: `bool`

### bIgnoreMissingFields
- **类型**: `bool`

## 方法

### EmptyTable
```angelscript
void EmptyTable()
```

### GetRowNames
```angelscript
TArray<FName> GetRowNames()
```

### RemoveRow
```angelscript
void RemoveRow(FName RowName)
```

### AddRow
```angelscript
void AddRow(FName RowName, ? InRow)
```

### FindRow
```angelscript
bool FindRow(FName RowName, ? OutRow)
```

### GetAllRows
```angelscript
void GetAllRows(? OutArray)
```

