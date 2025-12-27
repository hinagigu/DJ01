# FMovieSceneSequenceTickInterval

Structure defining a concrete tick interval for a Sequencer based evaluation

## 属性

### TickIntervalSeconds
- **类型**: `float32`
- **描述**: Defines the rate at which the sequence should update, in seconds

### EvaluationBudgetMicroseconds
- **类型**: `float32`
- **描述**: Defines an approximate budget for evaluation of this sequence (and any other sequences with the same tick interval)

### bTickWhenPaused
- **类型**: `bool`
- **描述**: When true, the sequence will continue to tick and progress even when the world is paused

### bAllowRounding
- **类型**: `bool`
- **描述**: When true, allow the sequence to be grouped with other sequences based on Sequencer.TickIntervalGroupingResolutionMs. Otherwise the interval will be used precisely.

## 方法

### opAssign
```angelscript
FMovieSceneSequenceTickInterval& opAssign(FMovieSceneSequenceTickInterval Other)
```

