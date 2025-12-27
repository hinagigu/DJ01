# ULiveLinkVirtualSubject

**继承自**: `UObject`

A Virtual subject is made up of one or more real subjects from a source

## 属性

### Subjects
- **类型**: `TArray<FLiveLinkSubjectName>`
- **描述**: Names of the real subjects to combine into a virtual subject

### FrameTranslators
- **类型**: `TArray<TObjectPtr<ULiveLinkFrameTranslator>>`
- **描述**: List of available translator the subject can use.

### bRebroadcastSubject
- **类型**: `bool`
- **描述**: If enabled, rebroadcast this subject

