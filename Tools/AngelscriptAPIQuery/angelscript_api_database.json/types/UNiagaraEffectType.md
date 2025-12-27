# UNiagaraEffectType

**继承自**: `UObject`

Contains settings and working data shared among many NiagaraSystems that share some commonality of type. For example ImpactFX vs EnvironmentalFX.

## 属性

### bAllowCullingForLocalPlayers
- **类型**: `bool`
- **描述**: Controls whether or not culling is allowed for FX that are owned by, attached to or instigated by a locally controlled pawn.

### UpdateFrequency
- **类型**: `ENiagaraScalabilityUpdateFrequency`
- **描述**: How regularly effects of this type are checked for scalability.

### CullReaction
- **类型**: `ENiagaraCullReaction`
- **描述**: How effects of this type react when they fail the cull checks.

### SignificanceHandler
- **类型**: `UNiagaraSignificanceHandler`
- **描述**: Used to determine the relative significance of FX in the scene which is used in other scalability systems such as instance count culling.

### SystemScalabilitySettings
- **类型**: `FNiagaraSystemScalabilitySettingsArray`

### EmitterScalabilitySettings
- **类型**: `FNiagaraEmitterScalabilitySettingsArray`

### ValidationRules
- **类型**: `TArray<TObjectPtr<UNiagaraValidationRule>>`
- **描述**: A set of rules to apply when checking content. To create your own rules, write a custom class that extends UNiagaraValidationRule.

### ValidationRuleSets
- **类型**: `TArray<TObjectPtr<UNiagaraValidationRuleSet>>`
- **描述**: Array of reusable rule sets to apply when checking content. To create your own rules, write a custom class that extends UNiagaraValidationRule.

### PerformanceBaselineController
- **类型**: `UNiagaraBaselineController`
- **描述**: Controls generation of performance baseline data for this effect type.

