# FARPDomainDefinitionByContentRoot

## 属性

### DomainName
- **类型**: `FString`
- **描述**: The name of this domain

### DomainDisplayName
- **类型**: `FText`
- **描述**: The display name of this domain (used in error message when attempting to reference content incorrectly)

### ErrorMessageIfUsedElsewhere
- **类型**: `FText`
- **描述**: The error message if something that is not allowed to attempts to reference content from this domain

### ContentRoots
- **类型**: `TArray<FDirectoryPath>`
- **描述**: The list of content root paths considered to be part of this domain

### SpecificAssets
- **类型**: `TArray<FName>`
- **描述**: A list of specific assets considered to be part of this domain

### ReferenceMode
- **类型**: `EARPDomainAllowedToReferenceMode`
- **描述**: What content is this domain allowed to access?

### CanReferenceTheseDomains
- **类型**: `TArray<FString>`
- **描述**: The list of additional domains always visible from this domain
(EngineContent is always visible)

## 方法

### opAssign
```angelscript
FARPDomainDefinitionByContentRoot& opAssign(FARPDomainDefinitionByContentRoot Other)
```

