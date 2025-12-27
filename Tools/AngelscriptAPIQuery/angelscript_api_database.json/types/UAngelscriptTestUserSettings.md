# UAngelscriptTestUserSettings

**继承自**: `UDeveloperSettings`

## 属性

### bRunUnitTestsOnHotReload
- **类型**: `bool`
- **描述**: Whether tests on hot reload is enabled.

### LimitNModulesToTestOnHotReload
- **类型**: `int`
- **描述**: When hot reloading, all tests depending on the newly recompiled files will be executed.
Use this setting to limit the number of modules to be tested upon hot reload.
Set to 0 to disable limit.

