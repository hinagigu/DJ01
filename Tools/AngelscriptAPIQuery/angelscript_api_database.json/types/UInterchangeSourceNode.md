# UInterchangeSourceNode

**继承自**: `UInterchangeBaseNode`

This class allows a translator to add general source data that describes the whole source. Pipelines can use this information.

## 方法

### GetCustomAnimatedTimeEnd
```angelscript
bool GetCustomAnimatedTimeEnd(float& AttributeValue)
```
Query the end of the source animated time.

### GetCustomAnimatedTimeStart
```angelscript
bool GetCustomAnimatedTimeStart(float& AttributeValue)
```
Query the start of the source animated time.

### GetCustomImportUnusedMaterial
```angelscript
bool GetCustomImportUnusedMaterial(bool& AttributeValue)
```
Query whether to import materials that aren't used.

### GetCustomSourceFrameRateDenominator
```angelscript
bool GetCustomSourceFrameRateDenominator(int& AttributeValue)
```
Query the source frame rate denominator.

### GetCustomSourceFrameRateNumerator
```angelscript
bool GetCustomSourceFrameRateNumerator(int& AttributeValue)
```
Query the source frame rate numerator.

### GetCustomSourceTimelineEnd
```angelscript
bool GetCustomSourceTimelineEnd(float& AttributeValue)
```
Query the end of the source timeline.

### GetCustomSourceTimelineStart
```angelscript
bool GetCustomSourceTimelineStart(float& AttributeValue)
```
Query the start of the source timeline.

### InitializeSourceNode
```angelscript
void InitializeSourceNode(FString UniqueID, FString DisplayLabel)
```
Initialize the base data of the node.
@param UniqueID - The unique ID for this node.
@param DisplayLabel - The name of the node.

### SetCustomAnimatedTimeEnd
```angelscript
bool SetCustomAnimatedTimeEnd(float AttributeValue)
```
Set the end of the source animated time.

### SetCustomAnimatedTimeStart
```angelscript
bool SetCustomAnimatedTimeStart(float AttributeValue)
```
Set the start of the source animated time.

### SetCustomImportUnusedMaterial
```angelscript
bool SetCustomImportUnusedMaterial(bool AttributeValue)
```
Set whether to import materials that aren't used.

### SetCustomSourceFrameRateDenominator
```angelscript
bool SetCustomSourceFrameRateDenominator(int AttributeValue)
```
Set the source frame rate denominator.

### SetCustomSourceFrameRateNumerator
```angelscript
bool SetCustomSourceFrameRateNumerator(int AttributeValue)
```
Set the source frame rate numerator.

### SetCustomSourceTimelineEnd
```angelscript
bool SetCustomSourceTimelineEnd(float AttributeValue)
```
Set the end of the source timeline.

### SetCustomSourceTimelineStart
```angelscript
bool SetCustomSourceTimelineStart(float AttributeValue)
```
Set the start of the source timeline.

