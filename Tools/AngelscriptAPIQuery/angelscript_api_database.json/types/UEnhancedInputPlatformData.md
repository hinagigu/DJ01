# UEnhancedInputPlatformData

**继承自**: `UObject`

A base class that can be used to store platform specific data for Enhanced Input.

Make a subclass of this to add some additional options for per-platform settings

## 属性

### MappingContextRedirects
- **类型**: `TMap<TObjectPtr<UInputMappingContext>,TObjectPtr<UInputMappingContext>>`

## 方法

### GetContextRedirect
```angelscript
const UInputMappingContext GetContextRedirect(UInputMappingContext InContext)
```
Returns a pointer to the desired redirect mapping context. If there isn't one, then this returns InContext.

