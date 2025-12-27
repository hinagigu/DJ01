# FARPDefaultPluginDomainRules

## 属性

### CanReferenceTheseDomains
- **类型**: `TArray<FString>`
- **描述**: The list of additional domains always visible from a plugin
(EngineContent is always visible, as is content from other plugins that are explicitly referenced)

### bCanProjectAccessThesePlugins
- **类型**: `bool`
- **描述**: Can content in the ProjectContent domain access plugin content automatically (for plugins that don't match a specific rule)?

### bCanBeSeenByOtherDomainsWithoutDependency
- **类型**: `bool`
- **描述**: Can content in other domains access plugin content automatically (for plugins that don't match a specific rule)?
Note: This rule may be deprecated in the future!

## 方法

### opAssign
```angelscript
FARPDefaultPluginDomainRules& opAssign(FARPDefaultPluginDomainRules Other)
```

