# UPostBufferUpdate

**继承自**: `UWidget`

Widget that when drawn, will trigger the slate post buffer to update. Does not draw anything itself.
This allows for you to perform layered UI / sampling effects with the GetSlatePost material functions,
by placing this widget after UI you would like to be processed / sampled is drawn.

* No Children

## 属性

### bPerformDefaultPostBufferUpdate
- **类型**: `bool`

### BuffersToUpdate
- **类型**: `TArray<ESlatePostRT>`
- **描述**: Buffers that we should update, all of these buffers will be affected by 'bPerformDefaultPostBufferUpdate' if disabled

