# UFractureCustomVoronoiSettings

**继承自**: `UFractureToolSettings`

## 属性

### VoronoiPattern
- **类型**: `EVoronoiPattern`
- **描述**: Method to generate next group of voronoi sites

### NormalOffset
- **类型**: `float32`
- **描述**: Offset point samples in the vertex normal directions

### Variability
- **类型**: `float32`
- **描述**: Amount to randomly displace each Voronoi site (in cm)

### SitesToAdd
- **类型**: `int`
- **描述**: Number of Voronoi sites to add

### GridX
- **类型**: `int`
- **描述**: Number of sites to add to grid in X

### GridY
- **类型**: `int`
- **描述**: Number of sites to add to grid in Y

### GridZ
- **类型**: `int`
- **描述**: Number of sites to add to grid in Z

### SkipFraction
- **类型**: `float32`
- **描述**: Fraction of points to skip

### SkipMode
- **类型**: `EDownsamplingMode`
- **描述**: Strategy used for skipping points; only used if SkipFraction is greater than 0

### bStartAtActor
- **类型**: `bool`
- **描述**: Whether to use the reference mesh actor's transform when placing the Voronoi sites, or center them at the current gizmo location instead

