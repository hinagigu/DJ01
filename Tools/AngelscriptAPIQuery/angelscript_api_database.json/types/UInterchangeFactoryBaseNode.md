# UInterchangeFactoryBaseNode

**继承自**: `UInterchangeBaseNode`

This struct is used to store and retrieve key-value attributes. The attributes are stored in a generic FAttributeStorage that serializes the values in a TArray64<uint8>.
See UE::Interchange::EAttributeTypes to know the supported template types.
This is an abstract class. This is the base class of the Interchange node graph format; all classes in this format should derive from this class.

## 方法

### AddFactoryDependencyUid
```angelscript
bool AddFactoryDependencyUid(FString DependencyUid)
```
Add one dependency to this object.

### GetCustomReferenceObject
```angelscript
bool GetCustomReferenceObject(FSoftObjectPath& AttributeValue)
```
Return the custom ReferenceObject: the UObject this factory node has created.

### GetCustomSubPath
```angelscript
bool GetCustomSubPath(FString& AttributeValue)
```
Return the custom sub-path under PackageBasePath where the assets will be created.

### GetFactoryDependencies
```angelscript
void GetFactoryDependencies(TArray<FString>& OutDependencies)
```
Retrieve the dependencies for this object.

### GetFactoryDependenciesCount
```angelscript
int GetFactoryDependenciesCount()
```
Retrieve the number of factory dependencies for this object.

### GetFactoryDependency
```angelscript
void GetFactoryDependency(int Index, FString& OutDependency)
```
Retrieve one dependency for this object.

### GetReimportStrategyFlags
```angelscript
EReimportStrategyFlags GetReimportStrategyFlags()
```
Return the reimport strategy flags.

### RemoveFactoryDependencyUid
```angelscript
bool RemoveFactoryDependencyUid(FString DependencyUid)
```
Remove one dependency from this object.

### SetCustomReferenceObject
```angelscript
bool SetCustomReferenceObject(FSoftObjectPath AttributeValue)
```
Set the custom ReferenceObject: the UObject this factory node has created.

### SetCustomSubPath
```angelscript
bool SetCustomSubPath(FString AttributeValue)
```
Set the custom sub-path under PackageBasePath where the assets will be created.

### SetForceNodeReimport
```angelscript
bool SetForceNodeReimport()
```
Allow the creation of the Unreal object even if it has been previously deleted in the editor.

### SetReimportStrategyFlags
```angelscript
bool SetReimportStrategyFlags(EReimportStrategyFlags ReimportStrategyFlags)
```
Change the reimport strategy flags.

### SetSkipNodeImport
```angelscript
bool SetSkipNodeImport()
```
Add the skip node attribute. Use this function to cancel the creation of the Unreal asset. See ShouldSkipNodeImport for more documentation.

### ShouldForceNodeReimport
```angelscript
bool ShouldForceNodeReimport()
```
Return whether or not an object should be created even if it has been deleted in the editor.
Return false by default.

### ShouldSkipNodeImport
```angelscript
bool ShouldSkipNodeImport()
```
Return true if this node should skip the factory import process, or false otherwise.
Nodes can be in a situation where we have to skip the import process because we cannot import the associated asset for multiple reasons. For example:
- An asset can already exist and represents a different type (UClass).
- An asset can already exist and is being compiled.
- An asset can already exist and is being imported by another concurrent import task (such as a user importing multiple files at the same time in the same content folder).

### UnsetForceNodeReimport
```angelscript
bool UnsetForceNodeReimport()
```
Disallow the creation of the Unreal object if it has been previously deleted in the editor.

### UnsetSkipNodeImport
```angelscript
bool UnsetSkipNodeImport()
```
Remove the skip node attribute. See ShouldSkipNodeImport for more documentation.

