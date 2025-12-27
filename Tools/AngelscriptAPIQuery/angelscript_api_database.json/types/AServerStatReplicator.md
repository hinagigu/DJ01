# AServerStatReplicator

**继承自**: `AInfo`

Class used to replicate server "stat net" data over. For server only values, the client data is
is overwritten when bUpdateStatNet == true. For data that both the client and server set, the server
data will only overwrite if bUpdateStatNet == true && bOverwriteClientStats == true.

## 属性

### bUpdateStatNet
- **类型**: `bool`
- **描述**: Whether to update stat net with data from the server or not

### bOverwriteClientStats
- **类型**: `bool`
- **描述**: Whether to overwrite client data stat net with data from the server or not

