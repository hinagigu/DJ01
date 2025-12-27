# __UAnimPoseExtensions

## 方法

### EvaluateAnimationBlueprintWithInputPose
```angelscript
void EvaluateAnimationBlueprintWithInputPose(FAnimPose InputPose, USkeletalMesh TargetSkeletalMesh, UAnimBlueprint AnimationBlueprint, FAnimPose& OutPose)
```
Evaluates an Animation Blueprint instance, using the provided Anim Pose and its Input Pose value, generating a valid Anim Pose using the result. Warning this function may cause performance issues.

@param        InputPose                               Anim Pose used to populate the input pose node value inside of the Animation Blueprint
@param        TargetSkeletalMesh              USkeletalMesh object used as the target skeletal mesh, should have same USkeleton as InputPose and Animation Blueprint
@param        AnimationBlueprint              Animation Blueprint to generate an AnimInstance with, used to evaluate the output Anim Pose
@param        OutPose                                 Anim pose to hold the data from evaluating the Animation Blueprint instance

### GetAnimPoseAtFrame
```angelscript
void GetAnimPoseAtFrame(const UAnimSequenceBase AnimationSequenceBase, int FrameIndex, FAnimPoseEvaluationOptions EvaluationOptions, FAnimPose& Pose)
```
Evaluates an Animation Sequence Base to generate a valid Anim Pose instance

@param        AnimationSequenceBase   Animation sequence base to evaluate the pose from
@param        FrameIndex                              Exact frame at which the pose should be evaluated
@param        EvaluationOptions               Options determining the way the pose should be evaluated
@param        Pose                                    Anim Pose to hold the evaluated data

### GetAnimPoseAtTime
```angelscript
void GetAnimPoseAtTime(const UAnimSequenceBase AnimationSequenceBase, float Time, FAnimPoseEvaluationOptions EvaluationOptions, FAnimPose& Pose)
```
Evaluates an Animation Sequence Base to generate a valid Anim Pose instance

@param        AnimationSequenceBase   Animation sequence base to evaluate the pose from
@param        Time                                    Time at which the pose should be evaluated
@param        EvaluationOptions               Options determining the way the pose should be evaluated
@param        Pose                                    Anim Pose to hold the evaluated data

### GetBoneNames
```angelscript
void GetBoneNames(FAnimPose Pose, TArray<FName>& Bones)
```
Returns an array of bone names contained by the pose

@param        Pose    Anim Pose to retrieve the names from
@param        Bones   Array to be populated with the bone names

### GetBonePose
```angelscript
FTransform GetBonePose(FAnimPose Pose, FName BoneName, EAnimPoseSpaces Space)
```
Retrieves the transform for the provided bone name from a pose

@param        Pose            Anim Pose to retrieve the transform from
@param        BoneName        Name of the bone to retrieve
@param        Space           Space in which the transform should be retrieved

@return       Transform in requested space for bone if found, otherwise return identity transform

### GetCurveNames
```angelscript
void GetCurveNames(FAnimPose Pose, TArray<FName>& Curves)
```
Returns an array of curve names contained by the pose

@param        Pose    Anim Pose to retrieve the names from
@param        Curves  Array to be populated with the curve names

### GetCurveWeight
```angelscript
float32 GetCurveWeight(FAnimPose Pose, FName CurveName)
```
Returns the weight of an evaluated curve - if found

@param   Pose            Anim Pose to retrieve the value from
@param   CurveName       Curve to retrieve the weight value for

@return  Curve weight value, if found - 0.f otherwise

### GetRefBonePose
```angelscript
FTransform GetRefBonePose(FAnimPose Pose, FName BoneName, EAnimPoseSpaces Space)
```
Retrieves the reference pose transform for the provided bone name

@param        Pose            Anim Pose to retrieve the transform from
@param        BoneName        Name of the bone to retrieve
@param        Space           Space in which the transform should be retrieved

@return       Transform in requested space for bone if found, otherwise return identity transform

### GetReferencePose
```angelscript
void GetReferencePose(USkeleton Skeleton, FAnimPose& OutPose)
```
Populates an Anim Pose with the reference poses stored for the provided USkeleton

@param        Skeleton                                USkeleton object to retrieve the reference pose from
@param        OutPose                                 Anim pose to hold the reference pose

### GetRefPoseRelativeTransform
```angelscript
FTransform GetRefPoseRelativeTransform(FAnimPose Pose, FName FromBoneName, FName ToBoneName, EAnimPoseSpaces Space)
```
Retrieves the relative transform for the reference pose between the two provided bone names

@param        Pose                    Anim Pose to retrieve the transform from
@param        FromBoneName    Name of the bone to retrieve the transform relative from
@param        ToBoneName              Name of the bone to retrieve the transform relative to
@param        Space                   Space in which the transform should be retrieved

@return       Relative transform in requested space for bone if found, otherwise return identity transform

### GetRelativeToRefPoseTransform
```angelscript
FTransform GetRelativeToRefPoseTransform(FAnimPose Pose, FName BoneName, EAnimPoseSpaces Space)
```
Retrieves the relative transform between reference and animated bone transform

@param        Pose                    Anim Pose to retrieve the transform from
@param        BoneName                Name of the bone to retrieve the relative transform for
@param        Space                   Space in which the transform should be retrieved

@return       Relative transform in requested space for bone if found, otherwise return identity transform

### GetRelativeTransform
```angelscript
FTransform GetRelativeTransform(FAnimPose Pose, FName FromBoneName, FName ToBoneName, EAnimPoseSpaces Space)
```
Retrieves the relative transform between the two provided bone names

@param        Pose                    Anim Pose to retrieve the transform from
@param        FromBoneName    Name of the bone to retrieve the transform relative from
@param        ToBoneName              Name of the bone to retrieve the transform relative to
@param        Space                   Space in which the transform should be retrieved

@return       Relative transform in requested space for bone if found, otherwise return identity transform

### GetSocketNames
```angelscript
void GetSocketNames(FAnimPose Pose, TArray<FName>& Sockets)
```
Returns an array of socket names contained by the pose

@param        Pose    Anim Pose to retrieve the names from
@param        Sockets Array to be populated with the socket names

### GetSocketPose
```angelscript
FTransform GetSocketPose(FAnimPose Pose, FName SocketName, EAnimPoseSpaces Space)
```
Retrieves the transform for the provided socket name from a pose

@param        Pose            Anim Pose to retrieve the transform from
@param        SocketName      Name of the socket to retrieve
@param        Space           Space in which the transform should be retrieved

@return       Transform in requested space for bone if found, otherwise return identity transform

### IsValid
```angelscript
bool IsValid(FAnimPose Pose)
```
Returns whether the Anim Pose contains valid data

@param        Pose    Anim Pose to validate

@return       Result of the validation

### SetBonePose
```angelscript
void SetBonePose(FAnimPose& Pose, FTransform Transform, FName BoneName, EAnimPoseSpaces Space)
```
Sets the transform for the provided bone name for a pose

@param        Pose            Anim Pose to set transform in
@param        Transform       Transform to set the bone to
@param        BoneName        Name of the bone to set
@param        Space           Space in which the transform should be set

### StaticClass
```angelscript
UClass StaticClass()
```

