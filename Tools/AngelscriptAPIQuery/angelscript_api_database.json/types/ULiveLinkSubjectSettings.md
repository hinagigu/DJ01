# ULiveLinkSubjectSettings

**继承自**: `UObject`

Base class for live link subject settings

## 属性

### PreProcessors
- **类型**: `TArray<TObjectPtr<ULiveLinkFramePreProcessor>>`
- **描述**: List of available preprocessor the subject will use.

### InterpolationProcessor
- **类型**: `ULiveLinkFrameInterpolationProcessor`
- **描述**: The interpolation processor the subject will use.

### Translators
- **类型**: `TArray<TObjectPtr<ULiveLinkFrameTranslator>>`
- **描述**: List of available translator the subject can use.

### bRebroadcastSubject
- **类型**: `bool`
- **描述**: If enabled, rebroadcast this subject

