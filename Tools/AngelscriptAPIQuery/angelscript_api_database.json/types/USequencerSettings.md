# USequencerSettings

**继承自**: `UObject`

Serializable options for sequencer.

## 属性

### AutoChangeMode
- **类型**: `EAutoChangeMode`
- **描述**: The auto change mode (auto-key, auto-track or none).

### AllowEditsMode
- **类型**: `EAllowEditsMode`
- **描述**: Allow edits mode.

### KeyGroupMode
- **类型**: `EKeyGroupMode`
- **描述**: Key group mode.

### KeyInterpolation
- **类型**: `EMovieSceneKeyInterpolation`
- **描述**: The interpolation type for newly created keyframes

### bAutoSetTrackDefaults
- **类型**: `bool`
- **描述**: When setting keys on properties and transforms automatically update the track default values used when there are no keys.

### SpawnPosition
- **类型**: `ESequencerSpawnPosition`
- **描述**: The default location of a spawnable when it is first dragged into the viewport from the content browser.

### bCreateSpawnableCameras
- **类型**: `bool`
- **描述**: Enable or disable creating of spawnable cameras whenever cameras are created.

### bShowRangeSlider
- **类型**: `bool`
- **描述**: Show the in/out range in the timeline with respect to the start/end range.

### bIsSnapEnabled
- **类型**: `bool`
- **描述**: Enable or disable snapping in the timeline.

### bSnapKeyTimesToInterval
- **类型**: `bool`
- **描述**: Enable or disable snapping keys to the time snapping interval.

### bSnapKeyTimesToKeys
- **类型**: `bool`
- **描述**: Enable or disable snapping keys to other keys.

### bSnapSectionTimesToInterval
- **类型**: `bool`
- **描述**: Enable or disable snapping sections to the time snapping interval.

### bSnapSectionTimesToSections
- **类型**: `bool`
- **描述**: Enable or disable snapping sections to other sections.

### bSnapKeysAndSectionsToPlayRange
- **类型**: `bool`
- **描述**: Enable or disable keeping keys and sections in the playback range.

### bSnapPlayTimeToKeys
- **类型**: `bool`
- **描述**: Enable or disable snapping the playhead to keys while scrubbing.

### bSnapPlayTimeToSections
- **类型**: `bool`
- **描述**: Enable or disable snapping the playhead to section bounds while scrubbing.

### bSnapPlayTimeToMarkers
- **类型**: `bool`
- **描述**: Enable or disable snapping the playhead to markers while scrubbing.

### bSnapPlayTimeToInterval
- **类型**: `bool`
- **描述**: Enable or disable snapping the playhead to the time snapping interval while scrubbing.

### bSnapPlayTimeToPressedKey
- **类型**: `bool`
- **描述**: Enable or disable snapping the playhead to the pressed key.

### bSnapPlayTimeToDraggedKey
- **类型**: `bool`
- **描述**: Enable or disable snapping the playhead to the dragged key.

### bSnapCurveValueToInterval
- **类型**: `bool`
- **描述**: Enable or disable snapping the curve value to the curve value interval.

### bShowSelectedNodesOnly
- **类型**: `bool`
- **描述**: Only show selected nodes in the tree view.

### bRewindOnRecord
- **类型**: `bool`
- **描述**: Defines whether to jump back to the start of the sequence when a recording is started

### bLeftMouseDragDoesMarquee
- **类型**: `bool`
- **描述**: Defines whether left mouse drag does marquee select instead of camera orbit

### ZoomPosition
- **类型**: `ESequencerZoomPosition`
- **描述**: Whether to zoom in on the current position or the current time in the timeline.

### bAutoScrollEnabled
- **类型**: `bool`
- **描述**: Enable or disable auto scroll in the timeline when playing.

### bLinkCurveEditorTimeRange
- **类型**: `bool`
- **描述**: Enable or disable linking the curve editor time range to the sequencer timeline's time range.

### bSynchronizeCurveEditorSelection
- **类型**: `bool`
- **描述**: When enabled, changing the sequencer tree selection will also select the relevant nodes in the curve editor tree if possible.

### bIsolateCurveEditorToSelection
- **类型**: `bool`
- **描述**: When enabled, changing the sequencer tree selection will isolate (auto-filter) the selected nodes in the curve editor.

### bResetPlayheadWhenNavigating
- **类型**: `bool`
- **描述**: Enable or disable resetting the playhead when navigating in and out of subsequences.

