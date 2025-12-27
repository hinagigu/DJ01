# ANavLinkProxy

**继承自**: `AActor`

ANavLinkProxy connects areas of Navmesh that don't have a direct navigation path.
It directly supports Simple Links (see PointLinks array). There can be multiple Simple links per ANavLinkProxy instance.
Simple links are designed to statically link areas of Navmesh and are associated with a particular area class that the link provides.
Smart Link functionality is provided via UNavLinkCustomComponent, see SmartLinkComp. They are designed to be able to be dynamically toggled
between enabled and disabled and provide different area classes for both cases. The area classes can be dynamically modified
without navmesh rebuilds.
There can only be at most one smart link per ANavLinkProxy instance.
Both simple and smart links on a single ANavLinkProxy instance, can be set / enabled at once, as well as either or neither of them.

## 属性

### PointLinks
- **类型**: `TArray<FNavigationLink>`

### SmartLinkComp
- **类型**: `UNavLinkCustomComponent`
- **描述**: Smart link: can affect path following

### bSmartLinkIsRelevant
- **类型**: `bool`
- **描述**: Smart link: toggle relevancy

### OnSmartLinkReached
- **类型**: `FSmartLinkReachedSignature`

## 方法

### HasMovingAgents
```angelscript
bool HasMovingAgents()
```
check if any agent is moving through smart link right now

### IsSmartLinkEnabled
```angelscript
bool IsSmartLinkEnabled()
```
check if smart link is enabled

### SmartLinkReached
```angelscript
void SmartLinkReached(AActor Agent, FVector Destination)
```
called when agent reaches smart link during path following, use ResumePathFollowing() to give control back

### ResumePathFollowing
```angelscript
void ResumePathFollowing(AActor Agent)
```
resume normal path following

### SetSmartLinkEnabled
```angelscript
void SetSmartLinkEnabled(bool bEnabled)
```
change state of smart link

