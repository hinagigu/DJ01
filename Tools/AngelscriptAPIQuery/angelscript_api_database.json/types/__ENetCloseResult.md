# __ENetCloseResult

Network Close results (can occur before NetDriver/NetConnection creation, and can be success or error)

Licensees should use ENetCloseResult::Extended, and specify an ErrorContext value to FNetCloseResult, to specify custom results

NOTE: If you modify this, run the enum-checking smoke test to verify you didn't forget to update anything else:
                    System.Core.Networking.FNetCloseResult.EnumTest

## 属性

### NetDriverAlreadyExists
- **类型**: `ENetCloseResult`

### NetDriverCreateFailure
- **类型**: `ENetCloseResult`

### NetDriverListenFailure
- **类型**: `ENetCloseResult`

### ConnectionLost
- **类型**: `ENetCloseResult`

### ConnectionTimeout
- **类型**: `ENetCloseResult`

### FailureReceived
- **类型**: `ENetCloseResult`

### OutdatedClient
- **类型**: `ENetCloseResult`

### OutdatedServer
- **类型**: `ENetCloseResult`

### PendingConnectionFailure
- **类型**: `ENetCloseResult`

### NetGuidMismatch
- **类型**: `ENetCloseResult`

### NetChecksumMismatch
- **类型**: `ENetCloseResult`

### SecurityMalformedPacket
- **类型**: `ENetCloseResult`

### SecurityInvalidData
- **类型**: `ENetCloseResult`

### SecurityClosed
- **类型**: `ENetCloseResult`

### Unknown
- **类型**: `ENetCloseResult`

### Success
- **类型**: `ENetCloseResult`

### Extended
- **类型**: `ENetCloseResult`

### HostClosedConnection
- **类型**: `ENetCloseResult`

### Disconnect
- **类型**: `ENetCloseResult`

### Upgrade
- **类型**: `ENetCloseResult`

### PreLoginFailure
- **类型**: `ENetCloseResult`

### JoinFailure
- **类型**: `ENetCloseResult`

### JoinSplitFailure
- **类型**: `ENetCloseResult`

### AddressResolutionFailed
- **类型**: `ENetCloseResult`

### RPCDoS
- **类型**: `ENetCloseResult`

### Cleanup
- **类型**: `ENetCloseResult`

### MissingLevelPackage
- **类型**: `ENetCloseResult`

### PacketHandlerIncomingError
- **类型**: `ENetCloseResult`

### ZeroLastByte
- **类型**: `ENetCloseResult`

### ZeroSize
- **类型**: `ENetCloseResult`

### ReadHeaderFail
- **类型**: `ENetCloseResult`

### ReadHeaderExtraFail
- **类型**: `ENetCloseResult`

### AckSequenceMismatch
- **类型**: `ENetCloseResult`

### BunchBadChannelIndex
- **类型**: `ENetCloseResult`

### BunchChannelNameFail
- **类型**: `ENetCloseResult`

### BunchWrongChannelType
- **类型**: `ENetCloseResult`

### BunchHeaderOverflow
- **类型**: `ENetCloseResult`

### BunchDataOverflow
- **类型**: `ENetCloseResult`

### BunchServerPackageMapExports
- **类型**: `ENetCloseResult`

### BunchPrematureControlChannel
- **类型**: `ENetCloseResult`

### BunchPrematureChannel
- **类型**: `ENetCloseResult`

### BunchPrematureControlClose
- **类型**: `ENetCloseResult`

### UnknownChannelType
- **类型**: `ENetCloseResult`

### PrematureSend
- **类型**: `ENetCloseResult`

### CorruptData
- **类型**: `ENetCloseResult`

### SocketSendFailure
- **类型**: `ENetCloseResult`

### BadChildConnectionIndex
- **类型**: `ENetCloseResult`

### LogLimitInstant
- **类型**: `ENetCloseResult`

### LogLimitSustained
- **类型**: `ENetCloseResult`

### EncryptionFailure
- **类型**: `ENetCloseResult`

### EncryptionTokenMissing
- **类型**: `ENetCloseResult`

### ReceivedNetGUIDBunchFail
- **类型**: `ENetCloseResult`

### MaxReliableExceeded
- **类型**: `ENetCloseResult`

### ReceivedNextBunchFail
- **类型**: `ENetCloseResult`

### ReceivedNextBunchQueueFail
- **类型**: `ENetCloseResult`

### PartialInitialReliableDestroy
- **类型**: `ENetCloseResult`

### PartialMergeReliableDestroy
- **类型**: `ENetCloseResult`

