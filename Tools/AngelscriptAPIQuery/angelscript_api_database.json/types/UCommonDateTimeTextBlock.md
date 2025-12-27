# UCommonDateTimeTextBlock

**继承自**: `UCommonTextBlock`

## 属性

### CustomTimespanFormat
- **类型**: `FText`
- **描述**: * Supplies a custom timespan format to use if desired
* Supported arguments include {Days}, {Hours}, {Minutes}, and {Seconds}

### bCustomTimespanLeadingZeros
- **类型**: `bool`
- **描述**: * If the custom timespan should use a leading zero for values, ie "02"

## 方法

### GetDateTime
```angelscript
FDateTime GetDateTime()
```

### SetCountDownCompletionText
```angelscript
void SetCountDownCompletionText(FText InCompletionText)
```

### SetDateTimeValue
```angelscript
void SetDateTimeValue(FDateTime InDateTime, bool bShowAsCountdown, float32 InRefreshDelay)
```

### SetTimespanValue
```angelscript
void SetTimespanValue(FTimespan InTimespan)
```

