# __UExporter

## 方法

### RunAssetExportTask
```angelscript
bool RunAssetExportTask(UAssetExportTask Task)
```
Export the given object to file.  Child classes do not override this, but they do provide an Export() function
to do the resource-specific export work.

@param        Task            The task to export.

@return       true if the the object was successfully exported

### RunAssetExportTasks
```angelscript
bool RunAssetExportTasks(TArray<UAssetExportTask> ExportTasks)
```
Export the given objects to files.  Child classes do not override this, but they do provide an Export() function
to do the resource-specific export work.

@param       ExportTasks             The array of tasks to export.

@return      true if all tasks ran without error

### StaticClass
```angelscript
UClass StaticClass()
```

