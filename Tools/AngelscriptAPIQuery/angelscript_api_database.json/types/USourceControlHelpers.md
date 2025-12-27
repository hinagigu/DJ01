# USourceControlHelpers

**继承自**: `UObject`

Editor source control common functionality.

@note Many of these source control methods use *smart* file strings which can be one of:
  - fully qualified path
  - relative path
  - long package name
  - asset path
  - export text path (often stored on clipboard)

  For example:
     - D:\Epic\Dev-Ent\Projects\Python3rdBP\Content\Mannequin\Animations\ThirdPersonIdle.uasset
     - Content\Mannequin\Animations\ThirdPersonIdle.uasset
     - /Game/Mannequin/Animations/ThirdPersonIdle
     - /Game/Mannequin/Animations/ThirdPersonIdle.ThirdPersonIdle
     - AnimSequence'/Game/Mannequin/Animations/ThirdPersonIdle.ThirdPersonIdle'

