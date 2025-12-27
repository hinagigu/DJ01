# __ACLPhantomTrackMode

An enum to control how to handle UE phantom tracks.
A phantom tracks are present in an animation sequence but aren't mapped to skeleton bones.
As such, they cannot be queried by the engine except manually through DecompressBone.
It should generally be safe to Strip them but we default to Ignore.
Re-importing the animation sequence should clean up any such stale data.

## 属性

### Ignore
- **类型**: `ACLPhantomTrackMode`

### Strip
- **类型**: `ACLPhantomTrackMode`

### Warn
- **类型**: `ACLPhantomTrackMode`

### ACLPhantomTrackMode_MAX
- **类型**: `ACLPhantomTrackMode`

