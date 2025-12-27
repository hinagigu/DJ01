# UInterchangeImportTestPlan

**继承自**: `UObject`

Define a test plan

## 属性

### Steps
- **类型**: `TArray<TObjectPtr<UInterchangeImportTestStepBase>>`
- **描述**: Set of steps to perform to carry out this test plan

### bIsEnabledInAutomationTests
- **类型**: `bool`
- **描述**: Whether or not this test plan is currently enabled

### DisabledTestReason
- **类型**: `FString`
- **描述**: Why is the test plan disabled.

## 方法

### RunThisTest
```angelscript
void RunThisTest()
```
Click here to immediately run this single test through the automation framework

