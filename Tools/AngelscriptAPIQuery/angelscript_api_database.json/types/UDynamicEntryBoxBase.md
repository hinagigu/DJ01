# UDynamicEntryBoxBase

**继承自**: `UWidget`

Base for widgets that support a dynamic number of auto-generated entries at both design- and run-time.
Contains all functionality needed to create, construct, and cache an arbitrary number of entry widgets, but exposes no means of entry creation or removal
It's up to child classes to decide how they want to perform the population (some may do so entirely on their own without exposing a thing)

@see UDynamicEntryBox for a ready-to-use version

## 属性

### SpacingPattern
- **类型**: `TArray<FVector2D>`

### EntryBoxType
- **类型**: `EDynamicBoxType`

### EntrySizeRule
- **类型**: `FSlateChildSize`

### EntryHorizontalAlignment
- **类型**: `EHorizontalAlignment`

### EntryVerticalAlignment
- **类型**: `EVerticalAlignment`

### MaxElementSize
- **类型**: `int`

### RadialBoxSettings
- **类型**: `FRadialBoxSettings`

### EntrySpacing
- **类型**: `FVector2D`

## 方法

### GetAllEntries
```angelscript
TArray<UUserWidget> GetAllEntries()
```

### GetNumEntries
```angelscript
int GetNumEntries()
```

### SetEntrySpacing
```angelscript
void SetEntrySpacing(FVector2D InEntrySpacing)
```

### SetRadialSettings
```angelscript
void SetRadialSettings(FRadialBoxSettings InSettings)
```

