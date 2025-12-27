# UWorldComposition

**继承自**: `UObject`

WorldComposition represents world structure:
    - Holds list of all level packages participating in this world and theirs base parameters (bounding boxes, offset from origin)
    - Holds list of streaming level objects to stream in and out based on distance from current view point
 - Handles properly levels repositioning during level loading and saving

