# __AnimNodeControlRig

## 方法

### ConvertToControlRig
```angelscript
FControlRigReference ConvertToControlRig(FAnimNodeReference Node, EAnimNodeReferenceConversionResult& Result)
```
Get a control rig context from an anim node context

### ConvertToControlRigPure
```angelscript
void ConvertToControlRigPure(FAnimNodeReference Node, FControlRigReference& ControlRig, bool& Result)
```
Get a control rig context from an anim node context (pure)

### SetControlRigClass
```angelscript
FControlRigReference SetControlRigClass(FControlRigReference Node, TSubclassOf<UControlRig> ControlRigClass)
```
Set the control rig class on the node

