# __EWidgetClipping

This enum controls clipping of widgets in Slate.  By default all SWidgets do not need to clip their children.
Most of the time, you don't need to clip, the only times it becomes important is when something might become hidden
due to panning.  You should use this wisely, as Slate can not batch across clipping areas, so if widget A and widget B
are set to EWidgetClipping::Yes, no drawing that happens inside their widget trees will ever be batch together, adding
additional GPU overhead.

## 属性

### Inherit
- **类型**: `EWidgetClipping`

### ClipToBounds
- **类型**: `EWidgetClipping`

### ClipToBoundsWithoutIntersecting
- **类型**: `EWidgetClipping`

### ClipToBoundsAlways
- **类型**: `EWidgetClipping`

### OnDemand
- **类型**: `EWidgetClipping`

### EWidgetClipping_MAX
- **类型**: `EWidgetClipping`

