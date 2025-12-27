# UMoviePlayerSettings

**继承自**: `UObject`

Implements the settings for the Windows target platform.

## 属性

### bWaitForMoviesToComplete
- **类型**: `bool`
- **描述**: If enabled, The game waits for startup movies to complete even if loading has finished.

### bMoviesAreSkippable
- **类型**: `bool`
- **描述**: If enabled, Startup movies can be skipped by the user when a mouse button is pressed.

### StartupMovies
- **类型**: `TArray<FString>`
- **描述**: Movies to play on startup. Note that these must be in your game's Game/Content/Movies directory.

