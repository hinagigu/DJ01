# URectangleMarqueeManager

**继承自**: `UObject`

* Adapted from URectangleMarqueeMechanic, the mechanic for a rectangle "marquee" selection, to operate without
* the UInteractionMechanic framework. It creates and maintains the 2D rectangle associated with a mouse drag.
* It does not test against any scene geometry, nor does it maintain any sort of list of selected objects.
*
* You must manually call the Setup(), Render() and DrawHUD() functions.
* Note these functions have been changed from the Mechanic versions to be easier to call without additional InteractiveTool machinery
*
* Attach to the delegates and use the passed rectangle to test against your geometry.
*
* TODO: Refactor this into a more generalized / generally usable class in RectangleMarqueeMechanic.h,
* and share more common code with URectangleMarqueeMechanic.

