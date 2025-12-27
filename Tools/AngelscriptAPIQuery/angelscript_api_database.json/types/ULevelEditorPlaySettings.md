# ULevelEditorPlaySettings

**继承自**: `UObject`

Implements the Editor's play settings.

## 属性

### GameGetsMouseControl
- **类型**: `bool`
- **描述**: Give the game mouse control when PIE starts or require a click in the viewport first

### UseMouseForTouch
- **类型**: `bool`
- **描述**: While using the game viewport, it sends mouse movement and clicks as touch events, instead of as mouse events.

### ShowMouseControlLabel
- **类型**: `bool`
- **描述**: Whether to show a label for mouse control gestures in the PIE view.

### MouseControlLabelPosition
- **类型**: `ELabelAnchorMode`
- **描述**: Location on screen to anchor the mouse control label when in PIE mode.

### ViewportGetsHMDControl
- **类型**: `bool`
- **描述**: Whether or not HMD orientation should be used when playing in viewport

### ShouldMinimizeEditorOnVRPIE
- **类型**: `bool`
- **描述**: Whether or not the editor is minimized on VR PIE

### bShouldMinimizeEditorOnNonVRPIE
- **类型**: `bool`
- **描述**: Whether or not the editor is minimized on non-VR PIE

### bEmulateStereo
- **类型**: `bool`
- **描述**: Whether we should emulate stereo (helps checking VR rendering issues).

### AutoRecompileBlueprints
- **类型**: `bool`
- **描述**: Automatically recompile blueprints used by the current level when initiating a Play In Editor session

### EnableGameSound
- **类型**: `bool`
- **描述**: Whether to play sounds when in a Play In Editor session

### SoloAudioInFirstPIEClient
- **类型**: `bool`
- **描述**: Whether to automatically solo audio in first PIE client

### EnablePIEEnterAndExitSounds
- **类型**: `bool`
- **描述**: Whether to play a sound when entering and exiting PIE

### PlayInEditorSoundQualityLevel
- **类型**: `int`
- **描述**: Which quality level to use when playing in editor

### bPromoteOutputLogWarningsDuringPIE
- **类型**: `bool`
- **描述**: Should warnings and errors in the Output Log during "Play in Editor" be promoted to the message log?

