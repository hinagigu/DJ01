# UMaterialExpressionMaterialXFractal3D

**继承自**: `UMaterialExpression`

Zero-centered 3D Fractal noise in 1, 2, 3 or 4 channels, created by summing several
octaves of 3D Perlin noise, increasing the frequency and decreasing the amplitude at each octave.

## 属性

### ConstAmplitude
- **类型**: `float32`
- **描述**: only used if Amplitude is not hooked up

### ConstOctaves
- **类型**: `int`
- **描述**: only used if Octaves is not hooked up

### ConstLacunarity
- **类型**: `float32`
- **描述**: only used if Lacunarity is not hooked up

### ConstDiminish
- **类型**: `float32`
- **描述**: only used if Diminish is not hooked up

### Scale
- **类型**: `float32`
- **描述**: can also be done with a multiply on the Position

### bTurbulence
- **类型**: `bool`
- **描述**: How multiple frequencies are getting combined

### Levels
- **类型**: `int`
- **描述**: 1 = fast but little detail, .. larger numbers cost more performance

### OutputMin
- **类型**: `float32`

### OutputMax
- **类型**: `float32`

