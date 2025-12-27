# UFieldNotificationLibrary

**继承自**: `UBlueprintFunctionLibrary`

The Field Notification system allows a user to know when a property value is modified at runtime (note that it can be a function return value).
The class needs to implement the INotifyFieldValueChanged interface.
The property' setter  usually follows this pattern "if (new value != old value) assign the new value; broadcast that the value changed;".
The Blueprint implementation handles that setter logic automatically with SetPropertyValueAndBroadcast.
When a property value is modified by replication, the RepNotify will call BroadcastFieldValueChanged.
A function can also be a Field Notify. The function needs to be const and return a single value.

