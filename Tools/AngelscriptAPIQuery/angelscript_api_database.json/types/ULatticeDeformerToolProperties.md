# ULatticeDeformerToolProperties

**继承自**: `UInteractiveToolPropertySet`

## 属性

### XAxisResolution
- **类型**: `int`
- **描述**: Number of lattice vertices along the X axis

### YAxisResolution
- **类型**: `int`
- **描述**: Number of lattice vertices along the Y axis

### ZAxisResolution
- **类型**: `int`
- **描述**: Number of lattice vertices along the Z axis

### Padding
- **类型**: `float32`
- **描述**: Relative distance the lattice extends from the mesh

### InterpolationType
- **类型**: `ELatticeInterpolationType`
- **描述**: Whether to use linear or cubic interpolation to get new mesh vertex positions from the lattice

### bDeformNormals
- **类型**: `bool`
- **描述**: Whether to use approximate new vertex normals using the deformer

### GizmoCoordinateSystem
- **类型**: `EToolContextCoordinateSystem`
- **描述**: Whether the gizmo's axes remain aligned with world axes or rotate as the gizmo is transformed

### bSetPivotMode
- **类型**: `bool`
- **描述**: If Set Pivot Mode is active, the gizmo can be repositioned without moving the selected lattice points

### bSoftDeformation
- **类型**: `bool`
- **描述**: Whether to use soft deformation of the lattice

