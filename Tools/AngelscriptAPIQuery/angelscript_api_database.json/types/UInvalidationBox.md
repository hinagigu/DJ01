# UInvalidationBox

**继承自**: `UContentWidget`

Invalidate
* Single Child
* Caching / Performance

## 属性

### bCanCache
- **类型**: `bool`

## 方法

### GetCanCache
```angelscript
bool GetCanCache()
```
@returns true when the invalidation box cache the widgets.
The widgets will be updated only if they get invalidated.

### SetCanCache
```angelscript
void SetCanCache(bool CanCache)
```
Tell the InvalidationBox to use the invalidation process.
@note the other internal flags can disable the option.

