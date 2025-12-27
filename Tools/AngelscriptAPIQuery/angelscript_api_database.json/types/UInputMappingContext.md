# UInputMappingContext

**继承自**: `UDataAsset`

UInputMappingContext : A collection of key to action mappings for a specific input context
Could be used to:
     Store predefined controller mappings (allow switching between controller config variants). TODO: Build a system allowing redirects of UInputMappingContexts to handle this.
     Define per-vehicle control mappings
     Define context specific mappings (e.g. I switch from a gun (shoot action) to a grappling hook (reel in, reel out, disconnect actions).
     Define overlay mappings to be applied on top of existing control mappings (e.g. Hero specific action mappings in a MOBA)

## 属性

### Mappings
- **类型**: `TArray<FEnhancedActionKeyMapping>`

### ContextDescription
- **类型**: `FText`

## 方法

### MapKey
```angelscript
FEnhancedActionKeyMapping& MapKey(const UInputAction Action, FKey ToKey)
```
Map a key to an action within the mapping context.

### UnmapAll
```angelscript
void UnmapAll()
```
Unmap everything within the mapping context.

### UnmapAllKeysFromAction
```angelscript
void UnmapAllKeysFromAction(const UInputAction Action)
```
Unmap all key maps to an action within the mapping context.

### UnmapKey
```angelscript
void UnmapKey(const UInputAction Action, FKey Key)
```
Unmap a key from an action within the mapping context.

