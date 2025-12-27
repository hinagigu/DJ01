# UMirrorToolProperties

**继承自**: `UInteractiveToolPropertySet`

## 属性

### OperationMode
- **类型**: `EMirrorOperationMode`
- **描述**: Mode of operation.

### bCropAlongMirrorPlaneFirst
- **类型**: `bool`
- **描述**: Cut off everything on the back side of the mirror plane before mirroring.

### bSimplifyAlongCrop
- **类型**: `bool`
- **描述**: Whether to locally simplify new edges created when cropping along the mirror plane. Will only simplify when doing so will not change the shape, UVs or PolyGroups.

### bWeldVerticesOnMirrorPlane
- **类型**: `bool`
- **描述**: Weld vertices that lie on the mirror plane. Vertices will not be welded if doing so would give an edge more than two faces, or if they are part of a face in the plane.

### PlaneTolerance
- **类型**: `float`
- **描述**: Distance (in unscaled mesh space) to allow a point to be from the plane and still consider it "on the mirror plane".

### bAllowBowtieVertexCreation
- **类型**: `bool`
- **描述**: When welding, whether to allow bowtie vertices to be created, or to duplicate the vertex.

### bShowPreview
- **类型**: `bool`
- **描述**: Whether to show the preview.

### WriteTo
- **类型**: `EMirrorSaveMode`
- **描述**: How to save the result.

