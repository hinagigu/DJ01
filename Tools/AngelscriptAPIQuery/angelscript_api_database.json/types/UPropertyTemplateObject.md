# UPropertyTemplateObject

**继承自**: `UObject`

In order to use PropertyEditorModule.CreateSingleProperty we have to give it an object instance
and the name of the target property to edit. It will then iterate the object for a property with that
name and create a property editor widget.

This is very limiting when editing a single entry within an FArrayProperty, as the inner and the
array prop will have the same name, leading it to create an array editor. Also, since we have to
give it an instance, modifying the widget will automatically modify the object, which we may not
want, we may just want a property editor of a particular type.

This class is a hack around all that: It has an instance of most property types,
so that you can instantiate one of these and just pass along the name of the property type you want.
They are all be named Captured<propertyType> (e.g. CapturedFloatProperty, CapturedObjectProperty,
bCapturedBoolProperty) but you can use the helper function to get the name of the property you want.
// TODO: Convert this into a static dictionary that maps to a small separate class for each property type
// Maybe even template it for array/map/set property types

## 属性

### CapturedByteProperty
- **类型**: `uint8`
- **描述**: Captured byte property

### CapturedUInt16Property
- **类型**: `uint16`
- **描述**: Captured uint16 property

### CapturedUInt32Property
- **类型**: `uint`
- **描述**: Captured uint32 property

### CapturedUInt64Property
- **类型**: `uint64`
- **描述**: Captured uint16 property

### CapturedInt8Property
- **类型**: `int8`
- **描述**: Captured int8 property

### CapturedInt16Property
- **类型**: `int16`
- **描述**: Captured int16 property

### CapturedIntProperty
- **类型**: `int`
- **描述**: Captured int32 property

### CapturedInt64Property
- **类型**: `int64`
- **描述**: Captured int64 property

### CapturedFloatProperty
- **类型**: `float32`
- **描述**: Captured float property

### CapturedDoubleProperty
- **类型**: `float`
- **描述**: Captured double property

### bCapturedBoolProperty
- **类型**: `bool`
- **描述**: Captured boolean property

### CapturedObjectProperty
- **类型**: `UObject`
- **描述**: Captured UObject property

### CapturedSoftObjectProperty
- **类型**: `TSoftObjectPtr<UObject>`
- **描述**: Captured Soft UObject property

### CapturedNameProperty
- **类型**: `FName`
- **描述**: Captured FName property

### CapturedStrProperty
- **类型**: `FString`
- **描述**: Captured FString property

### CapturedTextProperty
- **类型**: `FText`
- **描述**: Captured FText property

### CapturedVectorProperty
- **类型**: `FVector`
- **描述**: Captured FVector property

