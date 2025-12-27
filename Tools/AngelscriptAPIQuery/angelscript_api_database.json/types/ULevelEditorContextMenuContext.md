# ULevelEditorContextMenuContext

**继承自**: `UObject`

## 属性

### ContextType
- **类型**: `ELevelEditorMenuContext`

### CurrentSelection
- **类型**: `const UTypedElementSelectionSet`

### CursorWorldLocation
- **类型**: `FVector`

### SelectedComponents
- **类型**: `TArray<TObjectPtr<UActorComponent>>`

### HitProxyActor
- **类型**: `TWeakObjectPtr<AActor>`
- **描述**: If the ContextType is Viewport this property can be set to the HitProxy actor that triggered the ContextMenu.

## 方法

### GetHitProxyElement
```angelscript
FScriptTypedElementHandle GetHitProxyElement()
```

