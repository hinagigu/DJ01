# UCommonInputActionDomain

**继承自**: `UDataAsset`

Describes an input-event handling domain. It's InnerBehavior determines how events
flow between widgets within the domain and Behavior determines how events will flow to
other Domains in the DomainTable.

## 属性

### Behavior
- **类型**: `ECommonInputEventFlowBehavior`
- **描述**: Behavior of an input event between Action Domains, i.e., how an event flows into the next Action Domain

### InnerBehavior
- **类型**: `ECommonInputEventFlowBehavior`
- **描述**: Behavior of an input event within an Action Domain, i.e., how an event flows to a lower ZOrder active widget
within the same Action Domain

### bUseActionDomainDesiredInputConfig
- **类型**: `bool`

### InputMode
- **类型**: `ECommonInputMode`

### MouseCaptureMode
- **类型**: `EMouseCaptureMode`

