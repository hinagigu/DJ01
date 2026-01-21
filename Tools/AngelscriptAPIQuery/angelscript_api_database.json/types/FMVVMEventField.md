# FMVVMEventField

Generic structure to notify when an event occurs.

class UMyViewmodel : public UMVVMViewModelBase
{
  UPROPERTY(FieldNotify)
  FMVVMEventField SomeEvent;

  void OnSomeEvent()
  {
    UE_MVVM_BROADCAST_FIELD_VALUE_CHANGED(SomeEvent);
  }
};
};

## 方法

### opAssign
```angelscript
FMVVMEventField& opAssign(FMVVMEventField Other)
```

