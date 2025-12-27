# UToolMenu

**继承自**: `UToolMenuBase`

Represents a menu in the ToolMenus system.

An instance of this class is returned by basic APIs such as UToolMenus::RegisterMenu and UToolMenus::ExtendMenu.

## 属性

### MenuName
- **类型**: `FName`

### MenuParent
- **类型**: `FName`

### StyleName
- **类型**: `FName`

### TutorialHighlightName
- **类型**: `FName`

### MenuType
- **类型**: `EMultiBoxType`

### bShouldCloseWindowAfterMenuSelection
- **类型**: `bool`

### bCloseSelfOnly
- **类型**: `bool`

### bSearchable
- **类型**: `bool`

### bToolBarIsFocusable
- **类型**: `bool`

### bToolBarForceSmallIcons
- **类型**: `bool`

### bPreventCustomization
- **类型**: `bool`

### MenuOwner
- **类型**: `FToolMenuOwner`

## 方法

### AddDynamicSection
```angelscript
void AddDynamicSection(FName SectionName, UToolMenuSectionDynamic Object)
```

### AddMenuEntry
```angelscript
void AddMenuEntry(FName SectionName, FToolMenuEntry Args)
```

### AddMenuEntryObject
```angelscript
void AddMenuEntryObject(UToolMenuEntryScript InObject)
```

### AddSection
```angelscript
void AddSection(FName SectionName, FText Label, FName InsertName, EToolMenuInsertType InsertType)
```

### AddSubMenu
```angelscript
UToolMenu AddSubMenu(FName Owner, FName SectionName, FName Name, FText Label, FText ToolTip)
```

### InitMenu
```angelscript
void InitMenu(FToolMenuOwner Owner, FName Name, FName Parent, EMultiBoxType Type)
```

