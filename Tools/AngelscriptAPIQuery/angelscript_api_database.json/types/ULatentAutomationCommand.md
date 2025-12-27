# ULatentAutomationCommand

**继承自**: `UObject`

## 属性

### bAllowTimeout
- **类型**: `bool`

### bAlsoRunOnClient
- **类型**: `bool`

## 方法

### GetCurrentTest
```angelscript
FIntegrationTest& GetCurrentTest()
```
Retrieves the current test. You can only call this after the command has been
passed to T.AddLatentAutomationCommand() or after SetCurrentTest has been called.

### SetCurrentTest
```angelscript
void SetCurrentTest(FIntegrationTest& T)
```
Retrieves the client executor or null if it's not a client test. Clients only
have access to the client executor rather than the test itself.

### GetClientExecutor
```angelscript
ALatentAutomationCommandClientExecutor GetClientExecutor()
```
Use this for commands that are not added with AddLatentAutomationCommand.
This could be the case if a latent command is a child to another command.


### After
```angelscript
void After()
```

### AfterOnClient
```angelscript
bool AfterOnClient()
```

### Before
```angelscript
void Before()
```

### BeforeOnClient
```angelscript
bool BeforeOnClient()
```

### Describe
```angelscript
FString Describe()
```

### DescribeOnClient
```angelscript
FString DescribeOnClient()
```

### HasAuthority
```angelscript
bool HasAuthority()
```

### Update
```angelscript
bool Update()
```

### UpdateOnClient
```angelscript
bool UpdateOnClient()
```