### bKeepCursorInPlayRangeWhileScrubbing
- **类型**: `bool`
- **描述**: Enable or disable keeping the playhead in the current playback range while scrubbing.

### bKeepPlayRangeInSectionBounds
- **类型**: `bool`
- **描述**: Enable or disable keeping the playback range constrained to the section bounds.

### ZeroPadFrames
- **类型**: `uint8`
- **描述**: The number of zeros to pad the frame numbers by.

### JumpFrameIncrement
- **类型**: `FFrameNumber`
- **描述**: The number of frames to jump by when jumping forward or backwards.

### bShowLayerBars
- **类型**: `bool`
- **描述**: Enable or disable the layer bars to edit keyframes in bulk.

### bShowKeyBars
- **类型**: `bool`
- **描述**: Enable or disable key bar connections.

### bInfiniteKeyAreas
- **类型**: `bool`
- **描述**: Enable or disable setting key area sections as infinite by default.

### bShowChannelColors
- **类型**: `bool`
- **描述**: Enable or disable displaying channel bar colors for the key bars.

### bShowInfoButton
- **类型**: `bool`
- **描述**: Enable or disable displaying the info button in the playback controls.

### bShowTickLines
- **类型**: `bool`
- **描述**: Enable or disable displaying the tick lines.

### bShowSequencerToolbar
- **类型**: `bool`
- **描述**: Enable or disable displaying the sequencer toolbar.

### KeyAreaCurveExtents
- **类型**: `FString`
- **描述**: The key area curve extents, stored per channel name

### KeyAreaHeightWithCurves
- **类型**: `float32`
- **描述**: The key area height when showing curves

### ReduceKeysTolerance
- **类型**: `float32`
- **描述**: The tolerance to use when reducing keys

### bDeleteKeysWhenTrimming
- **类型**: `bool`
- **描述**: Enable or disable deleting keys that fall beyond the section range when trimming.

### bDisableSectionsAfterBaking
- **类型**: `bool`
- **描述**: Whether to disable sections after baking as opposed to deleting.

### SectionColorTints
- **类型**: `TArray<FColor>`
- **描述**: Section color tints

### bCleanPlaybackMode
- **类型**: `bool`
- **描述**: When enabled, sequencer will playback in clean mode (game view, hide viewport UI)

### bActivateRealtimeViewports
- **类型**: `bool`
- **描述**: When enabled, sequencer will activate 'Realtime' in viewports

### bEvaluateSubSequencesInIsolation
- **类型**: `bool`
- **描述**: When enabled, entering a sub sequence will evaluate that sub sequence in isolation, rather than from the root sequence

### bRerunConstructionScripts
- **类型**: `bool`
- **描述**: When enabled, construction scripts will be rerun on bound actors for every frame

### bShowDebugVisualization
- **类型**: `bool`
- **描述**: Enable or disable showing of debug visualization.

### bVisualizePreAndPostRoll
- **类型**: `bool`
- **描述**: Enable or disable showing of pre and post roll visualization.

### bCompileDirectorOnEvaluate
- **类型**: `bool`
- **描述**: Whether to recompile the director blueprint when the sequence is evaluated (if one exists)

### TrajectoryPathCap
- **类型**: `uint`
- **描述**: Specifies the maximum number of keys to draw when rendering trajectories in viewports

### FrameNumberDisplayFormat
- **类型**: `EFrameNumberDisplayFormats`
- **描述**: What format do we display time in to the user?

### MovieRendererName
- **类型**: `FString`
- **描述**: Which movie renderer to use

### bAutoExpandNodesOnSelection
- **类型**: `bool`
- **描述**: Whether to expand the sequencer tree view when a child element is selected (from outside of the tree view).

### bRestoreOriginalViewportOnCameraCutUnlock
- **类型**: `bool`
- **描述**: Whether unlocking a camera cut track should return the viewport to its original location, or keep it where the
camera cut was.
WARNING: Disabling this will make previewing camera cut blends useless, since it will blend to the same position.

### TreeViewWidth
- **类型**: `float32`
- **描述**: The tree view width percentage

### ViewDensity
- **类型**: `FName`

### TrackFilters
- **类型**: `TArray<FString>`
- **描述**: The track filters that are enabled

### ColumnVisibilitySettings
- **类型**: `TArray<FColumnVisibilitySetting>`
- **描述**: List of all columns and their visibility, in the order to be displayed in the outliner view

