# UOnlineHotfixManager

**继承自**: `UObject`

This class manages the downloading and application of hotfix data
Hotfix data is a set of non-executable files downloaded and applied to the game.
The base implementation knows how to handle INI, PAK, and locres files.
NOTE: Each INI/PAK file must be prefixed by the platform name they are targeted at

## 方法

### StartHotfixProcess
```angelscript
void StartHotfixProcess()
```
Starts the fetching of hotfix data from the OnlineTitleFileInterface that is registered for this game

