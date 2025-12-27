# __MeshVertexPainter

## 方法

### PaintVerticesLerpAlongAxis
```angelscript
void PaintVerticesLerpAlongAxis(UStaticMeshComponent StaticMeshComponent, FLinearColor StartColor, FLinearColor EndColor, EVertexPaintAxis Axis, bool bConvertToSRGB)
```
Paints vertex colors on a mesh component lerping from the start to the end color along the specified axis.

### PaintVerticesSingleColor
```angelscript
void PaintVerticesSingleColor(UStaticMeshComponent StaticMeshComponent, FLinearColor FillColor, bool bConvertToSRGB)
```
Paints vertex colors on a mesh component in a specified color.

### RemovePaintedVertices
```angelscript
void RemovePaintedVertices(UStaticMeshComponent StaticMeshComponent)
```
Removes vertex colors on a mesh component

