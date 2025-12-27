# UChaosVDParticleDataComponent

**继承自**: `UActorComponent`

Component that will reference all particle data for a specific solver for the current frame.
Currently it is empty and only used to interface with the component visualizer system for particle data,
but when we eventually remove the dependency on actors to represent particles as planned, the particle data will be referenced in this component.\
(similarly to how the Scene Query Data and Collision Data is referenced in their respective components)

