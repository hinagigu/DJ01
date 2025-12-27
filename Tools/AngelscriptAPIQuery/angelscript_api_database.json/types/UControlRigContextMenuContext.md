# UControlRigContextMenuContext

**继承自**: `UObject`

## 方法

### GetControlRig
```angelscript
UControlRig GetControlRig()
```
Get the active control rig instance in the viewport

### GetControlRigBlueprint
```angelscript
UControlRigBlueprint GetControlRigBlueprint()
```
Get the control rig blueprint that we are editing

### GetGraphNodeContextMenuContext
```angelscript
FControlRigGraphNodeContextMenuContext GetGraphNodeContextMenuContext()
```
Returns context for graph node context menu

### GetRigHierarchyDragAndDropContext
```angelscript
FControlRigRigHierarchyDragAndDropContext GetRigHierarchyDragAndDropContext()
```
Returns context for a drag & drop action that contains source and target element keys

### GetRigHierarchyToGraphDragAndDropContext
```angelscript
FControlRigRigHierarchyToGraphDragAndDropContext GetRigHierarchyToGraphDragAndDropContext()
```
Returns context for the menu that shows up when drag and drop from Rig Hierarchy to the Rig Graph

### IsAltDown
```angelscript
bool IsAltDown()
```
Returns true if either alt key is down

