# UParticleModuleRequired

**继承自**: `UParticleModule`

## 属性

### Material
- **类型**: `UMaterialInterface`
- **描述**: The material to utilize for the emitter at this LOD level.

### MinFacingCameraBlendDistance
- **类型**: `float32`
- **描述**: The distance at which PSA_FacingCameraDistanceBlend    is fully PSA_Square

### MaxFacingCameraBlendDistance
- **类型**: `float32`
- **描述**: The distance at which PSA_FacingCameraDistanceBlend    is fully PSA_FacingCameraPosition

### EmitterOrigin
- **类型**: `FVector`

### EmitterRotation
- **类型**: `FRotator`

### ScreenAlignment
- **类型**: `EParticleScreenAlignment`
- **描述**: The screen alignment to utilize for the emitter at this LOD level.
One of the following:
PSA_FacingCameraPosition - Faces the camera position, but is not dependent on the camera rotation.
                                                        This method produces more stable particles under camera rotation.
PSA_Square                      - Uniform scale (via SizeX) facing the camera
PSA_Rectangle           - Non-uniform scale (via SizeX and SizeY) facing the camera
PSA_Velocity            - Orient the particle towards both the camera and the direction
                                          the particle is moving. Non-uniform scaling is allowed.
PSA_TypeSpecific        - Use the alignment method indicated in the type data module.
PSA_FacingCameraDistanceBlend - Blends between PSA_FacingCameraPosition and PSA_Square over specified distance.

### SortMode
- **类型**: `EParticleSortMode`
- **描述**: The sorting mode to use for this emitter.
PSORTMODE_None                          - No sorting required.
PSORTMODE_ViewProjDepth         - Sort by view projected depth of the particle.
PSORTMODE_DistanceToView        - Sort by distance of particle to view in world space.
PSORTMODE_Age_OldestFirst       - Sort by age, oldest drawn first.
PSORTMODE_Age_NewestFirst       - Sort by age, newest drawn first.

### EmitterDuration
- **类型**: `float32`
- **描述**: How long, in seconds, the emitter will run before looping.

### EmitterDelay
- **类型**: `float32`
- **描述**: Indicates the time (in seconds) that this emitter should be delayed in the particle system.

### EmitterDelayLow
- **类型**: `float32`
- **描述**: The low end of the emitter delay if using a range.

### InterpolationMethod
- **类型**: `EParticleSubUVInterpMethod`
- **描述**: The interpolation method to used for the SubUV image selection.
One of the following:
PSUVIM_None                     - Do not apply SubUV modules to this emitter.
PSUVIM_Linear           - Smoothly transition between sub-images in the given order,
                                          with no blending between the current and the next
PSUVIM_Linear_Blend     - Smoothly transition between sub-images in the given order,
                                          blending between the current and the next
PSUVIM_Random           - Pick the next image at random, with no blending between
                                          the current and the next
PSUVIM_Random_Blend     - Pick the next image at random, blending between the current
                                          and the next

### OpacitySourceMode
- **类型**: `EOpacitySourceMode`

### EmitterNormalsMode
- **类型**: `EEmitterNormalsMode`
- **描述**: Normal generation mode for this emitter LOD.

### SubImages_Horizontal
- **类型**: `int`
- **描述**: The number of sub-images horizontally in the texture

### SubImages_Vertical
- **类型**: `int`
- **描述**: The number of sub-images vertically in the texture

### RandomImageChanges
- **类型**: `int`
- **描述**: The number of times to change a random image over the life of the particle.

### MacroUVPosition
- **类型**: `FVector`
- **描述**: Local space position that UVs generated with the ParticleMacroUV material node will be centered on.

### MacroUVRadius
- **类型**: `float32`
- **描述**: World space radius that UVs generated with the ParticleMacroUV material node will tile based on.

### UVFlippingMode
- **类型**: `EParticleUVFlipMode`
- **描述**: Controls UV Flipping for this emitter.

### BoundingMode
- **类型**: `ESubUVBoundingVertexCount`
- **描述**: More bounding vertices results in reduced overdraw, but adds more triangle overhead.
The eight vertex mode is best used when the SubUV texture has a lot of space to cut out that is not captured by the four vertex version,
and when the particles using the texture will be few and large.

### NormalsSphereCenter
- **类型**: `FVector`
- **描述**: When EmitterNormalsMode is ENM_Spherical, particle normals are created to face away from NormalsSphereCenter.
NormalsSphereCenter is in local space.

### AlphaThreshold
- **类型**: `float32`
- **描述**: Alpha channel values larger than the threshold are considered occupied and will be contained in the bounding geometry.
Raising this threshold slightly can reduce overdraw in particles using this animation asset.

### EmitterLoops
- **类型**: `int`
- **描述**: The number of times to loop the emitter.
    0 indicates loop continuously

### CutoutTexture
- **类型**: `UTexture2D`
- **描述**: Texture to generate bounding geometry from.

### MaxDrawCount
- **类型**: `int`
- **描述**: The maximum number of particles to DRAW for this emitter.
If set to 0, it will use whatever number are present.

### EmitterDurationLow
- **类型**: `float32`
- **描述**: The low end of the emitter duration if using a range.

### NormalsCylinderDirection
- **类型**: `FVector`
- **描述**: When EmitterNormalsMode is ENM_Cylindrical,
particle normals are created to face away from the cylinder going through NormalsSphereCenter in the direction NormalsCylinderDirection.
NormalsCylinderDirection is in local space.

### NamedMaterialOverrides
- **类型**: `TArray<FName>`
- **描述**: Named material overrides for this emitter.
Overrides this emitter's material(s) with those in the correspondingly named slot(s) of the owning system.

### bUseLocalSpace
- **类型**: `bool`

### bKillOnDeactivate
- **类型**: `bool`

### bKillOnCompleted
- **类型**: `bool`

### bUseLegacyEmitterTime
- **类型**: `bool`

### bRemoveHMDRoll
- **类型**: `bool`

### bSupportLargeWorldCoordinates
- **类型**: `bool`

### bEmitterDurationUseRange
- **类型**: `bool`

### bOverrideUseVelocityForMotionBlur
- **类型**: `bool`

### bUseVelocityForMotionBlur
- **类型**: `bool`

### bDelayFirstLoopOnly
- **类型**: `bool`

### bScaleUV
- **类型**: `bool`

### bEmitterDelayUseRange
- **类型**: `bool`

### bOverrideSystemMacroUV
- **类型**: `bool`

### bUseMaxDrawCount
- **类型**: `bool`

### bOrbitModuleAffectsVelocityAlignment
- **类型**: `bool`

### bDurationRecalcEachLoop
- **类型**: `bool`

