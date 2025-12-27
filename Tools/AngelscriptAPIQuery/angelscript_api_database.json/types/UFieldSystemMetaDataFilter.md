# UFieldSystemMetaDataFilter

**继承自**: `UFieldSystemMetaData`

Filter the particles on which the field will be applied

## 属性

### FilterType
- **类型**: `EFieldFilterType`

### ObjectType
- **类型**: `EFieldObjectType`

### PositionType
- **类型**: `EFieldPositionType`

## 方法

### SetMetaDataFilterType
```angelscript
UFieldSystemMetaDataFilter SetMetaDataFilterType(EFieldFilterType FilterType, EFieldObjectType ObjectType, EFieldPositionType PositionType)
```
Set the particles filter type
@param    FilterType State type used to select the state particles on which the field will be applied
@param    ObjectType Object type used to select the type of objects(rigid, cloth...) on which the field will be applied
@param    PositionType Position type used to compute the samples positions

