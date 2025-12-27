# UBrushBuilder

**继承自**: `UObject`

Base class of UnrealEd brush builders.


Tips for writing brush builders:

- Always validate the user-specified and call BadParameters function
  if anything is wrong, instead of actually building geometry.
  If you build an invalid brush due to bad user parameters, you'll
  cause an extraordinary amount of pain for the poor user.

- When generating polygons with more than 3 vertices, BE SURE all the
  polygon's vertices are coplanar!  Out-of-plane polygons will cause
  geometry to be corrupted.

