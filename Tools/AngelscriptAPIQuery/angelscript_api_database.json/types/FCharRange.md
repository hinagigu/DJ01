# FCharRange

Represents a range of characters, specified by the Unicode code point of the first and last characters in the range, both included.
 If you need a single-character range, simply use the same character for both the first and last characters.

## 属性

### First
- **类型**: `uint16`
- **描述**: Unicode code point of the first character in the range (inclusive). Only characters within the Basic Multilingual Plane are supported.
 Note: The code point must be entered in decimal, not hexadecimal.

### Last
- **类型**: `uint16`
- **描述**: Unicode code point of the last character in the range (inclusive). Only characters within the Basic Multilingual Plane are supported.
 Note: The code point must be entered in decimal, not hexadecimal.

## 方法

### opAssign
```angelscript
FCharRange& opAssign(FCharRange Other)
```

