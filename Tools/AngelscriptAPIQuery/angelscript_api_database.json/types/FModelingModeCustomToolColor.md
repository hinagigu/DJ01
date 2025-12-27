# FModelingModeCustomToolColor

Defines a color to be used for a particular Tool Palette Tool

## 属性

### ToolName
- **类型**: `FString`
- **描述**: Name of Section or Tool in Modeling Mode Tool Palette

Format:
SectionName        (Specifies a default color for all tools in the section.)
SectionName.ToolName        (Specifies an override color for a specific tool in the given section.)

### Color
- **类型**: `FLinearColor`
- **描述**: Custom Tool Color

## 方法

### opAssign
```angelscript
FModelingModeCustomToolColor& opAssign(FModelingModeCustomToolColor Other)
```

