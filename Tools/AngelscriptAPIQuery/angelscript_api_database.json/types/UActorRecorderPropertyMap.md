# UActorRecorderPropertyMap

**继承自**: `UObject`

This represents a list of all possible properties and components on an actor
which can be recorded by the Actor Recorder and whether or not the user wishes
to record them. If you wish to expose a property to be recorded it needs to be marked
as "Interp" (C++) or "Expose to Cinematics" in Blueprints.

## 属性

### Properties
- **类型**: `TArray<FActorRecordedProperty>`

### Children
- **类型**: `TArray<TObjectPtr<UActorRecorderPropertyMap>>`

