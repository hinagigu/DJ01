# AOnlineBeaconHost

**继承自**: `AOnlineBeacon`

Main actor that listens for side channel communication from another Unreal Engine application

The AOnlineBeaconHost listens for connections to route to a registered AOnlineBeaconHostObject
The AOnlineBeaconHostObject is responsible for spawning the server version of the AOnlineBeaconClient
The AOnlineBeaconHost pairs the two client actors, verifies the validity of the exchange, and accepts/continues the connection

