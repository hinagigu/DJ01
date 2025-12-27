# UGameplayMessageSubsystem

**继承自**: `UGameInstanceSubsystem`

This system allows event raisers and listeners to register for messages without
having to know about each other directly, though they must agree on the format
of the message (as a USTRUCT() type).


You can get to the message router from the game instance:
   UGameInstance::GetSubsystem<UGameplayMessageSubsystem>(GameInstance)
or directly from anything that has a route to a world:
   UGameplayMessageSubsystem::Get(WorldContextObject)

Note that call order when there are multiple listeners for the same channel is
not guaranteed and can change over time!

