# UAbilityTask_WaitInputRelease

**继承自**: `UAbilityTask`

Waits until the input is released from activating an ability. Clients will replicate a 'release input' event to the server, but not the exact time it was held locally.
We expect server to execute this task in parallel and keep its own time.

## 属性

### OnRelease
- **类型**: `FInputReleaseDelegate`

