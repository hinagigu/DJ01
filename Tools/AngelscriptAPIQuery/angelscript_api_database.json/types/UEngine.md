# UEngine

**继承自**: `UObject`

Abstract base class of all Engine classes, responsible for management of systems critical to editor or game systems.
Also defines default classes for certain engine systems.

## 属性

### TinyFontName
- **类型**: `FSoftObjectPath`
- **描述**: Sets the font used for the smallest engine text

### SmallFontName
- **类型**: `FSoftObjectPath`
- **描述**: Sets the font used for small engine text, used for most debug displays

### MediumFontName
- **类型**: `FSoftObjectPath`
- **描述**: Sets the font used for medium engine text

### LargeFontName
- **类型**: `FSoftObjectPath`
- **描述**: Sets the font used for large engine text

### SubtitleFontName
- **类型**: `FSoftObjectPath`
- **描述**: Sets the font used by the default Subtitle Manager

### AdditionalFontNames
- **类型**: `TArray<FString>`
- **描述**: Sets additional fonts that will be loaded at startup and available using GetAdditionalFont.

### ConsoleClassName
- **类型**: `FSoftClassPath`
- **描述**: Sets the class to use for the game console summoned with ~

### GameViewportClientClassName
- **类型**: `FSoftClassPath`
- **描述**: Sets the class to use for the game viewport client, which can be overridden to change game-specific input and display behavior.

### LocalPlayerClassName
- **类型**: `FSoftClassPath`
- **描述**: Sets the class to use for local players, which can be overridden to store game-specific information for a local player.

### WorldSettingsClassName
- **类型**: `FSoftClassPath`
- **描述**: Sets the class to use for WorldSettings, which can be overridden to store game-specific information on map/world.

### PhysicsCollisionHandlerClassName
- **类型**: `FSoftClassPath`
- **描述**: Sets the PhysicsCollisionHandler class to use by default, which can be overridden to change game-specific behavior when objects collide using physics.

### GameUserSettingsClassName
- **类型**: `FSoftClassPath`
- **描述**: Sets the GameUserSettings class, which can be overridden to support game-specific options for Graphics/Sound/Gameplay.

### LevelScriptActorClassName
- **类型**: `FSoftClassPath`
- **描述**: Sets the Level Script Actor class, which can be overridden to allow game-specific behavior in per-map blueprint scripting

### DefaultBlueprintBaseClassName
- **类型**: `FSoftClassPath`
- **描述**: Sets the base class to use for new blueprints created in the editor, configurable on a per-game basis

### GameSingletonClassName
- **类型**: `FSoftClassPath`
- **描述**: Sets the class for a global object spawned at startup to handle game-specific data. If empty, it will not spawn one

### AssetManagerClassName
- **类型**: `FSoftClassPath`
- **描述**: Sets the class to spawn as the global AssetManager, configurable per game. If empty, it will not spawn one

### PreviewShadowsIndicatorMaterialName
- **类型**: `FSoftObjectPath`
- **描述**: Path of the material that renders a message about preview shadows being used.

### DefaultDestructiblePhysMaterialName
- **类型**: `FSoftObjectPath`
- **描述**: Path of the PhysicalMaterial to use if none is defined for a particular object.

### NearClipPlane
- **类型**: `float32`
- **描述**: The distance of the camera's near clipping plane.

### MaximumLoopIterationCount
- **类型**: `int`
- **描述**: Script maximum loop iteration count used as a threshold to warn users about script execution runaway

### FixedFrameRate
- **类型**: `float32`
- **描述**: The fixed framerate to use.

### SmoothedFrameRateRange
- **类型**: `FFloatRange`
- **描述**: Range of framerates in which smoothing will kick in

### CustomTimeStepClassName
- **类型**: `FSoftClassPath`
- **描述**: Override how the Engine process the Framerate/Timestep.
This class will be responsible of updating the application Time and DeltaTime.
Can be used to synchronize the engine with another process (gen-lock).

### TimecodeProviderClassName
- **类型**: `FSoftClassPath`
- **描述**: Set TimecodeProvider when the engine is started.

### bGenerateDefaultTimecode
- **类型**: `bool`
- **描述**: Generate a default timecode from the computer clock when there is no timecode provider.
On desktop, the system time will be used and will behave as if a USystemTimecodeProvider was set.
On console, the high performance clock will be used. That may introduce drift over time.
If you wish to use the system time on console, set the timecode provider to USystemeTimecodeProvider.

### GenerateDefaultTimecodeFrameRate
- **类型**: `FFrameRate`
- **描述**: When generating a default timecode (bGenerateDefaultTimecode is true and no timecode provider is set) at which frame rate it should be generated (number of frames).

### GenerateDefaultTimecodeFrameDelay
- **类型**: `float32`
- **描述**: Number of frames to subtract from generated default timecode.

### GameScreenshotSaveDirectory
- **类型**: `FDirectoryPath`
- **描述**: The save directory for newly created screenshots

### UseStaticMeshMinLODPerQualityLevels
- **类型**: `bool`

### UseSkeletalMeshMinLODPerQualityLevels
- **类型**: `bool`

### UseGrassVarityPerQualityLevels
- **类型**: `bool`

### MinDesiredFrameRate
- **类型**: `float32`
- **描述**: Minimum desired framerate setting, below this frame rate visual detail may be lowered

### bSubtitlesEnabled
- **类型**: `bool`

### bSubtitlesForcedOff
- **类型**: `bool`

### bCanBlueprintsTickByDefault
- **类型**: `bool`

### bOptimizeAnimBlueprintMemberVariableAccess
- **类型**: `bool`

### bAllowMultiThreadedAnimationUpdate
- **类型**: `bool`

### bSmoothFrameRate
- **类型**: `bool`

### bUseFixedFrameRate
- **类型**: `bool`

