# UMeshTopologySelectionMechanic

**继承自**: `UInteractionMechanic`

Base class mechanic for selecting a subset of mesh elements (edge loops, groups, corners, etc.)
Internally it relies on an FMeshTopologySelector to define which type of mesh topology is selectable.

NOTE: Users should not use this class directly, but rather subclass it and specify a particular FMeshTopologySelector to use.

