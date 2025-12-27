# FMovieSceneEvent

## 属性

### PayloadVariables
- **类型**: `TMap<FName,FMovieSceneEventPayloadVariable>`
- **描述**: Array of payload variables to be added to the generated function

### BoundObjectPinName
- **类型**: `FName`

### WeakEndpoint
- **类型**: `TWeakObjectPtr<UObject>`
- **描述**: Serialized weak pointer to the function entry (UK2Node_FunctionEntry) or custom event node (UK2Node_CustomEvent) within the blueprint graph for this event. Stored as an editor-only UObject so UHT can parse it when building for non-editor.

## 方法

### opAssign
```angelscript
FMovieSceneEvent& opAssign(FMovieSceneEvent Other)
```

