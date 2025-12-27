# UNavModifierComponent

**继承自**: `UNavRelevantComponent`

## 属性

### FailsafeExtent
- **类型**: `FVector`
- **描述**: box extent used ONLY when owning actor doesn't have collision component

### NavMeshResolution
- **类型**: `ENavigationDataResolution`
- **描述**: Experimental: Indicates which navmesh resolution should be used around the actor.

### AreaClass
- **类型**: `TSubclassOf<UNavArea>`

### bIncludeAgentHeight
- **类型**: `bool`

## 方法

### SetAreaClass
```angelscript
void SetAreaClass(TSubclassOf<UNavArea> NewAreaClass)
```

