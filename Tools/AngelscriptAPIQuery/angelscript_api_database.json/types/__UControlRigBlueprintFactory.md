# __UControlRigBlueprintFactory

## 方法

### CreateControlRigFromSkeletalMeshOrSkeleton
```angelscript
UControlRigBlueprint CreateControlRigFromSkeletalMeshOrSkeleton(UObject InSelectedObject, bool bModularRig)
```
Create a new control rig asset within the contents space of the project
based on a skeletal mesh or skeleton object.
@param InSelectedObject The SkeletalMesh / Skeleton object to base the control rig asset on
@param bModularRig If true the rig will be created as a modular rig

### CreateNewControlRigAsset
```angelscript
UControlRigBlueprint CreateNewControlRigAsset(FString InDesiredPackagePath, bool bModularRig)
```
Create a new control rig asset within the contents space of the project.
@param InDesiredPackagePath The package path to use for the control rig asset
@param bModularRig If true the rig will be created as a modular rig

### StaticClass
```angelscript
UClass StaticClass()
```

