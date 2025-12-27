# USafeZone

**继承自**: `UContentWidget`

The Safe-Zone widget is an essential part of developing a game UI that can run on lots of different non-PC platforms.
While a modern flat panel computer monitor may not have over scan issues, this is a common occurrence for Consoles.
It's common for TVs to have extra pixels under the bezel, in addition to projectors and projection TVs having potentially
several vertical and horizontal columns of pixels hidden behind or against a black border of the projection screen.

Useful testing console commands to help, simulate the safe zone on PC,
  r.DebugSafeZone.TitleRatio 0.96
  r.DebugActionZone.ActionRatio 0.96

To enable a red band to visualize the safe zone, use this console command,
r.DebugSafeZone.Mode controls the debug visualization overlay (0..2, default 0).
  0: Do not display the safe zone overlay.
  1: Display the overlay for the title safe zone.
  2: Display the overlay for the action safe zone.

## 属性

### PadLeft
- **类型**: `bool`

### PadRight
- **类型**: `bool`

### PadTop
- **类型**: `bool`

### PadBottom
- **类型**: `bool`

## 方法

### SetSidesToPad
```angelscript
void SetSidesToPad(bool InPadLeft, bool InPadRight, bool InPadTop, bool InPadBottom)
```

