# URectangleMarqueeMechanic

**继承自**: `UInteractionMechanic`

* Mechanic for a rectangle "marquee" selection. It creates and maintains the 2D rectangle associated with a mouse drag.
* It does not test against any scene geometry, nor does it maintain any sort of list of selected objects.
*
* When using this mechanic, you should call Render() on it in the tool's Render() call so that it can cache
* necessary camera state, and DrawHUD() in the tool's DrawHUD() call so that it can draw the box.
*
* Attach to the mechanic's delegates and use the passed rectangle to test against your geometry.

