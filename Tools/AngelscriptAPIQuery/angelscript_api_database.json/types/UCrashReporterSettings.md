# UCrashReporterSettings

**继承自**: `UObject`

Implements per-project cooker settings exposed to the editor

## 属性

### UploadSymbolsPath
- **类型**: `FString`
- **描述**: Directory for uploading locally built binaries and .PDB files

### DownstreamStorage
- **类型**: `FString`
- **描述**: Local downstream PDB storage path (used for caching remote .PDB files)

### RemoteStorage
- **类型**: `TArray<FString>`
- **描述**: Remote PDB storage (directory path or http/https URL)

