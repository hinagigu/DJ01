# AQosBeaconClient

**继承自**: `AOnlineBeaconClient`

A beacon client used for quality timings to a specified session

## 方法

### ClientQosResponse
```angelscript
void ClientQosResponse(EQosResponseType Response)
```
Response from the host session after making a Qos request

### ServerQosRequest
```angelscript
void ServerQosRequest(FString InSessionId)
```
Contact the server with a Qos request and begin timing

@param InSessionId reference session id to make sure the session is the correct one

