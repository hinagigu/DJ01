# UCommonActivatableWidgetQueue

**继承自**: `UCommonActivatableWidgetContainerBase`

A display queue of ActivatableWidget elements.

- Only one widget is active/displayed at a time, all others in the queue are deactivated.
- When the active widget deactivates, it is automatically removed from the widget,
            released back to the pool, and the next widget in the queue (if any) is displayed

