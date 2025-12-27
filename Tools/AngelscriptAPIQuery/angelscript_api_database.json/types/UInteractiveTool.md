# UInteractiveTool

**继承自**: `UObject`

UInteractiveTool is the base class for all Tools in the InteractiveToolsFramework.
A Tool is is a "lightweight mode" that may "own" one or more Actors/Components/etc in
the current scene, may capture certain input devices or event streams, and so on.
The base implementation essentially does nothing but provide sane default behaviors.

The BaseTools/ subfolder contains implementations of various kinds of standard
"tool behavior", like a tool that responds to a mouse click, etc, that can be
extended to implement custom behaviors.

In the framework, you do not create instances of UInteractiveTool yourself.
You provide a UInteractiveToolBuilder implementation that can properly construct
an instance of your Tool, this is where for example default parameters would be set.
The ToolBuilder is registered with the ToolManager, and then UInteractiveToolManager::ActivateTool()
is used to kick things off.

@todo callback/delegate for if/when .InputBehaviors changes
@todo callback/delegate for when tool properties change

