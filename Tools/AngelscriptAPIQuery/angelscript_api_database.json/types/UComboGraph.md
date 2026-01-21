# UComboGraph

**继承自**: `UObject`

Combo Graph Assets provide a way to visually design combo strings and link montages together.

Combo Graphs are then run with custom Ability Tasks from within a Gameplay Ability.

## 属性

### EntryNode
- **类型**: `UComboGraphNodeEntry`
- **描述**: Represents the top level combo node direct child of entry node.

### FirstNode
- **类型**: `UComboGraphNodeBase`
- **描述**: Represents the top level combo node direct child of entry node.

### RootNodes
- **类型**: `TArray<TObjectPtr<UComboGraphNodeBase>>`
- **描述**: Holds any combo nodes with no direct parent

Note: should usually hold only one node, the first one. If more than one,
means that some combo nodes are present in graph but not linked to a valid
path from entry node as all nodes below entry should have direct
parent / child relationship.

### AllNodes
- **类型**: `TArray<TObjectPtr<UComboGraphNodeBase>>`
- **描述**: Holds all combo nodes defined for this graph

### DefaultNodeMontageType
- **类型**: `TSubclassOf<UComboGraphNodeMontage>`
- **描述**: Node Class type used for montages assets when dropped in a graph, or dropped on an existing node pin.

This property lets you customize which class Combo Graph will use to create a new montage node in these situations.
Mainly useful if you have a custom Combo Node Montage BP or native subclass.

### DefaultNodeSequenceType
- **类型**: `TSubclassOf<UComboGraphNodeSequence>`
- **描述**: Node Class type used for sequence assets when dropped in a graph, or dropped on an existing node pin.

This property lets you customize which class Combo Graph will use to create a new sequence node in these situations.
Mainly useful if you have a custom Combo Node Montage BP or native subclass.

### DefaultInputAction
- **类型**: `UInputAction`
- **描述**: Default Input Action to use when creating new connections.

### bCanBeCyclical
- **类型**: `bool`
- **描述**: Determine if we can have cycles or not in a graph

### ContextMapping
- **类型**: `TSoftObjectPtr<UInputMappingContext>`
- **描述**: Enhanced Input Context Mapping to use to draw edge (transition) icons in Graphs (if not set, will fallback to the one defined in Project Settings)

### IconPreference
- **类型**: `EComboGraphIconType`
- **描述**: Icon preference to draw edge (transition) icons in Graph. Can be either Keyboard or Gamepad based

