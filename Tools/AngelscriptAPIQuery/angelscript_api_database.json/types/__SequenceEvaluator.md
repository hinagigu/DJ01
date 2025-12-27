# __SequenceEvaluator

## 方法

### ConvertToSequenceEvaluator
```angelscript
FSequenceEvaluatorReference ConvertToSequenceEvaluator(FAnimNodeReference Node, EAnimNodeReferenceConversionResult& Result)
```
Get a sequence evaluator context from an anim node context

### ConvertToSequenceEvaluatorPure
```angelscript
void ConvertToSequenceEvaluatorPure(FAnimNodeReference Node, FSequenceEvaluatorReference& SequenceEvaluator, bool& Result)
```
Get a sequence evaluator context from an anim node context (pure)

### GetAccumulatedTime
```angelscript
float32 GetAccumulatedTime(FSequenceEvaluatorReference SequenceEvaluator)
```
Gets the current accumulated time of the sequence evaluator

### GetSequence
```angelscript
UAnimSequenceBase GetSequence(FSequenceEvaluatorReference SequenceEvaluator)
```
Gets the current sequence of the sequence evaluator

### SetExplicitFrame
```angelscript
FSequenceEvaluatorReference SetExplicitFrame(FSequenceEvaluatorReference SequenceEvaluator, int Frame)
```
Set the current accumulated time, using a frame number, of the sequence evaluator

### SetExplicitTime
```angelscript
FSequenceEvaluatorReference SetExplicitTime(FSequenceEvaluatorReference SequenceEvaluator, float32 Time)
```
Set the current accumulated time of the sequence evaluator

### SetSequence
```angelscript
FSequenceEvaluatorReference SetSequence(FSequenceEvaluatorReference SequenceEvaluator, UAnimSequenceBase Sequence)
```
Set the current sequence of the sequence evaluator

