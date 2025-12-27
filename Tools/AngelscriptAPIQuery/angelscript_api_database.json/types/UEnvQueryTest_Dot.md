# UEnvQueryTest_Dot

**继承自**: `UEnvQueryTest`

## 属性

### LineA
- **类型**: `FEnvDirection`
- **描述**: defines direction of first line used by test

### LineB
- **类型**: `FEnvDirection`
- **描述**: defines direction of second line used by test

### TestMode
- **类型**: `EEnvTestDot`

### bAbsoluteValue
- **类型**: `bool`
- **描述**: If true, this test uses the absolute value of the dot product rather than the dot product itself.  Useful
when you want to compare "how lateral" something is.  I.E. values closer to zero are further to the side,
and values closer to 1 are more in front or behind (without distinguishing forward/backward).

