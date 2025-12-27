# __UCommonUIExtensions

## 方法

### GetLocalPlayerFromController
```angelscript
ULocalPlayer GetLocalPlayerFromController(APlayerController PlayerController)
```

### GetOwningPlayerInputType
```angelscript
ECommonInputType GetOwningPlayerInputType()
```

### IsOwningPlayerUsingGamepad
```angelscript
bool IsOwningPlayerUsingGamepad()
```

### IsOwningPlayerUsingTouch
```angelscript
bool IsOwningPlayerUsingTouch()
```

### PopContentFromLayer
```angelscript
void PopContentFromLayer(UCommonActivatableWidget ActivatableWidget)
```

### PushContentToLayer_ForPlayer
```angelscript
UCommonActivatableWidget PushContentToLayer_ForPlayer(const ULocalPlayer LocalPlayer, FGameplayTag LayerName, TSubclassOf<UCommonActivatableWidget> WidgetClass)
```

### PushStreamedContentToLayer_ForPlayer
```angelscript
void PushStreamedContentToLayer_ForPlayer(const ULocalPlayer LocalPlayer, FGameplayTag LayerName, TSoftClassPtr<UCommonActivatableWidget> WidgetClass)
```

### ResumeInputForPlayer
```angelscript
void ResumeInputForPlayer(APlayerController PlayerController, FName SuspendToken)
```

### SuspendInputForPlayer
```angelscript
FName SuspendInputForPlayer(APlayerController PlayerController, FName SuspendReason)
```

### StaticClass
```angelscript
UClass StaticClass()
```

