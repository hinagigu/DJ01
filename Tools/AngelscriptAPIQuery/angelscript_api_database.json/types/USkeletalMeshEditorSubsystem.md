# USkeletalMeshEditorSubsystem

**继承自**: `UEditorSubsystem`

USkeletalMeshEditorSubsystem
Subsystem for exposing skeletal mesh functionality to scripts

## 方法

### GetLODMaterialSlot
```angelscript
int GetLODMaterialSlot(USkeletalMesh SkeletalMesh, int LODIndex, int SectionIndex)
```
Gets the material slot used for a specific LOD section.
@param       SkeletalMesh            SkeletalMesh to get the material index from.
@param       LODIndex                        Index of the StaticMesh LOD.
@param       SectionIndex            Index of the StaticMesh Section.
@return  MaterialSlotIndex   Index of the material slot used by the section or INDEX_NONE in case of error.

### GetNumSections
```angelscript
int GetNumSections(USkeletalMesh SkeletalMesh, int LODIndex)
```
Get number of sections for a LOD of a Skeletal Mesh

@param SkeletalMesh          Mesh to get number of vertices from.
@param LODIndex                      Index of the mesh LOD.
@return Number of sections. Returns INDEX_NONE if invalid mesh or LOD index.

### GetNumVerts
```angelscript
int GetNumVerts(USkeletalMesh SkeletalMesh, int LODIndex)
```
Get number of mesh vertices for an LOD of a Skeletal Mesh

@param SkeletalMesh          Mesh to get number of vertices from.
@param LODIndex                      Index of the mesh LOD.
@return Number of vertices. Returns 0 if invalid mesh or LOD index.

### GetSectionCastShadow
```angelscript
bool GetSectionCastShadow(const USkeletalMesh SkeletalMesh, int LODIndex, int SectionIndex, bool& bOutCastShadow)
```
Get bCastShadow from a section of a LOD of a Skeletal Mesh

@param SkeletalMesh                  Mesh to get number of vertices from.
@param LodIndex                              Index of the mesh LOD.
@param SectionIndex                  Index of the LOD section.
@param bOutCastShadow        The function will set the bCastShadow used by the section
@return false if invalid mesh or LOD index or section index.

### GetSectionRecomputeTangent
```angelscript
bool GetSectionRecomputeTangent(const USkeletalMesh SkeletalMesh, int LODIndex, int SectionIndex, bool& bOutRecomputeTangent)
```
Get bRecomputeTangent from a section of a LOD of a Skeletal Mesh

@param SkeletalMesh                  Mesh to get number of vertices from.
@param LodIndex                              Index of the mesh LOD.
@param SectionIndex                  Index of the LOD section.
@param bOutRecomputeTangent  The function will set the bRecomputeTangent used by the section
@return false if invalid mesh or LOD index or section index.

### GetSectionRecomputeTangentsVertexMaskChannel
```angelscript
bool GetSectionRecomputeTangentsVertexMaskChannel(const USkeletalMesh SkeletalMesh, int LODIndex, int SectionIndex, uint8& OutRecomputeTangentsVertexMaskChannel)
```
Get RecomputeTangentsVertexMaskChannel from a section of a LOD of a Skeletal Mesh

@param SkeletalMesh                  Mesh to get number of vertices from.
@param LodIndex                              Index of the mesh LOD.
@param SectionIndex                  Index of the LOD section.
@param OutRecomputeTangentsVertexMaskChannel The function will set the RecomputeTangentsVertexMaskChannel used by the section
@return false if invalid mesh or LOD index or section index.

### GetSectionVisibleInRayTracing
```angelscript
bool GetSectionVisibleInRayTracing(const USkeletalMesh SkeletalMesh, int LODIndex, int SectionIndex, bool& bOutVisibleInRayTracing)
```
Get bVisibleInRayTracing from a section of a LOD of a Skeletal Mesh

@param SkeletalMesh                  Mesh to get number of vertices from.
@param LodIndex                              Index of the mesh LOD.
@param SectionIndex                  Index of the LOD section.
@param bOutVisibleInRayTracing       The function will set the bVisibleInRayTracing used by the section
@return false if invalid mesh or LOD index or section index.

### SetSectionCastShadow
```angelscript
bool SetSectionCastShadow(USkeletalMesh SkeletalMesh, int LODIndex, int SectionIndex, bool bCastShadow)
```
Set bCastShadow for a section of a LOD of a Skeletal Mesh.

@param SkeletalMesh                  Mesh to get number of vertices from.
@param LodIndex                              Index of the mesh LOD.
@param SectionIndex                  Index of the LOD section.
@param bCastShadow   The function will set the bCastShadow used by the section
@return false if invalid mesh or LOD index or section index.

### SetSectionRecomputeTangent
```angelscript
bool SetSectionRecomputeTangent(USkeletalMesh SkeletalMesh, int LODIndex, int SectionIndex, bool bRecomputeTangent)
```
Set bRecomputeTangent for a section of a LOD of a Skeletal Mesh.

@param SkeletalMesh                  Mesh to get number of vertices from.
@param LodIndex                              Index of the mesh LOD.
@param SectionIndex                  Index of the LOD section.
@param bRecomputeTangent     The function will set the bRecomputeTangent used by the section
@return false if invalid mesh or LOD index or section index.

### SetSectionRecomputeTangentsVertexMaskChannel
```angelscript
bool SetSectionRecomputeTangentsVertexMaskChannel(USkeletalMesh SkeletalMesh, int LODIndex, int SectionIndex, uint8 RecomputeTangentsVertexMaskChannel)
```
Set RecomputeTangentsVertexMaskChannel for a section of a LOD of a Skeletal Mesh.

@param SkeletalMesh                  Mesh to get number of vertices from.
@param LodIndex                              Index of the mesh LOD.
@param SectionIndex                  Index of the LOD section.
@param RecomputeTangentsVertexMaskChannel    The function will set the RecomputeTangentsVertexMaskChannel used by the section
@return false if invalid mesh or LOD index or section index.

### SetSectionVisibleInRayTracing
```angelscript
bool SetSectionVisibleInRayTracing(USkeletalMesh SkeletalMesh, int LODIndex, int SectionIndex, bool bVisibleInRayTracing)
```
Set bVisibleInRayTracing for a section of a LOD of a Skeletal Mesh.

@param SkeletalMesh                  Mesh to get number of vertices from.
@param LodIndex                              Index of the mesh LOD.
@param SectionIndex                  Index of the LOD section.
@param bVisibleInRayTracing  The function will set the bVisibleInRayTracing used by the section
@return false if invalid mesh or LOD index or section index.

