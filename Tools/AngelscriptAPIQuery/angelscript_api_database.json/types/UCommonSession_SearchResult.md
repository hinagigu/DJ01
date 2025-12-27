# UCommonSession_SearchResult

**继承自**: `UObject`

A result object returned from the online system that describes a joinable game session

## 方法

### GetDescription
```angelscript
FString GetDescription()
```
Returns an internal description of the session, not meant to be human readable

### GetIntSetting
```angelscript
void GetIntSetting(FName Key, int& Value, bool& bFoundValue)
```
Gets an arbitrary integer setting, bFoundValue will be false if the setting does not exist

### GetMaxPublicConnections
```angelscript
int GetMaxPublicConnections()
```
The maximum number of publicly available connections that could be available, including already filled connections

### GetNumOpenPrivateConnections
```angelscript
int GetNumOpenPrivateConnections()
```
The number of private connections that are available

### GetNumOpenPublicConnections
```angelscript
int GetNumOpenPublicConnections()
```
The number of publicly available connections that are available

### GetPingInMs
```angelscript
int GetPingInMs()
```
Ping to the search result, MAX_QUERY_PING is unreachable

### GetStringSetting
```angelscript
void GetStringSetting(FName Key, FString& Value, bool& bFoundValue)
```
Gets an arbitrary string setting, bFoundValue will be false if the setting does not exist

