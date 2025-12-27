# FNiagaraSimpleClientInfo

Simple information on the connected client for use in continuous or immediate response UI elements.

## 属性

### Systems
- **类型**: `TArray<FString>`
- **描述**: List of all system names in the scene.

### Actors
- **类型**: `TArray<FString>`
- **描述**: List of all actors with Niagara components.

### Components
- **类型**: `TArray<FString>`
- **描述**: List of all Niagara components.

### Emitters
- **类型**: `TArray<FString>`
- **描述**: List of all Niagara emitters.

## 方法

### opAssign
```angelscript
FNiagaraSimpleClientInfo& opAssign(FNiagaraSimpleClientInfo Other)
```

