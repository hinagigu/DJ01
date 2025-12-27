# UNiagaraNodeCustomHlsl

**继承自**: `UNiagaraNodeFunctionCall`

## 属性

### CustomHlsl
- **类型**: `FString`

### AbsoluteIncludeFilePaths
- **类型**: `TArray<FFilePath>`
- **描述**: Links to hlsl files that will be included by the translator. These external files are not watched by the engine, so changes to them do not automatically trigger a recompile of Niagara scripts.

### VirtualIncludeFilePaths
- **类型**: `TArray<FString>`
- **描述**: Links to hlsl files that will be included by the translator. These paths are resolved with the virtual shader paths registered in the engine.
For example, /Plugin/FX/Niagara maps to /Engine/Plugins/FX/Niagara/Shaders. Custom mappings can be added via AddShaderSourceDirectoryMapping().

