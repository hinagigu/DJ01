# UGameFeatureAction_AddChunkOverride

**继承自**: `UGameFeatureAction`

Used to cook assets from a GFP into a specified chunkId.
This can be useful when individually cooking GFPs for iteration or splitting up a packaged
game into smaller downloadable chunks.

## 属性

### bShouldOverrideChunk
- **类型**: `bool`
- **描述**: Should this GFP have their packages cooked into the specified ChunkId

### ChunkId
- **类型**: `int`
- **描述**: What ChunkId to place the packages inside for this particular GFP.

