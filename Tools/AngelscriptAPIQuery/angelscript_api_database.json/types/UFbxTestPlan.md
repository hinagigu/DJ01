# UFbxTestPlan

**继承自**: `UObject`

Container for detailing collision automated test data.

## 属性

### TestPlanName
- **类型**: `FString`
- **描述**: Name of the Test Plan

### Action
- **类型**: `EFBXTestPlanActionType`
- **描述**: Tell the system what we want to do

### LodIndex
- **类型**: `int`
- **描述**: The LOD index in case the user choose to add or reimport a LOD

### bDeleteFolderAssets
- **类型**: `bool`
- **描述**: If true the test will delete all assets create in the import folder

### ExpectedResult
- **类型**: `TArray<FFbxTestPlanExpectedResult>`
- **描述**: Expected preset type

### ImportUI
- **类型**: `UFbxImportUI`
- **描述**: Options use for this test plan, Transient because we manually serialize the options.

