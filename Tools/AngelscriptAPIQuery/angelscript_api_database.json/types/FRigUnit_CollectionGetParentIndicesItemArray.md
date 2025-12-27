# FRigUnit_CollectionGetParentIndicesItemArray

Returns an array of relative parent indices for each item. Several options here
a) If an item has multiple parents the major parent (based on the weights) will be returned.
b) If an item has a parent that's not part of the collection INDEX_NONE will be returned.
c) If an item has a parent that's not part of the collection, but a grand parent is we'll use that index instead.

## 属性

### Items
- **类型**: `TArray<FRigElementKey>`

### ParentIndices
- **类型**: `TArray<int>`

## 方法

### opAssign
```angelscript
FRigUnit_CollectionGetParentIndicesItemArray& opAssign(FRigUnit_CollectionGetParentIndicesItemArray Other)
```

