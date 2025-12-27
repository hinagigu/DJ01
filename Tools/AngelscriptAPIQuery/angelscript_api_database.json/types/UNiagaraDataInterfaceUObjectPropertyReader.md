# UNiagaraDataInterfaceUObjectPropertyReader

**继承自**: `UNiagaraDataInterface`

Data interface to read properties from UObjects.
Rather than having BP tick functions that push data into Niagara this data interface will instead pull them.

## 属性

### SourceMode
- **类型**: `ENDIObjectPropertyReaderSourceMode`
- **描述**: Determines how we should select the source object we read from.

### UObjectParameterBinding
- **类型**: `FNiagaraUserParameterBinding`
- **描述**: User parameter Object binding to read properties from.

### PropertyRemap
- **类型**: `TArray<FNiagaraUObjectPropertyReaderRemap>`

### SourceActor
- **类型**: `TSoftObjectPtr<AActor>`
- **描述**: Optional source actor to use, if the user parameter binding is valid this will be ignored.

### SourceActorComponentClass
- **类型**: `UClass`
- **描述**: When an actor is bound as the object we will also search for a component of this type to bind properties to.
For example, setting this to a UPointLightComponent when binding properties we will first look at the actor
then look for a component of UPointLightComponent and look at properties on that also.
If no class is specified here we look at the RootComponent instead.

