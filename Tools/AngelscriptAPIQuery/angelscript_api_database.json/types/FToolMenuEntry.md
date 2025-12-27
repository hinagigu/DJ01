# FToolMenuEntry

Represents entries in menus such as buttons, checkboxes, and sub-menus.

Many entries are created for you via the methods of FToolMenuSection, such as FToolMenuSection::AddMenuEntry.

## 属性

### Name
- **类型**: `FName`

### Owner
- **类型**: `FToolMenuOwner`

### Type
- **类型**: `EMultiBlockType`

### UserInterfaceActionType
- **类型**: `EUserInterfaceActionType`

### TutorialHighlightName
- **类型**: `FName`

### InsertPosition
- **类型**: `FToolMenuInsert`

### bShouldCloseWindowAfterMenuSelection
- **类型**: `bool`

### ScriptObject
- **类型**: `UToolMenuEntryScript`

### StyleNameOverride
- **类型**: `FName`

## 方法

### opAssign
```angelscript
FToolMenuEntry& opAssign(FToolMenuEntry Other)
```

