# FAnimNode_StateMachine

State machine node

## 属性

### MaxTransitionsPerFrame
- **类型**: `int`
- **描述**: The maximum number of transitions that can be taken by this machine 'simultaneously' in a single frame

### MaxTransitionsRequests
- **类型**: `int`
- **描述**: The maximum number of transition requests that can be buffered at any time.
The oldest transition requests are dropped to accommodate for newly created requests.

### bSkipFirstUpdateTransition
- **类型**: `bool`
- **描述**: When the state machine becomes relevant, it is initialized into the Entry state.
It then tries to take any valid transitions to possibly end up in a different state on that same frame.
- if true, that new state starts full weight.
- if false, a blend is created between the entry state and that new state.
In either case all visited State notifications (Begin/End) will be triggered.

### bReinitializeOnBecomingRelevant
- **类型**: `bool`
- **描述**: Reinitialize the state machine if we have become relevant to the graph
after not being ticked on the previous frame(s)

### bCreateNotifyMetaData
- **类型**: `bool`
- **描述**: Tag Notifies with meta data such as the active state and mirroring state.  Producing this
data has a  slight performance cost.

### bAllowConduitEntryStates
- **类型**: `bool`
- **描述**: Allows a conduit to be used as this state machine's entry state
If a valid entry state cannot be found at runtime then this will generate a reference pose!

## 方法

### opAssign
```angelscript
FAnimNode_StateMachine& opAssign(FAnimNode_StateMachine Other)
```

