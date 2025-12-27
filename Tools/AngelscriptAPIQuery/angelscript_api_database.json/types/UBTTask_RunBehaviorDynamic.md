# UBTTask_RunBehaviorDynamic

**继承自**: `UBTTaskNode`

RunBehaviorDynamic task allows pushing subtrees on execution stack.
Subtree asset can be assigned at runtime with SetDynamicSubtree function of BehaviorTreeComponent.

Does NOT support subtree's root level decorators!

## 属性

### InjectionTag
- **类型**: `FGameplayTag`
- **描述**: Gameplay tag that will identify this task for subtree injection

### DefaultBehaviorAsset
- **类型**: `UBehaviorTree`
- **描述**: default behavior to run

