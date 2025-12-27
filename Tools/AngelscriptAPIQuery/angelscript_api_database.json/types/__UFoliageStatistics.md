# __UFoliageStatistics

## 方法

### FoliageOverlappingBoxCount
```angelscript
int FoliageOverlappingBoxCount(const UStaticMesh StaticMesh, FBox Box)
```
Gets the number of instances overlapping a provided box
@param StaticMesh Mesh to count
@param Box Box to overlap

### FoliageOverlappingBoxTransforms
```angelscript
void FoliageOverlappingBoxTransforms(const UStaticMesh StaticMesh, FBox Box, TArray<FTransform>& OutTransforms)
```
Get the transform of every instance overlapping the provided FBox
    @param StaticMesh Mesh to get instances of
    @param Box Box to use for overlap
    @param OutTransforms Array to populate with transforms

### FoliageOverlappingSphereCount
```angelscript
int FoliageOverlappingSphereCount(const UStaticMesh StaticMesh, FVector CenterPosition, float32 Radius)
```
Counts how many foliage instances overlap a given sphere

@param        Mesh                    The static mesh we are interested in counting
@param        CenterPosition  The center position of the sphere
@param        Radius                  The radius of the sphere.

return number of foliage instances with their mesh set to Mesh that overlap the sphere

### StaticClass
```angelscript
UClass StaticClass()
```

