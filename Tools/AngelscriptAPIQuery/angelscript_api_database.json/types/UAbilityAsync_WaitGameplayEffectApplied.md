# UAbilityAsync_WaitGameplayEffectApplied

**继承自**: `UAbilityAsync`

This action listens for specific gameplay effect applications based off specified tags.
Effects themselves are not replicated; rather the tags they grant, the attributes they
change, and the gameplay cues they emit are replicated.
This will only listen for local server or predicted client effects.

## 属性

### OnApplied
- **类型**: `FOnAppliedDelegate__AbilityAsync_WaitGameplayEffectApplied`

