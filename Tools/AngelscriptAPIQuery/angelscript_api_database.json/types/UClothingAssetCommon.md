# UClothingAssetCommon

**继承自**: `UClothingAssetBase`

Implementation of non-solver specific, but common Engine related functionality.

Solver specific implementations may wish to override this class to construct
their own default instances of child classes, such as \c ClothSimConfig and
\c CustomData, as well as override the \c AddNewLod() factory to build their
own implementation of \c UClothLODDataBase.

## 属性

### PhysicsAsset
- **类型**: `UPhysicsAsset`
- **描述**: The physics asset to extract collisions from when building a simulation.

### ClothConfigs
- **类型**: `TMap<FName,TObjectPtr<UClothConfigBase>>`
- **描述**: Simulation specific cloth parameters.
Use GetClothConfig() to retrieve the correct parameters/config type for the desired cloth simulation system.

