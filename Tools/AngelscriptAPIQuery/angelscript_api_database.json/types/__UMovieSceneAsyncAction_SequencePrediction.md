# __UMovieSceneAsyncAction_SequencePrediction

## 方法

### PredictLocalTransformAtFrame
```angelscript
UMovieSceneAsyncAction_SequencePrediction PredictLocalTransformAtFrame(UMovieSceneSequencePlayer Player, USceneComponent TargetComponent, FFrameTime FrameTime)
```
Initiate an asynchronous prediction for the specified component's local transform at a specific time in a sequence
Changes in attachment between the sequence's current time, and the predicted time are not accounted for
Calling this function on a stopped sequence player is undefined.

@param Player          An active, currently playing sequence player to use for predicting the transform
@param TargetComponent The component to predict a world transform for
@param FrameTime       The frame time to predict at in the sequence's display rate
@return An asynchronous prediction object that contains Result and Failure delegates

### PredictLocalTransformAtTime
```angelscript
UMovieSceneAsyncAction_SequencePrediction PredictLocalTransformAtTime(UMovieSceneSequencePlayer Player, USceneComponent TargetComponent, float32 TimeInSeconds)
```
Initiate an asynchronous prediction for the specified component's local transform at a specific time in a sequence
Changes in attachment between the sequence's current time, and the predicted time are not accounted for
Calling this function on a stopped sequence player is undefined.

@param Player          An active, currently playing sequence player to use for predicting the transform
@param TargetComponent The component to predict a world transform for
@param TimeInSeconds   The time within the sequence to predict the transform at
@return An asynchronous prediction object that contains Result and Failure delegates

### PredictWorldTransformAtFrame
```angelscript
UMovieSceneAsyncAction_SequencePrediction PredictWorldTransformAtFrame(UMovieSceneSequencePlayer Player, USceneComponent TargetComponent, FFrameTime FrameTime)
```
Initiate an asynchronous prediction for the specified component's world transform at a specific time in a sequence
Changes in attachment between the sequence's current time, and the predicted time are not accounted for
Calling this function on a stopped sequence player is undefined.

@param Player          An active, currently playing sequence player to use for predicting the transform
@param TargetComponent The component to predict a world transform for
@param FrameTime       The frame time to predict at in the sequence's display rate
@return An asynchronous prediction object that contains Result and Failure delegates

### PredictWorldTransformAtTime
```angelscript
UMovieSceneAsyncAction_SequencePrediction PredictWorldTransformAtTime(UMovieSceneSequencePlayer Player, USceneComponent TargetComponent, float32 TimeInSeconds)
```
Initiate an asynchronous prediction for the specified component's world transform at a specific time in a sequence
Changes in attachment between the sequence's current time, and the predicted time are not accounted for
Calling this function on a stopped sequence player is undefined.

@param Player          An active, currently playing sequence player to use for predicting the transform
@param TargetComponent The component to predict a world transform for
@param TimeInSeconds   The time within the sequence to predict the transform at
@return An asynchronous prediction object that contains Result and Failure delegates

### StaticClass
```angelscript
UClass StaticClass()
```

