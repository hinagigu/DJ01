# __DataTable

## 方法

### DoesDataTableRowExist
```angelscript
bool DoesDataTableRowExist(const UDataTable Table, FName RowName)
```
Returns whether or not Table contains a row named RowName

### EvaluateCurveTableRow
```angelscript
void EvaluateCurveTableRow(UCurveTable CurveTable, FName RowName, float32 InXY, EEvaluateCurveTableResult& OutResult, float32& OutXY, FString ContextString)
```

### ExportDataTableToCSVFile
```angelscript
bool ExportDataTableToCSVFile(const UDataTable DataTable, FString CSVFilePath)
```
Export a Data Table to CSV file.
@param       CSVFilePath     The file path of the CSV file to write (output file is UTF-8).
@return      True if the operation succeeds, check the log for errors if it didn't succeed.

### ExportDataTableToCSVString
```angelscript
bool ExportDataTableToCSVString(const UDataTable DataTable, FString& OutCSVString)
```
Export a Data Table to CSV string.
@param       OutCSVString Output representing the contents of a CSV file.
@return      True if the operation succeeds, check the log for errors if it didn't succeed.

### ExportDataTableToJSONFile
```angelscript
bool ExportDataTableToJSONFile(const UDataTable DataTable, FString JSONFilePath)
```
Export a Data Table to JSON file.
@param       JSONFilePath The file path of the JSON file to write (output file is UTF-8).
@return      True if the operation succeeds, check the log for errors if it didn't succeed.

### ExportDataTableToJSONString
```angelscript
bool ExportDataTableToJSONString(const UDataTable DataTable, FString& OutJSONString)
```
Export a Data Table to JSON string.
@param       OutJSONString Output representing the contents of a JSON file.
@return      True if the operation succeeds, check the log for errors if it didn't succeed.

### FillDataTableFromCSVFile
```angelscript
bool FillDataTableFromCSVFile(UDataTable DataTable, FString CSVFilePath, UScriptStruct ImportRowStruct)
```
Empty and fill a Data Table from CSV file.
@param       CSVFilePath                     The file path of the CSV file.
@param       ImportRowStruct         Optional row struct to apply on import. If set will also force the import to run automated (no questions or dialogs).
@return      True if the operation succeeds, check the log for errors if it didn't succeed.

### FillDataTableFromCSVString
```angelscript
bool FillDataTableFromCSVString(UDataTable DataTable, FString CSVString, UScriptStruct ImportRowStruct)
```
Empty and fill a Data Table from CSV string.
@param       CSVString                       The Data that representing the contents of a CSV file.
@param       ImportRowStruct         Optional row struct to apply on import. If set will also force the import to run automated (no questions or dialogs).
@return      True if the operation succeeds, check the log for errors if it didn't succeed.

### FillDataTableFromJSONFile
```angelscript
bool FillDataTableFromJSONFile(UDataTable DataTable, FString JSONFilePath, UScriptStruct ImportRowStruct)
```
Empty and fill a Data Table from JSON file.
@param       JSONFilePath            The file path of the JSON file.
@param       ImportRowStruct         Optional row struct to apply on import. If set will also force the import to run automated (no questions or dialogs).
@return      True if the operation succeeds, check the log for errors if it didn't succeed.

### FillDataTableFromJSONString
```angelscript
bool FillDataTableFromJSONString(UDataTable DataTable, FString JSONString, UScriptStruct ImportRowStruct)
```
Empty and fill a Data Table from JSON string.
@param       JSONString                      The Data that representing the contents of a JSON file.
@param       ImportRowStruct         Optional row struct to apply on import. If set will also force the import to run automated (no questions or dialogs).
@return      True if the operation succeeds, check the log for errors if it didn't succeed.

### GetDataTableColumnAsString
```angelscript
TArray<FString> GetDataTableColumnAsString(const UDataTable DataTable, FName PropertyName)
```
Export from the DataTable all the row for one column. Export it as string. The row name is not included.
@see GetDataTableColumnNames.
@see GetDataTableColumnNameFromExportName.

### GetDataTableColumnExportNames
```angelscript
void GetDataTableColumnExportNames(const UDataTable Table, TArray<FString>& OutExportColumnNames)
```
Get the friendly export name of each column in this Data Table.
@see GetDataTableColumnNameFromExportName.

### GetDataTableColumnNameFromExportName
```angelscript
bool GetDataTableColumnNameFromExportName(const UDataTable Table, FString ColumnExportName, FName& OutColumnName)
```
Get the raw property name of a data table column from its friendly export name.
@return True if a column was found for the friendly name, false otherwise.

### GetDataTableColumnNames
```angelscript
void GetDataTableColumnNames(const UDataTable Table, TArray<FName>& OutColumnNames)
```
Get the name of each column in this Data Table.
@note These are always the raw property names (@see GetDataTableColumnAsString) rather than the friendly export name that would be used in a CSV/JSON export (@see GetDataTableColumnNameFromExportName).

### GetDataTableRowNames
```angelscript
void GetDataTableRowNames(const UDataTable Table, TArray<FName>& OutRowNames)
```

### GetDataTableRowStruct
```angelscript
const UScriptStruct GetDataTableRowStruct(const UDataTable Table)
```
Get the row struct used by the given Data Table, if any

