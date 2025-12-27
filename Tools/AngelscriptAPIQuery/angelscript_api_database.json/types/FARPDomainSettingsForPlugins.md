# FARPDomainSettingsForPlugins

## 属性

### DefaultRule
- **类型**: `FARPDefaultPluginDomainRules`
- **描述**: The default rule if a more specific plugin rule doesn't apply

### AdditionalRules
- **类型**: `TArray<FARPDomainDefinitionForMatchingPlugins>`
- **描述**: Discovered plugins will be matched against these templates
Priority rules (a path match is preferred to a category match, and within each the longest match wins):
  Highest: The most specific path match
           Any path match
           The most specific category match
           Any category match

## 方法

### opAssign
```angelscript
FARPDomainSettingsForPlugins& opAssign(FARPDomainSettingsForPlugins Other)
```

