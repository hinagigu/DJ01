# UAngelscriptTestSettings

**继承自**: `UDeveloperSettings`

## 属性

### bEnableTestDiscovery
- **类型**: `bool`
- **描述**: Whether to enable test discovery from script files.

### IntegrationTestMapRoot
- **类型**: `FString`
- **描述**: Where integration test maps are stored.

### GarbageCollectEveryNTests
- **类型**: `int`
- **描述**: Force garbage collection every N tests.
This will also perform test execution in batches when hot reloading.
All the tests of an AS module are added or not, so the number of test in a batch can
be greater that this. Understand this setting as a minimum number of tests per batch but
don't continue adding modules once this number has been reached.
This allows the editor to refresh between batches and prevents a lock because of PhysX issues.
Set to 0 to disable.

### UnitTestGameInstanceClass
- **类型**: `TSoftClassPtr<UGameInstance>`
- **描述**: The game instance class to use for unit tests.

### bEnableCodeCoverage
- **类型**: `bool`
- **描述**: Turn on code coverage measurements. Reports are written to Saved/CodeCoverage/.

### CoverageExcludePatterns
- **类型**: `TArray<FString>`
- **描述**: Don't measure coverage in paths that match these wildcards.
Paths start at the Angelscript root (by convention this dir is named Script/). If you want
to exclude a directory from which modules are imported as Network.MyFile, you want to add
Network/_* to this list (NOTE: remove the _, it's there to avoid -Wcomment in clang).
If you just want to exclude MyFile.as, add Network/MyFile.as. If you have the convention
that unit tests be in files named _Test.as, add the pattern *_Test.as, and so on.

### bEnableDebugBreaksInTests
- **类型**: `bool`
- **描述**: Debug-break on ensures in tests. This is generally off in tests because ensures
are intentionally triggered by tests all the time, which is really annoying.

### IntegrationTestNamingConvention
- **类型**: `FString`
- **描述**: Module paths containing IntegrationTests must match the following wildcard pattern

### UnitTestNamingConvention
- **类型**: `FString`
- **描述**: Module paths containing UnitTests must match the following wildcard pattern

### bEnableNetworkEmulation
- **类型**: `bool`
- **描述**: Whether tests that use client/server should apply any network emulation.

### InPacketsMinLatency
- **类型**: `int`
- **描述**: The minimum latency of incoming packets.

### InPacketsMaxLatency
- **类型**: `int`
- **描述**: The maximum latency of incoming packets.

### InPacketsPacketLossPercentage
- **类型**: `int`
- **描述**: The packet loss percentage of incoming packets.

### OutPacketsMinLatency
- **类型**: `int`
- **描述**: The minimum latency of outgoing packets.

### OutPacketsMaxLatency
- **类型**: `int`
- **描述**: The maximum latency of outgoing packets.

### OutPacketsPacketLossPercentage
- **类型**: `int`
- **描述**: The packet loss percentage of outgoing packets.

