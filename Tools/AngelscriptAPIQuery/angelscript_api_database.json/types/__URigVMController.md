# __URigVMController

## 方法

### GetRegisteredTemplates
```angelscript
TArray<FString> GetRegisteredTemplates()
```
Returns all registered template notations

### GetRegisteredUnitStructs
```angelscript
TArray<UScriptStruct> GetRegisteredUnitStructs()
```
Returns all registered unit structs

### GetTemplateForUnitStruct
```angelscript
FString GetTemplateForUnitStruct(UScriptStruct InFunction, FString InMethodName)
```
Returns the template for a given function (or an empty string)

### GetUnitStructsForTemplate
```angelscript
TArray<UScriptStruct> GetUnitStructsForTemplate(FName InNotation)
```
Returns all supported unit structs for a given template notation

### StaticClass
```angelscript
UClass StaticClass()
```