### PartialInitialNonByteAligned
- **类型**: `ENetCloseResult`

### PartialNonByteAligned
- **类型**: `ENetCloseResult`

### PartialFinalPackageMapExports
- **类型**: `ENetCloseResult`

### PartialTooLarge
- **类型**: `ENetCloseResult`

### AlreadyOpen
- **类型**: `ENetCloseResult`

### ReliableBeforeOpen
- **类型**: `ENetCloseResult`

### ReliableBufferOverflow
- **类型**: `ENetCloseResult`

### RPCReliableBufferOverflow
- **类型**: `ENetCloseResult`

### ControlChannelClose
- **类型**: `ENetCloseResult`

### ControlChannelEndianCheck
- **类型**: `ENetCloseResult`

### ControlChannelPlayerChannelFail
- **类型**: `ENetCloseResult`

### ControlChannelMessageUnknown
- **类型**: `ENetCloseResult`

### ControlChannelMessageFail
- **类型**: `ENetCloseResult`

### ControlChannelMessagePayloadFail
- **类型**: `ENetCloseResult`

### ControlChannelBunchOverflowed
- **类型**: `ENetCloseResult`

### ControlChannelQueueBunchOverflowed
- **类型**: `ENetCloseResult`

### ClientHasMustBeMappedGUIDs
- **类型**: `ENetCloseResult`

### ClientSentDestructionInfo
- **类型**: `ENetCloseResult`

### UnregisteredMustBeMappedGUID
- **类型**: `ENetCloseResult`

### ObjectReplicatorReceivedBunchFail
- **类型**: `ENetCloseResult`

### ContentBlockFail
- **类型**: `ENetCloseResult`

### ContentBlockHeaderRepLayoutFail
- **类型**: `ENetCloseResult`

### ContentBlockHeaderIsActorFail
- **类型**: `ENetCloseResult`

### ContentBlockHeaderObjFail
- **类型**: `ENetCloseResult`

### ContentBlockHeaderPrematureEnd
- **类型**: `ENetCloseResult`

### ContentBlockHeaderSubObjectActor
- **类型**: `ENetCloseResult`

### ContentBlockHeaderBadParent
- **类型**: `ENetCloseResult`

### ContentBlockHeaderInvalidCreate
- **类型**: `ENetCloseResult`

### ContentBlockHeaderStablyNamedFail
- **类型**: `ENetCloseResult`

### ContentBlockHeaderNoSubObjectClass
- **类型**: `ENetCloseResult`

### ContentBlockHeaderUObjectSubObject
- **类型**: `ENetCloseResult`

### ContentBlockHeaderAActorSubObject
- **类型**: `ENetCloseResult`

### ContentBlockHeaderFail
- **类型**: `ENetCloseResult`

### ContentBlockPayloadBitsFail
- **类型**: `ENetCloseResult`

### FieldHeaderRepIndex
- **类型**: `ENetCloseResult`

### FieldHeaderBadRepIndex
- **类型**: `ENetCloseResult`

### FieldHeaderPayloadBitsFail
- **类型**: `ENetCloseResult`

### FieldPayloadFail
- **类型**: `ENetCloseResult`

### ReplicationChannelCountMaxedOut
- **类型**: `ENetCloseResult`

### BeaconControlFlowError
- **类型**: `ENetCloseResult`

### BeaconUnableToParsePacket
- **类型**: `ENetCloseResult`

### BeaconAuthenticationFailure
- **类型**: `ENetCloseResult`

### BeaconLoginInvalidIdError
- **类型**: `ENetCloseResult`

### BeaconLoginInvalidAuthHandlerError
- **类型**: `ENetCloseResult`

### BeaconAuthError
- **类型**: `ENetCloseResult`

### BeaconSpawnClientWorldPackageNameError
- **类型**: `ENetCloseResult`

### BeaconSpawnExistingActorError
- **类型**: `ENetCloseResult`

### BeaconSpawnFailureError
- **类型**: `ENetCloseResult`

### BeaconSpawnNetGUIDAckNoActor
- **类型**: `ENetCloseResult`

### BeaconSpawnNetGUIDAckNoHost
- **类型**: `ENetCloseResult`

### BeaconSpawnUnexpectedError
- **类型**: `ENetCloseResult`

### IrisProtocolMismatch
- **类型**: `ENetCloseResult`

### IrisNetRefHandleError
- **类型**: `ENetCloseResult`

### FaultDisconnect
- **类型**: `ENetCloseResult`

### NotRecoverable
- **类型**: `ENetCloseResult`

### ENetCloseResult_MAX
- **类型**: `ENetCloseResult`

