# AEditorUtilityActor

**继承自**: `AActor`

## 属性

### bReceivesEditorInput
- **类型**: `bool`

## 方法

### GetInputComponent
```angelscript
UInputComponent GetInputComponent()
```
Returns the current InputComponent on this utility actor. This will be NULL unless bReceivesEditorInput is set to true.

### GetReceivesEditorInput
```angelscript
bool GetReceivesEditorInput()
```

### Run
```angelscript
void Run()
```
Standard function to execute

### SetReceivesEditorInput
```angelscript
void SetReceivesEditorInput(bool bInValue)
```

