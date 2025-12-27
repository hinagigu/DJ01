# UUVEditorToolMeshInput

**继承自**: `UToolTarget`

A package of the needed information for an asset being operated on by a
UV editor tool. It includes a UV unwrap mesh, a mesh with the UV layer applied,
and background-op-compatible previews for each. It also has convenience methods
for updating all of the represenations from just one of them, using a "fast update"
code path when possible.

This tool target is a bit different from usual in that it is not created
by a tool target manager, and therefore doesn't have an accompanying factory.
Instead, it is created by the mode, because the mode has access to the worlds
in which the previews need to be created.

It's arguable whether this should even inherit from UToolTarget.

