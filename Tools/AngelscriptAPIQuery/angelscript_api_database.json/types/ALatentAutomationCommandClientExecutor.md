# ALatentAutomationCommandClientExecutor

**继承自**: `AActor`

ALatentAutomationCommandClientExecutor

Executes a ULatentAutomationCommand on client.

This Actor replicates. The provided ULatentAutomationCommand will be replicated.
When ticking, this Actor will inject a component into the player controller to be
able to synchronize execution between client and server.
This Actor executes the test on client.

The executor will use the different replicated properties to communicate the
different phases of execution from server to client.

## 方法

### AssertFalse
```angelscript
void AssertFalse(bool bExpression, FString Message)
```

### AssertNotNull
```angelscript
void AssertNotNull(const UObject Object, FString Message)
```

### AssertNotSame
```angelscript
void AssertNotSame(const UObject Expected, const UObject Actual, FString Message)
```

### AssertNull
```angelscript
void AssertNull(const UObject Object, FString Message)
```

### AssertSame
```angelscript
void AssertSame(const UObject Expected, const UObject Actual, FString Message)
```

### AssertTrue
```angelscript
void AssertTrue(bool bExpression, FString Message)
```

### Fail
```angelscript
void Fail(FString Message)
```
Client functions

### ServerAssertFalse
```angelscript
void ServerAssertFalse(bool bExpression, FString Message)
```

### ServerAssertNotNull
```angelscript
void ServerAssertNotNull(const UObject Object, FString Message)
```

### ServerAssertNotSame
```angelscript
void ServerAssertNotSame(const UObject Expected, const UObject Actual, FString Message)
```

### ServerAssertNull
```angelscript
void ServerAssertNull(const UObject Object, FString Message)
```

### ServerAssertSame
```angelscript
void ServerAssertSame(const UObject Expected, const UObject Actual, FString Message)
```

### ServerAssertTrue
```angelscript
void ServerAssertTrue(bool bExpression, FString Message)
```

### ServerFail
```angelscript
void ServerFail(FString Message)
```

### ServerLatentCommandClientChecked
```angelscript
void ServerLatentCommandClientChecked()
```

### ServerLatentCommandClientDone
```angelscript
void ServerLatentCommandClientDone()
```

### ServerLatentCommandClientReady
```angelscript
void ServerLatentCommandClientReady()
```

### ServerLatentCommandDescribeOnClient
```angelscript
void ServerLatentCommandDescribeOnClient(FString NewDescription)
```

