# UBaseBrushTool

**继承自**: `UMeshSurfacePointTool`

UBaseBrushTool implements standard brush-style functionality for an InteractiveTool.
This includes:
  1) brush radius property set with dimension-relative brush sizing and default brush radius hotkeys
  2) brush indicator visualization
  3) tracking of last brush stamp location via .LastBrushStamp FProperty
  4) status of brush stroke via .bInBrushStroke FProperty
  5) "B" hotkey to adjust brush radius / strength by click-dragging in the viewport

