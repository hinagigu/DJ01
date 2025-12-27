# UGizmoElementHitMultiTarget

**继承自**: `UObject`

UGizmoElementHitMultiTarget is an IGizmoClickMultiTarget implementation that
hit-tests any object derived from UGizmoElementBase. This implementation is used for
HitTargets which support hitting multiple parts within a gizmo element hierarchy.

For a gizmo with multiple parts, the part identifier establishes a correspondence between a gizmo part
and the elements representing that part within the hit target. The valid part identifiers should
be defined in the gizmo. Identifier 0 is reserved for the default ID which should be assigned to
elements that do not correspond to any gizmo part, such as non-hittable decorative elements.

