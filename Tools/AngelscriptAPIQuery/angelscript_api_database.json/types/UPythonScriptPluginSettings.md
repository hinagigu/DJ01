# UPythonScriptPluginSettings

**继承自**: `UDeveloperSettings`

Configure the Python plug-in.

## 属性

### StartupScripts
- **类型**: `TArray<FString>`
- **描述**: Array of Python scripts to run at start-up (run before the first Tick after the Engine has initialized).

### AdditionalPaths
- **类型**: `TArray<FDirectoryPath>`
- **描述**: Array of additional paths to add to the Python system paths.

### bIsolateInterpreterEnvironment
- **类型**: `bool`
- **描述**: Should the embedded interpreter be run in isolation mode. In isolation, the standard PYTHON* environment variables (PYTHONPATH,
PYTHONHOME, etc), the script's directory and the user's site-packages directory are ignored by the interpreter. This
prevents incompabible software to crash the engine. Consider turning this option off if you tightly control your Python
environment and you are sure everything is compatible. Note that the UE_PYTHONPATH environment variable is added to 'sys.path'
whether the interpreter runs in insolation mode or not.

### bDeveloperMode
- **类型**: `bool`
- **描述**: Should Developer Mode be enabled on the Python interpreter *for all users of the project*
Note: Most of the time you want to enable bDeveloperMode in the Editor Preferences instead!

(will also enable extra warnings (e.g., for deprecated code), and enable stub code generation for
use with external IDEs).

### bRunPipInstallOnStartup
- **类型**: `bool`
- **描述**: Should the pip install task be run on editor startup.

NOTE: The project pip install directory: <ProjectDir>/Intermediate/PipInstall/Lib/site-packages
      will still be added to site package path, if it exists, to allow for pre-populated installs
      even auto-running UBT PipInstall is disabled.

      See <ProjectDir>/Intermediate/PipInstall/merged_requirements.in for listing of required packages.

### bPipStrictHashCheck
- **类型**: `bool`
- **描述**: Require pip to use strict hash checking for all packages
WARNING: Disabling this setting is a security risk, particularly when combined with IndexUrl override

### bOfflineOnly
- **类型**: `bool`
- **描述**: Only run pip to generate merged requiremnts and/or validate requested packages are installed

### OverrideIndexURL
- **类型**: `FString`
- **描述**: Override all index/extra-index URLs, this is useful for internal NAT installs (using e.g. devpi or similar index cache)
WARNING: Strict hash checks should be enabled if an override index url is used

### bRemoteExecution
- **类型**: `bool`
- **描述**: Should remote Python execution be enabled?

### RemoteExecutionMulticastGroupEndpoint
- **类型**: `FString`
- **描述**: The multicast group endpoint (in the form of IP_ADDRESS:PORT_NUMBER) that the UDP multicast socket should join

### RemoteExecutionMulticastBindAddress
- **类型**: `FString`
- **描述**: The adapter address that the UDP multicast socket should bind to, or 0.0.0.0 to bind to all adapters

### RemoteExecutionSendBufferSizeBytes
- **类型**: `int`
- **描述**: Size of the send buffer for the remote endpoint connection

### RemoteExecutionReceiveBufferSizeBytes
- **类型**: `int`
- **描述**: Size of the receive buffer for the remote endpoint connection

### RemoteExecutionMulticastTtl
- **类型**: `uint8`
- **描述**: The TTL that the UDP multicast socket should use (0 is limited to the local host, 1 is limited to the local subnet)

