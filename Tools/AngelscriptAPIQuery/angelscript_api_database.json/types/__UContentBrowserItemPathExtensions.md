# __UContentBrowserItemPathExtensions

## 方法

### BreakContentBrowserItemPath
```angelscript
void BreakContentBrowserItemPath(FContentBrowserItemPath ItemPath, FName& VirtualPath, FName& InternalPath)
```

### GetInternalPath
```angelscript
FName GetInternalPath(FContentBrowserItemPath ItemPath)
```
Returns internal path if there is one (eg,. "/PluginA/MyFile").

### GetVirtualPath
```angelscript
FName GetVirtualPath(FContentBrowserItemPath ItemPath)
```
Returns virtual path as FName (eg, "/All/Plugins/PluginA/MyFile").

### MakeContentBrowserItemPath
```angelscript
FContentBrowserItemPath MakeContentBrowserItemPath(FName InPath, EContentBrowserPathType InPathType)
```

### SetPath
```angelscript
void SetPath(FContentBrowserItemPath& ItemPath, FName InPath, EContentBrowserPathType InPathType)
```
Set the path being stored

### StaticClass
```angelscript
UClass StaticClass()
```

