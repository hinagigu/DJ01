# __MotionExtractorUtility

## 方法

### GenerateCurveName
```angelscript
FName GenerateCurveName(FName BoneName, EMotionExtractor_MotionType MotionType, EMotionExtractor_Axis Axis)
```
Generates a curve name based on input settings.

@param BoneName                          The name of the bone
@param MotionType            What type of motion this curve represents (translation, rotation, speed, etc.)
@param Axis                              Which axis/axes the motion for this curve was extracted from

### GetDesiredValue
```angelscript
float32 GetDesiredValue(FTransform BoneTransform, FTransform LastBoneTransform, float32 DeltaTime, EMotionExtractor_MotionType MotionType, EMotionExtractor_Axis Axis)
```
Returns the desired value from the extracted poses based on input settings.

@param BoneTransform         Current frame's bone transform
@param LastBoneTransform     Last frame's bone transform. Unused when not calculating speeds.
@param DeltaTime                         Time step used between current and last bone transforms. Unused when not calculating speeds.
@param MotionType            What type of motion to extract (translation, rotation, speed, etc.)
@param Axis                              Which axis/axes to extract motion from

### GetMovingRangesFromRootMotion
```angelscript
TArray<FVector2D> GetMovingRangesFromRootMotion(const UAnimSequence AnimSequence, float32 StopSpeedThreshold, float32 SampleRate)
```
Returns the ranges (X/Start to Y/End) in the specified animation sequence where the animation is considered moving.

@param AnimSequence                   Anim sequence to check
@param StopSpeedThreshold             Root motion speed over which the animation is considered moving.
@param SampleRate                             Sample rate of the animation. It's recommended to use high values if the animation has very sudden direction changes.

### GetStoppedRangesFromRootMotion
```angelscript
TArray<FVector2D> GetStoppedRangesFromRootMotion(const UAnimSequence AnimSequence, float32 StopSpeedThreshold, float32 SampleRate)
```
Returns the ranges (X/Start to Y/End) in the specified animation sequence where the animation is considered stopped.

@param AnimSequence                   Anim sequence to check
@param StopSpeedThreshold             Root motion speed under which the animation is considered stopped.
@param SampleRate                             Sample rate of the animation. It's recommended to use high values if the animation has very sudden direction changes.

