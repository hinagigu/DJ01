# __UGLTFExporter

## 方法

### ExportToGLTF
```angelscript
bool ExportToGLTF(UObject Object, FString FilePath, const UGLTFExportOptions Options, TSet<AActor> SelectedActors, FGLTFExportMessages& OutMessages)
```
Export the specified object to a glTF file (.gltf or .glb)

@param Object          The object to export (supported types are UMaterialInterface, UStaticMesh, USkeletalMesh, UWorld, UAnimSequence, ULevelSequence, ULevelVariantSets). Will default to the currently active world if null.
@param FilePath        The filename on disk to save as. Associated textures and binary files will be saved in the same folder, unless file extension is .glb - which results in a self-contained binary file.
@param Options         The various options to use during export. Will default to the project's user-specific editor settings if null.
@param SelectedActors  The set of actors to export, only applicable if the object to export is a UWorld. An empty set results in the export of all actors.
@param OutMessages     The resulting log messages from the export.

@return true if the object was successfully exported

### StaticClass
```angelscript
UClass StaticClass()
```

