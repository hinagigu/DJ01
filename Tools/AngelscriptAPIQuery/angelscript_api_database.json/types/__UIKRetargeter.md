# __UIKRetargeter

## 方法

### GetChainSettingsFromRetargetAsset
```angelscript
FTargetChainSettings GetChainSettingsFromRetargetAsset(const UIKRetargeter RetargetAsset, FName TargetChainName, FName OptionalProfileName)
```
Returns the chain settings associated with a given target chain in an IK Retargeter Asset using the given profile name (optional)

### GetChainSettingsFromRetargetProfile
```angelscript
FTargetChainSettings GetChainSettingsFromRetargetProfile(FRetargetProfile& RetargetProfile, FName TargetChainName)
```
Returns the chain settings associated with a given target chain in the supplied Retarget Profile.

### GetChainUsingGoalFromRetargetAsset
```angelscript
FTargetChainSettings GetChainUsingGoalFromRetargetAsset(const UIKRetargeter RetargetAsset, FName IKGoalName)
```
Returns the chain settings associated with a given Goal in an IK Retargeter Asset using the given profile name (optional)

### GetGlobalSettingsFromRetargetAsset
```angelscript
void GetGlobalSettingsFromRetargetAsset(const UIKRetargeter RetargetAsset, FName OptionalProfileName, FRetargetGlobalSettings& OutSettings)
```
Returns the global settings in an IK Retargeter Asset using the given profile name (optional)

### GetGlobalSettingsFromRetargetProfile
```angelscript
FRetargetGlobalSettings GetGlobalSettingsFromRetargetProfile(FRetargetProfile& RetargetProfile)
```
Returns the global settings in the supplied Retarget Profile.

### GetRootSettingsFromRetargetAsset
```angelscript
void GetRootSettingsFromRetargetAsset(const UIKRetargeter RetargetAsset, FName OptionalProfileName, FTargetRootSettings& OutSettings)
```
Returns the root settings in an IK Retargeter Asset using the given profile name (optional)

### GetRootSettingsFromRetargetProfile
```angelscript
FTargetRootSettings GetRootSettingsFromRetargetProfile(FRetargetProfile& RetargetProfile)
```
Returns the root settings in the supplied Retarget Profile.

### SetChainFKSettingsInRetargetProfile
```angelscript
void SetChainFKSettingsInRetargetProfile(FRetargetProfile& RetargetProfile, FTargetChainFKSettings FKSettings, FName TargetChainName)
```
Set the chain FK settings in a retarget profile (will set bApplyChainSettings to true).

### SetChainIKSettingsInRetargetProfile
```angelscript
void SetChainIKSettingsInRetargetProfile(FRetargetProfile& RetargetProfile, FTargetChainIKSettings IKSettings, FName TargetChainName)
```
Set the chain IK settings in a retarget profile (will set bApplyChainSettings to true).

### SetChainSettingsInRetargetProfile
```angelscript
void SetChainSettingsInRetargetProfile(FRetargetProfile& RetargetProfile, FTargetChainSettings ChainSettings, FName TargetChainName)
```
Set the chain settings in a retarget profile (will set bApplyChainSettings to true).

### SetChainSpeedPlantSettingsInRetargetProfile
```angelscript
void SetChainSpeedPlantSettingsInRetargetProfile(FRetargetProfile& RetargetProfile, FTargetChainSpeedPlantSettings SpeedPlantSettings, FName TargetChainName)
```
Set the chain Speed Plant settings in a retarget profile (will set bApplyChainSettings to true).

### SetGlobalSettingsInRetargetProfile
```angelscript
void SetGlobalSettingsInRetargetProfile(FRetargetProfile& RetargetProfile, FRetargetGlobalSettings GlobalSettings)
```
Set the global settings in a retarget profile (will set bApplyGlobalSettings to true).

### SetRootSettingsInRetargetProfile
```angelscript
void SetRootSettingsInRetargetProfile(FRetargetProfile& RetargetProfile, FTargetRootSettings RootSettings)
```
Set the root settings in a retarget profile (will set bApplyRootSettings to true).

### StaticClass
```angelscript
UClass StaticClass()
```

