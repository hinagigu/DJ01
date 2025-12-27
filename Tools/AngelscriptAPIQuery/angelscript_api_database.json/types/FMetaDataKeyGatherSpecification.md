# FMetaDataKeyGatherSpecification

## 属性

### MetaDataKey
- **类型**: `FMetaDataKeyName`
- **描述**: The metadata key for which values will be gathered as text.

### TextNamespace
- **类型**: `FString`
- **描述**: The localization namespace in which the gathered text will be output.

### TextKeyPattern
- **类型**: `FMetaDataTextKeyPattern`
- **描述**: The pattern which will be formatted to form the localization key for the metadata value gathered as text.
      Placeholder - Description
      {FieldPath} - The fully qualified name of the object upon which the metadata resides.
      {MetaDataValue} - The value associated with the metadata key.

## 方法

### opAssign
```angelscript
FMetaDataKeyGatherSpecification& opAssign(FMetaDataKeyGatherSpecification Other)
```

