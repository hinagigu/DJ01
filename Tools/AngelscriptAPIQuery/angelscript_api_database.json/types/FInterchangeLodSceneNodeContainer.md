# FInterchangeLodSceneNodeContainer

* This container exists only because UPROPERTY cannot support nested container. See FInterchangeMeshInstance.

## 属性

### SceneNodes
- **类型**: `TArray<TObjectPtr<UInterchangeSceneNode>>`
- **描述**: Each scene node here represents a mesh scene node. If it represents a LOD group, there may be more then one mesh scene node for a specific LOD index.

## 方法

### opAssign
```angelscript
FInterchangeLodSceneNodeContainer& opAssign(FInterchangeLodSceneNodeContainer Other)
```

