# UProceduralFoliageSpawner

**继承自**: `UObject`

## 属性

### RandomSeed
- **类型**: `int`

### TileSize
- **类型**: `float32`

### NumUniqueTiles
- **类型**: `int`

### MinimumQuadTreeSize
- **类型**: `float32`

### FoliageTypes
- **类型**: `TArray<FFoliageTypeObject>`
- **描述**: The types of foliage to procedurally spawn.

### bUseOverrideFoliageTerrainMaterials
- **类型**: `bool`
- **描述**: If checked, will override the default behavior of using the global foliage material list and instead use the Override Foliage Terrain Materials defined here.
If the override is used, you must manually provide ALL materials this procedural foliage spawner should spawn on top of.

### OverrideFoliageTerrainMaterials
- **类型**: `TArray<TSoftObjectPtr<UMaterialInterface>>`
- **描述**: Procedural foliage will only spawn on materials specified here. These are only used if 'Use Override Foliage Terrain Materials' is checked.

## 方法

### Simulate
```angelscript
void Simulate(int NumSteps)
```

