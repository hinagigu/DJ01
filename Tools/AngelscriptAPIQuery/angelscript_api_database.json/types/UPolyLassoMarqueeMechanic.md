# UPolyLassoMarqueeMechanic

**继承自**: `UInteractionMechanic`

* Mechanic for a PolyLasso "marquee" selection. It creates and maintains the 2D PolyLasso associated with a mouse drag.
* It does not test against any scene geometry, nor does it maintain any sort of list of selected objects.
*
* The PolyLasso has two potential modes, a freehand polyline and a multi-click polygon. By default both are enabled
* but this can be selectively controlled with flags below. If a click-and-release is within a small distance tolerance,
* then a multi-click polygon is entered, and must be exited by clicking again at the start point. The freehand polyline
* is drawn by click-dragging, and exited by releasing the mouse.
*
* When using this mechanic, you should call DrawHUD() in the tool's DrawHUD() call so that it can draw the box.
*
* Attach to the mechanic's delegates and use the passed PolyLasso to test against your geometry.

