# UPlaneCutToolProperties

**继承自**: `UInteractiveToolPropertySet`

Standard properties of the plane cut operation

## 属性

### bKeepBothHalves
- **类型**: `bool`
- **描述**: If true, both halves of the cut are computed

### SpacingBetweenHalves
- **类型**: `float32`
- **描述**: If keeping both halves, separate the two pieces by this amount

### bExportSeparatedPiecesAsNewMeshAssets
- **类型**: `bool`
- **描述**: If true, meshes cut into multiple pieces will be saved as separate assets on 'accept'.

### bShowPreview
- **类型**: `bool`

### bFillCutHole
- **类型**: `bool`
- **描述**: If true, the cut surface is filled with simple planar hole fill surface(s)

### bFillSpans
- **类型**: `bool`
- **描述**: If true, will attempt to fill cut holes even if they're ill-formed (e.g. because they connect to pre-existing holes in the geometry)

### bSimplifyAlongCut
- **类型**: `bool`
- **描述**: If true, will simplify triangulation along plane cut when doing so will not affect the shape, UVs or PolyGroups

