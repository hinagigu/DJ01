# ADJ01WorldSettings

**继承自**: `AWorldSettings`

The default world settings object, used primarily to set the default gameplay experience to use when playing on this map

## 属性

### DefaultGameplayExperience
- **类型**: `TSoftClassPtr<UDJ01ExperienceDefinition>`
- **描述**: The default experience to use when a server opens this map if it is not overridden by the user-facing experience

### ForceStandaloneNetMode
- **类型**: `bool`
- **描述**: Is this level part of a front-end or other standalone experience?
When set, the net mode will be forced to Standalone when you hit Play in the editor

