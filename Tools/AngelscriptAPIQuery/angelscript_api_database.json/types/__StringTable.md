# __StringTable

## 方法

### GetKeysFromStringTable
```angelscript
TArray<FString> GetKeysFromStringTable(FName TableId)
```
Returns an array of all keys within the given string table

### GetMetaDataIdsFromStringTableEntry
```angelscript
TArray<FName> GetMetaDataIdsFromStringTableEntry(FName TableId, FString Key)
```
Returns an array of all meta-data IDs within the given string table entry

### GetRegisteredStringTables
```angelscript
TArray<FName> GetRegisteredStringTables()
```
Returns an array of all registered string table IDs

### GetTableEntryMetaData
```angelscript
FString GetTableEntryMetaData(FName TableId, FString Key, FName MetaDataId)
```
Returns the specified meta-data of the given string table entry (or an empty string).

### GetTableEntrySourceString
```angelscript
FString GetTableEntrySourceString(FName TableId, FString Key)
```
Returns the source string of the given string table entry (or an empty string).

### GetTableNamespace
```angelscript
FString GetTableNamespace(FName TableId)
```
Returns the namespace of the given string table.

### IsRegisteredTableEntry
```angelscript
bool IsRegisteredTableEntry(FName TableId, FString Key)
```
Returns true if the given table ID corresponds to a registered string table, and that table has.

### IsRegisteredTableId
```angelscript
bool IsRegisteredTableId(FName TableId)
```
Returns true if the given table ID corresponds to a registered string table.

