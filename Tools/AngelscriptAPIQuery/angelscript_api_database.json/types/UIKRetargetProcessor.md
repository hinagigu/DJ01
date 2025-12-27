# UIKRetargetProcessor

**继承自**: `UObject`

The runtime processor that converts an input pose from a source skeleton into an output pose on a target skeleton.
To use:
1. Initialize a processor with a Source/Target skeletal mesh and a UIKRetargeter asset.
2. Call RunRetargeter and pass in a source pose as an array of global-space transforms
3. RunRetargeter returns an array of global space transforms for the target skeleton.

