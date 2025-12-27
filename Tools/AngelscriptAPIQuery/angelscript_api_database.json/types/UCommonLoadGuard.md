# UCommonLoadGuard

**继承自**: `UContentWidget`

The Load Guard behaves similarly to a Border, but with the ability to hide its primary content and display a loading spinner
and optional message while needed content is loaded or otherwise prepared.

Use GuardAndLoadAsset to automatically display the loading state until the asset is loaded (then the content widget will be displayed).
For other applications (ex: waiting for an async backend call to complete), you can manually set the loading state of the guard.

## 属性

### bShowLoading
- **类型**: `bool`

### LoadingBackgroundBrush
- **类型**: `FSlateBrush`
- **描述**: The background brush to display while loading the content

### ThrobberAlignment
- **类型**: `EHorizontalAlignment`
- **描述**: The horizontal alignment of the loading throbber & message

### ThrobberPadding
- **类型**: `FMargin`
- **描述**: The horizontal alignment of the loading throbber & message

### TextStyle
- **类型**: `TSubclassOf<UCommonTextStyle>`
- **描述**: Style to apply to the loading message

### BP_OnLoadingStateChanged
- **类型**: `FOnLoadGuardStateChangedDynamic`

## 方法

### GuardAndLoadAsset
```angelscript
void GuardAndLoadAsset(TSoftObjectPtr<UObject> InLazyAsset, FOnAssetLoaded__CommonLoadGuard OnAssetLoaded)
```

### IsLoading
```angelscript
bool IsLoading()
```

### SetIsLoading
```angelscript
void SetIsLoading(bool bInIsLoading)
```

### SetLoadingText
```angelscript
void SetLoadingText(FText InLoadingText)
```

