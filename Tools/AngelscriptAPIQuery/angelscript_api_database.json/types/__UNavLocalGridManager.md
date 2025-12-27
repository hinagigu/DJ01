# __UNavLocalGridManager

## 方法

### AddLocalNavigationGridForBox
```angelscript
int AddLocalNavigationGridForBox(FVector Location, FVector Extent, FRotator Rotation, int Radius2D, float32 Height, bool bRebuildGrids)
```

### AddLocalNavigationGridForCapsule
```angelscript
int AddLocalNavigationGridForCapsule(FVector Location, float32 CapsuleRadius, float32 CapsuleHalfHeight, int Radius2D, float32 Height, bool bRebuildGrids)
```

### AddLocalNavigationGridForPoint
```angelscript
int AddLocalNavigationGridForPoint(FVector Location, int Radius2D, float32 Height, bool bRebuildGrids)
```
creates new grid data for single point

### AddLocalNavigationGridForPoints
```angelscript
int AddLocalNavigationGridForPoints(TArray<FVector> Locations, int Radius2D, float32 Height, bool bRebuildGrids)
```
creates single grid data for set of points

### FindLocalNavigationGridPath
```angelscript
bool FindLocalNavigationGridPath(FVector Start, FVector End, TArray<FVector>& PathPoints)
```

### RemoveLocalNavigationGrid
```angelscript
void RemoveLocalNavigationGrid(int GridId, bool bRebuildGrids)
```

### SetLocalNavigationGridDensity
```angelscript
bool SetLocalNavigationGridDensity(float32 CellSize)
```

### StaticClass
```angelscript
UClass StaticClass()
```

