# UEditorPerProjectUserSettings

**继承自**: `UObject`

## 属性

### bDisplayEngineVersionInBadge
- **类型**: `bool`
- **描述**: When enabled, Engine Version Number is displayed in the ProjectBadge

### bUseSimplygonSwarm
- **类型**: `bool`
- **描述**: When enabled, use SimplygonSwarm Module / server to create proxies

### SimplygonServerIP
- **类型**: `FString`
- **描述**: Server IP for the distributed Simplygon server

### bEnableSwarmDebugging
- **类型**: `bool`
- **描述**: Enable swarm debugging features. Temp ssf files are not removed. Detailed message printing

### SimplygonSwarmDelay
- **类型**: `uint`
- **描述**: Time between JSON net requests for Simplygon Swarm

### SwarmNumOfConcurrentJobs
- **类型**: `uint`
- **描述**: Number of concurrent swarm jobs to execute. This is independent of the main job queue.

### SwarmMaxUploadChunkSizeInMB
- **类型**: `uint`

### SwarmIntermediateFolder
- **类型**: `FString`
- **描述**: Folder in which Simplygon Swarm will store intermediate texture and mesh data that is uploaded to the Swarm

### DataSourceFolder
- **类型**: `FDirectoryPath`
- **描述**: Specify a project data source folder to store relative source file path to ease the re-import process

### bGetAttentionOnUATCompletion
- **类型**: `bool`
- **描述**: If enabled, the Editor will attempt to get the users attention whenever a UAT task (such as cooking or packaging) is completed

### bAlwaysBuildUAT
- **类型**: `bool`
- **描述**: Always build UAT\UBT before launching the game. It will decrease iteration times if disabled

### bDisplayUIExtensionPoints
- **类型**: `bool`

### bDisplayDocumentationLink
- **类型**: `bool`

### bAlwaysGatherBehaviorTreeDebuggerData
- **类型**: `bool`

### bDisplayBlackboardKeysInAlphabeticalOrder
- **类型**: `bool`

### bAutomaticallyHotReloadNewClasses
- **类型**: `bool`

### bShowCompilerLogOnCompileError
- **类型**: `bool`

### bKeepFbxNamespace
- **类型**: `bool`

### bShowImportDialogAtReimport
- **类型**: `bool`

### bKeepAttachHierarchy
- **类型**: `bool`

### bAnimationReimportWarnings
- **类型**: `bool`

