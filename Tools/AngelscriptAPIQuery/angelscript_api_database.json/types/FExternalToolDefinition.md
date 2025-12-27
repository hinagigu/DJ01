# FExternalToolDefinition

Structure for defining an external tool

## 属性

### ToolName
- **类型**: `FString`
- **描述**: The name of the tool / test.

### ExecutablePath
- **类型**: `FFilePath`
- **描述**: The executable to run.

### CommandLineOptions
- **类型**: `FString`
- **描述**: The command line options to pass to the executable.

### WorkingDirectory
- **类型**: `FDirectoryPath`
- **描述**: The working directory for the new process.

### ScriptExtension
- **类型**: `FString`
- **描述**: If set, look for scripts with this extension.

### ScriptDirectory
- **类型**: `FDirectoryPath`
- **描述**: If the ScriptExtension is set, look here for the script files.

## 方法

### opAssign
```angelscript
FExternalToolDefinition& opAssign(FExternalToolDefinition Other)
```

