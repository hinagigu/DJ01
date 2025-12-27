# UGameFrameworkComponentManager

**继承自**: `UGameInstanceSubsystem`

GameFrameworkComponentManager

A manager to handle putting components on actors as they come and go.
Put in a request to instantiate components of a given class on actors of a given class and they will automatically be made for them as the actors are spawned.
Submit delegate handlers to listen for actors of a given class. Those handlers will automatically run when actors of a given class or registered as receivers or game events are sent.
Actors must opt-in to this behavior by calling AddReceiver/RemoveReceiver for themselves when they are ready to receive the components and when they want to remove them.
Any actors that are in memory when a request is made will automatically get the components, and any in memory when a request is removed will lose the components immediately.
Requests are reference counted, so if multiple requests are made for the same actor class and component class, only one component will be added and that component wont be removed until all requests are removed.

## 方法

### AddReceiver
```angelscript
void AddReceiver(AActor Receiver, bool bAddOnlyInGameWorlds)
```
Adds an actor as a receiver for components. If it passes the actorclass filter on requests it will get the components.

### RegisterAndCallForActorInitState
```angelscript
bool RegisterAndCallForActorInitState(AActor Actor, FName FeatureName, FGameplayTag RequiredState, FActorInitStateChangedBPDelegate Delegate, bool bCallImmediately)
```
Registers blueprint delegate for feature state change notifications on a specific actor and may call it immediately

@param Actor                         The actor to listen for state changes to, if you don't have a specific actor call the Class version instead
@param FeatureName           If not empty, only listen to state changes for the specified feature
@param RequiredState         If specified, only activate if the init state of the feature is equal to or later than this
@param Delegate                      Native delegate to call
@param bCallImmediately      If true and the actor feature is already in the specified state, call delegate immediately after registering
@return true if delegate was registered

### RegisterAndCallForClassInitState
```angelscript
bool RegisterAndCallForClassInitState(TSoftClassPtr<AActor> ActorClass, FName FeatureName, FGameplayTag RequiredState, FActorInitStateChangedBPDelegate Delegate, bool bCallImmediately)
```
Registers blueprint delegate for feature state change notifications on a class of actors and may call it immediately

@param ActorClass            Name of an actor class to listen for changes to
@param FeatureName           If not empty, only listen to state changes for the specified feature
@param RequiredState         If specified, only activate if the init state of the feature is equal to or later than this
@param Delegate                      Native delegate to call
@param bCallImmediately      If true and the actor feature is already in the specified state, call delegate immediately after registering
@return true if delegate was registered

### RemoveReceiver
```angelscript
void RemoveReceiver(AActor Receiver)
```
Removes an actor as a receiver for components.

### SendExtensionEvent
```angelscript
void SendExtensionEvent(AActor Receiver, FName EventName, bool bOnlyInGameWorlds)
```
Sends an arbitrary extension event that can be listened for by other systems

### UnregisterActorInitStateDelegate
```angelscript
bool UnregisterActorInitStateDelegate(AActor Actor, FActorInitStateChangedBPDelegate DelegateToRemove)
```
Removes a registered delegate bound to a specific actor

### UnregisterClassInitStateDelegate
```angelscript
bool UnregisterClassInitStateDelegate(TSoftClassPtr<AActor> ActorClass, FActorInitStateChangedBPDelegate DelegateToRemove)
```
Removes a registered delegate bound to a class

