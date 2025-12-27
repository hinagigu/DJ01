# FWidgetEventField

Generic structure to notify when an event occurs.

class UMyWidget : public UWidget
{
  UPROPERTY(FieldNotify)
  FWidgetEventField SomeEvent;

  void OnSomeEvent()
  {
    BroadcastFieldValueChanged(FFieldNotificationClassDescriptor::Text);
  }
};
};

## 方法

### opAssign
```angelscript
FWidgetEventField& opAssign(FWidgetEventField Other)
```

