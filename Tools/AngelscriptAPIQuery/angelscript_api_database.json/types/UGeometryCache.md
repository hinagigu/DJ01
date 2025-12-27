# UGeometryCache

**继承自**: `UObject`

A Geometry Cache is a piece/set of geometry that consists of individual Mesh/Transformation samples.
In contrast with Static Meshes they can have their vertices animated in certain ways. *

## 属性

### AssetImportData
- **类型**: `UAssetImportData`
- **描述**: Importing data and options used for this Geometry cache object

### ThumbnailInfo
- **类型**: `UThumbnailInfo`
- **描述**: Information for thumbnail rendering

### Materials
- **类型**: `TArray<TObjectPtr<UMaterialInterface>>`

### MaterialSlotNames
- **类型**: `TArray<FName>`

### AssetUserData
- **类型**: `TArray<TObjectPtr<UAssetUserData>>`
- **描述**: Array of user data stored with the asset

### StartFrame
- **类型**: `int`

### EndFrame
- **类型**: `int`

