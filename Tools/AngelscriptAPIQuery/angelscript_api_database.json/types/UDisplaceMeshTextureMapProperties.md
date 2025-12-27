# UDisplaceMeshTextureMapProperties

**继承自**: `UInteractiveToolPropertySet`

PropertySet for properties affecting the Image Map displacement type.

## 属性

### DisplacementMap
- **类型**: `UTexture2D`
- **描述**: Displacement map. Only the first channel is used.

### Channel
- **类型**: `EDisplaceMeshToolChannelType`
- **描述**: Channel in the displacement map to use.

### DisplacementMapBaseValue
- **类型**: `float32`
- **描述**: The value in the texture map that corresponds to no displacement. For instance, if set to 0, then all
       displacement will be positive. If set to 0.5, displacement below 0.5 will be negative, and above will be
       positive. Default is for 128/255 to be no displacement.

### UVScale
- **类型**: `FVector2D`
- **描述**: When sampling from the texture map, how to scale the mesh UV's in the x and y directions. For a mesh with
      UV's in the range 0 to 1, setting a scale above 1 will result in tiling the texture map, and scaling below
      1 will result in using only part of the texture map.

### UVOffset
- **类型**: `FVector2D`
- **描述**: When sampling from the texture map, how to offset the mesh UV's. This will result in offsetting the
      tiling of the texture map across the mesh.

### bApplyAdjustmentCurve
- **类型**: `bool`
- **描述**: When true, applies a function to remap the values in the displacement map, which can be used
       for contrast adjustment. The texture map values are converted to the range [0,1] before applying
       the remapping.

### AdjustmentCurve
- **类型**: `UCurveFloat`
- **描述**: This curve is queried in the range [0,1] to adjust contrast of the displacement map.

### bRecalcNormals
- **类型**: `bool`
- **描述**: Recalculate normals from displaced mesh. Disable this if you are applying Displacements that are paired with an existing Normal Map in your Material.

