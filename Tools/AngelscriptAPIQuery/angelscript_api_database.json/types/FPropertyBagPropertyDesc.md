# FPropertyBagPropertyDesc

Describes a property in the property bag.

## 属性

### ValueTypeObject
- **类型**: `const UObject`
- **描述**: Pointer to object that defines the Enum, Struct, or Class.

### ID
- **类型**: `FGuid`
- **描述**: Unique ID for this property. Used as main identifier when copying values over.

### Name
- **类型**: `FName`
- **描述**: Name for the property.

### ValueType
- **类型**: `EPropertyBagPropertyType`
- **描述**: Type of the value described by this property.

### MetaClass
- **类型**: `UClass`
- **描述**: Editor-only meta class for IClassViewer

## 方法

### opAssign
```angelscript
FPropertyBagPropertyDesc& opAssign(FPropertyBagPropertyDesc Other)
```

