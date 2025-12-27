# UAssetImportData

**继承自**: `UObject`

todo: Make this class better suited to multiple import paths - maybe have FAssetImportInfo use a map rather than array?

## 方法

### ExtractFilenames
```angelscript
TArray<FString> ExtractFilenames()
```

### GetFirstFilename
```angelscript
FString GetFirstFilename()
```
Helper function to return the first filename stored in this data. The resulting filename will be absolute (ie, not relative to the asset).

### ScriptedAddFilename
```angelscript
void ScriptedAddFilename(FString InPath, int Index, FString SourceFileLabel)
```
Add or update a filename at the specified index. If the index is greater then the number of source file,
it will add empty filenames to fill up to the specified index. The timespan and MD5 will be computed.

@Param InPath: The filename we want to set at the specified index.
@Param Index: This specify the source file index in case you have many source file for an imported asset
@Param SourceFileLabel: Optional, can be empty string, the label we want to see in the UI when displaying the source file. (useful for multi source)

