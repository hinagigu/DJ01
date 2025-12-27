# UFractureCutterSettings

**继承自**: `UFractureToolSettings`

Settings specifically related to the one-time destructive fracturing of a mesh *

## 属性

### InternalMaterial
- **类型**: `FString`
- **描述**: Material to set for internal faces on fracture. 'Automatic' will use the most common 'internal' material in each geometry, or the last valid material if no internal faces are found

### RandomSeed
- **类型**: `int`
- **描述**: Random number generator seed for repeatability. If the value is -1, a different random seed will be used every time, otherwise the specified seed will always be used

### ChanceToFracture
- **类型**: `float32`
- **描述**: Chance to fracture each selected bone. If 0, no bones will fracture; if 1, all bones will fracture.

### bGroupFracture
- **类型**: `bool`
- **描述**: Generate a fracture pattern across all selected meshes.

### Grout
- **类型**: `float32`
- **描述**: Amount of space to leave between cut pieces

### bDrawSites
- **类型**: `bool`
- **描述**: Draw points marking the centers of pieces to be cut out by the fracture pattern.

### bDrawDiagram
- **类型**: `bool`
- **描述**: Draw the edges of the fracture pattern.

### bDrawNoisePreview
- **类型**: `bool`
- **描述**: Whether to show a solid preview of the cutting geometry, including any noise displacement

### FractionPreviewCells
- **类型**: `float32`
- **描述**: Fraction of cells to show in noise preview

### NoisePreviewScale
- **类型**: `float`
- **描述**: Scale of the noise preview plane

### Amplitude
- **类型**: `float32`
- **描述**: Size of the Perlin noise displacement (in cm). If 0, no noise will be applied

### Frequency
- **类型**: `float32`
- **描述**: Period of the Perlin noise.  Smaller values will create a smoother noise pattern

### Persistence
- **类型**: `float32`
- **描述**: Persistence of the layers of Perlin noise. At each layer (octave) after the first, the amplitude of the Perlin noise is scaled by this factor

### Lacunarity
- **类型**: `float32`
- **描述**: Lacunarity of the layers of Perlin noise. At each layer (octave) after the first, the frequency of the Perlin noise is scaled by this factor

### OctaveNumber
- **类型**: `int`
- **描述**: Number of fractal layers of Perlin noise to apply. Each layer is additive, with Amplitude and Frequency parameters scaled by Persistence and Lacunarity
Smaller values (1 or 2) will create noise that looks like gentle rolling hills, while larger values (> 4) will tend to look more like craggy mountains

### PointSpacing
- **类型**: `float32`
- **描述**: Distance (in cm) between vertices on cut surfaces where noise is added.  Larger spacing between vertices will create more efficient meshes with fewer triangles, but less resolution to see the shape of the added noise

