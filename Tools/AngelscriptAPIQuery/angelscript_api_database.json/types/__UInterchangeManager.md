# __UInterchangeManager

## 方法

### CreateSourceData
```angelscript
UInterchangeSourceData CreateSourceData(FString InFileName)
```
* Script helper to create a source data object that points to a file on disk.
* @Param InFilename: Specify a file on disk.
* @return: A new UInterchangeSourceData.

### GetInterchangeManagerScripted
```angelscript
UInterchangeManager GetInterchangeManagerScripted()
```
Return the pointer to the Interchange Manager singleton.

@note - We need to return a pointer to have a valid Blueprint-callable function.

### StaticClass
```angelscript
UClass StaticClass()
```

