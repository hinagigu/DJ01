# USequencerAnimationOverride

**继承自**: `UInterface`

## 方法

### AllowsCinematicOverride
```angelscript
bool AllowsCinematicOverride()
```
Whether this animation blueprint allows Sequencer to nuke this anim instance and replace it during Sequencer playback.

### GetSequencerAnimSlotNames
```angelscript
TArray<FName> GetSequencerAnimSlotNames()
```
Should return a list of valid slot names for Sequencer to output to in the case that Sequencer is not permitted to nuke the anim instance.
Will be chosen by the user in drop down on the skeletal animation section properties. Should be named descriptively, as in some contexts (UEFN), the user
will not be able to view the animation blueprint itself to determine the mixing behavior of the slot.

