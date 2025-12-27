# UCommonLazyWidget

**继承自**: `UWidget`

A special Image widget that can show unloaded images and takes care of the loading for you!

## 属性

### LoadingBackgroundBrush
- **类型**: `FSlateBrush`

### OnLoadingStateChanged
- **类型**: `FOnLoadGuardStateChangedDynamic`

## 方法

### GetContent
```angelscript
UUserWidget GetContent()
```

### IsLoading
```angelscript
bool IsLoading()
```

### SetLazyContent
```angelscript
void SetLazyContent(TSoftClassPtr<UUserWidget> SoftWidget)
```