### NewWindowWidth
- **类型**: `int`
- **描述**: The width of the new view port window in pixels (0 = use the desktop's screen resolution).

### NewWindowHeight
- **类型**: `int`
- **描述**: The height of the new view port window in pixels (0 = use the desktop's screen resolution).

### NewWindowPosition
- **类型**: `FIntPoint`
- **描述**: The position of the new view port window on the screen in pixels.

### AdditionalLaunchParameters
- **类型**: `FString`
- **描述**: Extra parameters to be include as part of the command line for the standalone game.

### BuildGameBeforeLaunch
- **类型**: `EPlayOnBuildMode`
- **描述**: Whether to build the game before launching on device.

### LaunchConfiguration
- **类型**: `EPlayOnLaunchConfiguration`
- **描述**: Which build configuration to use when launching on device.

### PackFilesForLaunch
- **类型**: `EPlayOnPakFileMode`
- **描述**: Whether to content should be stored in pak files when launching on device. */

### bAutoCompileBlueprintsOnLaunch
- **类型**: `bool`
- **描述**: Whether to automatically recompile dirty Blueprints before launching

### bLaunchSeparateServer
- **类型**: `bool`
- **描述**: This is a rarely used option that will launch a separate server (possibly hidden in-process depending on RunUnderOneProcess)
even if the net mode does not require a server (such as Standalone). If the net mode requires a server (such as Client) a
server will be launched for you (regardless of this setting). This allows you to test offline -> server workflows by connecting
("open 127.0.0.1:<ServerPort>") from the offline game.

### PlayNetMode
- **类型**: `EPlayNetMode`
- **描述**: NetMode to use for Play In Editor.

### RunUnderOneProcess
- **类型**: `bool`
- **描述**: Spawn multiple player windows in a single instance of UE. This will load much faster, but has potential to have more issues.

### PlayNumberOfClients
- **类型**: `int`
- **描述**: The number of client windows to open. The first one to open will respect the Play In Editor "Modes" option (PIE, PINW), additional clients respect the RunUnderOneProcess setting.

### PrimaryPIEClientIndex
- **类型**: `int`
- **描述**: In multiplayer PIE which client will be the 'primary'. Considered most important and given a larger client window, access to unique hardware like a VirtualReality HMD, etc. Intended to help test issues that affect the second, etc client.  0 is the first client. If the setting is >= than the number of clients the last will be primary. -1 will result in no primary.  Note that this is an index only of PIE instance windows, in netmode 'Play as Client' pie instance zero is a windowless dedicated server, so setting 0 here would make the fist pie window the primary which would be PIEInstance 1, rather than 0 as in other netmodes.

### ServerPort
- **类型**: `uint16`
- **描述**: What port used by the server for simple networking

### ClientWindowWidth
- **类型**: `int`
- **描述**: Width to use when spawning additional windows.

### RouteGamepadToSecondWindow
- **类型**: `bool`
- **描述**: When running multiple player windows in a single process, this option determines how the game pad input gets routed.

If unchecked (default) then the 1st game pad is attached to the 1st window, 2nd to the 2nd window, and so on.

If it is checked, the 1st game pad goes the 2nd window. The 1st window can then be controlled by keyboard/mouse, which is convenient if two people are testing on the same computer.

### CreateAudioDeviceForEveryPlayer
- **类型**: `bool`
- **描述**: If checked, a separate audio device is created for every player.

If unchecked, a separate audio device is created for only the first two players and uses the main audio device for more than 2 players.

Enabling this will allow rendering accurate audio from every player's perspective but will use more CPU. Keep this disabled on lower-perf machines.

### ClientWindowHeight
- **类型**: `int`
- **描述**: Height to use when spawning additional windows.

### ServerMapNameOverride
- **类型**: `FString`
- **描述**: Override the map launched by the dedicated server (currently only used when in PIE_StandaloneWithServer net mode)

### AdditionalServerGameOptions
- **类型**: `FString`
- **描述**: Additional options that will be passed to the server as URL parameters, in the format ?bIsLanMatch=1?listen - any additional command line switches should be passed in the Additional Server Launch Parameters field below.

### bShowServerDebugDrawingByDefault
- **类型**: `bool`
- **描述**: Controls the default value of the show flag ServerDrawDebug

### ServerDebugDrawingColorTintStrength
- **类型**: `float32`
- **描述**: How strongly debug drawing originating from the server will be biased towards the tint color

### ServerDebugDrawingColorTint
- **类型**: `FLinearColor`
- **描述**: Debug drawing originating from the server will be biased towards this color

### bOneHeadsetEachProcess
- **类型**: `bool`
- **描述**: When True each PIE process is launched with "-HMDSimulator" argument.
The usefullness of this will vary by XR platform.
The PIE instances may get special -HMDSimulator behavior from an XR plugin, they may successfully make connections to the HMD hardware, their attempt to connect to hardware may be rejected by the runtime.

### AdditionalServerLaunchParameters
- **类型**: `FString`
- **描述**: Additional options that will be passed to the server as arguments, for example -debug. Only works with separate process servers.

### ServerFixedFPS
- **类型**: `int`
- **描述**: If > 0, Tick dedicated server at a fixed frame rate. Does not impact Listen Server (use ClientFixedFPS setting). This is the target frame rate, e.g, "20" for 20fps, which will result in 1/20 second tick steps.

### ClientFixedFPS
- **类型**: `TArray<int>`
- **描述**: If > 0, Tick clients at a fixed frame rate. Each client instance will map to an element in the list, wrapping around if num clients exceeds size of list. Includes Listen Server. This is the target frame rate, e.g, "20" for 20fps, which will result in 1/20 second tick steps.

### NetworkEmulationSettings
- **类型**: `FLevelEditorPlayNetworkEmulationSettings`
- **描述**: Customizable settings allowing to emulate latency and packetloss for game network transmissions

### bPreferToStreamLevelsInPIE
- **类型**: `bool`

### CenterNewWindow
- **类型**: `bool`

### PIEAlwaysOnTop
- **类型**: `bool`

### DisableStandaloneSound
- **类型**: `bool`

